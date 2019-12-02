import string
user_input = input("Enter a string: ")
# Your function definition goes here
def upper_lower(count_ch):
    count_upper = 0
    count_lower = 0
    for char in count_ch:
        if char in string.ascii_uppercase:
            count_upper += 1
        elif char in string.ascii_lowercase:
            count_lower += 1
    return count_upper, count_lower

upper_count, lower_count = upper_lower(user_input)

# Call the function here

print("Upper case count: ", upper_count)
print("Lower case count: ", lower_count)