from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import sqlite3

from kivy.core.window import Window
Window.size = (1280, 720)

#Builder.load_file('loginscreen/loginscreen.kv')

class LoginScreenWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        self.user.login()

        # # conn=sqlite3.connect('Steam-Games.db')
        # # c = conn.cursor()

        # user = self.ids.user_field
        # pasw = self.ids.pass_field
        # info = self.ids.login_prompt

        # uname = user.text
        # pw = pasw.text

        # if uname == '' or pw == '':
        #     info.text = '[color=#FF0000]Both Username/Password is required.[/color]'
        # else:
        #     if uname == 'admin' and pw == 'admin':
        #         info.text = '[color=#00FF00]Logged In Successfully![/color]'
        #         self.parent.parent.current = 'scrn_ms'
        #     else:
        #         info.text = '[color=#FF0000]Username/Password is invalid.[/color]'
                
        # # if uname == '' or pw == '':
        # #     info.text = '[color=#FF0000]Both Username/Password is required.[/color]'
        # # else:
        # #     users = c.find_one({'user_name':uname})

        # #     if user == NONE:
        # #         info.text = '[color=#FF0000]Username/Password incorrect.[/color]'
        # #     else:
        # #         passw = hashlib.sha256(passw.encode()).hexdigest()
        # #         if pw == user['password']:
        # #             info.text = '[color=#00FF00]Logged In Successfully![/color]'
        # #             self.parent.parent.current = 'scrn_ms'
        # #         else:
        # #             info.text = '[color=#FF0000]Username/Password incorrect.[/color]'

class LoginScreenApp(App):
    def build(self):
        return LoginScreenWindow()

if __name__ == "__main__":
    la = LoginScreenApp()
    la.run() 