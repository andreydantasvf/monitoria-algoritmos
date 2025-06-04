def contarocorrencias(s, c):
    """
    Função que conta o número de vezes que um caractere aparece em uma string.
    
    Args:
        s (str): A string a ser analisada.
        c (str): O caractere a ser contado.
        
    Returns:
        int: O número de ocorrências do caractere na string.
    """
    # Inicializa o contador de ocorrências
    contador = 0
    
    # Percorre cada caractere da string
    for caractere in s:
        # Verifica se o caractere atual é igual ao caractere buscado
        if caractere == c:
            contador += 1
    
    return contador


# Exemplo de uso:
if __name__ == "__main__":
    texto = input("Digite um texto: ")
    caractere = input("Digite o caractere que deseja contar: ")
    
    resultado = contarocorrencias(texto, caractere)
    print(f"O caractere '{caractere}' aparece {resultado} vezes no texto.")