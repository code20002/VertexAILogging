import os
from google.cloud import aiplatform

# Set the environment variables for authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/credentials.json"

# Initialize aiplatform SDK client
client = aiplatform.gapic.ModelServiceClient()

# Define the path to your model artifacts
model_path = "path/to/your/model"

# Define the project and location where you want to upload the model
project_id = "your-project-id"
location = "us-central1"

# Define the display name and description for your model
display_name = "My Model"
description = "A description of my model"

# Define the model resource
model = {
    "display_name": display_name,
    "description": description,
    "artifact_uri": model_path,
}

# Upload the model to the registry
parent = f"projects/{project_id}/locations/{location}"
response = client.upload_model(parent=parent, model=model)

# Get the model ID and version ID from the response
model_id = response.name.split("/")[-1]
version_id = response.model_deployment_metadata.deployment.resource_name.split("/")[-1]

# Print the model and version IDs
print(f"Model ID: {model_id}")
print(f"Version ID: {version_id}")
