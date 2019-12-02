weight = input("Enter weight: ")
weight_float = float(weight)
height = input("Enter height: ")
height_float = float(height)

bmi = weight_float/((height_float/100)**2)

print("BMI is {0:.2f}".format(bmi))


'''BMI is a number calculated from a person's weight and height.  The formula for BMI is:

weight / height2

where weight is in kilograms and heights is in meters

Write a program  that prompts for weight in kilograms and height in centimeters and outputs the BMI.'''