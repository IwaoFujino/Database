from pymongo import MongoClient

# MongoDBに接続
client = MongoClient("localhost", 27017)
db = client["testbase"]
collection = db["memberlist"]
# MongoDBにデータを挿入する
memberdata=[{"name":"山田太郎", "age":21}, {"name":"田中花子", "age":20}]
result = collection.insert_many(memberdata)
# MongoDBに問い合わせる
query = {"name": "山田太郎"}
projection={"_id":0}
results=collection.find(query, projection)
# 問い合わせの結果を表示する
for result in results:
    print(result)
# testbaseを削除
client.drop_database(db)
