
num = 1
urange = int(raw_input("What is upper limit: "))
while True:
    #print "Num: %d" % num
    for i in range(1,urange + 1):
        if (num % i) != 0:
            break
        #print "i: %d" % i
    else:
        print "The number: %d " % num
        break
    num += 1