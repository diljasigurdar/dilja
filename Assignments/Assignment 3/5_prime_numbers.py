n = int(input("Input a natural number: ")) # Do not change this line
counter = 2
prime = True
# Fill in the missing code below

# Do not changes the lines below
while counter < n:
    if n % counter != 0:
        prime = True
        break
    if n % counter == 0:
        prime = False
        break
if n == 1:
    print("Not prime")

if prime:
    print("Prime")
else:
    print("Not prime")





#A prime number is a whole number greater than 1 whose only factors are 1 and itself.

#Write a program using a while statement, that given an int as the input, prints out 
# "Prime" if the int is a prime number, otherwise it prints "Not prime".