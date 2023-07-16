import sqlite3

dbname = 'VENDING.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

tablename = "Contents"

def change(num):

    cur.execute("SELECT * FROM Contents")

    a=[]
    i=0
    docs = cur.fetchall()
    for doc in docs:
        print(type(doc))
        a.append(list(doc))
        i+=1

    print(a)

    print(a[int(num)][2])

    cur.execute("UPDATE %s SET quantity = ? WHERE id=?;" % tablename,(a[int(num)][2]-1,int(num)))

    conn.commit()

    print(cur.fetchall())

if __name__ == "__main__":
    change()
