from google.cloud import logging

# Create a client for Google Cloud Logging
client = logging.Client()

# Specify the log name or log filter for the logs you want to fetch
log_name = "projects/your-project-id/logs/vertexai"

# Use the client to fetch logs from Google Cloud Logging
logs = client.list_entries(log_name)

# Iterate through the logs and print them
for log in logs:
    print(log.payload)


'''In this example, the Google Cloud Client Library is used to create a client for Google Cloud Logging. A log name or filter is specified, and the client is used to fetch logs from Google Cloud Logging. Finally, the logs are iterated through and printed.

Note: You'll need to have the google-cloud-logging library installed in your Python environment to run this code. You can install it using the following command:

pip install google-cloud-logging
'''