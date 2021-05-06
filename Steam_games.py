import sqlite3
import requests
import json

dealAPI = '44587204c43f4187a3b2b01f590949494717aa14'
steamKey = 'A6434537190388EB7A022C0C6780946B'
response = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v2/?key='+steamKey)
key = response.json()
site = "https://api.isthereanydeal.com/v01/game/prices/?key="+dealAPI+"&plains="

response2 =  requests.get("https://api.isthereanydeal.com/v01/game/plain/list/?key=" + dealAPI + "&shops=steam")
key2 = response2.json()
tempList = []

for i in key['applist']['apps']:
    plains =  key2['data']['steam'].get('app/'+str(i['appid']))
    if plains != None:
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

conn = sqlite3.connect('Steam Games.db')
c = conn.cursor()
c.executemany("INSERT INTO Steam_games VALUES (?,?,?)",finalList)

 
conn.commit()
conn.close()
