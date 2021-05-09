
from Notification import Notification
class GameBookmark:

    def __init__(self):
        self.bookmark = list()
        self.notification = Notification()

    def getList(self):
        return self.bookmark

    def update(self, newGame):
        #edit later
        for x in newGame:
            self.bookmark.append(x)

    def getNotification(self):
        return self.notification.getNo()

    def addGame(self,game):
        self.bookmark.append(game)

