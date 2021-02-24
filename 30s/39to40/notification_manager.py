from twilio.rest import Client

# auth_sid = sid here
# auth_token = token here
twilio_num = "+13852132550"
dest_num = "+19735083302"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init_(self):
        self.client = Client(auth_sid, auth_token)

    def send_notification(self, message):
        message = self.client.messages.create(
            body=message, from_=twilio_num, to=dest_num)
        print(message.sid)
