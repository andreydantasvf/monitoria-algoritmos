def contarpalavras(frase):
    """
    Função que conta o número de palavras em uma frase.
    
    Args:
        frase (str): A frase a ser analisada.
        
    Returns:
        int: O número de palavras na frase.
    """
    # Divide a frase pelos espaços e conta as partes não vazias
    palavras = frase.split() # transforma a frase em uma lista de palavras
    return len(palavras)


# Exemplo de uso:
if __name__ == "__main__":
    frase = input("Digite uma frase: ")
    
    numero_palavras = contarpalavras(frase)
    print(f"A frase contém {numero_palavras} palavras.")