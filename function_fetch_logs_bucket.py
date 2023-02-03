import os
from google.cloud import storage

def fetch_logs_from_bucket(bucket_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    logs = []
    for blob in bucket.list_blobs():
        logs.append(blob.download_as_string().decode("utf-8"))
    return logs

'''In this example, the function accepts a single parameter: bucket_name. It creates a Google Cloud Storage client and fetches the specified bucket. It then iterates over all the blobs in the bucket, downloads the contents of each blob, and decodes it as a UTF-8 string. The contents of each blob are added to a list, and the list is returned as the result of the function.

'''