# フライトデータベース：集約（航空会社別に平均遅延時間）
from pymongo import MongoClient

# MongoDBに接続
client = MongoClient("localhost", 27017)
db = client["flightdatabase"]
collection = db["flightdata"]
# クエリを指定
query = [
    {"$group":
        {
            "_id":"$UniqueCarrier",
            "AverageArrDelay":{"$avg":"$ArrDelay"}
        }
    }
]
# 検索結果を受け取る
results=collection.aggregate(query)
# 検索結果から各要素を取り出す
for result in results:
    #resultの全要素を表示
    #print(result)
    #resultの「_id」と「AverageArrDelay」を表示
    print(result["_id"], result["AverageArrDelay"],"min")
