# フライトデータベース：集約（航空会社別に平均遅延時間）
# ＋　結合（航空会社コードから航空会社名を取得）
# ＋　ソート（平均遅延時間の降順）

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
        },
        {"$lookup":
            {
                "from":"carrier",
                "localField":"_id",
                "foreignField":"Code",
                "as":"CarrierInfos"
            }
        },
        {'$sort': 
            {"AverageArrDelay":-1}
        }
]
# 検索結果を受け取る
results=collection.aggregate(query)
# 検索結果から各要素を取り出す
for result in results:
    #print(result["CarrierInfos"])
    print("%s (%s) %4.2f min" % (result["CarrierInfos"][0]["Description"], result["_id"], result["AverageArrDelay"]))
