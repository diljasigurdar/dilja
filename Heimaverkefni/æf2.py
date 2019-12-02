filename = input("Enter filename: ")

try:
    file_object = open(filename, "r")
except FileNotFoundError:
    print("File", filename, "not found")

def read_file(file_object):
    for char in string.punctuation:
        word_without_punctation = char.replace(char, "")
    return word_without_punctation

def find_scramble(word_without_punctation):
    scramble = word_without_punctation[1:-1]
    return scramble

def scramble_words(scramble, word_without_punctation):
    scramble_word = word_without_punctation[0] + scramble + word_without_punctation[-1]
    return scramble_word



filename = input("Enter filename: ")

try:
    file_object = open(filename, "r")
except FileNotFoundError:
    print("File", filename, "not found")

word_without_punctation = read_file(file_object)
scramble = find_scramble(word_without_punctation)
scramble_word = scramble_words(scramble, word_without_punctation)
print(scramble_word)
#def scramble_word(word_without_punctation):
 #   scramble_word = word_without_punctation[1:-2]