import requests
from pprint import pprint

SHEETY_ENDPT = "https://api.sheety.co/a634e768895c423c94322d9a327d8ad7/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.destination_data = {}
    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price" : {
                    "iataCode" : city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPT}/{city['id']}", json=new_data)
