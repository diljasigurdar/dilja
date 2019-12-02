def get_set():
    a_list = input("Input a list of integers separated with a comma: ").split(",")
    a_list = [int(i) for i in a_list]
    return set(a_list)

def print_set_operations():
    print("1. Intersection")
    print("2. Union")
    print("3. Difference")
    print("4. Quit")
    set_operation = int(input("Set operation: "))
    return set_operation

def find_intersection(set1, set2):
    return print(set1 & set2)

def find_union(set1, set2):
    return print(set1 | set2)

def find_difference(set1, set2):
    return print(set1 - set2)

def main():
    set_1 = get_set()
    set_2 = get_set()
    print(set_1)
    print(set_2)
    set_operation = print_set_operations()
    while set_operation != 4:
        if set_operation == 1:
            find_intersection(set_1, set_2)
        elif set_operation == 2:
            find_union(set_1, set_2)
        elif set_operation == 3:
            find_difference(set_1, set_2)
        set_operation = print_set_operations()
main()












'''Write a program that:

Reads in two lists of integers from the user and converts them to 
sets and prints out the sets.
Allows the user to repeatedly perform intersection, 
union and difference on the two sets and prints out the result of each operation'''