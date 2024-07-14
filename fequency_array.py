arr = [1, 3, 2, 4, 2, 1]


def frequency(arr):
    freq = {}

    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    return freq


if __name__ == "__main__":
    print(frequency(arr))
