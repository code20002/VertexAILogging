import requests

def display_logs(job_id):
    # Define the API endpoint for logs
    endpoint = f"https://api.vertex.ai/jobs/{job_id}/logs"

    # Make a GET request to the API endpoint
    response = requests.get(endpoint)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the logs
        print(response.text)
    else:
        # If the request was unsuccessful, print an error message
        print(f"Error retrieving logs for job {job_id}: {response.text}")

# Example usage:
display_logs("my_job_id")
