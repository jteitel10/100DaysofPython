import requests
from pprint import pprint

# SHEETY_PRICES_ENDPT = YOUR ENDPOINT HERE - PRICES TAB
# SHEETY_USERS_ENDPT = YOUR ENDPOINT HERE - USERS TAB


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPT}/{city['id']}", json=new_data)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
