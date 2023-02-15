import google.auth
from google.cloud import logging_v2

# Set the GCP project ID
project_id = "your-project-id"

# Initialize the Cloud Logging client
credentials, _ = google.auth.default()
client = logging_v2.LoggingServiceV2Client(credentials=credentials)

# Define the sink configuration
sink_name = "your-sink-name"
destination = "pubsub.googleapis.com/projects/{your-project-id}/topics/{your-topic-name}"
filter_ = "severity >= ERROR"
sink = logging_v2.types.LogSink(
    name=sink_name,
    destination=destination,
    filter=filter_,
)

# Create the sink
parent = client.project_path(project_id)
response = client.create_sink(parent=parent, sink=sink)

print("Created sink: {}".format(response.name))
