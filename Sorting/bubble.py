

def bubble_sort(arr, size):
    count = 0
    swapped = True

    while swapped:
        swapped = False
        for i in range(size - count - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        count += 1
