from airflow import DAG
from airflow.decorators import task
from datetime import datetime
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_app.apps_settings")
django.setup()

default_args = {
    "owner": "thitiwok",
    "start_date": datetime(2024, 1, 1),
    "retries": 0,
}

with DAG(
    dag_id="django_model",
    default_args=default_args,
    schedule="0 * * * *",
    max_active_runs=1,
    catchup=False,
    tags=["app"],
) as dag:
    import pandas as pd
    import requests
    from django_app.apps.models.report import Report

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
            reports = [
                Report(
                    user_id=row["userId"],
                    name=row["name"],
                    username=row["username"],
                    email=row["email"],
                    address=row["address"],
                    phone=row["phone"],
                    website=row["website"],
                    company=row["company"],
                    title=row["title"],
                    body=row["body"],
                )
                for _, row in report.iterrows()
            ]
            Report.objects.bulk_create(reports)

        users = get_users()
        posts = get_posts()
        report_df = generate_report(users, posts)
        save_report(report_df)

    taskflow_api()
