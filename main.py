# 1. Create working function
# 2. Add API
# 3. Debug and add details if necessary

import sys

height = float(input("height?"))
weight = float(input("weight?"))

def calculatebmi(height, weight):

  print(height)
  print(weight)

  bmi = round(weight / ((height/100)**2), 2)
  if bmi >= 40.0:
    print("CAUTION! You are MORBIDLY OBESE. Please go see a doctor")
  elif bmi >= 30.0 and bmi < 39.9:
    print("You are OBESE. Please go see a doctor")
  elif bmi >= 25.0 and bmi < 29.9:
    print("You are OVERWEIGHT. A little bit of exercise wwould be good for you")
  elif bmi >= 18.5 and bmi < 24.9:
    print("You are within NORMAL WEIGHT range! Way to go!")
  elif bmi < 18.5:
    print ("Oh dear. You need to bulk up a little. You are UNDERWEIGHT")

calculatebmi(height, weight)
