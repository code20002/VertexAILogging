from google.cloud import aiplatform

# Initialize the Vertex AI client
client_options = {"api_endpoint": "us-central1-aiplatform.googleapis.com"}
client = aiplatform.gapic.ModelServiceClient(client_options=client_options)

# Define the model name and version ID
model_name = "projects/{project_id}/locations/{location}/models/{model_id}"
version_id = "version_1"

# Define the new version description
new_description = "Updated version description"

# Get the existing model version resource name
version_name = f"{model_name}/versions/{version_id}"

# Update the version description
update_mask = {"paths": ["description"]}
update_mask = aiplatform.gapic.types.field_mask_pb2.FieldMask(**update_mask)
version = aiplatform.gapic.types.ModelDeploymentMetadata(description=new_description)
response = client.update_model_deployment_metadata(version_name=version_name, model_deployment_metadata=version, update_mask=update_mask)

# Print the updated version description
print(f"Updated description for version {version_id}: {response.description}")
