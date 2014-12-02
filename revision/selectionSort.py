def selectionSort(array):
    for i in range(len(array)):
        tmp = array[i]
        smallest = i
        for j in range(i, len(array)):
            if array[j] < tmp:
                tmp = array[j]
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]

if __name__ == '__main__':
    import random
    test = [random.randrange(10000) for row in range(100)]
    print test
    selectionSort(test)
    print test

