from google.cloud import aiplatform

# Set the project ID, model ID, and version ID
project_id = "your-project-id"
model_id = "your-model-id"
version_id = "your-version-id"

# Set the new version description
new_description = "New version description"

# Initialize the Vertex AI client
client_options = {"api_endpoint": "us-central1-aiplatform.googleapis.com"}
client = aiplatform.gapic.ModelServiceClient(client_options=client_options)

# Get the model name
model_name = f"projects/{project_id}/locations/us-central1/models/{model_id}"

# Get the version name
version_name = f"{model_name}/versions/{version_id}"

# Get the existing version
version = client.get_model_deployment(name=version_name)

# Update the version description
version.update_mask.paths.append("description")
version.deployment.description = new_description

# Update the version
update_mask = {"paths": ["deployment.description"]}
response = client.update_model_deployment(
    update_mask=update_mask,
    model_deployment=version,
)

# Print the updated version
print(f"Updated version: {response}")
