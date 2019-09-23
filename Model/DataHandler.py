import json

from Model.CarSeat import CarSeat
from Model.UserProfile import UserProfile


class DataHandler(object):

    @staticmethod
    def export_to_json(file_name, user_profiles):
        with open(file_name, 'W') as outfile:
            json.dump(user_profiles, outfile, indent=2)
            outfile.close()

    @staticmethod
    def import_from_json(file_name):
        with open(file_name) as json_file:
            data = json.load(json_file)
            return data

    @staticmethod
    def convert_json_to_profiles(data):
        """
            Hey Im not understanding the use of obj when
            referencing data for a user profile?
            obj in this since is a number
            When I go to create a controller instance,
            in order to call its methods (controller.login()),
            I get a "TypeError: string indices must be integers".
        """
        profiles = []
        for obj in data:
            profile = UserProfile(obj["email"])  # <----?----
            for seat in obj["car_seats"]:
                car_seat = CarSeat(seat["serial_number"])
                car_seat.set_gps_location(seat["latitude"], seat["longitude"])
                profile.add_car_seat(car_seat)
            profiles.append(profile)
        return profiles
