# CouChDBアクセステスト
import couchdb

# CouchDBに接続する
couch = couchdb.Server('http://localhost:5984/')
# 新規作成の場合
db = couch.create('testbase')
# 既存の場合
#db = couch['testbase']
# CouchDBにドキュメントを保存する
doc = {"name":"山田太郎", "age":21}
print(doc)
db.save(doc)
for id in db:
	print("doc id=",id)
print("--------------")
# ドキュメントを削除する
db.delete(doc)
for id in db:
	print("doc id=",id)
print("--------------")
# データベースを削除する
couch.delete('testbase')
