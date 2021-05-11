from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from loginscreen.loginscreen import LoginScreenWindow
from mainscreen.mainscreen import MainScreenWindow

class MainWindow(BoxLayout):

    login_widget = LoginScreenWindow()
    mainscreen_widget = MainScreenWindow()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.scrn_li.add_widget(self.login_widget)
        self.ids.scrn_ms.add_widget(self.mainscreen_widget)

class MainApp(App):
    def build(self):
        return MainWindow()
        
if __name__ == '__main__':
    MainApp().run()