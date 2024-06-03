arr = [18, 34, 20, 35, 10, 37, 43, 29, 3, 6]


def merge(a, b):
    merged_arr = []
    i, j = 0, 0
    size_a = len(a)
    size_b = len(b)
    while i < size_a and j < size_b:
        if a[i] < b[j]:
            merged_arr.append(a[i])
            i += 1
        else:
            merged_arr.append(b[j])
            j += 1

    if i == size_a:
        merged_arr += b[j:]
    elif j == size_b:
        merged_arr += a[i:]
        
    return merged_arr


def merge_sort(arr):
    size = len(arr)
    if size == 1:
        return arr
    mid = (size - 1)// 2

    sorted_left_arr = merge_sort(arr[:mid+1])
    sorted_right_arr = merge_sort(arr[mid + 1::])

    return merge(sorted_left_arr, sorted_right_arr)


# print(merge_sort(arr))
