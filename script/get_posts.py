"""
get_posts.py
X APIを叩いて直近の投稿を取得し、posts_latest.csvに保存する。
"""

import os
import csv
import requests
from dotenv import load_dotenv

OUTPUT_FILE = "posts_latest.csv"
RESULT_FILE = "result.txt"
SEARCH_KEYWORD = "from:ajiyoshiver2"
MAX_RESULTS = 10


def main():
    load_dotenv()
    token = os.getenv("BEARER_TOKEN")
    url = (
        "https://api.twitter.com/2/tweets/search/recent"
        f"?query={SEARCH_KEYWORD}&tweet.fields=author_id,created_at&max_results={MAX_RESULTS}"
    )
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if "data" not in data or not isinstance(data["data"], list):
            raise ValueError("dataが存在しない、または形式が不正")

        fieldnames = list(data["data"][0].keys())
        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data["data"])
        print(f"[get_posts.py] {OUTPUT_FILE}を更新しました。")

    except Exception as e:
        print(f"[get_posts.py] X APIエラー: {e}")


if __name__ == "__main__":
    main()
