import sqlite3

dbname = 'VENDING.db'
conn = sqlite3.connect(dbname,isolation_level=None)

cur = conn.cursor()
#contentsテーブルを作成しname,quantity,valueの初期設定をする
# cur.execute(
#     'CREATE TABLE Contents(id INTEGER, name STRING, quantity INTEGER ,value INTEGER)')
# 3.テーブルに商品データを登録する
# contentsテーブルのnameカラムに[orange] [melon] [apple] [soda]というデータを登録

#登録データ
r = [(1, "orange", 10,100), (2, "melon", 10,100),(3,"apple",10,150),(4,"soda",10,150)]

#レコード一括登録登録用SQL文
sql = """
    INSERT INTO Contents VALUES (
        ?, ?, ?, ?
    )
"""

cur.executemany(sql,r)
# 4.データベースにデータをコミット
conn.commit()

# 5.データベースの接続を切断
cur.close()
conn.close()
