def solve(target, bars, index=0, curr_sum=0):
    # base cases
    if curr_sum == target:
        return True
    if curr_sum > target or index == len(bars):
        return False

    # op1: take
    if solve(target, bars, index + 1, curr_sum + bars[index]):
        return True  # if valid state recurse

    # op1: leave
    return solve(target, bars, index + 1, curr_sum)  # if valid state recurse


def log(target, bars):
    if solve(target, bars):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        target = int(input())
        p = int(input())

        bars = list(map(int, input().split()))
        log(target, bars)
