# Prints string of axis_char from start to end with pos_char at position
def print_char(position, start, end, axis_char, pos_char):
    x_axis = (END - START + 1) * axis_char 
    print(x_axis[1:position] + pos_char + x_axis[position:])

# Calculates new position from current position for the specified range
def calculate_position(choice, position, start, end):
    if choice == "r" and position < end:
        position += 1
    elif choice == "l" and position > start:
        position -= 1
    return position

START = 1
END = 10
AXIS_CHAR = "x"
POSITION_CHAR = "o"
position = int(input("Input a position between 1 and 10: "))

print_char(position, START, END, AXIS_CHAR, POSITION_CHAR)
print("l - for moving left")
print("r - for moving right")
print("Any other letter for quitting")

choice = input("Input your choice: ")
while choice == "r" or choice == "l":
    position = calculate_position(choice, position, START, END)
    print_char(position, START, END, AXIS_CHAR, POSITION_CHAR)
    choice = input("Input your choice: ")

print_char(position, START, END, AXIS_CHAR, POSITION_CHAR)

