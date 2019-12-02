def get_name_and_number(result_dict):
    name_str = input("Name: ")
    number = input("Number: ")
    result_dict[name_str] = number

def print_results(result_dict):
    result_list = []
    for key, value in result_dict.items():
        temp = key, value
        result_list.append(temp)
    return result_list

def more_data():
    more = input("More data (y/n)? ")
    return more.lower() == 'y'

result_dict = {}

go_again = True
while go_again:
    get_name_and_number(result_dict)
    go_again = more_data()

result_list = print_results(result_dict)
print(sorted(result_list))
