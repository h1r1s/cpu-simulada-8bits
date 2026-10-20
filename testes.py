# testes.py

import unittest
from cpu import CPU

class TestCPUSimulada(unittest.TestCase):

    def test_load_e_limite_8bits(self):
        cpu = CPU()
        cpu.memoria[0] = "LOAD R0, 300" # 300 excede 8 bits (max 255)
        cpu.memoria[1] = "HALT"
        cpu.executar()
        # 300 & 0xFF = 44
        self.assertEqual(cpu.registradores["R0"], 44)

    def test_store(self):
        cpu = CPU()
        cpu.memoria[0] = "LOAD R0, 42"
        cpu.memoria[1] = "STORE R0, 15"
        cpu.memoria[2] = "HALT"
        cpu.executar()
        self.assertEqual(cpu.memoria[15], 42)

    def test_operacoes_ula(self):
        cpu = CPU()
        cpu.memoria[0] = "LOAD R0, 10"
        cpu.memoria[1] = "LOAD R1, 3"
        cpu.memoria[2] = "ADD R0, R1"   # R0 = 13
        cpu.memoria[3] = "SUB R0, R1"   # R0 = 10
        cpu.memoria[4] = "HALT"
        cpu.executar()
        self.assertEqual(cpu.registradores["R0"], 10)

    def test_jmp_e_pc(self):
        cpu = CPU()
        cpu.memoria[0] = "LOAD R0, 5"
        cpu.memoria[1] = "JMP 3"
        cpu.memoria[2] = "LOAD R0, 99"  # Deve ser saltado
        cpu.memoria[3] = "LOAD R1, 10"
        cpu.memoria[4] = "HALT"
        cpu.executar()
        self.assertEqual(cpu.registradores["R0"], 5)
        self.assertEqual(cpu.registradores["R1"], 10)

    def test_programa_exemplo(self):
        cpu = CPU()
        cpu.memoria[0] = "LOAD R0, 5"
        cpu.memoria[1] = "LOAD R1, 8"
        cpu.memoria[2] = "ADD R0, R1"
        cpu.memoria[3] = "STORE R0, 15"
        cpu.memoria[4] = "HALT"
        cpu.executar()
        self.assertEqual(cpu.memoria[15], 13)

if __name__ == "__main__":
    unittest.main()