maze = [
#    0     1    2    3    4    5
    ["R", ".", "#", "#", ".", "#"], # 0 
    ["#", ".", ".", ".", ".", "#"], # 1
    ["#", ".", "#", "#", ".", "#"], # 2
    [".", ".", ".", ".", ".", "."], # 3
    ["#", ".", "#", ".", "T", "#"], # 4
]
ans = 0  

def is_valid(rr, rc):
    return (rc < 6 and rr < 5) and maze[rr][rc] != "#" 

def ways_from_rat_to_cheese(rr, rc):
    global ans
    # Base Case
    if maze[rr][rc] == "T":
       ans += 1

    # Option 1: move right if valid state
    rc += 1     # DO
    if is_valid(rr, rc): ways_from_rat_to_cheese(rr, rc)  # recurse if valid state
    rc -= 1     # UNDO

    # Option 1: move right if valid state
    rr += 1     # DO
    if is_valid(rr, rc): ways_from_rat_to_cheese(rr, rc)  # recurse if valid state
    rr -= 1     # UNDO

ways_from_rat_to_cheese(0,0)
print(ans)
