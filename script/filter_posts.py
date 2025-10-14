"""
filter_posts_1st.py

get_posts.pyの実行結果をフィルタして、過去n時間以内の投稿だけを抽出する。
具体的には、posts_latest.csvを読み込んでposts_filtered_1st.csvに上書きする。
"""

import sys
import csv
from datetime import datetime, timezone, timedelta

n = 12  # 過去n時間以内の投稿だけを抽出
input_file = "data/posts_latest.csv"

# コマンドライン引数でリクエストが1回目か2回目かを指定
try:
    if sys.argv[1] == "-1":
        output_file = "data/posts_filtered_1st.csv"
    elif sys.argv[1] == "-2":
        output_file = "data/posts_filtered_2nd.csv"
except IndexError:
    print("Error: コマンドライン引数で -1 か -2 を指定してください。")
    sys.exit(1)

# 時刻の準備
now_utc = datetime.now(timezone.utc)  # 現在の時刻（UTC）
now_jst = now_utc.astimezone(timezone(timedelta(hours=9)))  # 現在の時刻（JST）

# posts_latest.csvを読み込む
with open(input_file, newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)
    header, *data_rows = rows
    filtered_rows = [header]  # まっさらな出力結果にヘッダーを追加しておく

    # row[0]: author_id, row[1]: id, row[2]: created_at, row[3]: text, ...
    for row in data_rows:
        # X APIの時刻表示をdatetimeに変換
        posts_utc = datetime.strptime(row[2], "%Y-%m-%dT%H:%M:%S.%fZ").replace(
            tzinfo=timezone.utc
        )  # X APIの時刻はUTC
        posts_jst = posts_utc.astimezone(timezone(timedelta(hours=9)))  # JSTに変換

        # 投稿がJSTで今日のものであれば抽出
        if posts_jst.date() == now_jst.date():
            filtered_rows.append(row)

    rows = filtered_rows

with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)
