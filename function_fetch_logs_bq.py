import os
from google.cloud import bigquery

def fetch_logs_from_bigquery(project_id, dataset_id, table_id):
    client = bigquery.Client(project=project_id)
    query = "SELECT * FROM `" + dataset_id + "." + table_id + "`"
    query_job = client.query(query)
    results = query_job.result()
    logs = []
    for row in results:
        logs.append(row)
    return logs


'''In this example, the function accepts three parameters: project_id, dataset_id, and table_id. It creates a BigQuery client and constructs a query that selects all rows from the specified table. The query is executed, and the results are stored in a list. Finally, the list is returned as the result of the function.
'''