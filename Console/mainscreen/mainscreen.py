from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from collections import OrderedDict
from kivy.lang import Builder
import  sqlite3

from kivy.core.window import Window
Window.size = (1280, 720)

Builder.load_file('mainscreen/mainscreen.kv')


class MainScreenWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # def get_users(self):
    #         conn = sqlite3.connect('Tatlong_Juan_Database.db')
    #         c = conn.cursor()
    #         _users=OrderedDict()
    #         _users['first_names']={}
    #         _users['last_names']={}
    #         _users['user_names']={}
    #         _users['passwords']={}
    #         _users['designations']={}
    #         first_names=[]
    #         last_names=[]
    #         user_names=[]
    #         passwords=[]
    #         designations=[]

    #         sql='SELECT * FROM Store'
    #         c.execute(sql)
    #         users=c.fetchall()

    #         for user in users:
    #             first_names.append(user[1])
    #             last_names.append(user[2])
    #             user_names.append(user[3])
    #             first_names.append(user[4])
    #             first_names.append(user[5])
                

class MainScreenApp(App):
    def build(self):
        return MainScreenWindow() 

if __name__ == "__main__": 
    oa = MainScreenApp()
    oa.run()