d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line
# Fill in the missing code below
sumd = d1 + d2

if 1 <= d1 <= 6 and 1 <= d2 <= 6:
    if sumd == 7 or sumd == 11:
        print("Winner")
    elif sumd == 2 or sumd == 3 or sumd == 12:
        print("Loser")
    else:
        print(sumd)
else:
    print("Invalid input")

            
