arr = [37, 45, 39, 49, 43, 5, 20, 19, 38, 30]


def merge(arr_1, arr_2):
    merged_arr = []
    i, j = 0, 0
    # print(arr_1)
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


def merge_sort(arr, l, h):
    print(l, h)
    print(arr)
    mid = (h - l) // 2
    if mid < 1:
        return arr
    print(f"mid: {mid}")

    sorted_left_arr = merge_sort(arr[l:mid], l, mid)
    sorted_right_arr = merge_sort(arr[mid + 1 : h], mid + 1, h)

    return merge(sorted_left_arr, sorted_right_arr)


print(merge_sort(arr=arr, l=0, h=(9 - 0) // 2))
