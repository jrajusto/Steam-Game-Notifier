from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, EventDispatcher, ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from Application import Application
from StorePrice import StorePrice
from Game import Game
from User import User
from GameBookmark import GameBookmark
from Notification import Notification

class MyState(EventDispatcher):
    application = Application()

class LogIn(Screen):
    def validate_user(self):
        
        print('initBookmark')
        self.manager.statedata.application.initUsers()
        self.manager.statedata.application.initBookmark()
        user = self.ids.user_field
        pasw = self.ids.pass_field
        uname = user.text
        pw = pasw.text
        info = self.ids.login_prompt  
        if uname == '' or pw == '':
            info.text = '[color=#FF0000]Both Username/Password is required.[/color]'
        else:
            found =  self.manager.statedata.application.login(uname,pw)
            if found:
                info.text = '[color=#00FF00]Logged In Successfully![/color]'
                return True
            else:
                info.text = '[color=#FF0000]Username/Password incorrect.[/color]'
               # passw = hashlib.sha256(passw.encode()).hexdigest()
                return False

class MainScreen(Screen):
    pass

class WindowManager(ScreenManager):
    statedata = ObjectProperty(MyState())


kv = Builder.load_file('new_window.kv')
class SteamGameNotif(App):
    def build(self):
        return kv


if __name__ == '__main__':
    SteamGameNotif().run()