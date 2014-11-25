lines = open('test.txt', 'r').readlines()
graph = [line.strip('\r\n').split(' ') for line in lines]
file = open('test2.txt', 'w')
for line in graph:
    tmp = line[0]
    line[0] = line[1]
    line[1] = tmp
for item in graph:
    file.write("%s %s\n" % (item[0], item[1]))
