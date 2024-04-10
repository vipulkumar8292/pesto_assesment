from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# Define DAG schedule and default arguments
default_args = {
    'owner': 'AdvertiseX',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'advertiseX_data_pipeline',
    default_args=default_args,
    description='Data pipeline for AdvertiseX',
    schedule_interval=timedelta(days=1),
)

# Define tasks
task_ingest_data = BashOperator(
    task_id='ingest_data',
    bash_command='python /path/to/ingestion_script.py',
    dag=dag,
)

task_process_data = BashOperator(
    task_id='process_data',
    bash_command='spark-submit /path/to/data_processing_script.py',
    dag=dag,
)

# Set task dependencies
task_ingest_data >> task_process_data
