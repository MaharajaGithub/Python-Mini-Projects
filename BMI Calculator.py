# BMI Calculator

height = input("Enter your height in metre(m):\n")
weight = input("Enter your weight in kilogram(kg):\n")

# Convert height and weight into floating number.
bmi = float(weight)/float(height) ** 2

# convert the BMI to integer
bmi_as_integer = int(bmi)

# convert the integer to string
bmi_result = str(bmi_as_integer)

print("Your BMI is " + bmi_result)