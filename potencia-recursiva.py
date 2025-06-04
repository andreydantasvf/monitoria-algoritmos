def potencia(base, expoente):
    """
    Função recursiva que calcula base elevado ao expoente.
    
    Args:
        base (int): O número base.
        expoente (int): O expoente.
        
    Returns:
        int: O resultado de base elevado ao expoente.
    """
    # Casos base
    if expoente == 0:
        return 1
    if expoente == 1:
        return base
    
    # Caso recursivo: base^expoente = base * base^(expoente - 1)
    # exemplo: 2^3 = 2 * 2^2 -> 2 * (2 * 2)
    return base * potencia(base, expoente - 1)


# Exemplo de uso:
if __name__ == "__main__":
  base = int(input("Digite a base (número inteiro): "))
  expoente = int(input("Digite o expoente (número inteiro): "))
  
  resultado = potencia(base, expoente)
  
  print(f"{base} elevado a {expoente} = {resultado}")
  