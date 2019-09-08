age = int(input("Input age: ")) # Do not change this line

# Fill in the missing code below
ticket_price = 30.0
ticket_senior = 30.0 * 0.5
ticket_children = 0.0


if age >= 65:
    print(ticket_senior)
elif age <= 5:
    print(ticket_children)
else:
    print(ticket_price)
