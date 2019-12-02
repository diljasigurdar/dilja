def split_columns(file_object):
    word_list = []
    line_list = []
    #wokring_tuple = (),
    #counter = 1
    words = ""
    #word = ""
    for line in file_object:
        #if counter != 1:
        line_list = line.split("  +")
        for word in line_list:
            if word != "":
                word_list.append(word.strip())
        #counter += 1
    return word_list

def split_list(word_list):
    new_line_str = "\n".join(word_list)
    new_line_list = new_line_str.split()
    return new_line_str

#def find_year(new_line_str):


try:
    file_object = open("population.txt", "r")
    word_list = split_columns(file_object)
    new_line_str = split_list(word_list)
    print(new_line_str)
except FileNotFoundError:
    print("File", filename, "not found!")

#try:
#    year = input("Enter year: ")
#except TypeError:
#    print("Invalid year!")