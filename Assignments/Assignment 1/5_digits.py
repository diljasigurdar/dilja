x_str = input("Input x: ")
# remember to convert to an int
x_int = int(x_str)

first_three = int(x_int / 1000)
last_two = x_int % 100
first_four = x_int // 100
middle_two = first_four % 100
              
print("original input:", x_str)
print("first_three:", first_three)
print("last_two:", last_two)
print("middle_two:", middle_two)
