from __future__ import annotations
from collections import defaultdict, Counter
from datetime import datetime
from typing import Dict, List, Tuple

def group_words_by_length(words: List[str]) -> Dict[int, List[str]]:
    groups: Dict[int, List[str]] = defaultdict(list)
    for w in words:
        groups[len(w)].append(w)
    return dict(groups)

def top_n_words(words: List[str], n: int = 3):
    return Counter(words).most_common(n)

def count_letters(s: str):
    return dict(Counter(s))

def group_by_first_letter(names: List[str]):
    groups: Dict[str, List[str]] = defaultdict(list)
    for name in names:
        if name:
            groups[name[0].lower()].append(name)
    return dict(groups)

def busiest_hours(timestamps: List[str], top_n: int = 3):
    hours = []
    for ts in timestamps:
        ts2 = ts[:-1] if ts.endswith("Z") else ts
        hours.append(datetime.fromisoformat(ts2).hour)
    return Counter(hours).most_common(top_n)

def run() -> None:
    words = ["alert","log","packet","alert","scan","packet","log","threat","scan","alert"]
    print("[Day1] groups:", group_words_by_length(words))
    print("[Day1] top3:", top_n_words(words, 3))

    print("[Day2] letter freq:", count_letters("mississippi"))
    names = ["Alice","bob","anna","Brian","amy","Zoe"]
    print("[Day2] names by first letter:", group_by_first_letter(names))
    logs = ["2025-08-10T02:10:00Z","2025-08-10T02:40:00Z","2025-08-10T03:05:00Z",
            "2025-08-10T03:05:30Z","2025-08-10T03:59:59Z","2025-08-10T14:00:00Z"]
    print("[Day2] busiest hours (top2):", busiest_hours(logs, top_n=2))
