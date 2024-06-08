import random


def input_int(prompt=""):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def input_array():
    size = input_int("Enter a Size: ")
    array = list(map(int, input().split(" ", maxsplit=size)))

    return array, size


def input_array(size):
    return list(map(int, input().split(maxsplit=size)))


def input_integers(size):
    return map(int, input().split(maxsplit=size))


def print_array(arr):
    print([num for num in arr])
