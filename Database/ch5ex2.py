# MySQLサーバーにデータベースを作成
import mysql.connector

config = {
        'user': 'root',
        'password': 'rootmysql',
        'host': 'localhost'
        }
		
# try～except文でエラー対処
try:
    dbconnector = mysql.connector.connect(**config)

# 例外が発生の場合，エラーメッセージを表示
except mysql.connector.Error as errmsg:
    print('データベースサーバーへの接続が失敗しました。')
    print('エラーメッセージ：', errmsg)
    exit(1)

# cursorオブジェクトの生成
cursor = dbconnector.cursor()

# SQL命令を実行
cursor.execute("DROP DATABASE IF EXISTS sampledb")
cursor.execute('CREATE DATABASE sampledb')
cursor.execute('SHOW databases')

# 実行結果データを取得、表示
tuples = cursor.fetchall()
for tpl in tuples:
    print(tpl[0])

#コミットする。（実際にMySQLに保存する）
dbconnector.commit()
#接続を切断
dbconnector.close()
