from Bookmark import GameBookmark
class User:

    def __init__(self, name, id):
        self.username = name
        self.userID = id
        self.bookmark = GameBookmark()

    def addGameToBookmark(self, newGame):
        self.bookmark.addGame(newGame)

    def getName(self):
        return self.username

    def getID(self):
        return self.userID

    def getBookmark(self):
        return self.bookmark