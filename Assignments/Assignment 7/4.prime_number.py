# is_prime function definition goes here
num = int(input("Input an integer greater than 1: "))

# Call the function here and print out the appropriate message
def prime_number(x):
    counter = 2
    if x ==2:
        result = True
    while counter < x:
        if x % counter != 0:
            result = True
        if x % counter == 0:
            result = False
            break
        counter += 1
    return result

result = prime_number(num)
if result == True:
    print(num, "is a prime")
else:
    print(num, "is not a prime")
