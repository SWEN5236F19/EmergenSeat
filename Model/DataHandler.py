import json

from Model.CarSeat import CarSeat
from Model.UserProfile import UserProfile


class DataHandler(object):

    @staticmethod
    def export_to_json(file_name, user_profiles):
        with open(file_name, 'w') as outfile:
            json.dump(user_profiles, outfile, indent=2)
            outfile.close()

    @staticmethod
    def import_from_json(file_name):
        with open(file_name) as json_file:
            data = json.load(json_file)
            return data

    @staticmethod
    def convert_json_to_profiles(data):
        profiles = []
        for obj in data:
            profile = UserProfile(obj["email"], obj["first_name"], obj["last_name"], obj["password"])
            for seat in obj["car_seats"]:
                car_seat = CarSeat(seat["serial_number"])
                car_seat.set_gps_location(seat["latitude"], seat["longitude"])
                profile.add_car_seat(car_seat)
            profiles.append(profile)
        return profiles
