lista = [1, 3, 5, 7, 9]


def binary_search(lista, item):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


print(binary_search(lista, 7))
#

# Exercicio 1.1
"""
Suponha que você tenha uma lista com 128 nomes e esteja fazendo uma pesquisa 
binaria, qual seria o número máximo de etapas que você levaria para 
encontrar o nome desejado? 128/2 = 64/2 = 32/2 = 16/2 = 8/2 = 4/2 = 2/2 = 1 
Ou seja, o número maximo de etapas que dá 7 tentativas.
Fatoração de 128 por 2, ou seja log de 128 = 7.
"""
# Exercicio 1.2
"""
Suponha que você duplique o tamanho da lista. Qual seria o número maximo de
 etapas agora? 8  tentativas. 
 fatoração de 256/2 = 128/2 = 64/2 = 32/2 = 16/2 = 8/2 = 4/2 = 2/2. = 8.
"""
