# main.py

from cpu import CPU
from programas import carregar_programa_exemplo, carregar_programa_grupo

def executar_e_exibir(nome_programa, funcao_carregamento):
    print("=" * 45)
    print(f"       EXECUÇÃO: {nome_programa}")
    print("=" * 45)
    
    cpu = CPU()
    funcao_carregamento(cpu)
    cpu.executar()
    
    print("\n------------------------")
    print("Estado Final da Memória Ocupada:")
    for addr in range(len(cpu.memoria)):
        conteudo = cpu.memoria[addr]
        if conteudo != 0:
            print(f"  MEM[{addr:02d}] = {conteudo}")
    print("=" * 45 + "\n")

if __name__ == "__main__":
    # 1. Executa o programa de exemplo (5 + 8)
    executar_e_exibir("PROGRAMA DE EXEMPLO (5 + 8)", carregar_programa_exemplo)
    
    # 2. Executa o programa próprio do grupo (mínimo 8 instruções)
    executar_e_exibir("PROGRAMA EXPRESSÃO (10 + 5) - (2 AND 3)", carregar_programa_grupo)