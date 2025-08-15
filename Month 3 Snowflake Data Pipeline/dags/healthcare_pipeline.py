from airflow import DAG
# from airflow.providers.dbt.core.operators.dbt import DbtRunOperator, DbtTestOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="healthcare",
    # owner='nate',
    start_date=datetime(2025, 8, 14),
    schedule=None,
    default_args={"retries": 2},
    catchup=False,
) as dag:

    ingest_data = BashOperator(
        task_id='ingest_data',
        bash_command='PYTHONPATH=/usr/local/airflow python /usr/local/airflow/src/load_to_snowflake/extract_load_snowflake.py'
    )

    test_dbt = BashOperator(
        task_id='test_dbt',
        bash_command='cd /usr/local/airflow/dbt_pipeline && dbt test --profiles-dir /usr/local/airflow/profiles'
    )

    run_dbt = BashOperator(
        task_id='run_dbt',
        bash_command='cd /usr/local/airflow/dbt_pipeline && dbt run --profiles-dir /usr/local/airflow/profiles'
    )

    ingest_data >> run_dbt >> test_dbt

