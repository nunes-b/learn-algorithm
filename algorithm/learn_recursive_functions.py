lista = [2, 3, 7, 9, 10, 23]


def sum_list(lista):
    if not lista:
        return 0
    if not lista[0]:
        return 0

    return lista[0] + sum_list(lista[1:])


# print(sum_list(lista))


def count_list(lista):
    list = 1
    if not lista:
        return 0
    if not lista[0]:
        return 0

    return list + count_list(lista[1:])


# print(count_list(lista))


def higher_value(lista):
    if not lista:
        return 0
    if not lista[0]:
        return 0

    return max(lista[0], higher_value(lista[1:]))


# print(higher_value(lista))


def binary_search_recursive(lista, item):
    if not lista:
        return None

    if not lista[0]:
        return None

    if item == lista[0]:
        return 0

    return 1 + binary_search_recursive(lista[1:], item)


print(binary_search_recursive(lista, 23))
