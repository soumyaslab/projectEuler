## Thanks to "Mike Molony"
## http://blog.dreamshire.com/project-euler-3-solution/


N = n = 600851475143 
p = 2

while (p*p <= n):
    if (n % p == 0):
        n //= p
        #print "N: %d" % n
    else:
        p += 2 if p>2 else 1   # after 2, consider only odd p
    #print "P: %d" % p

print "The largest prime factor of", N, "is", n

