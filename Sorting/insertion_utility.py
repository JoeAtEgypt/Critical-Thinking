from .swap_utility import swap


# arr = [11, 49, 1, 44, 19, 28, 10, 46, 4, 22]


def insertion_sort(arr, size):
    for i in range(1, size):
        unsorted_num = arr[i]
        for j in range(i-1, -1, -1):
            if unsorted_num < arr[j]:
                arr[j+1] = arr[j]

