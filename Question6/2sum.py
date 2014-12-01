filename = 'algo1-programming_prob-2sum.txt'
lines = [int(line.strip('\r\n')) for line in open(filename, 'r').readlines()]
count = 0
t = set()
lines.sort()
i = 0
j = len(lines) - 1
flag = 0
end = len(lines) - 1

for i in range(len(lines)):
    j = end
    if i == j:
        break
    while(abs(lines[i] + lines[j]) > 10000):
        if lines[i] + lines[j] < -10000:
            break
        j = j - 1
    end = j
    while(abs(lines[i] + lines[j]) <= 10000):
        if lines[i] != lines[j]:
            t.add(lines[i] + lines[j])
        j = j - 1
    continue
print t        
print len(t)   
'''part = [[] for row in range(50000)]
for line in lines:
    i = abs(line)/2000000
    part[i].append(line)
    
for i in range(len(part)):
    for x in part[i]:
        if -10000 <= x + y and x + y <= 10000 and x != y:
            t.append(x + y)
'''            

'''for t in range(-10000, 10001):
    find = 0
    for i in range(len(part)):
        if find == 1:
            break
        hasht = {}
        for x in part[i]:
            hasht[x] = True
        for x in part[i]:
            y = t - x
            if y in hasht and y != x:
                count = count + 1
                find = 1
                break
        
print count
'''
'''def two_sums(A, t):
    hash_table = dict()
    for x in A:
        hash_table[x] = True
    for x in A:
        if (t - x) in hash_table:
            if (t - x) != x:
                return(x, t-x)
    else:
        return None
for i in range(len(part)):
    for t in range(-10000, 10001):
        if two_sums(part[i], t) == True:
            count += 1
print count
'''
