# The main program starts here
def string_join(the_string):
    if " " in the_string:
        the_list = the_string.split()
    elif "," in the_string:
        the_list = the_string.split(",")
    else:
        the_list = the_string.split()
    return the_list



the_string = input("Enter the string: ")
# call your function here
the_list = string_join(the_string)
print(the_list)









# Write a function called 'to_list' that takes a string as a parameter and returns a list of words in the string.
# "Words" are entities that are seperated by either commas (',') or spaces (' '). 
# In case the string contains neither commas nor spaces, a list should be returned containing a single element.
# Note: We are not testing for the case where both commas and spaces are present in the string so feel free to ignore that.
