import unittest

from Model.Car import Car
from Model.CarSeat import CarSeat
from Model.UserProfile import UserProfile


class MyTestCase(unittest.TestCase):
    def test_create_profile(self):
        profile = UserProfile("parent123@gmail.com", "parent", "last", "password")
        self.assertEqual(profile.email, "parent123@gmail.com")
        self.assertEqual(profile.first_name, "parent")
        self.assertEqual(profile.last_name, "last")
        self.assertEqual(profile.password, hash("password"))
        self.assertEqual(profile.car_seats.__len__(), 0)

    def test_create_car_seat(self):
        car_seat = CarSeat("123ABC", "Graco - Extend to Fit")
        self.assertEqual(car_seat.serial_number, "123ABC")
        self.assertEqual(car_seat.model, "Graco - Extend to Fit")

    def test_gps_location(self):
        car_seat = CarSeat("123ABC", "Graco - Extend to Fit")
        car_seat.set_gps_location("29.760427", "-95.369804")
        self.assertEqual(car_seat.latitude, "29.760427")
        self.assertEqual(car_seat.longitude, "-95.369804")

    def test_create_car(self):
        car = Car()
        car.set_car("Toyota", "Highlander", "2019", "vin_number_goes_here")
        self.assertEqual(car.year, "2019")
        self.assertEqual(car.make, "Toyota")
        self.assertEqual(car.model, "Highlander")
        self.assertEqual(car.vin, "vin_number_goes_here")

    def test_update_weight(self):
        car_seat = CarSeat("123ABC", "Graco - Extend to Fit")
        car_seat.set_gps_location("29.760427", "-95.369804")
        car_seat.set_weight(6.5, "lbs")
        self.assertEqual(car_seat.weight, 6.5)
        self.assertEqual(car_seat.weight_unit, "lbs")

    def test_update_temp(self):
        car_seat = CarSeat("123ABC", "Graco - Extend to Fit")
        car_seat.set_gps_location("29.760427", "-95.369804")
        car_seat.set_temperature(72.1, "Fahrenheit")
        self.assertEqual(car_seat.temperature, 72.1)
        self.assertEqual(car_seat.temperature_unit, "Fahrenheit")

if __name__ == '__main__':
    unittest.main()
