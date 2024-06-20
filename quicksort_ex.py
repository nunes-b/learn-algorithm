arr = [2, 1]
arr2 = [5, 4]
pivot = [3]


def quick_sort(array):
    if len(array) <= 0:
        return []

    if len(array) <= 2:
        return array
    else:
        pivo = array[0]
        menores = [x for x in array[1:] if x <= pivo]
        maiores = [x for x in array[1:] if x > pivo]

        return quick_sort(menores) + [pivo] + quick_sort(maiores)


print(quick_sort([10, 5, 2, 3]))
