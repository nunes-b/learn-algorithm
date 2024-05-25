def search_min_indice(lst):
    min_val = lst[0]
    min_indice = 0

    for indice in range(1, len(lst)):
        if lst[indice] < min_val:
            min_val = lst[indice]
            min_indice = indice

    return min_indice


def order_arr(arr):
    sorted_arr = []
    arr_copy = arr[:]

    for _ in range(len(arr)):
        min_index = search_min_indice(arr_copy)
        sorted_arr.append(arr_copy.pop(min_index))

    return sorted_arr


arr1 = ["Melão", "Uva", "Mamão", "Banana", "Abobora", "Melancia", "Cereja"]
arr2 = [4, 55, 7, 89, 1, 2, 34, 5, 10]
sort_numbers = sorted(arr2)
sort_fruts = order_arr(arr1)
print(sort_fruts)
print(sort_numbers)
