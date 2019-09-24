from Model.Car import Car


class CarSeat:

    def __init__(self, serial_number):
        self.serial_number = serial_number;
        self.model = ""
        self.latitude = ""
        self.longitude = ""
        self.weight = 0.0
        self.weight_unit = "Lbs"
        self.temperature = 0.0
        self.temperature_unit = "Fahrenheit"
        self.car = Car()

    def __delete__(self, instance):
        del instance

    def __get__(self, instance, owner):
        return instance

    def set_gps_location(self, latitude, longitude):
        self.longitude = longitude
        self.latitude = latitude

    def set_weight(self, weight, unit):
        self.weight = weight
        self.weight_unit = unit

    def set_temperature(self, temp, unit):
        self.temperature = temp
        self.temperature_unit = unit

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
        car_seat = {
            "serial_number": self.serial_number,
            "model": self.model,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "weight": self.weight,
            "weight_unit": self.weight_unit,
            "temperature": self.temperature,
            "temperature_unit": self.temperature_unit,
            "car": self.car.to_json()
        }
        return car_seat
