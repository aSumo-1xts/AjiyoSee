"""
check_openclose.py
filter_posts.pyの結果から営業状況を判定し、result.txtを更新。
"""

import csv
from common import write_result

INPUT_FILE = "posts_filtered.csv"
RESULT_FILE = "result.txt"


def main():
    try:
        with open(INPUT_FILE, encoding="utf-8") as f:
            reader = list(csv.reader(f))
            if len(reader) == 1:  # ヘッダーしか無い場合
                print("[check_status.py] 今日はポストがありません。")
                result = 0  # お休みとみなす
            else:
                header = reader[0]
                text_idx = header.index("text")
                for row in reader[1:]:  # 新しい順に走査
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
                        result = 4  # UNKNOWN
                        continue
    except Exception as e:
        print(f"[check_status.py] {INPUT_FILE}が見つかりません: {e}")
        result = 3  # X API ERROR

    write_result(result)


if __name__ == "__main__":
    main()
