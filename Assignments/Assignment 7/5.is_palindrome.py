import string

def is_plaindrome(a_str):
    no_punctuation_str = ""
    result_str = ""
    for char in a_str:
        if char.strip() not in string.punctuation:
            no_punctuation_str += char
    result_str = no_punctuation_str.lower()
    if result_str == result_str[::-1]:
        result = True
    else:
        result = False
    return result
            
a_str = input("Enter a string: ")

result = is_plaindrome(a_str)
if result == True:
    print(a_str, "is a palindrome")
else:
    print(a_str, "is not a palindrome")
# call the function and print out the appropriate message



# A palindrome is a word, phrase, number, or other sequence of characters 
# which reads the same backward as forward, such as madam or racecar. 
# Sentence-length palindromes may be written when allowances are made 
# for adjustments to capital letters, punctuation, and word dividers, such as "

# ", "Was it a car or a cat I saw?" or "No 'x' in Nixon".

# Write a function that takes a string as an argument and returns True 
# if the string is a palindrome and False otherwise.

# Also write code that calls the function with the input as an 
# argument and prints out the appropriate message.