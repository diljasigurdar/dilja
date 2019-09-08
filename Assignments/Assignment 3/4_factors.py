n = int(input("Input an int: ")) # Do not change this line
counter = n
divisor = 0

# Fill in the missing code below
while counter <= n:
    if n % counter == 0:
        divisor = n // counter
        print(divisor)
    counter -= 1


