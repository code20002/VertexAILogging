from google.cloud import bigquery
from google.cloud import aiplatform

def create_bq_table(model_id):
    # Set up Vertex AI clients
    aiplatform.init(project="your-project-id")
    model_client = aiplatform.gapic.ModelServiceClient()

    # Get the model name and training job ID from the model ID
    model = model_client.get_model(name=model_id)
    model_name = model.display_name
    training_job_id = model.metadata.get("aiplatform.googleapis.com/training_job")

    # Get the evaluation metrics for the model
    metrics = model_client.get_model_evaluation(name=f"{model_id}/evaluations/-")
    metric_values = metrics.metrics

    # Set up the BigQuery client and table reference
    bq_client = bigquery.Client()
    table_ref = bq_client.dataset("your_dataset_name").table("your_table_name")

    # Define the schema for the table
    schema = [
        bigquery.SchemaField("Model ID", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("Model Name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("Time Stamp", "TIMESTAMP", mode="REQUIRED"),
        bigquery.SchemaField("Metrics Name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("Metric Value", "FLOAT", mode="REQUIRED")
    ]

    # Create the table if it does not already exist
    table = bigquery.Table(table_ref, schema=schema)
    table = bq_client.create_table(table, exists_ok=True)

    # Add the model evaluation metrics to the table
    rows_to_insert = []
    for metric_name, metric_value in metric_values.items():
        row = {
            "Model ID": model_id,
            "Model Name": model_name,
            "Time Stamp": bigquery.ScalarQueryParameter("TIMESTAMP", aiplatform.helpers.create_datetime().isoformat()),
            "Metrics Name": metric_name,
            "Metric Value": metric_value.double_value
        }
        rows_to_insert.append(row)

    errors = bq_client.insert_rows(table, rows_to_insert)  # Insert data into BigQuery
    if errors != []:
        print(f"Encountered errors while inserting rows: {errors}")
    else:
        print("Data was inserted into BigQuery successfully!")





"""

This function uses the google-cloud-bigquery and google-cloud-aiplatform libraries to interact with BigQuery and Vertex AI, respectively. It first initializes the Vertex AI clients and gets the model name and training job ID from the provided model ID. It then gets the evaluation metrics for the model using the get_model_evaluation method.

Next, it sets up the BigQuery client and table reference, and defines the schema for the table. If the table does not already exist, it creates it using the provided schema. Finally, it creates a list of rows to insert into the table, where each row contains the model ID, model name, current timestamp, metric name, and metric value.

The insert_rows method is used to insert the data into the BigQuery table, and any errors encountered during the insertion process are printed to the console. If no errors are encountered, a success message is printed to the console.

Note that you will need to replace the placeholders your-project-id, your_dataset_name, and your_table_name with your actual project ID, dataset name, and table name, respectively.

"""