
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
        
a , b , pnum = 999,999,0
braker = False

#pnum = int(raw_input("Enter your number: "))

while (a > 99):
    b = 999
    while(b > 99):
        pnum = a * b
        if ispalindrome(pnum):
            print "%d is a palindrom number." % pnum
            print "a is: %d " % a
            print "b is: %d " % b
            braker = True
            break
        b -= 1
        
    if (braker == True):
        break
    a -= 1

#ispalindrome(pnum)