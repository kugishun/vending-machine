import sqlite3

dbname = 'TEST.db'
conn = sqlite3.connect(dbname)

conn.close()