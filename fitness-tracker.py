# Create a program that asks a user for their name, age, and weight.
# Write a function to calculate their BMI (Body Mass Index) given their weight and height.
# Based on the BMI value, write an if statement that categorizes them as underweight, normal, overweight, or obese.
# Create another function that suggests a fitness plan based on the BMI category.
# if: underweight, 

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = int(input("Enter your height in inches: "))
weight = float(input("Enter your weight: "))
unit = input("Enter the unit of measurement (L for pounds, K for kilograms): ")
bmi = ""
bmivalue = ""

if unit == "L":
  pass
elif unit == "K":
  weight = round((weight * 2.20462), 2)

def calculateBMI():
  bmi = ((weight * 703) / height) / height
  print(bmi)

if bmi < 18.5:
  bmivalue = "Underweight"
elif 18.5 < bmi < 24.9:
  bmivalue = "Healthy"
elif 25 < bmi < 29.9:
  bmivalue = "Overweight"
else:
  bmivalue = "Please see a doctor"

def fitnessPlan():
  if bmivalue == "Underweight"