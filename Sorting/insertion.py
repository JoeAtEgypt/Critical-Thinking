

def insertion_sort(arr, size):
    for i in range(1, size):
        k = 0
        unsorted_num, sorted = arr[i], True
        for j in range(i - 1, -1, -1):
            if unsorted_num < arr[j]:
                arr[j + 1] = arr[j]
                k = j
                sorted = False
        if not sorted:
            arr[k] = unsorted_num


def enhanced_insertion_sort(arr, size):
    if size <= 1:
        return

    for i in range(1, size):
        key = arr[i]
        j = i - 1
        while j > -1 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
