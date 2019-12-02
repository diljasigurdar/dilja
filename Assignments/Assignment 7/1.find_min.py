# find_min function definition goes here
def find_min(first, second):
    if first < second:
        result = first
    else:
        result = second  
    return result

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
minimum = find_min(first, second)

    
# Call the function here
print("Minimum: ", minimum)