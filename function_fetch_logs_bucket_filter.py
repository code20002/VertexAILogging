import os
from google.cloud import storage

def fetch_filtered_logs_from_bucket(bucket_name, text_filter):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    filtered_logs = []
    for blob in bucket.list_blobs():
        log = blob.download_as_string().decode("utf-8")
        if text_filter in log:
            filtered_logs.append(log)
    return filtered_logs

'''In this example, the function accepts two parameters: bucket_name and text_filter. It creates a Google Cloud Storage client and fetches the specified bucket. It then iterates over all the blobs in the bucket, downloads the contents of each blob, decodes it as a UTF-8 string, and checks if the text filter appears in the log. If the filter appears in the log, the log is added to a list of filtered logs. Finally, the list of filtered logs is returned as the result of the function.
'''