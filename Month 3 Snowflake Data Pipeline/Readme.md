🔹 Week 1 – Snowflake + Staging from Python
Goal: Learn to load data into Snowflake manually and then programmatically.

✅ Set up your Snowflake trial account.

🔹 Load CSV data using SnowSQL CLI or Snowflake UI.

🔹 Connect to Snowflake using Python (e.g., snowflake-connector-python).

🔹 Write a Python function to upload Bronze/Silver CSVs to Snowflake staging tables.

🧠 Learn how Snowflake handles storage and compute (WAREHOUSES, DATABASES, SCHEMAS).

🔹 Week 2 – Data Modeling + dbt Core (Locally)
Goal: Build dimensional models and transform raw data with dbt.

🔹 Set up dbt Core locally and connect it to your Snowflake project.

🔹 Build your first dbt models (stg_customers, stg_claims, etc.).

🔹 Use Jinja templating, variables, and dbt run, dbt test, dbt docs.

🔹 Learn best practices: naming conventions, staging → marts structure.

🧠 Understand slowly changing dimensions (SCD), incremental models.

🔹 Week 3 – dbt Incremental + Testing
Goal: Move from full-refresh to incremental loading.

🔹 Convert models to incremental (is_incremental()).

🔹 Write basic tests (e.g., uniqueness, not null).

🔹 Use dbt seeds to simulate lookup/reference tables.

🔹 Learn the tradeoffs of full vs incremental and idempotency.

🧠 Learn how to document models and generate dbt docs.

🔹 Week 4 – End-to-End Project + Deployment Prep
Goal: Bring it all together in a repeatable, scalable pipeline.

🔹 Automate local pipeline: Extract → Upload to Snowflake → dbt Run.

🔹 Introduce lightweight orchestration (bash script or Python orchestration).

🔹 Optional: Try setting up dbt Cloud or GitHub Actions for CI/CD.

🔹 Write README and prep this as a portfolio project.