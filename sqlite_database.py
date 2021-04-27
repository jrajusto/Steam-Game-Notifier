import sqlite3
from sqlite3 import Error

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

def getStoreID(conn, appID):
    sql = ''' SELECT storeID WHERE id = ?'''

    cur = conn.cursor()
    cur.execute(sql, appID)

    return cur.fetchone()

def getAppID(conn, storeID):
    sql = ''' SELECT appID WHERE id = ?'''

    cur = conn.cursor()
    cur.execute(sql, storeID)
    
    return cur.fetchone()