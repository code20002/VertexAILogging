from google.cloud import aiplatform

# Set up authentication
# You can either use the Application Default Credentials (ADC) or a service account key file
# See https://cloud.google.com/docs/authentication for more information
aiplatform.init(project="<your-project-id>")

# Define the model version's resource name
model_version_name = "projects/<your-project-id>/locations/<region>/models/<model-id>/versions/<version-id>"

# Create a ModelVersion object
model_version = aiplatform.ModelVersion(model_version_name)

# Update the model version's metadata
model_version.set_metadata({"new-key": "new-value"})

# Update the model version's description
model_version.set_description("New description")

# Update the model version's labels
model_version.set_labels({"new-label-key": "new-label-value"})

# Update the model version
model_version.update()

# Close the client
aiplatform.shutdown()
