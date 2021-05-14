import sqlite3
import requests
import json
dealAPI = '44587204c43f4187a3b2b01f590949494717aa14'


conn = sqlite3.connect('Steam Games.db')
c = conn.cursor()
c.execute("SELECT * FROM Steam_games")
temp = c.fetchall()

tempList1 = []
tempList2 = []

site = "https://api.isthereanydeal.com/v01/game/prices/?key="+dealAPI+"&plains="

plainsList = []
idList = []
counter = 0
site2 = site
counter2 = 0
counter3 = 0 
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
                print(counter3,k['shop']['name'],k['price_old'],k['price_new'],k['price_cut'])
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


print('done')

conn.close()