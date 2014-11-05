import math

filename = 'QuickSort.txt'
lines = open(filename, 'r').readlines()
int_list = [int(line.strip('\r\n')) for line in lines]
#print int_list[0:10]

"""def quicksort(input_array):

    if not input_array: return input_array, 0
    if len(input_array) == 1:
        return input_array, 0
    else:
        pivot = input_array[0]
        less = [number for number in input_array if number < pivot]
        greater = [number for number in input_array if number > pivot]
        return quicksort(less)[0] + [pivot] + quicksort(greater)[0] \
                , len(less) - 1 + len(greater) - 1 + quicksort(less)[1] \
                + quicksort(greater)[1]
        print less
        print greater
print int_list[1:10]
print quicksort(int_list)[1]"""

class quicksort:
    comparisons = 0
    input_array = []
    def qsort(self,L):
        if len(L) <= 1:
            return L 
        self.comparisons = self.comparisons + len(L) - 1
        
        """tmp = L[0]
        L[0] = L[-1]
        L[-1] = tmp"""
        anticipates =  [L[0], L[1], L[int(math.floor((len(L) - 1.0)/2))]] 
        anticipates.sort()
        tmp = anticipates[1]
        L[0] = tmp
        pivot = L.index(tmp)
        L[pivot] = L[0]
        less = [lt for lt in L[1:] if lt < L[0]]
        if len(less) >1:
            less[0] ^= less[-1]
            less[-1] ^= less[0]
            less[0] ^= less[-1]
        return self.qsort(less) + L[0:1] + \
                self.qsort ([ge for ge in L[1:] if ge > L[0]])
                

x = quicksort()
print x.qsort(int_list)
print x.comparisons
