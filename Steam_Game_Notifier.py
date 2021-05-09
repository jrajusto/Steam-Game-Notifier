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

def printTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

application = Application()
print('initUsers')
printTime()
application.initUsers()
print('initBookmark')
printTime()
application.initBookmark()
print('login')
printTime()
application.login()
print('update')
printTime()
application.update()
printTime()
print('done')









