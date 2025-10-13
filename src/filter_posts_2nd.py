import csv
from datetime import datetime, timezone, timedelta

input_file = "data/posts_latest.csv"
output_file = "data/posts_filtered_2nd.csv"

# posts_latest.csvを読み込む
with open(input_file, newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

    JST = timezone(timedelta(hours=9))  # 日本標準時(JST)のタイムゾーン
    today_jst = datetime.now(JST).date()  # 今日の日付（JST）

    # ヘッダーを残して2行目以降をフィルタ
    header, *data_rows = rows
    filtered_rows = [header]
    for row in data_rows:
        if len(row) < 3:
            continue
        try:
            utc_dt = datetime.strptime(row[2], "%Y-%m-%dT%H:%M:%S.%fZ").replace(
                tzinfo=timezone.utc
            )
            jst_dt = utc_dt.astimezone(JST)
            if jst_dt.date() == today_jst:  # 今日の日付と一致するか確認
                filtered_rows.append(row)  # 一致する場合は追加
        except Exception:
            continue

    rows = filtered_rows

# フィルタ後のデータをposts_filtered.csvに書き込む
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)
