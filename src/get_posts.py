import os
from dotenv import load_dotenv
import requests
import csv
import json

load_dotenv()
token = os.getenv("BEARER_TOKEN")
SEARCH_KEYWORD = "from:ajiyoshiver2"
MAX_RESULTS = 10

URL = (
    f"https://api.twitter.com/2/tweets/search/recent"
    f"?query={SEARCH_KEYWORD}&tweet.fields=author_id,created_at&max_results={MAX_RESULTS}"
)
HEADERS = {"Authorization": f"Bearer {token}"}

response = requests.get(URL, headers=HEADERS).json()

# デバッグ用に内容を表示
print(json.dumps(response, indent=2, ensure_ascii=False))

# "data" が存在する場合のみCSV化
if "data" in response:
    with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=response["data"][0].keys())
        writer.writeheader()
        writer.writerows(response["data"])
    print("posts.csvを更新しました。")
else:
    print("ポストが見つからないか、エラーが発生しました。")
