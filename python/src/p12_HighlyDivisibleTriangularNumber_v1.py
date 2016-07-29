import time
from time import sleep
 
def num_divisors(n):
    # n = 10
    if n % 2 == 0: n = n/2
    # n = 5
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    # n = 1
    divisors = divisors * (count + 1)
    # divisor = 1
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        divisors = divisors * (count + 1)
        p += 2
    return divisors
 
def find_triangular_index(factor_limit):
    n = 1
    lnum, rnum = num_divisors(n), num_divisors(n+1)
    print "lnum: " + str(lnum) + " rum: " + str(rnum)
    print "***********>>>>>>>><<<<<<<**********"
    sleep(1)
    while lnum * rnum < 500:
        n += 1        
        print "Round: " +  str(n)        
        lnum, rnum = rnum, num_divisors(n+1)
        print "lnum: " + str(lnum) + " rum: " + str(rnum)
        sleep(1)
    return n
 
start = time.time()
index = find_triangular_index(500)
print "The index: " + str(index)
sleep(1)
triangle = (index * (index + 1)) / 2
elapsed = (time.time() - start)
 
print "result %s returned in %s seconds." % (triangle,elapsed)