def somadigitos(n):
    """
    Função recursiva que calcula a soma dos dígitos de um número inteiro.
    
    Args:
        n (int): O número inteiro.
        
    Returns:
        int: A soma dos dígitos de n.
    """
    # Caso base: se o número tem apenas um dígito, retorna ele mesmo
    if n < 10:
        return n
    
    # Caso recursivo: soma o último dígito (n % 10) com a soma dos dígitos restantes (n // 10)
    return (n % 10) + somadigitos(n // 10)


# Exemplo de uso:
if __name__ == "__main__":
  numero = int(input("Digite um número inteiro: "))
  
  resultado = somadigitos(numero)
  
  # Exibe o resultado
  print(f"A soma dos dígitos de {numero} é {resultado}")
  
  # Exibe os cálculos para melhor compreensão
  print(f"Cálculo passo a passo:")
  digitos = [int(d) for d in str(abs(numero))]
  print(" + ".join(map(str, digitos)), "=", resultado)
