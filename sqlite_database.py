import sqlite3
from sqlite3 import Error
import requests
import json

def create_connection(db_file):
    conn = None
    try: 
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def update_Store(conn, data):
    
    sql = ''' UPDATE Store
              SET current price = ? ,
                  discount = ? ,
              WHERE storeID = ?'''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()

def getStoreIDList(conn, appID):
    sql = "SELECT storeID FROM game_store WHERE appID = ?"

    cur = conn.cursor()
    cur.execute(sql, (appID,))

    return cur.fetchall()

def getStoreIDList2(conn, appID):
    sql = "SELECT storeID FROM game_store WHERE appID = ?"

    cur = conn.cursor()
    cur.execute(sql, appID)

    return cur.fetchall()

def getAppID(conn, storeID):
    sql = "SELECT appID FROM game_store WHERE storeID = ?"

    cur = conn.cursor()
    cur.execute(sql, storeID)
    
    return cur.fetchone()

def getUsers(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM Users")
    return c.fetchall()

def getGames(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM Steam_games")
    return c.fetchall()

def getBookmark(conn,id):
    cur = conn.cursor()
    sql = "SELECT appID FROM Bookmark WHERE userID = ?"
    cur.execute(sql, (id,))
    return cur.fetchall()

def getGameInfo(conn,id):
    cur = conn.cursor()
    sql = "SELECT * FROM Steam_games WHERE appID = ?"
    cur.execute(sql, id)
    return cur.fetchone()

def getStoreInfo(conn,storeID):
    sql = "SELECT * FROM Store_price WHERE storeID = ?"
    cur = conn.cursor()
    cur.execute(sql, storeID)
    return cur.fetchone()

