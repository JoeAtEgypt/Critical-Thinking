arr = [1, 3, 2, 4, 2, 1]


def frequency_dict(arr):
    freq = {}

    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    return freq


def frequency_array(arr):
    freq = [0 for _ in range(max(arr)+1)]

    for num in arr:
        freq[num] += 1

    return freq


if __name__ == "__main__":
    print(frequency_dict(arr))
    print(frequency_array(arr))
