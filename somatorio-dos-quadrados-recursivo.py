def somatorio_quadrados(n):
    """
    Função recursiva que calcula o somatório dos quadrados dos números de 1 até n.
    
    Args:
        n (int): Um número inteiro positivo.
        
    Returns:
        int: O somatório dos quadrados dos números de 1 até n (1² + 2² + 3² + ... + n²).
    """
    # Caso base: se n for 0, o somatório é 0
    if n == 0:
        return 0
    
    # Caso recursivo: soma(n) = n² + soma(n-1)
    return n**2 + somatorio_quadrados(n - 1)


# Exemplo de uso:
if __name__ == "__main__":
  n = int(input("Digite um número inteiro positivo: "))
  
  # Verificar se o número é não-negativo
  if n < 0:
      print("O valor de n deve ser um número inteiro não negativo.")
  else:
      resultado = somatorio_quadrados(n)
      print(f"O somatório dos quadrados de 1 até {n} é {resultado}")
      
      # Mostrar o cálculo detalhado para melhor compreensão
      if n > 0:
          calculo = " + ".join(f"{i}²" for i in range(1, n + 1))
          print(f"Cálculo: {calculo} = {resultado}")
          