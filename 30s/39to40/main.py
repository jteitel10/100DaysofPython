from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "JFK"

# Read/Write to Google Sheet
datamgr = DataManager()
sheet_data = datamgr.get_destination_data()
notification_manager = NotificationManager()
flight_search = FlightSearch()

today = datetime.now()
tomorrow = today + timedelta(days=1)
six_months = today + timedelta(days=(6*30))

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    datamgr.destination_data = sheet_data
    datamgr.update_destination_codes()

for destination in sheet_data:
    flight = flight_search.check_flights(
        origin_airport=ORIGIN_CITY_IATA,
        departure_airport_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months
    )
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_notification(
            message = f"Low price alert! Only ${flight.price} to fly from New York-{ORIGIN_CITY_IATA} to {flight.departure_city}-{flight.departure_airport_code}, from {flight.out_date} to {flight.return_date}."
        )