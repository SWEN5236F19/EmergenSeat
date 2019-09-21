from Model.Car import Car


class CarSeat:

    def __init__(self, serial_number):
        self.serial_number = serial_number;
        self.latitude = ""
        self.longitude = ""
        self.car = Car()

    def __delete__(self, instance):
        del instance

    def __get__(self, instance, owner):
        return instance

    def set_gps_location(self, latitude, longitude):
        self.longitude = longitude
        self.latitude = latitude

    def update_car_details(self, make, model, year, vin):
        self.car.make = make
        self.car.model = model
        self.car.year = year
        self.car.vin = vin

    def print_car_seat(self):
        print(self.serial_number)
        print(self.latitude)
        print(self.longitude)

    def to_json(self):
        car_seat = \
        {
            "serial_number": self.serial_number,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "car": self.car.to_json()
        }
        return car_seat
