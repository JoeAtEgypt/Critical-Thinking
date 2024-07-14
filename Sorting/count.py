from frequency import frequency_array
from cummulative_sum import prefix_sum

arr = [1, 2, 7, 4, 2, 4, 3, 2, 34, 43]
arr = [1, 2, 4, 3, 2, 3, 5, 2]

def count_sort(arr):
    freq = prefix_sum(frequency_array(arr))
    # print(freq)

    s_arr = [0 for _ in range(len(arr))]
    for num in arr:
        freq[num] -= 1
        s_arr[freq[num]] = num
    print(s_arr)


count_sort(arr)