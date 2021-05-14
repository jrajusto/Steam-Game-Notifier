from GameBookmark import GameBookmark
from Game import Game

class User:

    def __init__(self, id, name,password):
        self.username = name
        self.userID = id
        self.bookmark = GameBookmark()
        self.password = password

    def addGameToBookmark(self, newGame):
        self.bookmark.addGame(newGame)

    def getName(self):
        return self.username

    def getID(self):
        return self.userID

    def getBookmark(self):
        return self.bookmark

    def getPassword(self):
        return self.password

    def printBookmarks(self):
        gamesList = self.bookmark.getList()
        number = 0
        for i in gamesList:
            print("["+str(number)+"]")
            print("\nGame: "+i.getName())
            for store in i.getStore():
                print("\tStore: " + store.getName())
                print("\tNormal Price: "+ str(store.getNormalPrice()) + "USD")
                print("\tCurrent Price: " + str(store.getCurrentPrice())+ "USD")
                print("\tDiscount: " + str(store.getDiscount())+ "\n")
            number = number + 1


