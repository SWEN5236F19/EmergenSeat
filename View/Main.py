import os
from Model.DataHandler import DataHandler
from Model.UserProfile import UserProfile


profiles = [];

email = "parent123@gmail.com"
profile = UserProfile(email)
car_seat = profile.add_car_seat("123456ABCDEF")
car_seat.set_gps_location("29.760427", "-95.369804")

profiles.append(profile)

profile.print_user_profile()

file_name = os.getcwd() + "/userprofiles.json"
print(file_name)

DataHandler.export_to_json(file_name, profiles);
