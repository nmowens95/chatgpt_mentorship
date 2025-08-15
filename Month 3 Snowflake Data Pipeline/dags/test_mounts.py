from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='test_mounts',
    start_date=datetime(2025, 8, 15),
    schedule=None,
    catchup=False
) as dag:

    # Check that we can list the contents of src and dbt_pipeline
    list_src = BashOperator(
        task_id='list_src',
        bash_command='ls -l /usr/local/airflow/src'
    )

    list_dbt = BashOperator(
        task_id='list_dbt',
        bash_command='ls -l /usr/local/airflow/dbt_pipeline'
    )

    # Check that Python can import your packages
    check_imports = BashOperator(
        task_id='check_imports',
        bash_command='python -c "import airflow_dbt; import dbt; print(\'Imports successful\')"'
    )

    list_src >> list_dbt >> check_imports