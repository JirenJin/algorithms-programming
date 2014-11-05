"""read the input file containning an array of dictinct integers"""
filename = r'IntegerArray.txt'
int_list = []
lines = open(filename,'r').readlines()
int_list = [int(line.strip('\r\n')) for line in lines]
#print int_list[:10]

def sort_count_inversions(input_array):
    """function for computing inversion"""
    #divide and conquer, divide the problems into smaller subproblems
    first = input_array[:len(input_array)/2]
    second = input_array[len(input_array)/2:]
    if len(input_array) == 1:
        return 0
    else:
	#sort and compute the inversions of the first and second part of input array seperately
        first_Part_Inversions =  sort_count_inversions(first)
        """sort_count_inversions(input_array[:len(input_array)/2])"""
        second_Part_Inversions = sort_count_inversions(second) 
        """sort_count_inversions(input_array[len(input_array)/2:])"""
#        print first,second

        #print input_array
        #print "this is sorted input_array"
        """to update the input_array, we have to assign the value of input array.
        Be careful. you can't just use input_array = first + second, because
        you also want to change the int_list's elements' value, and then you
        should use slice, to update the value for higher recursive loop"""
        input_array[:len(input_array)/2] = first
        input_array[len(input_array)/2:] = second
        #input_array = first + second

        # finish sorting the whole input_array with first and second part, then compute the split inversions of these two parts
        split_Part_Inversions = count_split_inv(input_array)
        
        # return the sum of the three parts as result of this subroutine 
        return first_Part_Inversions + second_Part_Inversions + split_Part_Inversions


def count_split_inv(input_array):
    """compute the split inversions of 2 parts of input array
       as well as sorting the 2 parts together"""
    #print input_array
    #print "this is input array"   
    output_array = [0] * len(input_array)
    #print output_array
    #print "this is output array"
    first_part = input_array[:len(input_array)/2]
    second_part = input_array[len(input_array)/2:]
    #print first_part
    #print second_part
    #print "these are 2 parts"

    # in case first_part[i] or second_part[j] becomes out of indexes, add an infinity at the end of each array. and it will be only used in comparing.
    first_part[len(first_part):] = [float("inf")]
    second_part[len(second_part):] = [float("inf")]
    i = 0
    j = 0
    split_inversions = 0 
    for k in range(0,len(input_array)):
    #    print k
    #    print "this is k"
        if first_part[i] < second_part[j]:
    #        print k,i,j
            output_array[k] = first_part[i]
    #        print output_array
            i = i + 1
        else: 
    #        print k,i,j
            output_array[k] = second_part[j]
    #        print output_array
            j = j + 1
            split_inversions = split_inversions + len(first_part) - i - 1 

    # important! to update the value, notice the slice!
    input_array[:] = output_array
#    print input_array
#    print "this the newer input_array"
#    print split_inversions
    #print output_array
    return split_inversions

print sort_count_inversions(int_list)
