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

# Define the version details
version = {
    "display_name": "v1",
    "description": "First version of the model",
    "labels": {"env": "prod", "team": "ml"},
    "alias": "my-alias",
    "is_default": True
}

# Define the model resource
model = {
    "display_name": display_name,
    "description": description,
    "artifact_uri": model_path,
    "default_version": version,
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


"""
In the script above, we first set the environment variables for authentication and initialize the aiplatform client. Then we define the path to our model artifacts, as well as the project and location where we want to upload the model. We also define a display name and description for the model.

Next, we define the version details including a display name, description, labels, alias, and whether it is the default version. We then create a dictionary with the model resource information, including the version details, and call the upload_model method on the client to upload the model to the registry.

In this example, we're setting the is_default value to True, meaning that the version we're uploading will be the default version of the model. If we set it to False, it won't be the default version.

Finally, we extract the model ID and version ID from the response and print them out for verification.

"""