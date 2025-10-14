# AjiyoSee

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![ESP](https://img.shields.io/badge/ESP-E7352C?logo=Espressif&logoColor=white)](https://www.espressif.com/ja-jp)
[![X-API](https://img.shields.io/badge/API-%23000000.svg?logo=X&logoColor=white)](https://developer.x.com/ja/docs/x-api)
[![MIT](https://img.shields.io/badge/License-MIT-green)](./LICENSE)

つくば市の飲食店「あじよし」の営業状況をざっくりリアルタイムで可視化する非公認プロジェクト。

必要に応じて`CONTRIBUTING.md`も参照してください。

## dir: `script`

X APIを叩いてツイートを取得し、営業時間を判別するPythonスクリプト。

1. 昼過ぎに`get_posts.py`を実行し、おばちゃんの直近10件の投稿を取得
2. `filter_posts.py -1`によって今日の投稿だけを抽出
3. `check_openclose.py`によって開店状況を判定
4. 開店している場合、夜に`get_posts` `filter_posts.py -2` `check_soldout.py`を実行して売り切れかどうかを調べる

## dir: `src`

マイコンがGitHub Actionsによって更新された`data/result.txt`を読み取り、LEDやLCDに反映するためのファームウェア。
