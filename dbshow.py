import sqlite3

dbname = 'VENDING.db'
conn = sqlite3.connect(dbname,isolation_level=None)

cur = conn.cursor()

sql = """SELECT * FROM Contents""" #Fruitテーブル内のすべての項目を選択

#cursorオブジェクトでSQL文を実行
def show():
    cur.execute(sql)

    #選択した項目を表示
    a=[]
    i=0
    docs = cur.fetchall()
    for doc in docs:
        print(type(doc))
        a.append(list(doc))
        i+=1

    print(a)
    conn.close()
    return a

if __name__ == "__main__":
    show()
