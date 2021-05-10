
from Notification import Notification
import sqlite_database
import sqlite3

class GameBookmark:

    def __init__(self):
        self.bookmark = list()
        self.notification = Notification()

    def getList(self):
        return self.bookmark

    def update(self):
        #edit later
        conn = sqlite3.connect('Steam games.db')
        for game in self.bookmark:
            storeList = game.getStore()
            for storePrice in storeList:
                if store.getName() == "Steam":
                    discount = sqlite_database.getStoreDiscount(conn,storePrice.getStoreID())
                    if discount[0] != storePrice.getDiscount():
                        storePrice.setDiscount(discount[0])
                        storePrice.setCurrentPrice(sqlite_database.getStoreCurPrice(conn,storePrice.getStoreID()))
                        if discount[0] > storePrice.getDiscount():
                            self.notification.addNotif(game.getName(),discount[0])

    def getNotification(self):
        return self.notification.getNo()

    def addGame(self,game):
        self.bookmark.append(game)

