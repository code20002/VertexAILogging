import datetime
from google.cloud import bigquery
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Set up BigQuery client and table information
client = bigquery.Client()
table_id = 'your-project.your_dataset.model_evaluation'
prediction_table_id = 'your-project.your_dataset.prediction_out'
model_id = 'your_model_id'
model_name = 'your_model_name'

# Define the evaluation metric functions to be used
metric_functions = {
    'accuracy': accuracy_score,
    'precision': precision_score,
    'recall': recall_score
}

# Define the evaluation metric types to be used
metric_types = list(metric_functions.keys())

# Define the training and prediction metrics to be captured
training_metrics = {
    'train_loss': 0.123,
    'val_loss': 0.456,
    'train_accuracy': 0.789,
    'val_accuracy': 0.987
}
prediction_metrics = {
    'y_actuals': [0, 1, 1, 0],
    'y_pred': [0, 1, 0, 1]
}

# Define the time stamp
timestamp = datetime.datetime.now()

# Evaluate the model on the prediction data and update the prediction metrics
for metric_type, metric_function in metric_functions.items():
    prediction_metrics[metric_type] = metric_function(
        prediction_metrics['y_actuals'], prediction_metrics['y_pred'])

# Define the rows to be inserted into the BigQuery table
rows_to_insert = []
for metric_type in metric_types:
    row = {
        'model_id': model_id,
        'model_name': model_name,
        'timestamp': timestamp,
        'metric_type': metric_type,
        'training_metrics': training_metrics,
        'prediction_metrics': prediction_metrics
    }
    rows_to_insert.append(row)

# Insert the rows into the BigQuery table
errors = client.insert_rows_json(table_id, rows_to_insert)
if errors:
    print(f'Errors: {errors}')

# Update the prediction out table with the ground truth values
query = f'''
    UPDATE `{prediction_table_id}`
    SET y_actuals = {prediction_metrics['y_actuals']},
        y_pred = {prediction_metrics['y_pred']}
    WHERE model_id = '{model_id}'
'''
query_job = client.query(query)
