from google.cloud import logging

# Create a client to interact with Google Cloud Logging
client = logging.Client()

# Define the filter to search for logs from a specific vertex pipeline
filter_str = 'resource.type="cloud_composer_environment" AND logName="projects/<PROJECT_ID>/logs/airflow-worker" AND jsonPayload.task_instance.is_pulled=true AND jsonPayload.task_instance.task_id="<TASK_ID>"'

# Fetch the logs using the defined filter
for entry in client.list_entries(filter_=filter_str):
    print(entry.payload)
