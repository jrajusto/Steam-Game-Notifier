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
        
        userName = input("Username: ")
        password = input("Password: ")
        userID  = sqlite_database.findUserID(conn,userName,password)
        
        if userID != None:
            #print(self.userList[userID[0]])
            self.user = self.userList[userID[0]]
            print(self.user)
        

    def addUser(self,userInfo):
        user = User(userInfo[0],userInfo[1],userInfo[2])
        self.userList.append(user)

    def addGame(self,game):
        self.gameList.append(game)
    
    def initBookmark(self):
        conn = sqlite3.connect('Steam games.db')
        for user in self.userList:
            id = user.getID()
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
                user.addGameToBookmark(game)

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
                print(len(existance))
                if len(existance) == 0:
                    newGame.append(i['appid'])
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
            if counter == 150 or counter2 == max:
                counter = 0
                response = requests.get(site2+"&region=us&country=US")
                site2 = site
                key = response.json()
                for j in gameList:
                    shopList = key['data'][j[2]].get("list")
                    if len(shopList)!=0:
                        finalList.append(j)
                        print(finalList)
                
                gameList = []

        
        c.executemany("INSERT INTO Steam_games VALUES (?,?,?)",finalList)
        conn.commit()
        conn.close()


        
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
            info = sqlite_database.getGameInfo(conn,i)
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
                c.executemany("INSERT INTO Store_price_price VALUES (?,?,?,?,?)",tempList1)    
                c.executemany("INSERT INTO game_store VALUES (?,?)",tempList2)    
                conn.commit()
                tempList1 = [] 
                tempList2 = [] 
                plainsList = []
                idList = []
        conn.commit()
        conn.close()


    def addNewGamesToClass(self,newGame):
        #add to classes
        conn = sqlite3.connect('Steam Games.db')
        for i in newGame:
            storeList = []
            storeIDlist = sqlite_database.getStoreIDList(conn,i)
            for j in storeIDlist:
                
                storeInfo = sqlite_database.getStoreInfo(conn,j)
                storePrice = StorePrice(storeInfo[0],storeInfo[1],storeInfo[2],storeInfo[3],storeInfo[4])
                storeList.append(storePrice)
            
            gameInfo = sqlite_database.getGameInfo(conn,i)
            game = Game(gameInfo[0],gameInfo[1],gameInfo[2],storeList)
            self.addGame(game)

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
                        storeID = sqlite_database.getStoreIDList(conn,idList[counter4])
                        index = 0
                        found = False
                        while found != True:
                            c.execute("SELECT * FROM game_store WHERE storeID = ? AND name = ?", (storeID[index]),k['shop']['name'])
                            if len(c.fetchall()) == 1:
                                found = True
                        store = sqlite_database.getStoreInfo(conn, storeID[index])
                        if store[4] != k['price_cut']:
                            tempTuple1 = (k['price_new'],k['price_cut'],store[0])
                        tempList1.append(tempTuple1)
                    counter4 = counter4 + 1
                counter4 = 0 
                sqlite_database.update_Store(conn,tempList1)  
                conn.commit()
                tempList1 = [] 
                plainsList = []
                idList = []

        print('done')

        conn.commit()
        conn.close()



        
 
