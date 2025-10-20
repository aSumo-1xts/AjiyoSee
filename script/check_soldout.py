"""
check_soldout.py

check_openclose.pyの実行結果がOPENの場合にのみ実行される。
2回目のfilter_posts.pyの実行結果からSOLD OUT or STILL OPENを判定する。
具体的には、posts_filtered_2nd.csvを読み込んでresult.txtを更新する。
"""

import csv

input_file = "posts_filtered_2nd.csv"
output_file = "result.txt"
result = 1 # 1: OPEN, 2: SOLD OUT

# posts_filtered_2nd.csvを読み込む
with open(input_file, encoding="utf-8") as f:
    reader = list(csv.reader(f))
    data_rows = reader[1:]  # ヘッダーをスキップ

    # "text"列のインデックスを取得
    header = reader[0]
    try:
        text_idx = header.index("text")
    except ValueError:
        raise Exception('"text"列が見つかりません')

    # 時系列に沿って降順に走査
    for row in reversed(data_rows):
        text = row[text_idx]
        if "完売" in text:
            result = 2

if result == 2:
    print("Result: SOLD OUT")
else:
    print("Result: STILL OPEN")

# 結果をresult.txtに書き込む
with open(output_file, "w", encoding="utf-8") as f:
    f.write(str(result))
