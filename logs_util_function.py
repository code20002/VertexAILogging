from google.cloud import logging

def get_logs(project_id, filter_):
    """Retrieve logs from Google Cloud Platform.

    Args:
    project_id (str): The GCP project ID.
    filter_ (str): The filter expression for logs.

    Returns:
    list: A list of logs.
    """
    client = logging.Client(project=project_id)
    logs = client.list_entries(filter_=filter_)
    logs = [entry.payload for entry in logs]
    return logs
