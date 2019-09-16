class UserProfile:
    def __init__(self, email):
        self.email = email
        self.car_seats = []
        self.longitude = ""
        self.latitude = ""

    def __get__(self, instance, owner):
        return self

    def __getitem__(self, item):
        return self

    def __delete__(self, instance):
        assert isinstance(instance, UserProfile)
        del instance

    def set_gps_location(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    def add_car_seat(self, serial_number):
        self.car_seats.append(self.car_seats, serial_number)

    def delete_car_seat(self, serial_number):
        if self.car_seats.__contains__(serial_number):
            index = self.car_seats.index(serial_number)
            self.car_seats.remove(serial_number)
