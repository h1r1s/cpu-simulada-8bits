from ula import executar_ula, limitar_8bits

class CPU:
    def __init__(self):
        self.registradores = {
            "R0": 0,
            "R1": 0,
            "R2": 0,
            "R3": 0
        }
        self.memoria = [0] * 16
        self.pc = 0
        self.halted = False

    def ula(self, operacao, a, b):
        return executar_ula(operacao, a, b)

    def executar_instrucao(self, instrucao):
        partes = instrucao.replace(",", "").split()
        if not partes:
            return
        
        operacao = partes[0]

        if operacao == "LOAD":
            registrador = partes[1]
            valor = int(partes[2])
            self.registradores[registrador] = limitar_8bits(valor)
            self.pc += 1

        elif operacao == "STORE":
            registrador = partes[1]
            endereco = int(partes[2])
            self.memoria[endereco] = self.registradores[registrador]
            self.pc += 1

        elif operacao in ["ADD", "SUB", "AND", "OR", "XOR"]:
            reg_destino = partes[1]
            reg_origem = partes[2]
            self.registradores[reg_destino] = self.ula(
                operacao, 
                self.registradores[reg_destino], 
                self.registradores[reg_origem]
            )
            self.pc += 1

        elif operacao == "JMP":
            endereco = int(partes[1])
            self.pc = endereco

        elif operacao == "HALT":
            self.halted = True

        else:
            raise ValueError(f"Instrução desconhecida: {operacao}")

    def ciclo(self):
        instrucao = self.memoria[self.pc]
        print()
        print("------------------------")
        print(f"PC: {self.pc:02d}")
        print("Instrução:", instrucao)
        self.executar_instrucao(instrucao)
        self.mostrar_estado()

    def executar(self):
        while not self.halted:
            self.ciclo()

    def mostrar_estado(self):
        print("Registradores:")
        for nome, valor in self.registradores.items():
            print(f"  {nome} = {valor:02X} ({valor})")