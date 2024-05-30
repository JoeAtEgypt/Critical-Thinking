from Sorting.insertion import insertion_sort, enhanced_insertion_sort
from Sorting.bubble import bubble_sort
from Sorting.selection import selection_sort


def input_array():
    def input_int(prompt=""):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter an integer.")

    size = input_int("Enter a Size: ")
    array = list(map(int, input().split(" ", maxsplit=size)))

    return array, size


def print_array(arr):
    print([num for num in arr])


while True:
    arr, size = input_array()
    print(f"Before Sorting: ")
    print_array(arr)

    # insertion_sort(arr, size)
    # enhanced_insertion_sort(arr, size)

    # bubble_sort(arr, size)

    selection_sort(arr, size)

    print(f"After Sorting: ")
    print_array(arr)
