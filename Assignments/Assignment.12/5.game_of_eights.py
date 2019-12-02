def get_list(numbers):
    working_list = numbers.split(",")
    number_list = []
    try:
        for char in working_list:
            char_int = int(char)
            number_list.append(char_int)
        return number_list
    except ValueError:
        print("Error - please enter only integers")

def is_eights(number_list):
    index = 0
    length = len(number_list) - 1
    result = False
    while index < length:
        if number_list[index] == 8 and number_list[index+1] == 8:
            result = True
        index += 1
    return result




def main():
    numbers = input("Enter elements of list separated by commas: ")
    number_list = get_list(numbers)
    result = is_eights(number_list)
    print(result)

main()






''' Write a program that accepts a list of numbers as an argument and then prints 
'True' if two consecutive eights are found in the list. 
The program prints out an error message saying 'Error - 
please enter only integers.' if the list is found to contain any non-numeric characters. '''