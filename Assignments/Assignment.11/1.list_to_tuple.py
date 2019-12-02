#list_to_tuple function goes here
def list_to_tuple(a_tuple):
    try:
        a_tuple = int(tuple(a_list))
        return a_tuple
    except TypeError:
        print("Error. Please enter only integers.")   
        return ()

# Main program starts here - DO NOT change it
a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_tuple(a_list)
print(a_tuple)