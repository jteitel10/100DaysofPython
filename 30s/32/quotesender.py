import datetime as dt
import smtplib
import random

# EMAIL = host email address
# SEND_TO_EMAIL = destination email address
# PWD = host password

# check if today is monday
now = dt.datetime.now()
if now.weekday() == 0:
    # created a list of quotes from text file
    with open ("quotes.txt") as file:
        quote_list = file.readlines()

    random_quote = random.choice(quote_list)


    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PWD)
        connection.sendmail(from_addr=EMAIL, to_addrs= SEND_TO_EMAIL, msg=f"Subject:Motivational Quote\n\n{random_quote}")
