# simple insertion sort
def run(array):
    for index in range(1,len(array)):
        current = array[index]
        prev = index - 1
        while prev >= 0 and current < array[prev]:
            array[prev + 1] = array[prev]
            prev -= 1
        array[prev + 1] = current
    return array
