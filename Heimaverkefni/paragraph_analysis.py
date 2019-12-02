import string
from operator import itemgetter

def open_file(filename):
    '''Function that opens file and returns filestream if filename is found, 
    otherwise the function returns none. '''
    try:
        filestream = open(filename, "r")
        return filestream
    except FileNotFoundError:
        return None

def process_file(filestream):
    '''Reads through file and returns a list of lists, each list containing each
    paragraph. '''
    working_list = []
    paragraph_list = []
    for line in filestream:
        if line != "\n":                      # if line is not empty then it is added to working_list
            line = line.strip().split()
            working_list += line
        else:                                 # if line is empty then the working list is appended to final_list
            paragraph_list.append(working_list)
            working_list = [] 
    paragraph_list.append(working_list)
    return paragraph_list

def get_paragraph_index(paragraph_list):
    '''Function that iterates through paragraph list and returns unique words and
    their paragraph index. '''
    index = 1
    working_dict = {}
    for paragraph in paragraph_list:
        for word in paragraph:
            word = word.lower().strip(string.punctuation)
            if word not in working_dict:                                 # add word to dictionary with index
                working_dict[word] = str(index)          
            elif str(index) not in working_dict[word]:                   # add index if word is found in another paragraph
                working_dict[word] += ", " + str(index)
        index += 1
    paragraph_index_list = sorted(working_dict.items(), key= itemgetter(0))    # create a list sorted aphabetically from working_dict
    return paragraph_index_list

def count_words(final_list):
    ''' Function that iterates through file list and counts unique words using 
    dictionaries and then returns a list of tuples sorted on value and alphabet '''
    count_dict = {}
    for a_list in final_list:
        for word in a_list:
            word = word.lower().strip(string.punctuation)
            if word in count_dict:
                count_dict[word] += 1
            else:
                count_dict[word] = 1
    alpabetical_sort = sorted(count_dict.items(), key=itemgetter(0))
    sorted_count_list = sorted(alpabetical_sort, key=itemgetter(1), reverse=True)
    return sorted_count_list

def print_results(sorted_count_dict, paragraph_list):
    '''Function that prints out results in correct format. '''
    print("The paragraph index: ")
    for key, val in paragraph_list:
        print(key, val)
    print()
    print("The highest 10 counts:")
    for key, val in sorted_count_dict[:10]:
        print("{}: {}".format(key,val))
    print()
    print("The highest 20 counts:")
    for key, val in sorted_count_dict[:20]:
        print("{}: {}".format(key,val))

def main():
    '''Main program'''
    filename = input("Enter filename: ")
    print()
    filestream = open_file(filename)
    if filestream:
        paragraph_list = process_file(filestream)
        paragraph_index_list = get_paragraph_index(paragraph_list)
        sorted_count_list = count_words(paragraph_list)
        print_results(sorted_count_list, paragraph_index_list)
    else:
        print("Filename", filename, "not found!")
main()