import requests
import json

# Replace with your own Vertex AI API endpoint and access token
api_endpoint = "https://api.vertex.ai/v2/jobs"
access_token = "YOUR_ACCESS_TOKEN"

# Replace with the desired job ID
job_id = "JOB_ID"

# Build the API request URL
url = f"{api_endpoint}/{job_id}/logs"

# Set the API request headers
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Send the API request to retrieve the logs
response = requests.get(url, headers=headers)

# Check the API response status code
if response.status_code != 200:
    raise Exception("Failed to retrieve logs, status code: " + str(response.status_code))

# Parse the API response JSON
logs = json.loads(response.text)

# Display the logs
for log in logs:
    print(log["message"])
