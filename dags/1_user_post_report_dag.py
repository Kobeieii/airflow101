from datetime import datetime, timedelta
from airflow import DAG
from airflow.decorators import task

default_args = {
    'owner': 'thitiwok',
    'start_date': datetime(2023, 1, 1),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
        dag_id="user_post_report_dag",
        default_args=default_args,
        schedule="0 0 * * *",
        max_active_runs=1,
        catchup=False,
        tags=['apm', 'apm_sensor']
) as dag:
    import pandas as pd
    import requests
    from utils import save_csv_report

    def taskflow_api():
        
        @task
        def get_users():
            response = requests.get("https://jsonplaceholder.typicode.com/users")
            users = response.json()
            return users
        
        @task
        def get_posts():
            response = requests.get("https://jsonplaceholder.typicode.com/posts")
            posts = response.json()
            return posts
        
        @task
        def generate_report(users, posts):
            users_df = pd.DataFrame(users)
            posts_df = pd.DataFrame(posts)
            report = users_df.merge(posts_df, left_on="id", right_on="userId")
            return report
        
        @task
        def save_report(report):
            save_csv_report(report, "test_report")

        users = get_users()
        posts = get_posts()
        report_df = generate_report(users, posts)
        save_report(report_df)


    taskflow_api()
