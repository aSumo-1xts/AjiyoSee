"""
check_soldout.py

2回目のfilter_posts.pyの実行結果からSOLD OUT or STILL OPENを判定する。
具体的には、posts_filtered_2nd.csvを読み込んでresult.txtを更新する。
そもそもCLOSEである場合には実行されない。
"""

import csv

input_file_filtered_1st = "data/posts_filtered_1st.csv"
input_file_filtered_2nd = "data/posts_filtered_2nd.csv"
output_file = "data/result.txt"
result = 1  # 1: OPEN, 2: SOLD OUT

# posts_filtered_1st.csvとposts_filtered_2nd.csvを読み込む
with (
    open(input_file_filtered_1st, newline="", encoding="utf-8") as f_filtered_1st,
    open(input_file_filtered_2nd, newline="", encoding="utf-8") as f_filtered_2nd,
):
    reader_1st = csv.reader(f_filtered_1st)
    reader_2nd = csv.reader(f_filtered_2nd)
    rows_1st = list(reader_1st)
    rows_2nd = list(reader_2nd)

    # 新たに投稿が無ければ完売していないと判定
    if rows_1st[1][1] == rows_2nd[1][1]:
        result = 1
    else:
        # ヘッダーから"id"列のインデックスを取得
        id_idx_1st = rows_1st[0].index("id")
        id_idx_2nd = rows_2nd[0].index("id")
        # ヘッダーから"text"列のインデックスを取得
        text_idx_2nd = rows_2nd[0].index("text")

        # idの列を比較して、2回目にしか無い行のindexを取得
        diff_indices = [
            idx
            for idx, row in enumerate(rows_2nd[1:], start=1)
            if row[id_idx_2nd] not in [r[id_idx_1st] for r in rows_1st[1:]]
        ]
        # その行のtext列を調べて、「完売」が含まれていれば売り切れと判定
        if any("完売" in rows_2nd[idx][text_idx_2nd] for idx in diff_indices):
            result = 2

if result == 2:
    print("Result: SOLD OUT")
else:
    print("Result: STILL OPEN")

# 結果をresult.txtに書き込む
with open(output_file, "w", encoding="utf-8") as f:
    f.write(str(result))
