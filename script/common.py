import sys
import json
import csv
from datetime import datetime, timezone, timedelta


def write_result(code: int, path: str = "result.txt"):
    """結果コードを result.txt に書き込む"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(str(code))
    print(f"[INFO] result.txtを更新: {code}")


def read_result(path: str = "result.txt") -> int:
    """result.txt を読み取って int を返す"""
    try:
        with open(path, encoding="utf-8") as f:
            return int(f.read().strip())
    except Exception:
        return 4  # UNKNOWN


def utc_to_jst(dt_utc_str: str) -> datetime:
    """X API の UTC 文字列を JST datetime に変換"""
    dt_utc = datetime.strptime(dt_utc_str, "%Y-%m-%dT%H:%M:%S.%fZ").replace(
        tzinfo=timezone.utc
    )
    return dt_utc.astimezone(timezone(timedelta(hours=9)))


def today_jst() -> datetime.date:
    """今日の日付（JST）を返す"""
    return datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=9))).date()
