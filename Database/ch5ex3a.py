# データベースにテーブル作成
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

# 属性id, name, gender, ageを持つテーブルを作成, データ入力, 問い合わせ
cursor.execute("DROP TABLE IF EXISTS memberlist;")
cursor.execute("CREATE TABLE memberlist ( mid INT, name CHAR(20), gender CHAR(10), age int, PRIMARY KEY (mid) );")
cursor.execute("INSERT INTO memberlist VALUES ( 1, '田中花子', '女', 28);")
cursor.execute("INSERT INTO memberlist VALUES ( 2, '山田聡', '男', 32);")
cursor.execute("INSERT INTO memberlist VALUES ( 3, '佐藤美那子', '女', 21);")
cursor.execute("INSERT INTO memberlist VALUES ( 4, '鈴木博', '男', 25);")
#コミットする
dbconnector.commit()

#問い合わせ
cursor.execute("SELECT * FROM memberlist;")
# 全てのデータを取得、表示
tuples = cursor.fetchall()
print("テーブルmemberlistのデータ：")
for tpl in tuples:
    print(tpl)

#接続を切断
dbconnector.close()
