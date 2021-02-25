from twilio.rest import Client
import smtplib

# auth_sid = your twilio sid
# auth_token = your twilio token
# twilio_num = your twilio verified num
# dest_num = your desination num
# MAIL_PROVIDER_SMTP_ADDR = your smtp provider address
# MY_EMAIL = your email
# MY_PWD = your password


class NotificationManager:
    def __init__(self):
        self.client = Client(auth_sid, auth_token)

    def send_notification(self, message):
        message = self.client.messages.create(
            body=message,
            from_=twilio_num,
            to=dest_num,
        )
        print(message.sid)

    def send_emails(self, emails, message, flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDR) as connection:
            connection.starttls().connection.login(MY_EMAIL, MY_PWD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject: New Low Price Flight!\n\n{message}\n{flight_link}".encode(
                        'utf-8')
                )
