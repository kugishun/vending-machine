import pymysql.cursors

connector = pymysql.connect(
        user='root',# 自分で設定したユーザー名を設定してください。(適宜変更)
        passwd='raspberry',# 自分で設定したパスワードを設定してください。(適宜変更)
        host='localhost',# 接続先DBのホスト名或いはIPを設定してください。(適宜変更)
        db='test1'# 接続したいデータベース名を設定してください。(適宜変更)
)

c = connector.cursor()
conn.close()
print("PythonからMariaDBに接続できました。")