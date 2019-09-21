import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

# ADDED: classes below
from Model.UserProfile import UserProfile
from Model.DataHandler import DataHandler
# ADDED: everything above


# Greeting
class GreetingScreen(Screen):
    pass


# Member Login
class LoginScreen(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

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
            # may need add_usr_to_db()
            usr = UserProfile(self.usrEmail.text)
            usr.first_name = self.usrFirstName.text
            usr.last_name = self.usrLastName.text
            usr.password = self.usrPassword.text
            usr.add_car_seat(self.usrCarSeat.text)

            DataHandler.export_to_json("test_deleteMe.json", usr.to_json())
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

    # ADDED: below
    userData = DataHandler.import_from_json("test_deleteMe.json")  # hard coded file name
    # ADDED: above

    def on_enter(self, *args):
        count = 0
        self.mbrFName.text = "Full name:   "+self.userData["First Name"]
        self.mbrLName.text = "Last Name:   " + self.userData["Last Name"]
        self.mbrEmail.text = "Account Email:   " + self.userData["email"]

        # ADDED: below
        # this does not print all car seats in list :-(
        for seat in self.userData["car_seats"]:
            count += 1
            self.mbrSeat.text = "\nCar Seats: \n" + ("{}. {}".format(count, seat))


        # ADDED: temperature and weight
        """
            TODO: add get_weight(weight, car_seat),
                  add get_temp(tmp, car_seat), 
                  add generate_alarm()
                  
             get_weight(weight, car_seat) will take a weight and car_seat serial
                if weight is 0, then no alarms
                if weight > 0 
                    call get temp()
            
            get_temp(temp, car_seat) will monitor the temperature
                if temp == normal 
                    no alarms
                if temp > normal | temp < normal
                    call generate_alarm()
                    
            generate_alarm() will pull in will temp and weight
                alarm is sound and lights 
                for now its just a text output maybe with colors flashing.                  
        """



class Utility:
    @staticmethod
    def showPopup(self, msg, tlt):
        pop = Popup(title=tlt,
                    content=Label(text=msg),
                    size_hint=(None, None), size=(400, 400))
        pop.open()


class WindowManager(ScreenManager):
    pass


# loads the kv lang file
fl = Builder.load_file("emergenseat.kv")

# ScreenManagers
manager = WindowManager()
app_screens = [GreetingScreen(name='greeting'), LoginScreen(name='login'),
               SignUpScreen(name='signup'), RegisterSeat(name='register'),
               MemberArea(name='member')]

for apps in app_screens:
    manager.add_widget(apps)

# sets the first page of app
manager.current = "greeting"


class EmergenSeatApp(App):
    def build(self):
        return manager


if __name__ == "__main__":
    EmergenSeatApp().run()
