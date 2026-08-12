# tinytext

> **⚠️ This repository is a test bed, not a real project — it is not seeking contributions.**
> It exists as a fixture for an automation project I am building. Some of the bugs
> in it were planted deliberately and some issues are synthetic. Please don't spend
> real effort here: any pull request you open will be closed unmerged, and I would
> rather tell you that now than waste your afternoon.

A very small collection of text helpers, used as a practice repository.

## Install

```bash
pip install -e ".[dev]"
```

## Usage

```python
from tinytext import slugify, truncate, word_count

slugify("Hello, World!")      # 'hello-world'
truncate("hello world", 8)    # 'hello...'
word_count("one two  three")  # 3
```

## Development

```bash
pytest -q
```
