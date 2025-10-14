"""
check_openclose.py

1回目のfilter_posts.pyの実行結果からOPEN or CLOSEを判定する。
具体的には、posts_filtered_1st.csvを読み込んでresult.txtを更新する。
"""

import csv

input_file = "data/posts_filtered_1st.csv"
output_file = "data/result.txt"
result = 0  # 0: CLOSE, 1: OPEN

# posts_filtered_1st.csvを読み込む
with open(input_file, encoding="utf-8") as f:
    reader = list(csv.reader(f))
    if len(reader) > 1:  # そもそも投稿が無ければお休みと判定
        data_rows = reader[1:]  # ヘッダーをスキップ
        for row in reversed(data_rows):  # 時系列に沿って降順に走査
            text = row[3]
            if "メニュー" in text:
                result = 1
            elif "お休み" in text:
                result = 0

if result == 1:
    print("Result: OPEN")
else:
    print("Result: CLOSE")

# 結果をresult.txtに書き込む
with open(output_file, "w", encoding="utf-8") as f:
    f.write(str(result))
