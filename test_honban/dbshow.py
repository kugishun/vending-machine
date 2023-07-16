import sqlite3

dbname = 'VENDING.db'
conn = sqlite3.connect(dbname,isolation_level=None)

cur = conn.cursor()

sql = """SELECT * FROM Contents""" #Fruitテーブル内のすべての項目を選択

#cursorオブジェクトでSQL文を実行
cur.execute(sql)

#選択した項目を表示
for item in cur:
    print(item)

conn.close()
