import string

#all variables are string unless otherwise indicated

#function that scrambles each word
def scramble_word(word):
    working_str = word
    punctuation = ""
    scramble = ""
    index = 0
    if word[-1] in string.punctuation:                                      #if word contains punctuation, then add it to the final
        punctuation = working_str[-1]                                       #string
        working_str = working_str[0:-1]
    if len(working_str) <= 3:                                               #if word cointains 3 or less letters, do nothing
        return word
    middle_part = working_str[1:-1]
    while (index + 1) < len(middle_part):                                   #scramble two letters at a time
        scramble += middle_part[index + 1] + middle_part[index]       
        index += 2
    if len(middle_part) % 2 == 1:                                           #if middle_part is an odd number,                                                                             
        scramble += middle_part[-1]                                         #add the last char to the string
    scramble = working_str[0] + scramble + working_str[-1] + punctuation
    return scramble

#function that iterates through each word in file and then adds
#all scrambled words together into a sentence
def scramble_words(file_object):
    words_scrambled = ""
    for word in file_object:
        word = word.strip()
        words_scrambled += scramble_word(word) + " "
    return words_scrambled

try:
    filename = input("Enter name of file: ")
    file_object = open(filename, "r")
    words_scrambled = scramble_words(file_object)
    print(words_scrambled)
except FileNotFoundError:
    print("File", filename, "not found!")
