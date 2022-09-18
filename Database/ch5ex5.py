# 結合を用いた問い合わせ
# 繰り返しによる複数問い合わせの実行と表示

import mysql.connector

# コネクターを作成
config = {
        'host': 'localhost',
        'port': '3306',
        'user': 'root',
        'password': 'rootmysql',
        'database': 'jikanwaribase'        
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

operations=(
"SELECT * FROM gakusei INNER JOIN rishu ON gakusei.gakuseino = rishu.gakuseino;",
"SELECT * FROM gakusei natural INNER JOIN rishu;",
"SELECT gakusei.namae, kamoku.kamokumei, kamoku.kyoushitsu, kamoku.youbi, kamoku.jigen FROM gakusei INNER JOIN rishu ON gakusei.gakuseino = rishu.gakuseino INNER JOIN kamoku ON rishu.kamokuno = kamoku.kamokuno;",
"SELECT gakusei.namae, kamoku.kamokumei, kamoku.kyoushitsu, kamoku.youbi, kamoku.jigen FROM gakusei natural INNER JOIN rishu natural INNER JOIN kamoku;"
)

#問い合わせの実行と結果表示
for no, operation in enumerate(operations):
    #問い合わせの実行
    cursor.execute(operation)
    # 問い合わせ結果の全てのデータを取得、表示
    print("問い合わせ"+str(no+1)+"：")
    print(operation)
    print("問い合わせ"+str(no+1)+"の結果：")
    tuples = cursor.fetchall()
    for tpl in tuples:
        print(tpl)

#接続を切断
dbconnector.close()
