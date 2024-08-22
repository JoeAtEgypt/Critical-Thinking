from collections import defaultdict

arr = [1, 3, 2, 4, 2, 1]


def frequency_dict(arr):
    freq = defaultdict(int)

    for i in arr:
        freq[i] += 1

    return dict(freq)


def frequency_array(arr):
    freq = [0 for _ in range(max(arr) + 1)]

    for num in arr:
        freq[num] += 1

    return freq


if __name__ == "__main__":
    print(frequency_dict(arr))
    print(frequency_array(arr))
