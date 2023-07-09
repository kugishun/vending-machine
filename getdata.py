import sqlite3

dbname = 'TEST.db'
# 1.データベースに接続
conn = sqlite3.connect(dbname)

# 2.sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

# 3.テーブルのデータを取得
# 例では、personsテーブルデータを全件取得
cur.execute('SELECT * FROM persons')

# 取得したデータを出力
a=[]
i=0
docs = cur.fetchall()
for doc in docs:
    print(type(doc))
    a.append(list(doc))
    i+=1
print(a)
# 4.データベースの接続を切断
cur.close()
conn.close()