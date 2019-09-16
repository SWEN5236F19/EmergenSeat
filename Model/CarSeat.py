class CarSeat:

    def __init__(self, serial_number):
        self.serial_number = serial_number;
        self.latitude = ""
        self.longitude = ""

    def __delete__(self, instance):
        del instance

    def __get__(self, instance, owner):
        return instance

    def set_gps_location(self, latitude, longitude):
        self.longitude = longitude
        self.latitude = latitude

    def print_car_seat(self):
        print(self.serial_number);
        print(self.latitude)
        print(self.longitude)
