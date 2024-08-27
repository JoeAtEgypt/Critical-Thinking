from Bitmasking.is_bit_on import is_bit_on


def solve(target, bars):
    curr_sum = 0
    n = len(bars)
    for mask in range((2 << n)):
        for i in range(n):
            if is_bit_on(mask, i):
                curr_sum += bars[i]
        if curr_sum == target:
            return True
        curr_sum = 0

    return False


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        target = int(input())
        p = int(input())

        bars = list(map(int, input().split()))
        is_there_fit_bar = solve(target, bars)
        if is_there_fit_bar:
            print("YES")
        else:
            print("NO")
