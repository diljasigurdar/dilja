num = int(input("Enter a number: "))

def num_in_range(number):
    if 1 < num < 555:
        result = num
    else:
        result = 0
    return result

result = num_in_range(num)

if result == num:
    print(num, "is in range.")
else:
    print(num, "is outside the range!")



    
# The function definition goes here



# You call the function here