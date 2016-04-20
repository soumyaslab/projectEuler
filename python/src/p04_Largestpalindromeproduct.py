
def ispalindrome (n):
    m = n
    a = 0
    while (m != 0):
        a = m % 10 + a * 10
        m = m / 10
        
    if(n == a):
        #print "%d is a palindrome number." % n
        return True
    else:
        #print "%d is not a palindrom number." % n
        return False


## some globals      
a , b , pnum = 999,999,0
braker = False
maxp,maxa,maxb = 0,0,0

while (a > 99):
    b = a
    while(b > 99):
        pnum = a * b
        if (ispalindrome(pnum) and (pnum > maxp)):
            maxp = b * a
            maxa = a
            maxb = b
        b -= 1
    a -= 1

print "MAX Palindrome: a: %d  X  b: %d  =  %d " % (maxa,maxb,maxp)
