def save_csv_report(report, report_name="report"):
    file_path = f"/opt/airflow/reports/{report_name}.csv"
    report.to_csv(file_path, index=False)
    return file_path
