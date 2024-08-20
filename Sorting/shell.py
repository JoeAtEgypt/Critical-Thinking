array = [19, 2, 31, 45, 30, 11, 121, 27]


def shell_sort(arr, size):
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j = j - gap
        gap = gap // 2
    return arr


print(shell_sort(array, len(array)))
