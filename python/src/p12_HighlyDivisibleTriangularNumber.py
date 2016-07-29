from time import sleep

def find_numcount(count):
    
    num = 1
#     counter = 0
    
    while (True):
        #print "1st loop .."
        #sleep(1)
        counter = 0
        divided_by = 1
        print "*********************************************"
        print "Divisor set for number: " + str(num)
        print "*********************************************"
        while (True):
            #sleep(1)
            #print "2nd loop .."
#             print "Num: " + str(num) + " and divided_by: " + str(divided_by) 
            if divided_by <= int(num/2):
                if not (num % divided_by):
                    #print "1st if statement .."
                    counter += 1
                    print "Num: " + str(num) + " and divided_by: " + str(divided_by) 
                    print "Counter is: " + str(counter)
                if counter == count:
                    #print "2nd if statement .."
                    return num
                divided_by += 1
            else:
                break
        num += 1
        
no_counters = int(raw_input("Enter the required count: "))
final_num = 0
if not (no_counters >= 2):
    print "Enter number more than 1 ..."
else:
    final_num = find_numcount(no_counters)
    
print "The number is: " + str(final_num)

