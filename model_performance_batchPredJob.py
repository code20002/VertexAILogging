from google.cloud import aiplatform

# Set the location of your model
model_location = "projects/<your-project-id>/locations/<your-model-location>/models/<your-model-id>"

# Set the location of your training dataset
training_data_location = "<your-training-data-location>"

# Set the location of your production dataset
production_data_location = "<your-production-data-location>"

# Create a client object for the Vertex AI API
client_options = {"api_endpoint": "us-central1-aiplatform.googleapis.com"}
client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)

# Define a function to evaluate the model on a given dataset
def evaluate_model(model_location, data_location):
    # Set the parameters for the batch prediction job
    batch_prediction_job = aiplatform.gapic.BatchPredictionJob(
        display_name="Batch prediction job",
        model=model_location,
        input_config=aiplatform.gapic.BatchPredictionJob.InputConfig(
            instances_format="jsonl",
            gcs_source=aiplatform.gapic.GcsSource(uris=[data_location]),
        ),
        output_config=aiplatform.gapic.BatchPredictionJob.OutputConfig(
            predictions_format="jsonl",
            gcs_destination=aiplatform.gapic.GcsDestination(
                output_uri_prefix="gs://<your-bucket-name>/output"
            ),
        ),
    )

    # Start the batch prediction job and wait for it to complete
    batch_prediction_job = client.create_batch_prediction_job(
        parent="projects/<your-project-id>/locations/<your-model-location>",
        batch_prediction_job=batch_prediction_job,
    )
    batch_prediction_job.result()

    # Get the predictions from the output file
    output_uri = batch_prediction_job.output_info.gcs_output_directory
    output_blob = aiplatform.gapic.gcs.GcsClient().read_blob(output_uri + "/predictions.jsonl")
    predictions = output_blob.splitlines()

    # Compute the accuracy of the predictions
    num_correct = 0
    num_total = 0
    for prediction in predictions:
        prediction = json.loads(prediction)
        if prediction["predicted_label"] == prediction["true_label"]:
            num_correct += 1
        num_total += 1
    accuracy = num_correct / num_total

    return accuracy

# Evaluate the model on the training dataset
training_accuracy = evaluate_model(model_location, training_data_location)
print("Training accuracy:", training_accuracy)

# Evaluate the model on the production dataset
production_accuracy = evaluate_model(model_location, production_data_location)
print("Production accuracy:", production_accuracy)



"""

In this code, we first set the location of the model, the training dataset, and the production dataset. We then create a client object for the Vertex AI API.

The evaluate_model function takes as input the location of a dataset and evaluates the model on that dataset using a batch prediction job. The function returns the accuracy of the predictions.

We then call the evaluate_model function on the training dataset and the production dataset to evaluate the model in both training and production. The results are printed to the console.

"""