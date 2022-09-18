# Twitter Streaming DataをCouchDBに保存する

import datetime
import tweepy
import json
import jsonpickle
import couchdb
import re

# クラス定義
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        tdatetime = datetime.datetime.now()
        dstr = tdatetime.strftime('%Y%m%d')
        tstr = tdatetime.strftime('%H:%M:%S')
        dbname=dbname0+dstr
        try:
            db = server.create(dbname)
        except couchdb.http.PreconditionFailed:
            db = server[dbname]
        text = status.text.strip()
        # urlとRTと@usernameを除去する
        text=' '.join(re.sub("(@[A-Za-z0-9_:]+)|(\w+:\/\/\S+)","",text).split())
        text=re.sub("RT","",text)
        if len(text) >= 20:
            print(">>>>> Date=",dstr, "Time=",tstr, "Twitter ID=",status.id_str)
            # オブジェクトをJSON文字列に変換
            status_json = jsonpickle.encode(status, unpicklable=False)
            # JSON文字列をディクショナリーに変換
            status_dic = json.loads(status_json.replace('\r\n', ''), encoding = 'utf-8')
		    #保存実行：save()メソッドは，ディクショナリーを保存する
            db.save(status_dic['_json']) 

    def on_error(self, status_code):
        print("エラー発生：エラーコード=", status_code)
        return True
 
    def on_timeout(self):
        print("タイムアウト...")
        return True
        
#　ここから実行する
if __name__ == "__main__":
    # サーバー定義 
    server = couchdb.Server('http://localhost:5984')
    # データベース名のPrefix
    dbname0='twitter-sample-'
    #ファイルからTwitterの認証情報を取得する 
    with open("mytwitterkey.json") as fjson:
        twkey=json.load(fjson)
    #Twitetrの認証を行う
    twitterauth = tweepy.OAuthHandler(twkey["CONSUMER_KEY"], twkey["CONSUMER_SECRET"])
    twitterauth.set_access_token(twkey["ACCESS_TOKEN"], twkey["ACCESS_TOKEN_SECRET"])
    # ストリミングオブジェクトを定義する
    streaming_api = tweepy.streaming.Stream(twitterauth, MyStreamListener(), timeout=60)
    # エラーの場合は，繰り返し再実行する
    errcnt=0   
    while(True):
        try:
            # 日本語のTweetを取得  
            streaming_api.sample(languages=['ja'])
        except Exception as err:
            errcnt+=1
            print("エラー第%d回: 発生時間=%s エラーメッセージ=%s" % (errcnt, str(datetime.datetime.now()), str(err)))
