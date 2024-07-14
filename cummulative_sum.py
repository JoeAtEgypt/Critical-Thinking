arr = [1, 3, 9, 5, 2, 7, 4]


def prefix_sum(arr):
    size = len(arr)
    prefix_sum = [arr[0]]

    for i in range(1, size):
        prefix_sum.append(arr[i] + prefix_sum[i-1])

    return prefix_sum

if __name__ == "__main__":
    print(prefix_sum(arr))