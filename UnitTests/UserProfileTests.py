import unittest

from Model.CarSeat import CarSeat
from Model.UserProfile import UserProfile


class MyTestCase(unittest.TestCase):
    def test_create_profile(self):
        profile = UserProfile("parent123@gmail.com")
        self.assertEqual(profile.email, "parent123@gmail.com")
        self.assertEqual(profile.car_seats.__len__(), 0)

    def test_create_car_seat(self):
        car_seat = CarSeat("123ABC")
        self.assertEqual(car_seat.serial_number, "123ABC")

    def test_gps_location(self):
        car_seat = CarSeat("123ABC")
        car_seat.set_gps_location("29.760427", "-95.369804")
        self.assertEqual(car_seat.latitude, "29.760427")
        self.assertEqual(car_seat.longitude, "-95.369804")

if __name__ == '__main__':
    unittest.main()
