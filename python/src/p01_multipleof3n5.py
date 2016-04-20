
upper_range = int(raw_input("Enter your range: "))

totalsum = 0

for n in range(upper_range):
    if ((not n%3) or (not n%5)):
        totalsum += n

print "Sum total: ", totalsum