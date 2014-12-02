def mergeSort(array):
    ''' Merge Sort, return a sorted array, stable sort.'''
    # base case
    if len(array) == 1:
        return array
    # recursive call mergeSort()
    else:
        midSplit = len(array)/2
        left = mergeSort(array[:midSplit])
        right = mergeSort(array[midSplit:])
        i, j, k = 0, 0, 0

        # when i, j hasn't reached the end of list, compare them and merge
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # after left or right list has reached the end, then 
        # merge the numbers which haven't been merged
        array[k:] = left[i:] + right[j:]

        return array

        '''if i < len(left):
            array[k:] = left[i:]
        if j < len(right):
            array[k:] = right[j:]
        '''

        '''for k in range(len(array)):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            if i >= len(left) and j < len(right):
                array[k + 1:] = right[j:]
                break
            if j >= len(right) and i < len(left):
                array[k + 1:] = left[i:]
                break
        '''
    
if __name__ == '__main__':
    import random
    test = [random.randrange(10000) for row in range(100)]
    mergeSort(test)
    print test
