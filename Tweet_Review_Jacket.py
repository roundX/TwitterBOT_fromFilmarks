# Filmarksのレビューをポスター画像と一緒に呟く
import tweepy
# KEYの指定
def get_api():
    keys = dict(
        # 自身のアカウントを代入
        screen_name = "",
        # 各キーを代入
        consumer_key = "",
        consumer_secret = "",
        access_token = "",
        access_token_secret = ""
    )

    SCREEN_NAME = keys["screen_name"]
    CONSUMER_KEY = keys["consumer_key"]
    CONSUMER_SECRET = keys["consumer_secret"]
    ACCESS_TOKEN = keys["access_token"]
    ACCESS_TOKEN_SECRET = keys["access_token_secret"]

    # APIの取得と認証
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api#, SCREEN_NAME

#ツイートの実行
def tweet(api, post):
    jacket_names="./img/_.jpg"
    api.update_with_media(filename=jacket_names,status=post)
