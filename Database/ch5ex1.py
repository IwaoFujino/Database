# MySQLサーバーへ接続
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
    print('MySQLサーバーへの接続が失敗しました。')
    print('エラーメッセージ：', errmsg)

# 成功した場合，メッセージを表示，接続を切断   
else:
    print('MySQLサーバーへの接続が成功しました。')
    dbconnector.close()
