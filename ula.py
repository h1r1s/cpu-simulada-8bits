def limitar_8bits(valor):
    return valor & 0xFF

def executar_ula(operacao, a, b):
    if operacao == "ADD":
        resultado = a + b
    elif operacao == "SUB":
        resultado = a - b
    elif operacao == "AND":
        resultado = a & b
    elif operacao == "OR":
        resultado = a | b
    elif operacao == "XOR":
        resultado = a ^ b
    else:
        raise ValueError("Operação da ULA inválida")
    return limitar_8bits(resultado)