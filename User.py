from GameBookmark import GameBookmark
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

