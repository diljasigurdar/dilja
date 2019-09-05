n = int(input("Enter the length of the sequence: ")) # Do not change this line
first = 1
second = 2
third = 3
sum_n = 0
counter = 1

while counter <= n/3:
    print(first)
    print(second)
    print(third)
    first = first+second+third
    second = first+second+third
    third =  first+second+third
    counter += 1
    
