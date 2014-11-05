import math

filename = 'QuickSort.txt'
lines = open(filename, 'r').readlines()
# this is input integer array
int_list = [int(line.strip('\r\n')) for line in lines]

class quicksort:
    # total comparisons of quicksort procedure
    comparisons = 0
    # L is array to sort, l is the start index, r is the end index 
    def qsort(self, L, l, r):

        if len(L[l : r + 1]) <= 1:
            return L 
#       print L
#       print l
#       print r

        self.choose_pivot(L, l, r, 2)
        # simply compute the comparisons: length of subarray - 1
        self.comparisons = self.comparisons + r - l 
#       print r-l
#       print "this is r-l"
        # p_index is the index of pivot
        p_index = self.partition(L, l, r)  #partition using pivot = 0
#       print index 
#       print L,'\n', l,'\n', index -1
        # sort the two partions
        self.qsort(L, l, p_index - 1)
        self.qsort(L, p_index + 1, r)
        return L
    def partition(self,A,l,r):
        p = A[l]
        i = l + 1
        for j in range(l + 1, r + 1):

            """ if A[j] < pivot, then swap it to first element of 
            Greater Partition, and plus 1 to i. Else do nothing."""
            if A[j] < p:   
                if i != j:
                    A[j] ^= A[i]
                    A[i] ^= A[j]
                    A[j] ^= A[i]
                i = i + 1
        # swap the last element of Less Partition to the pivot 
        if (i-1) != l:
            A[l] ^= A[i-1]
            A[i-1] ^= A[l]
            A[l] ^= A[i-1]
        p_index = i - 1
        # return pivot's index for the subarray sort
        return p_index 
                    
    def choose_pivot(self, L, l, r, mode):
        if mode == 1:
            return
        elif mode == 2:
            L[l] ^= L[r]
            L[r] ^= L[l]
            L[l] ^= L[r]
        elif mode == 3:
            anticipates =  [L[l], L[r], L[l + int(math.floor((r - l) / 2))]]
            anticipates.sort()
            pivot = anticipates[1]
            index = L.index(pivot)
            L[index] = L[l]
            L[l] = pivot
        else:
            return

x = quicksort()
print x.qsort(int_list, 0, len(int_list) - 1)
print x.comparisons
