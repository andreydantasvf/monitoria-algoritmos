def convertertempo(minutos):
    """
    Função que converte um valor em minutos para horas e minutos.
    
    Args:
        minutos (int): O valor em minutos a ser convertido.
        
    Returns:
        str: String formatada representando o tempo.
    """
    # Calcula as horas (divisão inteira)
    horas = minutos // 60
    
    # Calcula os minutos restantes (resto da divisão)
    minutos_restantes = minutos % 60

    texto_hora = "1 hora" if horas == 1 else f"{horas} horas"
    texto_minuto = "1 minuto" if minutos_restantes == 1 else f"{minutos_restantes} minutos"
    
    return f"{texto_hora} e {texto_minuto}"

# Exemplo de uso:
if __name__ == "__main__":
  valor_minutos = int(input("Digite o valor em minutos: "))

  # Converte o tempo
  resultado = convertertempo(valor_minutos)
  print(f"{valor_minutos} minutos equivalem a {resultado}.")
