top_num = int(input("Upper number for the range: ")) # Do not change this line
sumOfDivisor = 0
perfect_num = 0


for x in range(1, top_num):
    for i in range(1, x):
        if x % i == 0:
            sumOfDivisor += i   
    if x == sumOfDivisor:
        print(x)
    sumOfDivisor = 0


#Write a Python program using for loops that, given an integer n, prints all the perfect numbers from 1 to n.

#A perfect number is an integer whose sum of integer divisiors (excluding the number itself) add up to the number.

#For example, 6 is a perfect number because the sum of its integer divisors (1+2+3) is equal to 6.