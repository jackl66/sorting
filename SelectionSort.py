# simple selection sort
def run(array):
    for index in range(len(array)):
        min = index
        # find minimum element
        for j in range(index + 1, len(array)):
            if array[min] > array[j]:
                min = j
        # swap
        temp = array[min]
        array[min] = array[index]
        array[index] = temp

    return array
