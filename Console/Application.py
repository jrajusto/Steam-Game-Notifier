from logging import StringTemplateStyle
from User import User
import sqlite_database
import sqlite3
from GameBookmark import GameBookmark
from StorePrice import StorePrice
from Game import Game
import requests

class Application:

    def __init__(self):
        self.gameList = list()
        self.userList = list()
        self.user = User(None,None,None)

    def getUsers(self):
        return self.userList

    def login(self):
        conn = sqlite3.connect('Steam games.db')
        login = False
        while login == False:
            username = input("Username: ")
            password = input("Password: ")
            userID  = sqlite_database.findUserID(conn,username,password)
        
            if userID != None:
                #print(self.userList[userID[0]])
                self.user = self.userList[userID[0]]
                #print(self.user)
                login = True
            else:
                print("Username and password does not match!")
        

    def addUser(self,userInfo):
        user = User(userInfo[0],userInfo[1],userInfo[2])
        self.userList.append(user)

    def addGame(self,game):
        self.gameList.append(game)
    
    def initBookmark(self):
        conn = sqlite3.connect('Steam games.db')
        id = self.user.getID()
        bookmarkList = sqlite_database.getBookmark(conn,id)
        for i in bookmarkList:
            storeList = []
            storeIDlist = sqlite_database.getStoreIDList2(conn,i)
            for j in storeIDlist:
                
                storeInfo = sqlite_database.getStoreInfo(conn,j)
                storePrice = StorePrice(storeInfo[0],storeInfo[1],storeInfo[2],storeInfo[3],storeInfo[4])
                storeList.append(storePrice)
            
            gameInfo = sqlite_database.getGameInfo(conn,i)
            game = Game(gameInfo[0],gameInfo[1],gameInfo[2],storeList)
            self.user.addGameToBookmark(game)

        notifs = sqlite_database.getNotifs(conn,(id,))
        for i in notifs:
            game = sqlite_database.getGameInfo(conn,i)
            storeID = sqlite_database.getStorePriceSteamDiscount(conn,i)
            self.user.bookmark.notification.addNotif(game[1],str(storeID[0]))

    def initUsers(self):
        conn = sqlite3.connect('Steam games.db')
        users = sqlite_database.getUsers(conn)

        for i in users:
             self.addUser(i)

    def initGames(self):
        conn = sqlite3.connect('Steam games.db')
        games = sqlite_database.getGames(conn)
        for i in games:

            storeList = []
            storeIDlist = sqlite_database.getStoreIDList(conn,i[0])
            for j in storeIDlist:
                
                storeInfo = sqlite_database.getStoreInfo(conn,j)
                #print (storeInfo)
                storePrice = StorePrice(storeInfo[0],storeInfo[1],storeInfo[2],storeInfo[3],storeInfo[4])
                storeList.append(storePrice)
            game = Game(i[0],i[1],i[2],storeList)
            self.addGame(game)
    
    
    def updateNewGames(self):
        #add new games
        conn = sqlite3.connect('Steam Games.db')
        c = conn.cursor()
        dealAPI = '44587204c43f4187a3b2b01f590949494717aa14'
        steamKey = 'A6434537190388EB7A022C0C6780946B'
        response = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v2/?key='+steamKey)
        key = response.json()
        site = "https://api.isthereanydeal.com/v01/game/prices/?key="+dealAPI+"&plains="
        response2 =  requests.get("https://api.isthereanydeal.com/v01/game/plain/list/?key=" + dealAPI + "&shops=steam")
        key2 = response2.json()
        tempList = []
        newGame = []
        for i in key['applist']['apps']:
            plains =  key2['data']['steam'].get('app/'+str(i['appid']))
            if plains != None:
                c.execute("SELECT * FROM Steam_games WHERE appID = ?",(i['appid'],))
                existance = c.fetchall()
                if len(existance) == 0:
                    temp = (i['appid'],i['name'],plains)
                    tempList.append(temp)
            
        counter = 0
        site2 = site
        counter2 = 0
        max = len(tempList)
        gameList = []
        finalList = []
        for i in tempList:
            counter2 = counter2 + 1
            counter = counter + 1
            plains = i[2]
            site2 = site2 + plains +"%2C"
            gameList.append(i)
            if counter == 115 or counter2 == max:
                counter = 0
                response = requests.get(site2+"&region=us&country=US")
                #print(site2)
                site2 = site
                key = response.json()
                if key != None:
                    for j in gameList:
                        shopList = key['data'][j[2]].get("list")
                        if len(shopList)!=0:
                            newGame.append(j[0])
                            finalList.append(j)
                            #print(finalList)
                
                gameList = []

        
        c.executemany("INSERT INTO Steam_games VALUES (?,?,?)",finalList)
        conn.commit()
        conn.close()
        return newGame


        
    def updateNewGamePrices(self,newGame):
        #add new game prices
        conn = sqlite3.connect('Steam Games.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Store_price")
        number = c.fetchall()
        tempList1 = []
        tempList2 = []
        dealAPI = '44587204c43f4187a3b2b01f590949494717aa14'
        site = "https://api.isthereanydeal.com/v01/game/prices/?key="+dealAPI+"&plains="
        plainsList = []
        idList = []
        counter = 0
        site2 = site
        counter2 = 0
        counter3 = len(number) 
        counter4 = 0
        max = len(newGame)
        for i in newGame:
            info = sqlite_database.getGameInfo2(conn,str(i))
            counter2 = counter2 + 1
            counter = counter + 1
            plains = info[2]
            id = i
            site2 = site2 + plains +"%2C"
            plainsList.append(plains)
            idList.append(id)
            if counter == 150 or counter2 == max:
                
                counter = 0
                response = requests.get(site2+"&region=us&country=US")
                site2 = site
                key = response.json()
                for j in plainsList:
                    shopList = key['data'][j].get("list")
                    for k in shopList:
                        #print(counter3,k['shop']['name'],k['price_old'],k['price_new'],k['price_cut'])
                        tempTuple1 = (counter3,k['shop']['name'],k['price_old'],k['price_new'],k['price_cut'])
                        tempList1.append(tempTuple1)
                        tempTuple2 = (idList[counter4],counter3)
                        tempList2.append(tempTuple2)
                        counter3 = counter3 + 1
                    counter4 = counter4 + 1
                counter4 = 0 
                c.executemany("INSERT INTO Store_price VALUES (?,?,?,?,?)",tempList1)    
                c.executemany("INSERT INTO game_store VALUES (?,?)",tempList2)    
                conn.commit()
                tempList1 = [] 
                tempList2 = [] 
                plainsList = []
                idList = []
        conn.commit()
        conn.close()

    def updateGames(self):
        #update existing games
        
        conn = sqlite3.connect('Steam Games.db')
        c = conn.cursor()

        c.execute("SELECT * FROM Steam_games")
        temp = c.fetchall()

        tempList1 = []
        dealAPI = '44587204c43f4187a3b2b01f590949494717aa14'
        site = "https://api.isthereanydeal.com/v01/game/prices/?key="+dealAPI+"&plains="

        plainsList = []
        idList = []
        counter = 0
        site2 = site
        counter2 = 0
        counter4 = 0
        max = len(temp)
        for i in temp:
            counter2 = counter2 + 1
            counter = counter + 1
            plains = i[2]
            id = i[0]
            site2 = site2 + plains +"%2C"
            plainsList.append(plains)
            idList.append(id)
            if counter == 150 or counter2 == max:
                
                counter = 0
                response = requests.get(site2+"&region=us&country=US")
                site2 = site
                key = response.json()
                for j in plainsList:
                    shopList = key['data'][j].get("list")
                    for k in shopList:
                        #print(k['shop']['name'],k['price_old'],k['price_new'],k['price_cut'])
                        storeID = sqlite_database.getStorePriceID(conn,idList[counter4],k['shop']['name'])
                        if storeID != None:
                            store = sqlite_database.getStoreInfo(conn, (storeID[0],))
                            if store[4] != k['price_cut']:
                                tempTuple1 = (k['price_new'],k['price_cut'],store[0])
                                tempList1.append(tempTuple1)
                            if (k['price_cut'] > store[4]) and sqlite_database.gameInBookmark(conn,self.user.getID(),idList[counter4]) and k['shop']['name'] == 'Steam':
                                sqlite_database.addNotif(conn,self.user.getID(),idList[counter4])
                                gameInfo = sqlite_database.getGameInfo(conn,(idList[counter4],))
                                self.user.bookmark.notification.addNotif(gameInfo[1],str(k['price_cut']))
                        
                    counter4 = counter4 + 1
                counter4 = 0 
                plainsList = []
                idList = []

        #print('done')
        sqlite_database.update_Store(conn,tempList1)  
        conn.commit()
        conn.close()

    def addGames(self, gameName):
        conn = sqlite3.connect('Steam Games.db')
        games = sqlite_database.getGamesByName(conn,gameName)
        for i in games:
            storeIDs = sqlite_database.getStoreIDList(conn,i[0])
            storeList = []
            for store in storeIDs:
                storeInfo = sqlite_database.getStoreInfo(conn,store)
                storeprice = StorePrice(storeInfo[0],storeInfo[1],storeInfo[2],storeInfo[3],storeInfo[4])
                storeList.append(storeprice)
            game = Game(i[0],i[1],i[2],storeList)
            self.gameList.append(game)

    def printGames(self):
        number = 0
        for i in self.gameList:
            print("["+str(number)+"]")
            print("\nGame: "+i.getName())
            for store in i.getStore():
                print("\tStore: " + store.getName())
                print("\tNormal Price: "+ str(store.getNormalPrice()) + "USD")
                print("\tCurrent Price: " + str(store.getCurrentPrice())+ "USD")
                print("\tDiscount: " + str(store.getDiscount())+ "\n")
            number = number + 1

    def update(self):
        print("adding new games...")
        newGames = self.updateNewGames()
        print("setting prices for new games...")
        self.updateNewGamePrices(newGames)
        print("updating all games...")
        self.updateGames()

    def clearList(self):
        self.gameList = []

    def getFreeGames(self):
        conn = sqlite3.connect('Steam Games.db')
        storePrices = sqlite_database.getFreeGames(conn)

        for i in storePrices:
            storeList = []
            #print(i)
            appID = sqlite_database.getAppID(conn, (str(i[0]),))
            gameInfo = sqlite_database.getGameInfo(conn,appID)
            storePrice = StorePrice(i[0],i[1],i[2],i[3],i[4])
            storeList.append(storePrice)
            game = Game(gameInfo[0],gameInfo[1],gameInfo[2],storeList)
            self.gameList.append(game)
    
    def printBookmarks(self):
        self.user.printBookmarks()

    def printNotifications(self):
        self.user.bookmark.notification.printNotif()

    def clearNotifs(self):
        self.user.bookmark.notification.clear()
        conn = sqlite3.connect('Steam Games.db')
        sqlite_database.deleteNotifs(conn,self.user.getID())

    def printNotificationNo(self):
        number = self.user.bookmark.notification.getNo()
        print("\n---You have "+str(number)+" notifications.---\n")


        
 
