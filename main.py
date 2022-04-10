# 1. Create working function
# 2. Add API
# 3. Debug and add details if necessary

from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from typing import Optional

app = FastAPI()

@app.get("/")
async def root():
  return {
    "Hi! Welcome to the BMI Calculator"
    "message": "BMI or Body Mass Index is a measure of body fat based on height and weight that applies to adult men and women.",
    "height": "Please provide your height in Meters, e.g. 1.5",
    "weight": "Please provide your weight in Kilograms",
    "morbidlyObese": "CAUTION! You are MORBIDLY OBESE. Please go see a doctor",
    "obese": "You are OBESE. Please go see a doctor",
    "overWeight": "You are OVERWEIGHT. A little bit of exercise would be good for you",
    "normalWeight": "You are within NORMAL WEIGHT range! Way to go!",
    "underWeight": "Oh dear. You need to bulk up a little. You are UNDERWEIGHT"
  }

@app.get("/api/bmi/")
async def calculatebmi(height: float = Query(None, gt=0), weight: float = Query (None, gt=0)):


  bmi = round(weight / ((height/100)**2), 2)
  if bmi >= 40.0:
    return JSONResponse(
      content={
        "bmi": bmi,
        "label": "CAUTION! You are MORBIDLY OBESE. Please go see a doctor",
        },
      status_code=200)
  elif bmi >= 30.0 and bmi < 39.9:
    return JSONResponse(
      content={
        "bmi": bmi,
        "label": "You are OBESE. Please go see a doctor",
        },
      status_code=200)
  elif bmi >= 25.0 and bmi < 29.9:
    return JSONResponse(
      content={
        "bmi": bmi,
        "label": "You are OVERWEIGHT. A little bit of exercise would be good for you",
        },
      status_code=200)
  elif bmi >= 18.5 and bmi < 24.9:
    return JSONResponse(
      content={
        "bmi": bmi,
        "label": "You are within NORMAL WEIGHT range! Way to go!",
        },
      status_code=200)
  elif bmi < 18.5:
    return JSONResponse(
      content={
        "bmi": bmi,
        "label": "Oh dear. You need to bulk up a little. You are UNDERWEIGHT",
        },
      status_code=200)
