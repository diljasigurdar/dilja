for x in range(10,100):
    firstDigit = int(x / 10)                    
    secondDigit = x % 10
    num = firstDigit + secondDigit
    if (num ** 2) == x:
        print(x)

count_of_divisors = 0

for x in range(1,100):
    for y in range(1,(x+1)):
        if x % y == 0:
            count_of_divisors += 1
    if count_of_divisors == 10:
        print(x)
    count_of_divisors = 0