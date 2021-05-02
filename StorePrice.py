class StorePrice:

    def __init__(self, sname, sid, ds,np,cp):
        self.name = sname
        self.storeid = sid
        self.ds = ds
        self.normalPrice = np
        self.currentPrice = cp
        
    def getName(self):
        return self.name

    def getNormalPrice(self):
        return self.normalPrice

    def getCurrentPrice(self):
        return self.currentPrice

    def setName(self):
        self.name = input("Enter name of store: ") /"placeholder for UI and database"

    def setCurrentPrice(self,price):
        
        self.currentPrice = price