import os
import csv
import json
from dotenv import load_dotenv
import requests

output_file = "data/posts_latest.csv"

# 自分で設定する項目
SEARCH_KEYWORD = "from:ajiyoshiver2"
MAX_RESULTS = 10  # リクエスト1回につき10以上100未満

# 半自動的に設定される項目
URL = (
    f"https://api.twitter.com/2/tweets/search/recent"
    f"?query={SEARCH_KEYWORD}&tweet.fields=author_id,created_at&max_results={MAX_RESULTS}"
)
load_dotenv()
token = os.getenv("BEARER_TOKEN")
HEADERS = {"Authorization": f"Bearer {token}"}

# APIを叩いてJSONを取得、表示
response = requests.get(URL, headers=HEADERS).json()
print(json.dumps(response, indent=2, ensure_ascii=False))

# "data" が存在する場合のみcsv化
if "data" in response:
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=response["data"][0].keys())
        writer.writeheader()
        writer.writerows(response["data"])
    print(f"{output_file} を更新しました。")
else:
    print("ポストが見つからないか、エラーが発生しました。")
