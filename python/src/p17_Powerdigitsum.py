from num2words import num2words

range_num = int(raw_input("Enter your range for calculation: "))

char_count = 0
number_arr = []

for i in range(1,range_num + 1):
    word = num2words(i)
    number_arr.append(word)
    for c in word:
        if c == " " or c == '-':
            continue
        char_count += 1

print "The arr is: "
print number_arr
print "The character counts: " + str(char_count)