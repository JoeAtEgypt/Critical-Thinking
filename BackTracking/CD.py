
def get_CD(n, tracks, index=0, curr_sum=0, max=0):
    if index == 20 or curr_sum > n or index == len(tracks):
        return max
    option1 = get_CD(n, tracks, index+1, curr_sum+tracks[index], max)
    if max < option1:
        max = option1
    
    option2 = get_CD(n, tracks, index+1, curr_sum, max)
    if max < option2:
        max = option2

def solve_CD(test_cases):
    for n, tracks in test_cases:
        print(get_CD(n, tracks))
        # if get_CD(target_length, tracks):
            # print("YES")
        # else:
            # print("NO")    

def read_inputs():
    test_cases = []
    t = int(input())
    
    for _ in range(t):
        n, num_track, *tracks = list(map(int, input().split()))
        print(n, num_track, tracks)
        test_cases.append((n, tracks))

    return test_cases

if __name__ == "__main__":
    test_cases = read_inputs()
    solve_CD(test_cases)


    