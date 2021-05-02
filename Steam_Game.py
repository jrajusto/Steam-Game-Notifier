'''This is the main logic for the program. It will'''

class User:

    def __init__(self, name, id):
        self.username = name
        self.userID = id
        self.bookmark = GameBookmark()

    def addGameToBookmark(self, newGame):
        self.bookmark.add(newGame)

    def getName(self):
        return self.username

    def getID(self):
        return self.userID

    def getBookmark(self):
        return self.bookmark

class GameBookmark:

       def __init__(self):
           self.bookmark = list(None)
           self.notification = Notification()

       def getList(self):
            return self.bookmark

       def update(self, newGame):
           for x in newGame:
            self.bookmark.append(x)

       def getNotification(self):
           return self.Notification().number

class Notification:
    
    def __init__(self):
        self.number = 0
        self.notifList = list(None)
        seenNotification = false

    def getNo(self):
        return self.number

    def printNotif(self):
        for x in notifList:
            print(x)
        self.seenNotification = true

    def addNotif(self, newNot):
        self.notifList.append()
        self.seenNotification = false

class Game:

    def __init__(self, aid, gname, storelist):
        self.appid = aid
        self.name = gname
        self.store = storelist

    def getName(self):
        return self.name

    def getAppID(self):
        return self.appid

    def getStore(self):
        return self.store

    
class Store:

    def __init__(self, sname, sid, ds):
        self.name = sname
        self.storeid = sid
        self.ds = ds
        self.normalPrice = 100 /"placeholder normal price from database"
        
    def getName(self):
        return self.name

    def getNormalPrice(self):
        return normalPrice

    def getCurrentPrice(self):
        return currentPrice

    def setName(self):
        self.name = input("Enter name of store: ") /"placeholder for UI and database"

    def setCurrentPrice(self):
        discountP = input("Enter the discount percent: ") /"placeholder input for database"
        self.currentPrice = self.normalPrice - (self.NormalPrice * discountP)

class Application:

    def __init__(self):
        self.gameList = list(None)
        self.gamesList = list(None)
        self.userList = list(None)

    def getUsers(self):
        return self.userList