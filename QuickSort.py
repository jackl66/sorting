# simple insertion sort

def run(array, start, end,self=None):
    if start < end:
        splitPoint = partition(array, start, end)
        run(array, start, splitPoint)
        run(array, splitPoint + 1, end)
    return array


# find the median of three and sort the array
def partition(array, start, end):
    median = int((end - 1 - start) / 2)
    median = median + start
    left = start + 1
    # if (array[median] - array[end - 1]) * (array[start] - array[median]) >= 0:
    #     swap(array, start, median)
    # elif (array[end - 1] - array[median]) * (array[start] - array[end - 1]) >= 0:
    #     swap(array, start, end - 1)
    find_pivot(array, median, start)
    pivot = array[start]
    for right in range(start, end):
        if pivot > array[right]:
            swap(array, left, right)
            left = left + 1
    swap(array, start, left - 1)
    return left - 1


# swapping two elements
def swap(array, a, b):
    array[a], array[b] = array[b], array[a]


# find the pivot and move it to index 0
def find_pivot(array, median, start):
    pivot = median
    # median of first, last, pivot
    if array[start] < array[-1]:
        if array[median] < array[start]:
            pivot = start
        elif array[-1] < array[median]:
            pivot = len(array) - 1
    # array[0] > array[- 1] as premise
    elif array[median] < array[-1]:
        pivot = len(array) - 1
    elif array[start] < array[median]:
        pivot = start
    # move pivot to index 0
    swap(array, start, pivot)

