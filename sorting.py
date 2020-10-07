import sys
import numpy as np
import time


import InsertionSort
import SelectionSort
import QuickSort


# create the expected array
def array_builder(size, category):
    array = np.ones(size, dtype=int)
    # if it asks for constant elements, stop here
    if category == 'c':
        return array
    elif category == 's':
        i = 0
        for element in range(len(array)):
            array[element] += i
            i += 1
        return array
    else:
        # random element from 1 to 10
        array = np.random.randint(1, 10, size)
        return array


# check if the array is sorted after
# returning
def isSorted(array):
    index = 0
    while index < len(array) - 1:
        if array[index] > array[index + 1]:
            print("the algorithm doesn't sort the array")
            print(array)
            return False
        index += 1
    print('Data correctly sorted after running algorithm.')
    print(array)
    return True


def main():
    # simple input check
    if len(sys.argv) != 4:
        print("invalid input")
        return 0
    # which sorting algorithm to use
    algorithm = sys.argv[1]
    # size of the array
    try:
        size = int(sys.argv[2])
    except:
        print("invalid input")
        return 0

    # type of element
    category = sys.argv[3]
    if algorithm not in ['q', 'i', 's']:
        print("invalid input")
        return 0
    if category not in ['s', 'c', 'r']:
        print("invalid input")
        return 0
    array = array_builder(size, category)

    start = 0
    end = 0
    # run algorithm accordingly and mark time
    if algorithm == 'q':
        algorithm = "QuickSort"
        start = time.time()
        sys.setrecursionlimit((2**31)-1)
        print(sys.getrecursionlimit())
        result = QuickSort.run(array,0,size)
        print(2)
        end = time.time()
    elif algorithm == 'i':
        algorithm = "InsertionSort"
        start = time.time()
        result = InsertionSort.run(array)
        end = time.time()
    else:
        algorithm = "SelectionSort"
        start = time.time()
        result = SelectionSort.run(array)
        end = time.time()
    # check if it is sorted
    isSorted(result)

    print("Chosen algorithm:", algorithm)
    print("duration: ", end - start, " in s")


if __name__ == '__main__':
    main()
