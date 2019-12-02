# sort_list() function goes here
def get_list():
    a_list = []
    num = input()
    valid_input = True
    while valid_input:
        try: 
            a_list.append(int(num))
            num = input()
        except:
            valid_input = False
            return a_list

# get_list() function goes here
def sort_list(a_list):
    sort_list = a_list.sort()


# Do not modify this part
def main():
    a_list = get_list()
    print(a_list)
    print(sort_list(a_list))
    print(a_list)
    
main()




''' Write a function 'sort_list()' that accepts a list of integers and sorts it. 
The function should not explicitly return this list and yet the list will be 
sorted when printed within main() after being passed to sort_list() as a parameter.

Complete the main() module such that it accepts numbers from the user, until a 
non-digit string is entered (you could use try-except for this), and stores 
them in a list called 'a_list'.'''