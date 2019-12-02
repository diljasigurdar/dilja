def merge_lists(list1, list2):
    merge_list = []
    union = []
    merge_list = list1 + list2
    for char in merge_list:
        if char not in union:
            union.append(char)
    union.sort()
    return union



# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))






''' Write a function merge_lists that takes two lists as arguments, 
merges them into a third list without duplicates and returns the third list sorted.

The elements of each list are strings.'''