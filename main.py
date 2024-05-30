from Sorting.insertion_utility import insertion_sort

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

    insertion_sort(arr, size)

    print(f"After Sorting: ")
    print_array(arr)
