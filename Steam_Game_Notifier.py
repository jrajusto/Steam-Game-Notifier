'''This is the main logic for the program. It will'''
from Application import Application
from StorePrice import StorePrice
from Game import Game
from User import User
from GameBookmark import GameBookmark
from Notification import Notification
import sqlite3
import sqlite_database


application = Application()
application.initUsers()
application.initBookmark()
application.initGames()




