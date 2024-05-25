def search_min_indice(list):
    min = list[0]
    min_indice = min

    for indice in range(1, len(list)):
        if list[indice] < min:
            min = list[indice]
            min_indice = indice

    return min_indice


list = [1, 3, 5, 7, 9]
search_min_indice = search_min_indice(list)

print(search_min_indice)
