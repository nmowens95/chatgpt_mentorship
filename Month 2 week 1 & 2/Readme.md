# Month 2: Building Real Pipelines

## 🎯 Goal:
Move from local CLI tools to modular, realistic data pipelines that handle files, configs, transformations, and orchestration readiness.

---

## 📆 Week 5 – First Real ETL
- Build a basic Extract → Transform → Load pipeline
- Decompose into pure functions: `extract()`, `transform()`, `load()`
- Add logging and exception handling per step
- Write test coverage for each ETL stage

## 📆 Week 6 – Transformations & Scaling
- Create multiple reusable `transform_*()` functions
- Handle bad rows, missing fields, or wrong types
- Chain transformations declaratively (function registry?)
- Add CLI options or config for enabling/disabling steps

## 📆 Week 7 – Config-Driven Pipelines
- Use `.yaml` or `.json` to define pipeline behavior
- Parse and inject config into pipeline
- Add more real-world transforms (enriching with lookups, normalizing)
- Build 2 pipelines that use the same core engine

## 📆 Week 8 – Orchestration Simulations
- Simulate orchestration (manual DAG or `click`)
- Add retry/failure logic and logging hooks
- Add timestamps or unique run IDs to outputs
- Capstone pipeline: from raw data → clean summary → logged + tested

---

## 🧠 Stretch Goals (Optional):
- Add API extraction
- Use SQL (DuckDB or SQLite) as destination
- Begin exploring `dbt` for transformations
