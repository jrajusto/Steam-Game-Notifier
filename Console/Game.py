class Game:

    def __init__(self, aid, gname,plains, storelist):
        self.appid = aid
        self.name = gname
        self.store = storelist
        self.plains = plains

    def getName(self):
        return self.name

    def getAppID(self):
        return self.appid

    def getStore(self):
        return self.store
