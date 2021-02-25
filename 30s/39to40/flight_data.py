class FlightData:
    def __init__(self, price, origin_city, origin_airport, departure_airport_code, departure_city, out_date, return_date, stop_overs=0, via_city=""):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.departure_airport_code = departure_airport_code
        self.departure_city = departure_city
        self.out_date = out_date
        self.return_date = return_date
        self.stop_overs = stop_overs
        self.via_city = via_city
