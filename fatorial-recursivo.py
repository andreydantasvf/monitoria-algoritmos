def fatorial(n):
    """
    Função recursiva que calcula o fatorial de um número inteiro positivo.
    
    Args:
        n (int): O número inteiro positivo para calcular o fatorial.
        
    Returns:
        int: O fatorial de n (n!).
        
    Raises:
        ValueError: Se n for negativo.
    """
    # Caso base: fatorial de 0 ou 1 é 1
    if n == 0 or n == 1:
        return 1
    
    # Caso recursivo: n! = n * (n-1)!
    return n * fatorial(n - 1)


# Exemplo de uso:
if __name__ == "__main__":
    num = int(input("Digite um número inteiro positivo: "))
    
    # Verificar se o número é positivo
    if num < 0:
        print("O fatorial não está definido para números negativos.")
    else:
        resultado = fatorial(num)
        print(f"O fatorial de {num} é {resultado}")
            