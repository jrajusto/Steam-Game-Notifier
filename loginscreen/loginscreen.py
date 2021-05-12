from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import sqlite3
from Application import Application
from StorePrice import StorePrice
from Game import Game
from User import User
from GameBookmark import GameBookmark
from Notification import Notification
from kivy.core.window import Window

Window.size = (1280, 720)

Builder.load_file('loginscreen/loginscreen.kv')

class LoginScreenWindow(BoxLayout):
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)
        
        
        

    def validate_user(self):
        
        user = self.ids.user_field
        pasw = self.ids.pass_field
        uname = user.text
        pw = pasw.text
        info = self.ids.login_prompt  
        if uname == '' or pw == '':
            info.text = '[color=#FF0000]Both Username/Password is required.[/color]'
        else:
            found =  root.application.login(uname,pw)
            if found:
                info.text = '[color=#00FF00]Logged In Successfully![/color]'
                self.parent.parent.dingdong = "dong ding"
                self.parent.parent.current = 'scrn_ms'
                print(self.parent.parent.dingdong)
            else:
                info.text = '[color=#FF0000]Username/Password incorrect.[/color]'
                passw = hashlib.sha256(passw.encode()).hexdigest()
                
                     

class LoginScreenApp(App):
    def build(self):
        return LoginScreenWindow()

if __name__ == "__main__":
    
    la = LoginScreenApp()
    la.run() 
    
    