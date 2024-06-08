from inputs import *

from Sorting.insertion import insertion_sort, enhanced_insertion_sort
from Sorting.bubble import bubble_sort
from Sorting.selection import selection_sort

if __name__ == "__main__":
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
