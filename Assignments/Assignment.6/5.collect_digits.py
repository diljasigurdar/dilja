import string

a_str = input("Input a string: ")

for ch in a_str:
    if ch in string.digits:
        print(ch, end='')
 







#Given a string of any length, extract the numbers (digits) and print them on one line without spaces.
#Hint 1: start with an empty string
#Hint 2: isdigit() is your friend.
#For example, given this string:
#some 1! likes 2 put 14 digits, in 3 strings
#the output will be
#12143