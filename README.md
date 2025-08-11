# 01-grouping-words

Day 12 Python mini-lab:
- **Grouping & Top-N** (Counter, defaultdict)
- **Counting & Aggregation** (letter frequency, grouping by key)
- **Busiest Hours** from ISO timestamps

![CI](https://github.com/Jwolf13/01-grouping-words/actions/workflows/ci.yml/badge.svg)

## Run locally (Windows PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
python -m pytest -q
python -m scripts.run
