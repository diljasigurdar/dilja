num = int(input("Input an int: ")) # Do not change this line
theSum = 0

for x in range(1,num + 1):
    theSum = theSum + x
    print(theSum)


#Write a Python program using for loops that, given an integer n as input, prints all consecutive sums from 1 to n.

#For example, if 5 is entered, the program will print five sums of consecutive numbers:

#1 = 1
#1 + 2 = 3
#1 + 2 + 3 = 6
#1 + 2 + 3 + 4 = 10
#1 + 2 + 3 + 4 + 5 = 15

#Print only each sum, not the arithmetic expression.