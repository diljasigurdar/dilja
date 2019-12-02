import string
from operator import itemgetter

def open_file(filename):
    try:
        filestream = open(filename, "r")
        return filestream
    except FileNotFoundError:
        return None

def process_file(filestream):
    working_list = []
    for line in filestream:
        line = line.strip().split()
        for word in line:
            if word != '...':
                working_list.append(word.strip(string.punctuation).lower())
    return working_list

def word_list(working_list):
    final_list = []
    index = 0
    while index < len(working_list):
        a_tuple = tuple(working_list[index:index+2])
        final_list.append(a_tuple)
        index += 1
    return final_list


def count_bigrams(final_list):
    count_dict = {}
    for bigram in final_list:
        if bigram in count_dict:
            count_dict[bigram] += 1
        else:
            count_dict[bigram] = 1
    sorted_list = sorted(count_dict.items(), key=itemgetter(1), reverse=True)
    return sorted_list


def main():
    filename = input("Enter name of file: ")
    filestream = open_file(filename)
    if filestream:
        working_list = process_file(filestream)
        final_list = word_list(working_list)
        sorted_list = count_bigrams(final_list)
        print(sorted_list[0:10])
main()