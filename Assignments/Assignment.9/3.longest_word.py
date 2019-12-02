def open_file(filename):
    file_object = open(filename, "r")
    return(file_object)

def read_file(file_object):
    longest_word = ""
    word_length = 0
    for word in file_object:
        word = word.strip()
        if len(word) > word_length:
            longest_word = word
            word_length = len(word)
    return longest_word, word_length

filename = input("Enter filename: ")

file_object = open_file(filename)
longest_word, word_length = read_file(file_object)



print("Longest word is","'"+longest_word+"'", "of length", word_length)

# Write a Python program that reads a file, input by the user, 
# containing one word/token per line with an empty line between sentences.  
# The program prints out the longest word found in the file along with its length.