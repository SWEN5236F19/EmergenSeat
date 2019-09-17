import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

#Greeting
class GreetingScreen(Screen):
    pass

#Member Login
class LoginScreen(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def checkCreds(self):
        """
            TODO: Check with DB for valid credentials
        """
        if not ((self.password.text and self.email.text)
                and self.email.text.count("@") == 1
                and self.email.text.count(".") > 0):
            self.clear()
            utility.showPopup(self,"Invalid Username of Password!", "Invalid Login" )
            manager.current = 'login'
        else:
            self.clear()
            manager.current = 'member'

    def clear(self):
        self.email.text = ""
        self.password.text = ""

#New User Signup
class SignUpScreen(Screen):
    """
        TODO: send validated data to DB
    """
    usrFirstName = ObjectProperty(None)
    usrLastName = ObjectProperty(None)
    usrEmail = ObjectProperty(None)
    usrPassword =ObjectProperty(None)

    def sendnewUser(self):
        if not (self.usrFirstName.text and self.usrLastName.text
                and self.usrEmail.text and self.usrPassword.text
                and self.usrEmail.text.count("@") == 1
                and self.usrEmail.text.count(".") > 0):
            utility.showPopup(self,"Invalid information", "Invalid Registration!")
            self.clear()
            manager.current = 'signup'
        else:
            utility.showPopup(self,"Thank you, your account has been created", "Account Created")
            manager.current = 'login'

    def clear(self):
        self.usrFirstName.text = ""
        self.usrLastName.text = ""
        self.usrEmail.text = ""
        self.usrPassword.text = ""

#Member Register carseat
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
            utility.showPopup(self,"Please fill all fields!", "Invalid Car Seat")
            self.clear()
            manager.current = 'register'
        else:
            utility.showPopup(self,"Thank you, new car seat added!", "Car Seat Registration")
            manager.current = 'member'

    def clear(self):
        self.serialNum.text = ""
        self.nameOfSeat.text = ""


class MemberArea(Screen):
    pass

class utility:
    @staticmethod
    def showPopup(self, msg, tlt):
        pop = Popup(title=tlt,
                    content=Label(text=msg),
                    size_hint = (None, None), size = (400, 400))
        pop.open()

class WindowManager(ScreenManager):
    pass

#loads the kv lang file
fl = Builder.load_file("emergenseat.kv")

#ScreenManager
manager = WindowManager()
app_screens = [GreetingScreen(name='greeting'), LoginScreen(name='login'),
           SignUpScreen(name='signup'), RegisterSeat(name='register'),
           MemberArea(name='member')]
for apps in app_screens:
    manager.add_widget(apps)

manager.current = "greeting"

class EmergenSeatApp(App):
    def build(self):
        return manager

if __name__ == "__main__":
    EmergenSeatApp().run()
