"""
filter_posts.py
今日の投稿のみを抽出。
"""

import csv
from common import utc_to_jst, today_jst

INPUT_FILE = "posts_latest.csv"


def main():
    output_file = "posts_filtered.csv"

    try:
        with open(INPUT_FILE, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = list(reader)

            if not rows:
                print(f"[INFO] {INPUT_FILE} は空です。")
                return

            header, *data_rows = rows
            created_at_idx = header.index("created_at")
            filtered = [header]

            # 各行について、created_at を UTC->JST に変換して本日か確認
            for row in data_rows:
                try:
                    # created_at の日時文字列を utc_to_jst() で変換し、日付部分を比較
                    if utc_to_jst(row[created_at_idx]).date() == today_jst():
                        filtered.append(row)
                except Exception:
                    # 日時パースやインデックスエラーなどが発生した行は無視
                    continue

        # フィルタ済みデータを新しいCSVとして出力
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerows(filtered)
        print(f"[INFO] {output_file}を生成しました。")

    except FileNotFoundError:
        # 入力ファイルが存在しない場合のエラーメッセージ
        print(f"[ERROR] {INPUT_FILE}が存在しません。")


if __name__ == "__main__":
    main()
