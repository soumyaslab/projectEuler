import os

def isprime(n):
    for a in range(2,n):
        if ( n % a ) == 0:
            return False
    else:
        return True

r = int(raw_input("Enter the range: "))
sum1 = 0
for i in range(2,r + 1):
    #print "Counter: %d " % i
    if isprime(i):
        sum1 += i
        os.system('clear')
        print "Prime number: %d, Sum: %d " % (i,sum1)
        
print "Sum of all prime number bellow %d is: %d" % (r,sum1)