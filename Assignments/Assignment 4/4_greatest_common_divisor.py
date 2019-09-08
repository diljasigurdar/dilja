m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line

if m > n:
    small = n
else:
    small = n

gcd = 0

for x in range(1, small +1):
    if ((n % x == 0) and (m % x == 0)):
        if gcd > 0:
            gcd = x
print(gcd)
    





#Write a Python program using a for loop, that given two integers as input, prints the greatest common divisor (GCD) of them.

#GCD is the largest integer that divides each of the two integers.

#For example, given the numbers 12 and 15, the output will be:
#3