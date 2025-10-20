"""
check_openclose.py
filter_posts.pyの結果から営業状況を判定し、result.txtを更新。
"""

import csv
from common import read_result, write_result

INPUT_FILE = "posts_filtered.csv"
RESULT_FILE = "result.txt"


def main():
    result = read_result(RESULT_FILE)
    print(f"[INFO] 既存の結果コード: {result}")

    try:
        with open(INPUT_FILE, encoding="utf-8") as f:
            reader = list(csv.reader(f))
            if len(reader) <= 1:
                print("[INFO] 投稿がありません。")
            else:
                header = reader[0]
                text_idx = header.index("text")
                for row in reversed(reader[1:]):  # 古い順
                    text = row[text_idx]
                    if "お休み" in text:
                        result = 0
                        break
                    elif "メニュー" in text:
                        result = 1
                        break
                    elif "完売" in text:
                        result = 2
                        break
                    else:
                        continue
    except FileNotFoundError:
        print(f"[ERROR] {INPUT_FILE}が見つかりません。")

    write_result(result, RESULT_FILE)


if __name__ == "__main__":
    main()
