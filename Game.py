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

    