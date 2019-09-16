import os
import unittest
from Model.DataHandler import DataHandler
from Model.CarSeat import CarSeat
from Model.UserProfile import UserProfile


class DataHandlerTestCase(unittest.TestCase):
    def test_json_export(self):
        profile = UserProfile("parent123@gmail.com")
        car_seat = CarSeat("123ABC")
        car_seat.set_gps_location("29.760427", "-95.369804")
        profile.add_car_seat(car_seat);

        data = [profile.to_json()];
        DataHandler.export_to_json(os.getcwd() + "/resources/userprofiles.json", data)

    def test_json_import(self):
        data = DataHandler.import_from_json(os.getcwd() + "/resources/userprofiles.json")
        self.assertEqual(data["email"], "parent123@gmail.com")

    def test_convert_json_to_profiles(self):
        data = DataHandler.import_from_json(os.getcwd() + "/resources/userprofiles.json")
        profiles = DataHandler.convert_json_to_profiles(data)
        self.assertEqual(profiles[0].email, "parent123@gmail.com")
        car_seat = profiles[0].car_seats[0]
        self.assertEqual(car_seat.serial_number, "123ABC")
        self.assertEqual(car_seat.latitude, "29.760427")
        self.assertEqual(car_seat.longitude, "-95.369804")


if __name__ == '__main__':
    unittest.main()
