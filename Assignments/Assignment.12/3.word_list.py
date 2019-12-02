import string

def open_file(filename):
    file_object = open(filename, "r")
    return file_object


def read_file(file_object):
    result_list = []
    for line in file_object:
        list_of_words = line.split()
        result_list += list_of_words
    return result_list

def find_unique_words(result_list):
    no_punctuation_list = []
    unique_words = []
    for word in result_list:   
        if word[-1] in string.punctuation:
            word = word[0:-1]
        if word[0] in string.punctuation:
            word = word[1:]
        word = word.strip('''"''')
        if word not in unique_words:
            unique_words.append(word)
    unique_words.sort()
    return unique_words

def main():
    filename = input("Enter filename: ")
    file_object = open_file(filename)
    result_list = read_file(file_object)
    unique_words = find_unique_words(result_list)
    print(unique_words)

main()








''' This program builds a wordlist out of all of the words found 
in an input file and prints all of the unique words found in the 
file in alphabetical order. Remove punctuations using 
ring.punctuation' and 'strip()' before adding words to the wordlist.'''