# ECサイト請求書作成データベース
# データベース作成
# テーブル作成，データを挿入，表示
 
import mysql.connector

# コネクターを作成
config = {
        'host': 'localhost',
        'port': '3306',
        'user': 'root',
        'password': 'rootmysql'
        }
dbconnector = mysql.connector.connect(**config)

# 接続できているかどうか確認
if dbconnector.is_connected():
    print('データベースへの接続が成功しました。')
else:
    print('データベースへの接続が失敗しました。')
    exit(1)

# cursorオブジェクトの生成
cursor = dbconnector.cursor()

fp=open("ch7ex1.sql", "r") 
operations=()
for sqlcmd in fp:
    sqlcmd=sqlcmd.strip()
    operations+=(sqlcmd,)

#print(operations)

#SQLの実行と結果表示
for no, operation in enumerate(operations):
   #問い合わせの実行
    cursor.execute(operation)
    if operation.split()[0]=="SELECT":
        print("SQL No."+str(no+1)+"：")
        print(operation)
        print("問い合わせの結果：")
        tuples = cursor.fetchall()
        for tpl in tuples:
            print(tpl)
    if operation.split()[0]=="SHOW":
        print("SQL No."+str(no+1)+"：")
        print(operation)
        print("SHOWの結果：")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

#接続を切断
dbconnector.close()
