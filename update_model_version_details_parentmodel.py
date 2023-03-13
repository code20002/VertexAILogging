from google.cloud import aiplatform
from google.protobuf import json_format

# Set the parent model ID and the new version's details
parent_model_id = "your-parent-model-id"
version_display_name = "v2"
version_description = "Second version of the model"
version_alias = "latest"
is_default = True

# Authenticate to the Vertex AI API using a service account key
client_options = {"api_endpoint": "us-central1-aiplatform.googleapis.com"}
client = aiplatform.gapic.ModelServiceClient(client_options=client_options)
location = "us-central1"

# Get the parent model object
parent_model_path = client.model_path(project="your-project-id", location=location, model=parent_model_id)
parent_model = client.get_model(name=parent_model_path)

# Create the new version object
version = {
    "display_name": version_display_name,
    "description": version_description,
    "labels": {"alias": version_alias},
    "is_default": is_default,
}

# Convert the version object to a JSON string and parse it into a protobuf message
version_json = json.dumps(version)
version_proto = json_format.Parse(version_json, aiplatform.gapic.Model.Version)

# Upload the new version to the parent model
upload_config = {
    "model": parent_model_path,
    "display_name": version_display_name,
    "description": version_description,
    "labels": {"alias": version_alias},
    "is_default": is_default,
}

response = client.upload_model_version(
    parent=parent_model_path,
    model_version=version_proto,
    upload_config=upload_config,
)

# Print the response
print(response)
