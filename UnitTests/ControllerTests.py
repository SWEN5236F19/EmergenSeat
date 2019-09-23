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

if __name__ == '__main__':
    unittest.main()
