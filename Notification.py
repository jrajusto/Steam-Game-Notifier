class Notification:
    
    def __init__(self):
        self.number = 0
        self.notifList = list()
        self.seenNotification = False

    def getNo(self):
        return self.number

    def printNotif(self):
        for x in self.notifList:
            print(x)
        self.seenNotification = True

    def addNotif(self,game,discount):
        self.notifList.append("The game "+game+" now has a " +discount+"%\ discount on Steam!" )
        self.number = self.number + 1
        self.seenNotification = False