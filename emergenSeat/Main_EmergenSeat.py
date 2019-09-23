import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.popup import Popup
import random

# ADDED: classes below
from Controller.controller import Controller

# Greeting
class GreetingScreen(Screen):
    pass


# Member Login
class LoginScreen(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    #usrCon = Controller()

    def checkCreds(self):
        """
            TODO: Check with DB for valid credentials
            # ADDED: check to see if email exist in DB
                    Pull in user email to validate returning user
                    check password with user email (Plain test = not secure, demo only)
        """
        if not ((self.password.text and self.email.text)
                and self.email.text.count("@") == 1
                and self.email.text.count(".") > 0):
            self.clear()
            Utility.showPopup(self, "Invalid Username of Password!", "Invalid Login")
            manager.current = 'login'
        else:
            # call login()
            # self.usrCon.login(self.email.text, self.password.text))
            self.clear()
            manager.current = 'member'

    def clear(self):
        self.email.text = ""
        self.password.text = ""


# New User Signup
class SignUpScreen(Screen):
    usrFirstName = ObjectProperty(None)
    usrLastName = ObjectProperty(None)
    usrEmail = ObjectProperty(None)
    usrPassword = ObjectProperty(None)
    usrCarSeat = ObjectProperty(None)

    def sendnewUser(self):
        if not (self.usrFirstName.text and self.usrLastName.text
                and self.usrEmail.text and self.usrPassword.text
                and self.usrCarSeat.text
                and self.usrEmail.text.count("@") == 1
                and self.usrEmail.text.count(".") > 0):
            Utility.showPopup(self, "Invalid information", "Invalid Registration!")
            self.clear()
            manager.current = 'signup'
        else:
            # ADDED: below, new user to DB (JSON)
            manager.controller.register(self.usrEmail, self.usrFirstName, self.usrLastName, self.usrPassword)
            # ADDED: everything above

            Utility.showPopup(self, "Thank you, your account has been created", "Account Created")
            self.clear()
            manager.current = 'login'

    def clear(self):
        self.usrFirstName.text = ""
        self.usrLastName.text = ""
        self.usrEmail.text = ""
        self.usrPassword.text = ""
        self.usrCarSeat.text = ""


# Member Register carseat
class RegisterSeat(Screen):
    """
        TODO: send validated data to DB
        carMake = ObjectProperty(None)
        carModel = ObjectProperty(None)
        carMYear = ObjectProperty(None)
        carVin = ObjectProperty(None)
        longitude = ObjectProperty(None)
        latitude = ObjectProperty(None)
    """
    nameOfSeat = ObjectProperty(None)
    serialNum = ObjectProperty(None)

    def sendCarSeat(self):
        if not (self.serialNum.text and self.nameOfSeat.text):
            Utility.showPopup(self, "Please fill all fields!", "Invalid Car Seat")
            self.clear()
            manager.current = 'register'
        else:
            # ADDED: send new car seat to DB
            '''
                TODO: get new car seat data, 
                      pull in user.email.car_seat from DB
                      append new seat to DB
                      
                (!) A car seat will be added to a user profile by user email                      
            '''
            # ADDED: above new car seat to DB

            Utility.showPopup(self, "Thank you, new car seat added!", "Car Seat Registration")
            self.clear()
            manager.current = 'member'

    def clear(self):
        self.serialNum.text = ""
        self.nameOfSeat.text = ""


class MemberArea(Screen):
    mbrFName = ObjectProperty(None)
    mbrLName = ObjectProperty(None)
    mbrEmail = ObjectProperty(None)
    mbrSeat = ObjectProperty(None)

    def on_enter(self, *args):
        self.mbrFName.text = "Full name:   " + controller.active_user.first_name
        self.mbrLName.text = "Last Name:   " + controller.active_user.last_name
        self.mbrEmail.text = "Account Email:   " + controller.active_user.email

        self.seatList(controller.active_user.car_seats)  # this does not print all car seats in list :-(
        self.status_check()
        Clock.schedule_interval(self.status_check, 10)

    def status_check(self, *args):
        self.generate_alarm(self.seat_weight(self.car_seat_list), self.seat_temp(self.car_seat_list))

    def seatList(self, data):
        # seat_list = self.userData["car_seats"]
        # hello = [({"text": result[0]}) for result in seat_list]
        count = 0
        for seat in data:
            count += 1
            self.mbrSeat.text = "\nCar Seats: \n" + ("{}. {}".format(count, seat))

    def seat_weight(self, car_seat):
        """
            weight will be set my a sensor in the seat.
            For now, randomly generated.
        """
        rn_weight = 0
        for cs in self.userData["car_seats"]:
            # random generated weight between 4lbs and 20lbs
            rn_weight = random.randrange(4, 20 + 1)
            print("Weight Sensor: {}".format(rn_weight))
        return rn_weight

    def seat_temp(self, car_seat):
        """
            temperature will be set my a sensor in the seat.
            For now, its randomly generated.
        """
        rn_temp = 0.0
        for cs in self.userData["car_seats"]:
            # random generated weight between 4lbs and 20lbs
            rn_temp = round(random.uniform(50.0, 101.9), 2)
            print("Car Temperature: {}".format(rn_temp))
        return rn_temp

    def generate_alarm(self, weight, temp):
        """
            this will check if weight >= 4lbs and if
            temp >= 80.0 degrees. If conditions are met,
            for now, the user will see a popup stating temp
            and weight.
        """
        warning_msg = ("         [!] Baby was left in the car!\n\n      The temperature is now {}\n"
                       "\nPLEASE RETURN TO YOUR VEHICLE".format(temp))
        if (weight >= 4) and (temp >= 80.0):
            Utility.showAlarmPopup(self, warning_msg, "EmergenSeat Alarm")


class Utility(object):
    @staticmethod
    def showPopup(self, msg, tlt):
        pop = Popup(title=tlt,
                    content=Label(text=msg),
                    size_hint=(None, None), size=(400, 400))
        pop.open()

    @staticmethod
    def showAlarmPopup(self, msg, tlt):
        pop = Popup(title=tlt,
                    content=Label(text=msg),
                    size_hint=(None, None), size=(400, 400),
                    font_size="100sp",
                    background="warning.jpeg")
        pop.open()


class WindowManager(ScreenManager):
    pass

# loads the kv lang file
fl = Builder.load_file("emergenseat.kv")

# ScreenManagers
manager = WindowManager()
controller = Controller()
app_screens = [GreetingScreen(name='greeting'), LoginScreen(name='login'),
               SignUpScreen(name='signup'), RegisterSeat(name='register'),
               MemberArea(name='member')]

for apps in app_screens:
    manager.add_widget(apps)

# sets the first page of app
manager.current = "member"


class EmergenSeatApp(App):
    def build(self):
        return manager


if __name__ == "__main__":
    EmergenSeatApp().run()
