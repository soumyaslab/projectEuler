
fiblist = []
rangefor = int(raw_input("Enter your range: "))
#totalsum = 0
fib2 = []

def fib(n):
    a,b = 1,2
    totalsum = 0
    #fiblist.append(a)
    for i in range(n - 1):
        if (b >= 4000000):
            break
        else:
            fib2.append(b)
            if not b%2:
                print "B: %s" % b
                fiblist.append(b)
                totalsum += b
            a,b = b, a+b
    return totalsum
    
##fib(rangefor)
print "Total sum of all fib number: %s" % fib(rangefor)
print "Total fib list: %s" % fiblist
print "Complete list: %s" % fib2