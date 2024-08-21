from google.protobuf.text_encoding import string


def solve(target, tracks, index=0, curr_sum=0, cd_tracks=None):
    if cd_tracks is None:
        cd_tracks = []

    # base case
    if curr_sum > target or index == len(tracks):
        cd_tracks = None
        return bool(cd_tracks)

    if curr_sum == target:
        cd_tracks.append(tracks[index])
        return cd_tracks

    # opt1: take
    if bool(solve(target, tracks, index + 1, curr_sum + tracks[index], cd_tracks)):
        return cd_tracks

    # opt2: leave
    return solve(target, tracks, index + 1, curr_sum, cd_tracks)


# def log(target, tracks):
#     cd_tracks = solve(target, tracks)
#
#     if bool(cd_tracks):
#         str = string.
#         print(cd_tracks)


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        target, p, *tracks = list(map(int, input().split()))

        log(target, tracks)
