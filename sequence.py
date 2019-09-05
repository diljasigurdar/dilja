n = int(input("Enter the length of the sequence: ")) # Do not change this line
first = 1
second = 2
third = 3
sum_n = 0
counter = 1
current = 0

if n >= 1:
    print(1)
if n >= 2:
    print(2)
if n >=3:
    print(3)

while counter <= (n - 3):
    current = first + second + third
    third, second, first = current, third, second
    print(current)
    counter += 1
   



    
