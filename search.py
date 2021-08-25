
import pandas as pd
import eel

### デスクトップアプリ作成課題
def kimetsu_search(word,csv_path):
    # 検索対象取得
    df=pd.read_csv("./"+csv_path)
    source=list(df["name"])

    # 検索
    if word in source:
        print("『{}』はあります".format(word))
        eel.view_log_js("『{}』はあります".format(word))
    else:
        print("『{}』はありません".format(word))
        eel.view_log_js("『{}』はありません".format(word))
        # 追加
        add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        if add_flg=="1":
            source.append(word)
    
    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    df.to_csv("./"+csv_path,encoding="utf_8-sig")
    print(source)