arr = [34, 18, 13, 32, 35, 4, 37, 12, 34, 43]


def quick_sort(arr, l, h):
    if l < h:
        i, j = l, h
        pivot = arr[l]
        pivot_index = l

        while i < j:
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            if pivot == arr[j]:
                i += 1
                pivot_index = j
            else:
                j -= 1
                pivot_index = i

        quick_sort(arr, l, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, h)


quick_sort(arr, 0, len(arr) - 1)
print(arr)
