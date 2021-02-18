import requests
import os
from twilio.rest import Client

OMW_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = os.environ.get("OWM_API_KEY")
NY_LAT = 40.730610 # NYC latitude
NY_LONG = -73.935242 # NYC longitude
UMBRELLA_RESPONSE = "☔️ Don't forget an umbrella today! ☔️"
auth_sid = os.environ.get("TW_AUTH_SID")
auth_token = os.environ.get("TW_AUTH_TOKEN")
# trial_num = insert account phone number
# dest_num = insert destination phone number

params = {
    "lat" : NY_LAT,
    "lon" : NY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OMW_ENDPOINT, params=params)
response.raise_for_status()
ny_weather_json = response.json()
hourly_weather_codes = [ny_weather_json["hourly"][i]["weather"][0]["id"] for i in range(12)]

will_rain = False

for i in range(len(hourly_weather_codes)):
    if int(hourly_weather_codes[i]) < 700:
        will_rain = True


if will_rain:
    client = Client(auth_sid, auth_token)
    message = client.messages \
        .create(
        body=UMBRELLA_RESPONSE,
        from_=trial_num,
        to=dest_num
        )
