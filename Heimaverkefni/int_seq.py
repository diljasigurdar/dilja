largestInt = 0
countEven = 0
countOdd = 0
cumulativeSum = 0
num = 0

while num >= 0:
    num = int(input("Enter an integer: "))
    if num <= 0:
        break
    if num % 2 == 1:
        countOdd += 1
    elif num % 2 == 0:
        countEven += 1
    if num > largestInt:
        largestInt = num
    cumulativeSum += num
    print("Cumulative total: ", cumulativeSum)

if largestInt != 0:
    print("Largest number: ", largestInt)
    print("Count of even numbers: ", countEven)
    print("Count of odd numbers: ", countOdd)