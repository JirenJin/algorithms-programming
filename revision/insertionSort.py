def insertionSort(array):
    for i in range(len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j = j - 1

if __name__ == '__main__':
    import random
    test = [random.randrange(10000) for row in range(100)]
    print test
    insertionSort(test)
    print test
