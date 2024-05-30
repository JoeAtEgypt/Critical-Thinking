arr = [37, 45, 39, 49, 43, 5, 20, 19, 38, 30]


def selection_sort(arr, size):
    for i in range(size - 1):
        min_index = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]


selection_sort(arr, 10)
print(arr)