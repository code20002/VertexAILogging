from google.cloud import bigquery
from google.cloud import aiplatform

# Initialize a BigQuery client and dataset ID
client = bigquery.Client()
dataset_id = 'your_dataset_id'

# Initialize an AI Platform client and model ID
ai_platform_client = aiplatform.gapic.ModelServiceClient()
model_id = 'your_model_id'

# Initialize a batch prediction job
job_spec = {
    "model": f"projects/{PROJECT_ID}/locations/{REGION}/models/{model_id}",
    "input_config": {
        "instances_format": "jsonl",
        "jsonl_instance_schema_uri": "gs://your-bucket/schema.json"
    },
    "output_config": {
        "predictions_format": "jsonl",
        "jsonl_instance_schema_uri": "gs://your-bucket/schema.json",
        "gcs_destination": {"output_uri_prefix": "gs://your-bucket/output/"}
    }
}
job = ai_platform_client.create_batch_prediction_job(
    parent=f"projects/{PROJECT_ID}/locations/{REGION}",
    batch_prediction_job=job_spec,
)

# Wait for the batch prediction job to complete
job.result()

# Load the predicted and ground truth data into pandas dataframes
predicted_df = pd.read_json('gs://your-bucket/output/predictions.jsonl', lines=True)
ground_truth_df = pd.read_json('gs://your-bucket/ground_truth.jsonl', lines=True)

# Calculate prediction output metrics
accuracy = accuracy_score(ground_truth_df['label'], predicted_df['label'])
precision = precision_score(ground_truth_df['label'], predicted_df['label'])
recall = recall_score(ground_truth_df['label'], predicted_df['label'])
f1 = f1_score(ground_truth_df['label'], predicted_df['label'])

# Save the evaluation metrics for both training and actuals in the same BigQuery table
table_ref = client.dataset(dataset_id).table('model_evaluation_metrics')
job_config = bigquery.LoadJobConfig(
    write_disposition='WRITE_APPEND',
    schema=[
        bigquery.SchemaField('model_id', 'STRING'),
        bigquery.SchemaField('dataset_type', 'STRING'),
        bigquery.SchemaField('accuracy', 'FLOAT'),
        bigquery.SchemaField('precision', 'FLOAT'),
        bigquery.SchemaField('recall', 'FLOAT'),
        bigquery.SchemaField('f1', 'FLOAT'),
    ],
)
rows_to_insert = [
    (model_id, 'training', training_accuracy, training_precision, training_recall, training_f1),
    (model_id, 'actuals', accuracy, precision, recall, f1),
]
job = client.load_table_from_rows(
    table_ref,
    rows_to_insert,
    job_config=job_config
)
job.result()

print('Evaluation metrics saved to BigQuery table.')


"""

In this example, the code initializes a BigQuery client and dataset ID, an AI Platform client and model ID, and a batch prediction job. The code then waits for the batch prediction job to complete and loads the predicted and ground truth data into pandas dataframes. The code calculates prediction output metrics (accuracy, precision, recall, and f1 score) and saves the evaluation metrics for both training and actuals in the same BigQuery table using a load job with a write append disposition. The code outputs a message indicating that the evaluation metrics have been saved to the BigQuery table.

"""