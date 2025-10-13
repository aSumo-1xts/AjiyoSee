import csv

input_file_latest = "data/posts_latest.csv"
input_file_filtered_1st = "data/posts_filtered_1st.csv"
input_file_filtered_2nd = "data/posts_filtered_2nd.csv"
output_file = "data/result.txt"
result = None

# 再び今日の投稿内容を確認
# 1度目のリクエストから結果が変わっていなければ1をresultにセット
with (
    open(input_file_filtered_1st, newline="", encoding="utf-8") as f_filtered_1st,
    open(input_file_filtered_2nd, newline="", encoding="utf-8") as f_filtered_2nd,
):
    reader_1st = csv.reader(f_filtered_1st)
    reader_2nd = csv.reader(f_filtered_2nd)
    rows_1st = list(reader_1st)
    rows_2nd = list(reader_2nd)

    if rows_1st[1][1] == rows_2nd[1][1]:
        result = 1
    else:
        diff_indices = [
            i
            for i, row in enumerate(rows_2nd[1:], start=1)
            if row[1] not in [r[1] for r in rows_1st[1:]]
        ]
        if any(rows_2nd[i][3] == "完売" for i in diff_indices):
            result = 2
        else:
            result = 1

print(f"Result: {result}")

# 結果をresult.txtに書き込む
with open(output_file, "w", encoding="utf-8") as f:
    if result is not None:
        f.write(str(result))
    else:
        f.write("")
