import sys
from itertools import combinations

from Bitmasking.is_bit_on import is_bit_on


def solve(target, n, tracks):
    curr_sum = 0
    currents = {"curr_tracks": [], "curr_sum": 0}

    for mask in range(2 << n):
        for i in range(n):
            if is_bit_on(mask, i):
                curr_sum += tracks[i]
                currents["curr_tracks"].append(tracks[i])

        if currents["curr_sum"] < curr_sum <= target:
            currents["curr_sum"] = curr_sum
        currents = {"curr_tracks": [], "curr_sum": 0}

    return currents["curr_tracks"], currents["curr_sum"]


# def load_input():
#     while True:
#         target, p, *tracks = map(int, next(sys.stdin).split())
#         yield target, p, tracks
#         next(sys.stdin)  # Skip blank line


# if __name__ == "__main__":
#     for target, p, tracks in load_input():
#         print(target, p, tracks)
#         sol_tracks, sol_sum = solve(target, p, tracks)
#         print(" ".join(map(str, sol_tracks)), "sum:", sol_sum)

t = int(input())

for _ in range(t):
    target, p, *tracks = list(map(int, input().split()))

    log(target, tracks)
