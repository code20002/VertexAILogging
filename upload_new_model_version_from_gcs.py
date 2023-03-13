from google.cloud import aiplatform

# Set the project ID, location, and model display name
project_id = "YOUR_PROJECT_ID"
location = "us-central1"
model_display_name = "YOUR_MODEL_DISPLAY_NAME"

# Create a Vertex AI model client
client_options = {"api_endpoint": f"{location}-aiplatform.googleapis.com"}
client = aiplatform.gapic.ModelServiceClient(client_options=client_options)

# Define the metadata for the model version
metadata = aiplatform.gapic.ModelVersion.Metadata(
    inputs={
        "image": "JPG image",
        "text": "UTF-8 encoded string",
    },
    outputs={"label": "Class label"},
)

# Create a model version object
model_version = aiplatform.gapic.ModelVersion(
    display_name="v1",
    metadata=metadata,
)

# Upload the model version to the registry
response = client.upload_model(
    parent=f"projects/{project_id}/locations/{location}",
    model_display_name=model_display_name,
    model=aiplatform.gapic.Model(
        display_name=model_display_name,
    ),
    model_version=model_version,
    source={
        "uri": "gs://YOUR_BUCKET_NAME/YOUR_MODEL_DIRECTORY",
    },
)

# Print the response
print(response)
