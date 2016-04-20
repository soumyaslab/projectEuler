
counter = 1

def isprime(n):
    for a in range(2,n):
        if ( n % a ) == 0:
            return False
    else:
        return True

num = 2
theprimenumber = 0

while True:
#     print "Counter: %d " % counter
    if isprime(num):
        theprimenumber = num
        print "Counter: %d, Prime number: %d " % (counter, theprimenumber)
        if counter <= 10001:
            counter += 1
        else:
            break
    num += 1

print "The 10001th prime number is: %d " % theprimenumber