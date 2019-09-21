import os

from Model.CarSeat import CarSeat
from Model.DataHandler import DataHandler
from Model.UserProfile import UserProfile


class Controller:

    def __init__(self):
        self.file_name = os.getcwd() + "/userprofiles.json"
        data = DataHandler.import_from_json(self.file_name)
        self.user_profiles = DataHandler.convert_json_to_profiles(data)
        self.active_user = None

    def login(self, username, password):
        potential_user = next((x for x in self.user_profiles if x.username == username), None)
        if potential_user is not None:
            if hash(password) == potential_user.password:
                self.active_user = potential_user
                return 1
        return 0

    def register(self, email, first_name, last_name, password):
        new_profile = UserProfile(email, first_name, last_name, password)
        self.active_user = new_profile
        self.user_profiles.append(new_profile)

    def get_car_seats(self):
        return self.active_user.car_seats

    def add_car_seat(self, serial_number):
        car_seat = CarSeat(serial_number)
        self.active_user.add_car_seat(car_seat)

    def delete_car_seat(self, serial_number):
        car_seat = next((x for x in self.active_user.car_seats if x.serial_number == serial_number), None)
        if car_seat is not None:
            self.active_user.car_seats.remove(car_seat)



    def __del__(self):
        DataHandler.export_to_json(self.file_name)