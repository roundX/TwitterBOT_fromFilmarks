# filmarks new entry get
import requests
from bs4 import BeautifulSoup

def getReview():
    # ユーザーページのHTML取得、解析
    res = requests.get("https://filmarks.com/users/Round")
    soup = BeautifulSoup(res.content, "lxml")
    images = []
    newMovieInfo = soup.find("div", class_="c-movie-card") # 最新のレビュー部分のHTMLだけを取得

    # 作品の詳細ページのHTML取得、解析
    linkDetail = newMovieInfo.find("a")
    urlDetail = "https://filmarks.com" + linkDetail.get("href")
    resReview = requests.get(urlDetail)
    reviewSoup = BeautifulSoup(resReview.content, "lxml")

    title = newMovieInfo.find("h3") # 作品タイトル部分のHTML取得
    infobar = newMovieInfo.find("div",class_="c-rating__score") # 評価部分のHTML取得
    review = reviewSoup.find("div", class_="p-mark__review") # レビュー取得

    # ポスター画像取得〜ファイルとして保存
    jacket = reviewSoup.find("div", class_="c-content__jacket")
    imgLarge = jacket.find("img")
    images.append(imgLarge.get("src")) # ポスター画像取得

    re = requests.get(images[0])
    with open('img/' + images[0].split('/')[-1], 'wb') as f: # imgフォルダに格納
        f.write(re.content) # .contentにて画像データとして書き込む

    # twitterの文字数制限を超えている場合でreturn分岐(★と改行を抜いた137文字)
    if len(title.text[0:-12] + infobar.text + review.text) > 137:
        review = urlDetail # 
        return title.text[0:-12] + "\n★ {}\n".format(infobar.text) + review
    else:
        return title.text[0:-12] + "\n★ {}\n".format(infobar.text) + review.text
    

# 既に一度投稿された内容のレビューかどうか調べる
def checkNewEntry(post):
    title = post.split('\n')[0]
    with open("titleList.txt", "r", encoding='utf-8') as f:
        movieTitles = f.read().split("\n")
        for movieTitle in movieTitles:
            if movieTitle == title:
                return True
    with open("titleList.txt", "a", encoding='utf-8') as f:
        f.write(title + '\n')
    return False
