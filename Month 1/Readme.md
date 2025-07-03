# Month 1: Foundations of Data Engineering

## ✅ Week 1 – Setup & Warm-up
- Set up project structure: `src/`, `tests/`, CLI entry point
- Reviewed Python fundamentals & good modular design
- Started working with file inputs and CSVs
- Added logging with a centralized logger

## ✅ Week 2 – CLI Tools, Features & Summary Engine
- Built a CLI using `argparse`
- Created `summarize_df()` and feature registry
- Added support for `dtype`, `null`, and `mode` summaries
- Explored how to write modular and testable code

## ✅ Week 3 – Writers, Registry Pattern & Output Handling
- Created writer functions (`write_txt`, `write_json`)
- Registered writers in `WRITER_REGISTRY` for clean dispatch
- Used return values for file paths and logging clarity
- Strengthened error handling in file reading and writing

## ✅ Week 4 – Testing & Mocking
- Introduced `pytest`, unit tests, and `conftest.py`
- Created `tmp_path` fixtures for testing file reads
- Mocked the writer to ensure dispatch was called (first use of `patch`)
- Refactored CLI: `--features`, `--writer`, and added defaults + choices
- Reviewed `lambda` functions and CLI type handling

---

## 🔚 End of Month 1 Milestone:
- Built a working CLI app
- Tested data summarization with configurable outputs
- Practiced mocking and proper CLI parsing
- Built a habit of logging, separating logic, and writing testable code