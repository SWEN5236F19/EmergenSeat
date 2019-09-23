from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen

# Changed: classes below
from Controller.Controller import Controller


# Changed: everything above


# Greeting
class GreetingScreen(Screen):
    pass


# Member Login
class LoginScreen(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def checkCreds(self):
        #added login controller.login will return 1 if successfull login and 0 if failed
        logged_in = manager.controller.login(self.email, self.password)
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
            # Changed: used controller
            # may need add_usr_to_db()
            
            manager.controller.register(self.usrEmail, self.usrFirstName, self.usrLastName, self.usrPassword)

            # changed: everything above

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
            # changed: send new car seat to DB
            manager.controller.add_car_seat(self.serialNum)
            # changed: above new car seat to DB

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
        count = 0
        self.mbrFName.text = "Full name:   "+ manager.controller.active_user.first_name
        self.mbrLName.text = "Last Name:   " + manager.controller.active_user.last_name
        self.mbrEmail.text = "Account Email:   " + manager.controller.active_user.email

        # changed: below
        # this will get you an array of car seats for the current active user
        manager.controller.get_car_seats();


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
    def __init__(self):
        controller = Controller()
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
