import datetime as dt
import smtplib
import pandas
import random
##################### Normal Starting Project ######################

LETTER_ONE = "letter_templates/letter_1.txt"
LETTER_TWO = "letter_templates/letter_2.txt"
LETTER_THREE = "letter_templates/letter_3.txt"
# my_email = your email
# my_password = your password
PLACEHOLDER = "[NAME]"

# Check if today matches a birthday in the birthdays.csv
today_month = dt.datetime.now().month
today_day = dt.datetime.now().day
today = (today_month, today_day)

# read birthday csv
data = pandas.read_csv(('birthdays.csv'))

# create a birthday dictionary
birth_dict = {(data_row.month, data_row.day) : data_row for (index, data_row) in data.iterrows()}

# If there is a match, pick a random letter  and replace the [NAME] with the person's actual name from birthdays.csv
if today in birth_dict:
    birthday_person = birth_dict[today]
    letter_list = [LETTER_ONE, LETTER_TWO, LETTER_THREE]
    chosen_letter = random.choice(letter_list)
    with open(f"{chosen_letter}") as letter:
        letter = letter.read()
        ready_letter = letter.replace(PLACEHOLDER, birthday_person["name"])

# Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person.email,
        msg=f"Subject:Happy Birthday\n\n{ready_letter}")
