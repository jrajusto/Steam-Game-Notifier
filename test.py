import sqlite_database
import sqlite3
conn = sqlite3.connect('Steam Games.db')

sqlite_database.findUser(conn,"dick")