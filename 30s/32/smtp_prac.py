import smtplib

# my_email = starting email address
# my_password = starting email's password
# dest_email = destination email address

with smtplib.SMTP(host="smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=dest_email,
                        msg="Subject:Hello\n\nThis is the message body")
