from Model.CarSeat import CarSeat


class UserProfile:
    def __init__(self, email, first_name, last_name, password):
        self.email = email
        self.password = hash(password)
        self.first_name = first_name
        self.last_name = last_name
        self.car_seats = []

    def __get__(self, instance, owner):
        return instance

    def __delete__(self, instance):
        assert isinstance(instance, UserProfile)
        del instance

    def add_car_seat(self, car_seat):
        self.car_seats.append(car_seat)
        return car_seat

    def delete_car_seat(self, serial_number):
        if self.car_seats.__contains__(serial_number):
            index = self.car_seats.index(serial_number)
            self.car_seats.remove(serial_number)

    def print_user_profile(self):
        print("Email: " + self.email)
        for car_seat in self.car_seats:
            car_seat.print_car_seat()

    def to_json(self):
        profile = {"email": self.email,
                   "first_name": self.first_name,
                   "last_name": self.last_name,
                   "password": self.password,
                   "car_seats": []}
        for car_seat in self.car_seats:
            profile["car_seats"].append(car_seat.to_json())
        return profile
