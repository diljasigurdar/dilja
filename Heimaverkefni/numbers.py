for x in range(10,100):
    firstDigit = int(x / 10)                    
    secondDigit = x % 10
    sumOfDigits = firstDigit + secondDigit
    if (sumOfDigits ** 2) == x:
        print(x)

countOfDivisors = 0

for numberToCheck in range(1,100):
    for potentialDivisor in range(1,(x+1)):
        if numberToCheck % potentialDivisor == 0:
            countOfDivisors += 1
    if countOfDivisors == 10:
        print(numberToCheck)
    countOfDivisors = 0