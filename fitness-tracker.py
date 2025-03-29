# Create a program that asks a user for their name, age, and weight.
# Write a function to calculate their BMI (Body Mass Index) given their weight and height.
# Based on the BMI value, write an if statement that categorizes them as underweight, normal, overweight, or obese.
# Create another function that suggests a fitness plan based on the BMI category.
# if: underweight, 



name = input("Enter your name: ").capitalize()
age = int(input("Enter your age: "))
height = int(input("Enter your height in inches: "))
weight = float(input("Enter your weight: "))
unit = input("Enter the unit of measurement (L for pounds, K for kilograms): ")
bmi = None
bmivalue = None

if unit == "L":
  pass
elif unit == "K":
  weight = round((weight * 2.20462), 2)

bmi = ((weight * 703) / height) / height


if bmi < 18.5:
  bmivalue = "Underweight"
elif 18.5 < bmi < 24.9:
  bmivalue = "Healthy"
elif 25 < bmi < 29.9:
  bmivalue = "Overweight"
else:
  bmivalue = "Very overweight"

print(f"{name}, your BMI is {bmivalue}. To begin your fitness journey, please answer some more questions:")

fitness_level = input("Please let us know your fitness level (beginner, intermediate, expert): ")
muscle_groups = input("What kind of work out would you like? (full-body, upper-body, lower-body): ")
exercise_style = input("What kind of workout would you prefer? (cardio, weightlifting, stretching): ")




# def fitnessPlan():
#  if bmivalue == "Underweight"