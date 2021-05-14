import sqlite_database
import sqlite3
conn = sqlite3.connect('Steam Games.db')

thing = sqlite_database.getStoreDiscount(conn,26)
print(thing[0])