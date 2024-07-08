def recursive_sum(nums):
    size = len(nums)

    if size == 1:
        return nums[0]
    return recursive_sum(nums[0:size-1]) + nums[size-1]

if __name__ == "__main__":
    t = int(input())

    res = []

    for i in range(t):
        inputs = list(map(int, input().split()))
        size, arr = inputs[0], inputs[1:]
        res.append(recursive_sum(arr))

    for i in range(t):
        print(f"Case {i+1}: {res[i]}")
    