def countInversions(array):
    length = len(array)
    if length == 1:
        return 0, array
    mid = len(array) / 2
    x, left = countInversions(array[:mid])
    y, right = countInversions(array[mid:])
    z, sortedArray = countSplitInversions(left, right)
    return x + y + z, sortedArray

def countSplitInversions(left, right):
    leftLen = len(left)
    rightLen = len(right)
    totalLen = leftLen + rightLen
    i, j, k = 0, 0, 0
    sortedArray = [None] * totalLen
    count = 0

    while i < leftLen and j < rightLen:
        if left[i] <= right[j]:
            sortedArray[k] = left[i]
            i += 1
        else:
            sortedArray[k] = right[j]
            j += 1
            count += leftLen - i
        k += 1

    sortedArray[k:] = left[i:] + right[j:]

    return count, sortedArray


if __name__ == '__main__':
    import random
    test = [random.randrange(10000) for row in range(100)]
    print test
    inversions, sortedArray = countInversions(test)
    print sortedArray
    print inversions
    # it's very important to use int() or, '5' will be larger than '10000'
    #lines = [int(line.strip('\r\n')) for line in \
    #        open('../Question1/IntegerArray.txt', 'r').readlines()]
    #print lines[:100]
    #inversions, sortedArray = countInversions(lines)
    #print sortedArray[:100]
    #print inversions
