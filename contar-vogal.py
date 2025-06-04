def contarvogais(s):
    """
    Função que conta o número de vogais em uma string.
    
    Args:
        s (str): A string a ser analisada.
    
    Returns:
        int: O número de vogais encontradas na string.
    """
    # Inicializa o contador de vogais
    contador = 0
    
    # Converte a string para minúsculo para facilitar a verificação
    s = s.lower()
    
    # Lista de vogais
    vogais = ['a', 'e', 'i', 'o', 'u']
    
    # Percorre cada caractere da string
    for caractere in s:
        # Verifica se o caractere é uma vogal
        if caractere in vogais:
            contador += 1

    # outra forma de fazer
    # for caractere in s:
    #     if caractere == 'a' or caractere == 'e' or caractere == 'i' or caractere == 'o' or caractere == 'u':
    #         contador += 1
    
    return contador


# Exemplo de uso:
if __name__ == "__main__":
    texto = input("Digite um texto para contar as vogais: ")
    resultado = contarvogais(texto)
    print(f"O texto possui {resultado} vogais.")