'''This is the main logic for the program. It will'''
from Application import Application
from StorePrice import StorePrice
from Game import Game
from User import User
from GameBookmark import GameBookmark
from Notification import Notification
import sqlite3
import sqlite_database
from datetime import datetime
import sys
from loginscreen.loginscreen import LoginScreenWindow
from loginscreen.loginscreen import LoginScreenApp
from kivy.core.window import Window
from kivy.lang import Builder
#Builder.load_file('loginscreen/loginscreen.kv')

def printTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)


#Builder.load_file('loginscreen/loginscreen.kv')
la = LoginScreenApp()
la.run() 
    
'''
print('login')
printTime()
application.login()
print('update')
printTime()
application.update()
printTime()
print('done')
'''









