# tests/test_grouping.py
from lab01.main import (
    group_words_by_length, top_n_words,
    count_letters, group_by_first_letter, busiest_hours
)

def test_grouping_and_top3():
    words = ["a", "bb", "a", "ccc", "bb", "ccc", "ccc"]
    assert group_words_by_length(words)[1] == ["a", "a"]
    assert group_words_by_length(words)[2] == ["bb", "bb"]
    assert top_n_words(words, 2) == [("ccc", 3), ("a", 2)]

def test_count_letters():
    s = "mississippi"
    freq = count_letters(s)
    assert freq["i"] == 4
    assert freq["s"] == 4
    assert freq["m"] == 1
    assert freq["p"] == 2

def test_group_by_first_letter():
    names = ["Alice", "bob", "anna", "Brian", "amy", ""]
    out = group_by_first_letter(names)
    assert out["a"] == ["Alice", "anna", "amy"]
    assert out["b"] == ["bob", "Brian"]

def test_busiest_hours():
    logs = [
        "2025-08-10T02:10:00Z", "2025-08-10T02:40:00Z",
        "2025-08-10T03:05:00Z", "2025-08-10T03:05:30Z",
        "2025-08-10T03:59:59Z", "2025-08-10T14:00:00Z"
    ]
    # hour 3 has 3 events, hour 2 has 2, hour 14 has 1
    assert busiest_hours(logs, top_n=2) == [(3, 3), (2, 2)]
