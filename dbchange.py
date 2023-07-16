import sqlite3

dbname = 'VENDING.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

tablename = "Contents"

def change(num,money):

    cur.execute("SELECT * FROM Contents")

    a=[]
    i=0
    docs = cur.fetchall()
    for doc in docs:
        a.append(list(doc))
        i+=1

    print(a)

    print(a[int(num)][2])

    if(money >= a[int(num)][3]):
        cur.execute("UPDATE %s SET quantity = ? WHERE id=?;" % tablename,(a[int(num)][2]-1,int(num)))
    else:
        return False

    conn.commit()

    # print(cur.fetchall())
    return True

if __name__ == "__main__":
    change()
