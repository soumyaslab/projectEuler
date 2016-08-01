import time

def collatzproblem(range):
    arr = []
    while range > 1:
        if range % 2 == 0:
            #print "Even number: " + str(range)
            range = range/2            
        else:
            #print "Odd number: " + str(range)
            range = (3*range ) + 1
            
        arr.append(range)
    return arr
        
####### MAIN  CODE #######

num = int(raw_input("Enter your range: "))

start = time.time()

if (num <= 0):
    print "Invalid entry, Enter a valid positive number."
    exit()
else:
    print "You have entered: " + str(num)
    
collatz = {}

while (num >= 1):
    print "Num is: " + str(num)
    
    collatz[num] = {}
    collatz[num]['arr'] = collatzproblem(num)
    collatz[num]['length'] = len(collatz[num]['arr'])
    highest = 0
    num -= 1

final_hey = 0
    
for i in collatz.keys():
    if collatz[i]['length'] > highest:
        highest = collatz[i]['length']
        final_key = i
    elif (collatz[i]['length'] <= highest):
        pass

elapsed = (time.time() - start)

print "The highest number of list is: " + str(final_key)
print "\nresult %s returned in %s seconds.\n" % (final_key,elapsed)
print collatz[final_key]




    