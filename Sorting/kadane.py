arr = [1, 3, -4, 5, -6, 4, 8, -7, 1]


def kadane(arr):
    size = len(arr)
    pre_sum = [arr[0]] if arr[0] >= 0 else [0]

    for i in range(1, size):
        sum = arr[i] + pre_sum[i-1]
        if sum < 0: pre_sum.append(0)
        else:   pre_sum.append(sum)

    return pre_sum

def largest_sum_range(kadane):
    max_index, maxi = 0, kadane[0]

    for i, num in enumerate(kadane):
        if maxi < num:
            maxi = num
            max_index = i

    for i in range(max_index, -1, -1):
        if kadane[i] == 0:
            return i, max_index
    
    return 0, max_index 


if __name__ == "__main__":
    pre_sum = kadane(arr)
    print(pre_sum)
    print(largest_sum_range(pre_sum))
    

    

