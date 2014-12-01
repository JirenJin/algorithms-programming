from heapq import *

def median(integer_list):
    median_value = [None] * len(integer_list)
    hmax = []
    hmin = []
    if integer_list[0] <= integer_list[1]:
        heappush(hmax, -integer_list[0])
        heappush(hmin, integer_list[1])
        median_value[0] = integer_list[0]
        median_value[1] = integer_list[0]
    else:
        heappush(hmax, -integer_list[1])
        heappush(hmin, integer_list[0])
        median_value[0] = integer_list[0]
        median_value[1] = integer_list[1]

#    print median_value
#    print hmax, hmin
    for i in range(2, len(integer_list)):
        if i % 2 == 0:
            if integer_list[i] <= nsmallest(1, hmin)[0]:
                heappush(hmax, -integer_list[i])
            else:
                heappush(hmax, -heappop(hmin))
                heappush(hmin, integer_list[i])
        else:
            if integer_list[i] >= -nsmallest(1, hmax)[0]:
                heappush(hmin, integer_list[i])
            else:
                heappush(hmin, -heappop(hmax))
                heappush(hmax, -integer_list[i])
        median_value[i] = -nsmallest(1, hmax)[0]
#        print median_value 
#        print hmax, hmin
    return median_value
# test
#integer_list = range(1, 11)

lines = [int(line.strip('\r\n')) for line in open('Median.txt', 'r').readlines()]
a = median(lines)
print sum(a) % 10000
