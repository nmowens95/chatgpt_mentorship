from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'nate',
    'start_date': days_ago(1),
}

with DAG('healthcare_pipeline', default_args=default_args, schedule_interval='@daily') as dag:

    ingest_data = BashOperator(
        task_id='ingest_data',
        bash_command='python /path/to/your/ingestion_script.py'
    )

    run_dbt = BashOperator(
        task_id='run_dbt',
        bash_command='cd /path/to/your/dbt_project && dbt run'
    )

    ingest_data >> run_dbt
