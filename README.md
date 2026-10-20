
Modelo executável e didático de uma CPU de 8 bits implementado em Python, desenvolvido como trabalho prático da disciplina de Arquitetura de Computadores.

## Especificações da Arquitetura
* **Tamanho dos dados:** 8 bits (com máscara de segurança `& 0xFF`)
* **Registradores Gerais:** `R0`, `R1`, `R2` e `R3`
* **Contador de Programa (PC):** Regista a posição da instrução atual.
* **Memória:** 16 posições de 8 bits (endereços de `0` a `15`)
* **ULA:** Suporta operações aritméticas e lógicas (`ADD`, `SUB`, `AND`, `OR`, `XOR`)
* **Ciclo de Execução:** `Fetch` -> `Decode` -> `Execute`

## Organização dos Arquivos
* `cpu.py`: Classe principal com a lógica da CPU, gestão de memória, registos e ciclo de execução.
* `ula.py`: Implementação das operações da ULA e limitação de 8 bits.
* `programas.py`: Repositório de programas de teste e do grupo.
* `testes.py`: Testes automáticos para validação das instruções obrigatórias.
* `main.py`: Ponto de entrada para visualização da execução passo a passo.
