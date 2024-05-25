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


arr1 = [11, 1, 90, 3, 5, 7, 9]
sorted_arr = order_arr(arr1)
print(sorted_arr)
