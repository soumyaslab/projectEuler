
sqrofsum, sumofsqr = 0,0

for i in range(1,101):
    sumofsqr += (i*i)
    sqrofsum += i

sqrofsum *= sqrofsum

dif = sqrofsum - sumofsqr

print "Sum of sqr: %d " % sumofsqr
print "Sqr of sum: %d " % sqrofsum

print "Different between the sums: %d " % dif

