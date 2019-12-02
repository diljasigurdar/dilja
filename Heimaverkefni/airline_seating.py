SEATS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

def get_input():
    rows_int = int(input("Enter number of rows: "))
    seats_int = int(input("Enter number of seats in each row: "))
    return rows_int, seats_int

def get_seat_number():
    seat_number = input("Input seat number (row seat): ")
    row, seat = seat_number.split()
    row = int(row)
    return row, seat

def mark_seat_number(row, seat, seat_list):
    if seat not in seat_list[0]:
        return False
    try:
        seat_index = seat_list[row - 1].index(seat)
    except ValueError:
        return None
    except IndexError:
        return False
    seat_list[row - 1][seat_index] = 'X'
    return seat_list

def more_seats():
    more = input("More seats (y/n)? ")
    return more.lower() == 'y'

def get_rows(rows_int, seats_int):
    seat_numbers_list = []
    counter = 0
    while counter < rows_int:
        seat_numbers_list.append(list(SEATS[0:seats_int]))
        counter += 1
    return seat_numbers_list

def print_seats(seat_list):
    seats_per_hall = int(len(seat_list[0]) / 2)
    line = 1
    seat_counter = 0
    for row in seat_list:
        print('{:>2}  '.format(line), end=" ")
        for seat in row:
            if seat_counter == (seats_per_hall - 1):
                print('{:<3}'.format(seat), end=" ")
            else:
                print(seat, end=" ")
            seat_counter += 1
        line += 1
        seat_counter = 0
        print()

def main():
    rows_int, seats_int = get_input()
    seat_numbers_list = get_rows(rows_int, seats_int)
    print_seats(seat_numbers_list)
    go_again = True
    while go_again:
        row, seat = get_seat_number()
        marked_seat = mark_seat_number(row, seat, seat_numbers_list)
        if marked_seat == None:
            print("That seat is taken!")
            marked_seat = mark_seat_number(row, seat, seat_numbers_list)
        elif marked_seat == False:
            print("Seat number is invalid!")
            marked_seat = mark_seat_number(row, seat, seat_numbers_list)
        else:
            print_seats(seat_numbers_list)
            go_again = more_seats()

main()