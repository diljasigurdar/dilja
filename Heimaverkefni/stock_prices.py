DATE = 0
ADJ_CLOSE = 5
VOLUME = 6

def open_file(filename):
    ''' Returns filestream if file found. Otherwise returns None '''
    try: 
        filestream = (open(filename, "r"))
        return filestream
    except:
        FileNotFoundError
        return None

def get_data_list(filestream):
    ''' reads through file and returns each line from file in a list of lists, and converts
    certain elements to float and integer '''
    data_list = []
    working_list = []
    line_number = 1
    for line in filestream:
        line_list = line.strip().split(",")
        if line_number != 1:
            working_list.append(line_list[0])
            working_list.append(float(line_list[1]))
            working_list.append(float(line_list[2]))
            working_list.append(float(line_list[3]))
            working_list.append(float(line_list[4]))
            working_list.append(float(line_list[5]))
            working_list.append(int(line_list[6]))
            data_list.append(working_list)
        line_number += 1
        working_list = []
    return data_list
            
'''def get_monthly_averages(data_list):
    function that returns average per day 
    working_month = ''
    index = 0
    volume = 0
    sum_adj_close = 0.0
    average = 0.0
    result_tuple = (),
    results_list = []
    for line in data_list:
        month = line[0][0:7]

        if [item for item in result if item[0] == month]:
            working_items = [item for item in result if item[0 == month] 
            new_working_item = (month, working_items[0][1] + line[ADJ_CLOSE] * line[VOLUME], working_items[0][2] + line[VOLUME])
            results_list.remove(working_item[0])
            results_list.append(new_working_item)
        else:
            result_tuple = (month, line[ADJ_CLOSE] * line[VOLUME])
            results_list.append(result_tuple)
        
    for result in results_list:
        (print result)'''

def find_highest_price(data_list):
    highest_price_list = []
    date_list = []
    highest_price = 0
    for line in data_list:
        data_list.append(line[0])
        highest_price_list.append(line[ADJ_CLOSE])
    highest_price = max(highest_price_list)
    index_of_highest_price = inde
    print(highest_price)
    return highest_price
    

def main():
    ''' main program '''
    filename = "words.txt"
    filestream = open_file(filename)
    data_list = get_data_list(filestream)
    #monthly_averages_list = get_monthly_averages(data_list)
    highest_price = find_highest_price(data_list)
    print('{:>10s} {:>15s}'.format('month', 'price'))
    #sum_volume = get_monthly_averages(data_list)
    if filestream:
        print('123')
    else: 
        print("Filename {} not found!".format(filename))

main()