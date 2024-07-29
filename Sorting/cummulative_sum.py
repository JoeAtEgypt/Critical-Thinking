arr = [1, 3, 9, 5, 7, 2, 4, 1]


def prefix_sum(arr):
    size = len(arr)
    pre_sum = [arr[0]]

    for i in range(1, size):
        pre_sum.append(arr[i] + pre_sum[i - 1])

    return pre_sum


def sum(pre, left, right):
    if left == 0:
        return pre[right]
    if left <= right:
        return pre[right] - pre[left - 1]
    else:
        print("the left index must be smaller than or equal right index")
        return -1


if __name__ == "__main__":
    pre_sum = prefix_sum(arr)
    print(pre_sum)
    print(sum(pre_sum, 1, 4))
    print(sum(pre_sum, 0, 7))
    print(sum(pre_sum, 4, 4))
    print(sum(pre_sum, 7, 4))
