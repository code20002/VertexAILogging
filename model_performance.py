from google.cloud import aiplatform
from google.protobuf import json_format
from sklearn.metrics import classification_report
import numpy as np

# Initialize Vertex AI clients
aiplatform.init(project='PROJECT_ID', location='us-central1')

# Load data and split into input and target arrays
X = np.load('data/X.npy') # Features
y = np.load('data/y.npy') # Labels

# Get the name of the deployed model
model_name = 'projects/PROJECT_ID/locations/us-central1/endpoints/ENDPOINT_ID'

# Evaluate model performance on training data
train_inputs = {'input': X}
train_targets = y
train_response = aiplatform.Endpoint().predict(
    endpoint= model_name, instances=train_inputs
)
train_preds = np.array(json_format.MessageToDict(train_response.predictions))
train_preds = train_preds.squeeze().astype(np.int64)
print('Training set classification report:')
print(classification_report(train_targets, train_preds))

# Evaluate model performance on new data
test_inputs = {'input': X_test}
test_targets = y_test
test_response = aiplatform.Endpoint().predict(
    endpoint= model_name, instances=test_inputs
)
test_preds = np.array(json_format.MessageToDict(test_response.predictions))
test_preds = test_preds.squeeze().astype(np.int64)
print('Test set classification report:')
print(classification_report(test_targets, test_preds))



"""

In this example, we first initialize the Vertex AI clients using the aiplatform.init function. Then we load the data and split it into input and target arrays. We get the name of the deployed model, which is required to send prediction requests. We evaluate the model's performance on both the training and test sets using the predict function from the Endpoint class, which sends prediction requests to the deployed model. We convert the prediction responses to numpy arrays and use the classification_report function from scikit-learn to print a report of the model's precision, recall, F1 score, and support for each class in each set.

Note that to use this code, you will need to have deployed a Vertex AI model as an endpoint and have the necessary permissions to access the endpoint. You will also need to substitute the PROJECT_ID and ENDPOINT_ID with your actual project and endpoint IDs.
"""