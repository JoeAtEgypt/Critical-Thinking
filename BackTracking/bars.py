
def is_there_possible_bar(target_length, lengths, index = 0, curr_sum=0):
    if curr_sum == target_length:
        return True

    if curr_sum > target_length or index == len(lengths):
        return False

    if is_there_possible_bar(target_length, lengths, index+1, curr_sum+lengths[index]):
        return True
    
    return is_there_possible_bar(target_length, lengths, index+1, curr_sum)

def solve_bars(test_cases):
    for target_length, bars in test_cases:
        if is_there_possible_bar(target_length, bars):
            print("YES")
        else:
            print("NO")    

def read_inputs():
    test_cases = []
    t = int(input())
    
    for _ in range(t):
        target_length = int(input())
        p = int(input())
        bars = list(map(int, input().split(maxsplit=p)))
        test_cases.append((target_length, bars))

    return test_cases

if __name__ == "__main__":
    test_cases = read_inputs()
    solve_bars(test_cases)


    