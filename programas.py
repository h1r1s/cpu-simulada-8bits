# programas.py

def carregar_programa_exemplo(cpu):
    """
    Programa de exemplo da especificação:
    Calcula 5 + 8 e armazena na posição 15 da memória.
    Resultado esperado: MEM[15] = 13
    """
    cpu.memoria[0] = "LOAD R0, 5"
    cpu.memoria[1] = "LOAD R1, 8"
    cpu.memoria[2] = "ADD R0, R1"
    cpu.memoria[3] = "STORE R0, 15"
    cpu.memoria[4] = "HALT"


def carregar_programa_grupo(cpu):
    """
    Programa próprio com 9 instruções (cumpre o requisito de no mínimo 8):
    Calcula: (10 + 5) - (2 AND 3) = 15 - 2 = 13
    Utiliza: LOAD, STORE, ADD, SUB, AND e HALT.
    Armazena o resultado na posição 14 da memória.
    """
    cpu.memoria[0] = "LOAD R0, 10"
    cpu.memoria[1] = "LOAD R1, 5"
    cpu.memoria[2] = "ADD R0, R1"     # R0 = 15
    cpu.memoria[3] = "LOAD R2, 2"
    cpu.memoria[4] = "LOAD R3, 3"
    cpu.memoria[5] = "AND R2, R3"     # R2 = 2
    cpu.memoria[6] = "SUB R0, R2"     # R0 = 13
    cpu.memoria[7] = "STORE R0, 14"   # MEM[14] = 13
    cpu.memoria[8] = "HALT"