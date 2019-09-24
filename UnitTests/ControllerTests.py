import unittest

from Controller.controller import Controller


class ControllerTestCase(unittest.TestCase):
    def test_controller_instantiate(self):
        controller = Controller()
        self.assertIsNotNone(controller)
        self.assertIsNotNone(controller.user_profiles)

    def test_register(self):
        controller = Controller()
        controller.register("test@abc.com", "john", "doe", "p@ssw0rd")
        self.assertIsNotNone(controller.active_user)
        self.assertEqual(controller.active_user.email, "test@abc.com")

    def test_login(self):
        controller = Controller()
        loggedIn = controller.login("test@abc.com", "p@ssw0rd")
        self.assertEqual(loggedIn, 1)
        self.assertIsNotNone(controller.active_user)
        self.assertEqual(controller.active_user.email, "test@abc.com")

    def test_get_user_car_seats(self):
        controller = Controller()
        controller.login("parent123@gmail.com", "password")
        self.assertIsNotNone(controller.active_user.car_seats)
        self.assertEqual(controller.active_user.car_seats[0].serial_number, "123ABC")

    def test_add_car_seat(self):
        controller = Controller()
        controller.login("parent123@gmail.com", "password")
        controller.add_car_seat("CD80D789SD8090S", "Graco - Extend to Fit")
        self.assertEqual(controller.active_user.car_seats[1].serial_number, "CD80D789SD8090S")
        self.assertEqual(controller.active_user.car_seats[1].model, "Graco - Extend to Fit")

    def test_delete_car_seat(self):
        controller = Controller()
        controller.login("parent123@gmail.com", "password")
        controller.delete_car_seat("CD80D789SD8090S")
        self.assertEqual(len(controller.active_user.car_seats), 1)


if __name__ == '__main__':
    unittest.main()
