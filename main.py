from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from Application import Application
from StorePrice import StorePrice
from Game import Game
from User import User
from GameBookmark import GameBookmark
from Notification import Notification
from kivy.uix.screenmanager import ScreenManager, Screen, EventDispatcher

from loginscreen.loginscreen import LoginScreenWindow
from mainscreen.mainscreen import MainScreenWindow

class MainWindow(BoxLayout):

    login_widget = LoginScreenWindow()
    mainscreen_widget = MainScreenWindow()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('initUsers')
        self.application = Application()
        print('initBookmark')
        self.application.initUsers()
        self.application.initBookmark()
        self.ids.scrn_li.add_widget(self.login_widget)
        self.ids.scrn_ms.add_widget(self.mainscreen_widget)
        self.dingdong = "ding dong"
        
class MainApp(App):
    def build(self):
        return MainWindow()
        
if __name__ == '__main__':
    MainApp().run()