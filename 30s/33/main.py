import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 40.730610 # NYC latitude
MY_LONG = -73.935242 # NYC longitude

# MY_EMAIL = your email
# MY_PASSWORD = your password
# DEST_EMAIL = your destination email

# check to see if ISS is above NYC
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    # check to see if ISS is within +/- 5 deg of NYC
    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LONG+5 >= iss_long >=MY_LONG-5:
        return True

# check to see if currently dark out
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    current_time = datetime.now().hour

    # check to see if current time is dark (between sunrise and sunset)
    if current_time >= sunset or current_time <= sunrise:
        return True

# run every 60 seconds
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=DEST_EMAIL,
                                msg="Subject:Look Up\n\nThe ISS is directly above you in the sky.")
