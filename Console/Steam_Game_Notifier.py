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
application.initUsers()

print('\nLogin\n')
application.login()
application.initBookmark()
conn = sqlite3.connect('Steam games.db')
application.printNotificationNo()
prompt = "\nWhat would you like to do? \n [0] quit [1] search game  [2] show free games [3] access bookmarks [4] access notifications [5] update Database\n\n>> "


userInput = input(prompt)
while userInput != '0':

    if userInput == "1":
        gameName = input("\nEnter game name: ")
        application.addGames(gameName)
        application.printGames()
        userInput = input("Would you like to add to bookmark? (y/n) \n\n >> ")
        while userInput != "n":
            userInput = input("\nInput the game number of the game you would like to add:\n\n>> ")
            application.user.addGameToBookmark(application.gameList[int(userInput)])
            sqlite_database.addGameToBookmark(conn,application.user.getID(),application.gameList[int(userInput)].getAppID())
            userInput = input("\nWould you like to add to bookmark? (y/n) \n\n>> ")
        application.clearList()

    if userInput == "2":
        print("\nFree games today: ")
        application.getFreeGames()
        application.printGames()
        application.clearList()
    if userInput == "3":
        print("\nBookmark List \n")
        application.printBookmarks()

    if userInput == '4':
        application.printNotifications()
        userInput = input("\nWould you like to clear your notifications (y/n)\n\n>> ")
        if userInput == "y":
            application.clearNotifs()

    if userInput == "5":
        application.update()
        
    application.printNotificationNo()
    userInput = input(prompt)


'''
print('update')
printTime()
application.update()
printTime()
print('done')
'''

