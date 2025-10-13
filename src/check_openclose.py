import csv

input_file = "data/posts_filtered_1st.csv"
output_file = "data/result.txt"
result = None

# 今日の投稿内容を確認
# 「メニュー」の文言があれば1、「お休み」の文言があれば0をresultにセット
with open(input_file, encoding="utf-8") as f:
    reader = list(csv.reader(f))
    if len(reader) > 1:  # 2行目以降が存在するか確認
        data_rows = reader[1:]  # skip header
        for row in reversed(data_rows):  # 時系列に沿って降順に走査
            if len(row) < 4:
                continue
            text = row[3]
            if "メニュー" in text:
                result = 1
            elif "お休み" in text:
                result = 0
    else:
        result = 0  # 2行目以降が存在しない場合は0をセット

print(f"Result: {result}")

# 結果をresult.txtに書き込む
with open(output_file, "w", encoding="utf-8") as f:
    if result is not None:
        f.write(str(result))
    else:
        f.write("")
