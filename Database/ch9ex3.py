# 郵便番号データベース：住所から郵便番号を検索
from pymongo import MongoClient

# MongoDBに接続
client = MongoClient("localhost", 27017)
db = client["zipcodebase"]
collection = db["zipcode"]
# 住所のキーワードを指定して検索する
keyword="原宿"
query = {"$or":[{"都道府県":{"$regex":keyword}}, {"市区町村":{"$regex":keyword}}, {"町域":{"$regex":keyword}}]}
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
        print(result["都道府県"],result["市区町村"])
        print(result["事業所住所"])
    print("------------------------")
