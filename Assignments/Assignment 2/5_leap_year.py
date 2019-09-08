year = int(input("Input a year: ")) # Do not change this line

# Fill in the missing code below
leap = True
notleap = False
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(leap)
        else: print(notleap)
    else:
        print(leap)
else:
    print(notleap)



