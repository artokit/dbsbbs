f = open('stiki.txt')
f1 = open('tw.txt', 'w')
for line in f:
    r = line.split(' ')[1]
    f1.write('1.2-2 ' + r)
