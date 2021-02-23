import requests
from datetime import datetime
import os

# YOUR BIO INFO
GENDER = "male"
AGE = "28"
WEIGHT_KG = "81"
HEIGHT_CM = "182.88"

# NUTRITION IX INFO
NUTR_APP_ID=os.environ.get("NUTR_APP_ID")
NUTR_APP_KEY=os.environ.get("NUTR_APP_KEY")
NUTR_ENDPT=os.environ.get("NUTR_ENDPT")

# SHEET API INFO
SHEETY_ENDPOINT=os.environ.get("SHEETY_ENDPOINT")

sheety_headers={
    "Authorization" : f"Basic {os.environ.get('SHEETY_TOKEN')}"
        }

#TODO print exercise stats for a plain text input
exercise_text = input("What did you work out today?\n")

nutr_headers = {
    "x-app-id" : NUTR_APP_ID,
    "x-app-key" : NUTR_APP_KEY,
}

nutr_params = {
    "query" : exercise_text,
    "gender": GENDER,
    "weight_kg" : WEIGHT_KG,
    "height_cm" : HEIGHT_CM,
    "age" : AGE
}

nutr_response = requests.post(url=NUTR_ENDPT, json=nutr_params,headers=nutr_headers)
results = nutr_response.json()
#print(results)

today = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%H:%M:%S")

for exercise in results["exercises"]:
    sheety_json = {
        "workout" : {
            "date" : today,
            "time" : time_now,
            "exercise" : exercise["name"].title(),
            "duration" : exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_json, headers=sheety_headers)
print(sheet_response.text)
