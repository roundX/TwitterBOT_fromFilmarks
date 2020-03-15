# Filmarksに投稿したレビューを自動でTwitterに投稿するBOT
import FilmarksGetNewEntry # 自作Filmarksレビュー取得モジュール
import Tweet_Review_Jacket # 自作呟きモジュール

def main():
    post = FilmarksGetNewEntry.getReview() #レビュー取得
    #print(post)
    if FilmarksGetNewEntry.checkNewEntry(post) == False: # 既に投稿されたレビューか確認
        account = Tweet_Review_Jacket.get_api() # Twitterのapi取得
        Tweet_Review_Jacket.tweet(account, post) # Tweet

if __name__ == '__main__':
    main()
