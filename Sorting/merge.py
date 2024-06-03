arr = [18, 34, 20, 35, 10, 37, 43, 29, 3, 6]


def merge(arr_1, arr_2):
    merged_arr = []
    i, j = 0, 0
    while i < len(arr_1) or j < len(arr_2):
        if arr_1[i] < arr_2[j]:
            merged_arr.append(arr_1[i])
            i += 1
        else:
            merged_arr.append(arr_2[j])
            j += 1
        if i == len(arr_1):
            merged_arr += arr_2[j:]
            break
        elif j == len(arr_2):
            merged_arr += arr_1[i:]
            break
    return merged_arr


def merge_sort(arr):
    size = len(arr)
    if size == 1:
        return arr
    mid = (size - 1)// 2

    sorted_left_arr = merge_sort(arr[:mid+1])
    sorted_right_arr = merge_sort(arr[mid + 1::])

    return merge(sorted_left_arr, sorted_right_arr)


print(merge_sort(arr))
