import string

# Implement a function here
def find_unique_letters(sentence):
    sentence = sentence.strip()
    unique_letters = []
    for element in sentence:
        if element == " ":
            element = element.replace(element, "")
        if element in unique_letters:
            element = element.replace(element, "")
        if element in string.punctuation:
            element = element.replace(element, "")
        unique_letters += element
    return unique_letters



# Main starts here
sentence = input("Input a sentence: ")
# Call the function here
unique_letters = find_unique_letters(sentence)
print("Unique letters:", unique_letters)



# Write a program that makes a list of the unique letters in an input sentence.  
# That is, if the letter "x" is used twice in a sentence, it shouild only appear once in your list.  
# Neither punctuation nor white space should appear in your list.  
# The letters should appear in your list in the order they appear in the input sentence.