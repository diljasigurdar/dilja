def split_name():
    name = input("Enter name: ")
    first_name, last_name = name.split()
    return first_name, last_name

def name_list(first_name, last_name):
    first_name_list = [char.lower() for char in first_name]
    last_name_list = [char.lower() for char in last_name]
    common_letters = []
    for char in first_name_list:
        if char in last_name_list:
            common_letters.append(char)
    return common_letters, first_name_list, last_name_list

def get_list(common_letters):
    common_letters_list = []
    for char in common_letters:
        if char not in common_letters_list:
            common_letters_list.append(char)
    return common_letters_list

def get_set(first_name, last_name):
    first_set = set(first_name)
    second_set = set(last_name)
    result_set = first_set & second_set
    return result_set

first_name, last_name = split_name()
common_letters, first_name_list, last_name_list = name_list(first_name, last_name)
common_letters_list = get_list(common_letters)
result_set = get_set(first_name_list, last_name_list)
print(sorted(common_letters_list))
print(sorted(result_set))

'''Write a program that prompts the user for a name.  
The program then splits the name into first and last name (case insensitive).

Then it:

calls a function that returns a list of the common letters in first and last. 
The data structures used in this implementation can only be lists.
calls a function that returns a set containing the common letters in first and last.  
The data structures used in this implementation can only be sets.
prints out a sorted list version of the results from 1) and 2)
Example input/output:'''