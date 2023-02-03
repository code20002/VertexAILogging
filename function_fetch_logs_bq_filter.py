import os
from google.cloud import bigquery

def fetch_filtered_logs_from_bigquery(project_id, dataset_id, table_id, text_filter):
    client = bigquery.Client(project=project_id)
    query = "SELECT * FROM `" + dataset_id + "." + table_id + "` WHERE message LIKE '%" + text_filter + "%'"
    query_job = client.query(query)
    results = query_job.result()
    filtered_logs = []
    for row in results:
        filtered_logs.append(row)
    return filtered_logs


'''In this example, the function accepts four parameters: project_id, dataset_id, table_id, and text_filter. It creates a BigQuery client and constructs a query that selects all rows from the specified table where the message column contains the text filter. The query is executed, and the results are stored in a list. Finally, the list is returned as the result of the function.
'''