def mdc(a, b):
    """
    Função recursiva que calcula o máximo divisor comum (MDC) entre dois números inteiros.
    Utiliza o algoritmo de Euclides.
    
    Args:
        a (int): O primeiro número inteiro.
        b (int): O segundo número inteiro.
        
    Returns:
        int: O máximo divisor comum entre a e b.
    """
    # Caso base: se b for 0, o MDC é a
    if b == 0:
        return a
    
    # Caso recursivo: MDC(a, b) = MDC(b, a % b)
    return mdc(b, a % b)


# Exemplo de uso:
if __name__ == "__main__":
    a = int(input("Digite o primeiro número inteiro: "))
    b = int(input("Digite o segundo número inteiro: "))
    
    # Verificar se pelo menos um dos números não é zero
    if a == 0 and b == 0:
        print("O MDC não está definido quando ambos os números são zero.")
    else:
        resultado = mdc(a, b)
        print(f"O MDC de {a} e {b} é {resultado}")
            