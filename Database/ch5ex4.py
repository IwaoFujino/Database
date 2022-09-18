# 簡単な問い合わせ

import mysql.connector

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

#問い合わせ１
cursor.execute("SELECT name, age FROM memberlist WHERE gender='女' and age<=25")
# 問い合わせ結果の全てのデータを取得、表示
tuples = cursor.fetchall()
print("問い合わせ１の結果：")
for tpl in tuples:
    print(tpl)

#問い合わせ２
cursor.execute("SELECT name, age  FROM memberlist ORDER BY age DESC")
# 問い合わせ結果の全てのデータを取得、表示
tuples = cursor.fetchall()
print("問い合わせ２の結果：")
for tpl in tuples:
    print(tpl)

#接続を切断
dbconnector.close()
