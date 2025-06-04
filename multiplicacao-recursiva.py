def multiplicacao(a, b):
    """
    Função recursiva que calcula o produto de dois números inteiros utilizando apenas somas.
    
    Args:
        a (int): O primeiro número inteiro.
        b (int): O segundo número inteiro.
        
    Returns:
        int: O produto de a e b.
    """
    # Casos base
    if b == 0:
        return 0
    elif b == 1:
        return a
    elif b < 0:
        # Se b for negativo, invertemos o sinal e chamamos a função novamente
        return -multiplicacao(a, -b)
    else:
        # Caso recursivo: a * b = a + a * (b - 1)
        return a + multiplicacao(a, b - 1)


# Exemplo de uso:
if __name__ == "__main__":
    a = int(input("Digite o primeiro número inteiro: "))
    b = int(input("Digite o segundo número inteiro: "))
    
    resultado = multiplicacao(a, b)
    print(f"{a} * {b} = {resultado}")
        