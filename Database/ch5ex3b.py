# データベースにテーブル作成
# SQL命令文をまとめて実行
# csvファイルからデータを読み込む

import mysql.connector
import csv

# コネクターを作成
config = {
        'host': 'localhost',
        'port': '3306',
        'user': 'root',
        'password': 'rootmysql',
        'database': 'sampledb'        
        }
dbconnector = mysql.connector.connect(**config)

# 接続できているかどうか確認
if dbconnector.is_connected():
    print('データベースへの接続が成功しました。')
else:
    print('データベースへの接続が失敗しました。')
    exit(1)

# cursorオブジェクトの生成
cursor = dbconnector.cursor(buffered=True)

# 属性id, name, gender, ageを持つテーブルを作成, データ入力
operation = (
    "DROP TABLE IF EXISTS newlist;"
    "CREATE TABLE newlist ( mid INT, name CHAR(20), gender CHAR(10), age int, PRIMARY KEY (mid) ); "
)

# SQL命令文を実行
results = cursor.execute(operation, multi=True)
for res in results:
    print(res)

operation = ("INSERT INTO newlist VALUES (%s, %s, %s, %s);")
seqs = []
with open('newlistdata.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        tuple=(int(row[0]), row[1], row[2], int(row[3]))
        seqs.append(tuple)

#executemany()で実行する
cursor.executemany(operation, seqs)
#コミットする
dbconnector.commit()

#問い合わせ
cursor.execute("SELECT * FROM newlist")
# 問い合わせ結果の全てのデータを取得、表示
tuples = cursor.fetchall()
print("テーブルnewlistのデータ：")
for tpl in tuples:
    print(tpl)

#接続を切断
dbconnector.close()
