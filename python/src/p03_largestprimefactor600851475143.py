import sys
# from _ast import Num
# print "Max integer: %s" % sys.maxint

testnumber = int(raw_input("Please enter the number for test: "))
num,largenum, highestnum = 1,0,0

#print "Type: %s" % type(testnumber)
 
def isprime(n):
    for a in range(2,n):
        if ( n % a ) == 0:
            return False
    else:
        return True

def isfactor(n):
    if ((testnumber % n) == 0):
        return True
    else:
        return False
 
#while (num < testnumber):
num = 2
while (num < testnumber):
    print "Num: %s" % num
    if isprime(num):
        if (isfactor(num) and num <= (testnumber / 2)):
            highestnum = num
            #break
    num += 1
 
print "Highest prime number factor: %s " % highestnum

# num = 2
# divisor = 0
# 
# while (num <= testnumber/2):
#     if (testnumber % num == 0):
#         divisor = testnumber/num
#         print "Numbers: %s " % divisor
#         if isprime(divisor):
#             print "The highest primer factor: %s" % divisor
#             break
#     num += 1
    

#
#
# print "The number is: %s" % testnumber

# for i in range(1,testnumber):
#     print "Number: %s" % i
#     if i > 1:
#         for j in range(2,i):
#             if (i % j) == 0:
#                 break
#         else:
#             print "Prime Num: %s " % i
#             largenum = i


        
#print "Largest prime number: %s" % largenum
# 
# def isprime(n):
#     for i in range(2,n):
#         
