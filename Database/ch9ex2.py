# 郵便番号データベース：郵便番号から住所を検索
from pymongo import MongoClient

# MongoDBに接続
client = MongoClient("localhost", 27017)
db = client["zipcodebase"]
collection = db["zipcode"]
# 郵便番号を指定して検索する
#query = {"郵便番号": "103-0013"}
#query = {"郵便番号": "060-8406"}
# 郵便番号の範囲を指定して検索する
startzipcode="060-0007"
stopzipcode="060-0010"
query = {"$and":[{"郵便番号":{"$gte":startzipcode}}, {"郵便番号":{"$lte":stopzipcode}}]}
# 射影を指定
projection={"_id":0}
# 検索結果を受け取る
results=collection.find(query,projection)
# 検索結果を郵便番号でソート
results_sorted = sorted(results, key=lambda x:x["郵便番号"])
# 検索結果から各要素を取り出す
for result in results_sorted:
    print(result["郵便番号"])
    # 事業所の判別
    if result["事業所フラグ"]==0:
        print(result["都道府県"],result["市区町村"])
        print(result["町域"],result["字丁目"])
    else:
        print(result["事業所名"].replace("　",""))
        print(result["都道府県"],"市区町村")
        print(result["事業所住所"])
    print("---------------------------")
