import google.auth
from google.cloud import logging_v2
from google.cloud import storage

# Set the GCP project and storage bucket name
project_id = "your-project-id"
bucket_name = "your-bucket-name"

# Initialize the Cloud Logging and Cloud Storage clients
credentials, _ = google.auth.default()
logging_client = logging_v2.LoggingServiceV2Client(credentials=credentials)
storage_client = storage.Client(project=project_id, credentials=credentials)

# Define the filter for the logs you want to export
filter_ = "logName:projects/{}/logs/your-log-name".format(project_id)

# Create the storage bucket if it doesn't already exist
bucket = storage_client.bucket(bucket_name)
if not bucket.exists():
    bucket.create()

# Set the storage bucket URL for the Cloud Logging sink
destination_uri = "gs://{}/{}".format(bucket_name, "logs/")

# Configure the Cloud Logging sink to export logs to the new storage bucket
sink_name = "your-sink-name"
parent = logging_client.project_path(project_id)
sink = logging_v2.types.LogSink(
    name=sink_name,
    destination=destination_uri,
    filter=filter_,
)
logging_client.create_sink(parent=parent, sink=sink)

print("Logs will now be exported from Cloud Logging to Cloud Storage at gs://{}/logs/".format(bucket_name))
