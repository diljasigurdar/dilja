def open_file(filename):
    ''' Function that takes filename in as parameter and opens the file. '''
    file_object = open(filename, "r")
    return file_object

def get_first_line(filename, year):
    ''' This function takes in file_object ans year in as parameters an returns the \n
        first line in a list. '''
    file_object = open_file(filename)
    first_line_list = []
    for line in file_object:
        first_line_list = line.split()
        break
    file_object.close()
    return first_line_list

def get_year_index(year, first_line_list):
    ''' This functino takes in year and first_line_list as parameters and finds the index \n
        of input year. '''
    valid_input_bool = False
    while not valid_input_bool:
        try:
            index = first_line_list.index(year)
            valid_input_bool = True
        except ValueError:
            print("Invalid year!")
            year = input("Enter year: ")
    return index

def get_population(index, filename):
    ''' This function takes in index of year and file_object an return list of population \n
        for each state that year. '''
    file_object = open_file(filename)
    population_list = []
    line_list = []
    for line in file_object:
        for char in line:
            if char == "\t":                     
                line = line.replace(char, " ")
        items = line.split("  ")
        for item in items:
            if item != "":
                line_list.append(item.strip())
        population_list.append(int(line_list[index]))
        line_list = []
    file_object.close()
    population_list = population_list[1:]
    return population_list

def get_state_list(filename):
    ''' Functions that takes filename in as a parameter and returns list of states. '''
    file_object = open_file(filename)
    state_list = []
    line_list = []
    for line in file_object:
        items = line.split("  ")
        for item in items:
            if item !="":
                line_list.append(item.strip())
        state_list.append(line_list[0])
        line_list = []
    file_object.close()
    state_list = state_list[1:]
    return state_list

def get_max_pop_and_state(population_list, state_list):
    ''' Function that takes in population_list in as argument an returns the maximum population \n
        for the given year and the state '''
    max_population = max(population_list)
    index_of_max = population_list.index(max_population)
    state = state_list[index_of_max]
    return (max_population, state)

def get_min_pop_and_state(population_list, state_list):
    ''' Function that takes in population_list in as argument an returns the minimum population \n
        for the given year and the state '''
    min_population = min(population_list)
    index_of_min = population_list.index(min_population)
    state = state_list[index_of_min]
    return (min_population, state)


# main program

filename = input("Enter filename: ")

try:
    file_object = open(filename, "r")
    file_object = open_file(filename)
    file_object.close()
    year = input("Enter year: ")

    # function calls
    first_line_list = get_first_line(filename, year)
    index = get_year_index(year, first_line_list)
    population_list = get_population(index, filename)
    state_list = get_state_list(filename)
    max_pop_and_state = get_max_pop_and_state(population_list, state_list)
    min_pop_and_state = get_min_pop_and_state(population_list, state_list)

    print("Minimum:", min_pop_and_state)
    print("Maximum:", max_pop_and_state)
except FileNotFoundError:
    print("Filename", filename, "not found!")




