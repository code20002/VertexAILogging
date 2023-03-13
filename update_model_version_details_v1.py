import os
from google.cloud import aiplatform

# Set the environment variables for authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/credentials.json"

# Initialize aiplatform SDK client
client = aiplatform.gapic.ModelServiceClient()

# Define the project and location where your model is located
project_id = "your-project-id"
location = "us-central1"
model_id = "your-model-id"
version_id = "your-version-id"

# Define the new version details
version = {
    "description": "New version description",
    "labels": {"env": "prod", "team": "ml"},
    "alias": "new-alias",
    "is_default": True
}

# Update the model version with the new details
version_name = f"projects/{project_id}/locations/{location}/models/{model_id}/versions/{version_id}"
update_mask = {"paths": ["description", "labels", "alias", "is_default"]}
response = client.update_model_deployment_metadata(
    name=version_name, 
    update_mask=update_mask, 
    model_deployment_metadata=version
)

# Print the updated version details
print(f"Updated version details: {response.model_deployment_metadata}")
