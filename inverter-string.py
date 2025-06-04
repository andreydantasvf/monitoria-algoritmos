def inverterstring(s):
    """
    Função recursiva que recebe uma string s e retorna a string invertida
    """
    # Função auxiliar recursiva que inverte a string
    def rec(i: int):
        if i < 0:
            return ""
        # Pega o caractere na posição i e concatena com o resultado da chamada recursiva
        return s[i] + rec(i - 1)

    return rec(len(s) - 1)
# Exemplo de uso:
if __name__ == "__main__":
    texto = input("Digite um texto para inverter: ")
    
    texto_invertido = inverterstring(texto)
    
    print(f"Texto original: {texto}")
    print(f"Texto invertido: {texto_invertido}")
