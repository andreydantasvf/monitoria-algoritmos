def trailingzerosfatorial(n):
    """
    Função recursiva que calcula o número de zeros à direita no resultado de n! (fatorial de n).
    
    O número de zeros à direita é determinado pelo número de fatores 10 (que são formados por 
    fatores 2 e 5). Como há sempre mais fatores 2 do que 5 em um fatorial, basta contar 
    o número de fatores 5.
    
    Args:
        n (int): O número inteiro positivo para calcular o fatorial.
        
    Returns:
        int: O número de zeros à direita no resultado do fatorial de n.
    """
    # Caso base: para 0 <= n < 5, não há zeros à direita
    if n < 5:
        return 0
    
    # Caso recursivo: Conta o número de múltiplos de 5 até n
    # e adiciona recursivamente os múltiplos de 25, 125, etc.
    return (n // 5) + trailingzerosfatorial(n // 5)


# Função auxiliar para calcular o fatorial (para visualização)
def fatorial(n):
    """
    Calcula o fatorial de n.
    
    Args:
        n (int): O número inteiro positivo para calcular o fatorial.
        
    Returns:
        int: O fatorial de n (n!).
    """
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)


# Exemplo de uso:
if __name__ == "__main__":
  n = int(input("Digite um número inteiro positivo: "))
  
  # Verifica se o número é não-negativo
  if n < 0:
      print("O fatorial não está definido para números negativos.")
  else:
      zeros = trailingzerosfatorial(n)
      
      print(f"O fatorial de {n} tem {zeros} zero(s) à direita.")
      
      # Para números pequenos, mostra o valor do fatorial para verificação
      if n <= 20:  # Limite para evitar números muito grandes
          valor_fatorial = fatorial(n)
          print(f"{n}! = {valor_fatorial}")
          print(f"Verificação: {valor_fatorial} tem {zeros} zero(s) à direita.")