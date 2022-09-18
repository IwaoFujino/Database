# CouchDBからツイートを取得する->形態素解析->単語の出現回数
import couchdb
import MeCab
import emoji
import re

#サーバーに接続
server = couchdb.Server('http://localhost:5984')
# データベース名の指定
dbname0='twitter-sample-'
dbdate='20200313'
dbname=dbname0+dbdate
#データベースへアクセス
db = server[dbname]
#viewを作成する
design = {}
#viewのデザイン名を指定
design['_id'] = "_design/mytest"
#使用する言語を指定
design['language'] = "javascript"
#viewを作成
views = {}
map = {}
map['map'] = """
function(doc) {
        emit(doc._id, {Twitter_id:doc.id_str, Screen_name:doc.user.screen_name, Text:doc.text})
}"""
views['myview1'] = map
design['views'] = views
#デザインの追加を実行
if "_design/mytest" not in db:
    db.save(design)
#viewを指定して，データを一括取得する
results = db.view("mytest/myview1")

tagger = MeCab.Tagger('-Ochasen')
wordsdic={}
#取得したデータを処理する
for result in results:
    text=result['value']['Text']
    #print("Tweet Text", text)
    # wwwwwを除去
    text = re.sub("ww+|WW+|w+$|W+$", " ", text)
    # @usernameを除去
    text=re.sub("(@[A-Za-z0-9_:]+)"," ",text)
    # urlを除去
    text=re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', " ", text)
    # HTML表記の特殊記号を除去
    text = re.sub("(&[A-Za-z0-9]+)", " ", text)
    # 半角記号を除去
    text = re.sub("[!-/:-@[-`{-~,.+;ﾟ^|]", " ", text)
    # 数字を除去
    text = re.sub("\d+", " ", text)
    # RT,DMを除去
    text = re.sub("RT|DM", " ", text)
    # https…を除去
    text = re.sub("https…|htt…", " ", text)
    # 全角記号を除去
    text = re.sub(u'[■-♯]', ' ', text)
    # 絵文字を除去
    text = ''.join(['' if c in emoji.UNICODE_EMOJI else c for c in text])
    # 1行にまとめる
    text=" ".join(text.split())
    # print('Text:',text)
    node = tagger.parseToNode(text)
    while node:
        # print(node.surface + '\t' + node.feature)
        # 形態素属性を分割してリストに入れる
        node_features=node.feature.split(",")
        if node_features[0]=="名詞" and (node_features[1]=="一般" or node_features[1]=="固有名詞"):
            word=node.surface
            wordsdic[word]=wordsdic.get(word,0)+1
        node = node.next

fout=open("top100words-"+dbdate+".csv", "w", encoding="utf-8")
n=0
for word, cnt in sorted(wordsdic.items(), key=lambda x:x[1], reverse=True)[0:100]:
    n+=1
    print(n,"番：単語=", word, "出現回数＝",cnt)
    foutstr=word+","+str(cnt)+"\n"
    fout.write(foutstr)
fout.close()
