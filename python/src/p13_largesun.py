
fd = open("../conf/13problemmatrix.txt")
sum = 0
for line in fd.readlines():
    line = line.rstrip('\n')
    num = long(line)
    sum = sum + num

fd.close()

print "The num is: " + str(sum)
print "Length of number: " + str(len(str(sum)))