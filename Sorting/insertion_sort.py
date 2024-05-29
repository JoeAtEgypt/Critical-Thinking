
def swap(a, b):
    c = a
    a = b
    b = c


arr = [11, 49, 1, 44, 19, 28, 10, 46, 4, 22]


def insertion_sort(arr, size):
    for i in range(1, size):
        unsorted_num = arr[i]
        for j in range(i, -1, -1):
            if unsorted_num < arr[j]:
                swap(arr[i], arr[j])


insertion_sort(arr, 10)
print(arr)
