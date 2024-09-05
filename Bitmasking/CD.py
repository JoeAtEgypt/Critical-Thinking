import sys
from itertools import combinations

from Bitmasking.is_bit_on import is_bit_on


def solve(target, n, tracks):
    curr_sum = 0
    curr_tracks = []
    currents = {"curr_tracks": [], "curr_sum": 0}

    for mask in range(2 << n):
        for i in range(n):
            if is_bit_on(mask, i):
                curr_sum += tracks[i]
                curr_tracks.append(tracks[i])
        if currents["curr_sum"] < curr_sum <= target and len(curr_tracks) >= len(
            currents["curr_tracks"]
        ):
            currents["curr_sum"] = curr_sum
            currents["curr_tracks"] = []
            currents["curr_tracks"].extend(curr_tracks)
        curr_sum = 0
        curr_tracks = []

    return currents["curr_tracks"], currents["curr_sum"]


def load_input():
    while True:
        cur_input = next(sys.stdin)
        print("input: ", cur_input)
        if bool(cur_input.strip()):
            target, p, *tracks = map(int, cur_input.split())
            yield target, p, tracks
        else:
            break
        # next(sys.stdin)  # Skip blank line


if __name__ == "__main__":
    for target, p, tracks in load_input():
        sol_tracks, sol_sum = solve(target, p, tracks)
        print(" ".join(map(str, sol_tracks)), "sum:", sol_sum)

# t = int(input())
#
# for _ in range(t):
#     target, p, *tracks = list(map(int, input().split()))
#
#     sol_tracks, sol_sum = solve(target, p, tracks)
#     print(" ".join(map(str, sol_tracks)), "sum:", sol_sum)
