# Your functions should appear here
def add_to_list(value):
    value_list = []
    while value != "exit":
        value_list.append(value)
        value = input("Enter a value to be added to the list: ")
    result_list = value_list*3
    result_str = "\n".join(result_list)
    return result_str


# Main program starts here
value = input("Enter value to be added to list: ")
# It should mostly be a sequence of function calls
result_str = add_to_list(value)
print(result_str)






# Write a program that keeps asking the user for new values to be added to a list 
# until the user enters 'exit' ('exit' should NOT be added to the list). After that, 
# the program creates a new list with 3 copies of every value in the initial list.  
# Finally, the program prints out all of the values in the new list.