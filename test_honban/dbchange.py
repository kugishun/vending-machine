import sqlite3

dbname = 'VENDING.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

tablename = "Contents"

cur.execute("SELECT * FROM Contents")

a=[]
i=0
docs = cur.fetchall()
for doc in docs:
    print(type(doc))
    a.append(list(doc))
    i+=1

print(a)
string = input("0~3の数字を入力してください:")

print(a[int(string)][2])

cur.execute("UPDATE %s SET quantity = ? WHERE id=?;" % tablename,(a[int(string)][2]-1,int(string)))

conn.commit()

print(cur.fetchall())