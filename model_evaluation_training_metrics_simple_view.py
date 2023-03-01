from google.cloud import aiplatform

def get_vertex_model_metrics(model_name):
    # Initialize aiplatform's ModelServiceClient
    client_options = {"api_endpoint": "us-central1-aiplatform.googleapis.com"}
    client = aiplatform.gapic.ModelServiceClient(client_options=client_options)

    # Get the Vertex AI model ID
    models = client.list_models(parent=f"projects/{PROJECT_ID}/locations/us-central1")
    for model in models:
        if model.display_name == model_name:
            model_id = model.name.split("/")[-1]

    # Get the model evaluation
    evaluation = client.list_model_evaluations(parent=f"projects/{PROJECT_ID}/locations/us-central1/models/{model_id}")\
        .evaluations[0]

    # Get the model evaluation metrics
    metrics = evaluation.metrics.metrics
    auroc = metrics["aiplatform.googleapis.com/auroc"]
    auprc = metrics["aiplatform.googleapis.com/auprc"]
    log_loss = metrics["aiplatform.googleapis.com/log_loss"]
    accuracy = metrics["aiplatform.googleapis.com/accuracy"]
    confusion_matrix = metrics["aiplatform.googleapis.com/confusion_matrix"]
    
    # Print the model evaluation metrics
    print(f"Model Evaluation Metrics for {model_name}:")
    print(f"AUROC: {auroc.double_value}")
    print(f"AUPRC: {auprc.double_value}")
    print(f"Log Loss: {log_loss.double_value}")
    print(f"Accuracy: {accuracy.double_value}")
    print(f"Confusion Matrix: {confusion_matrix.confusion_matrix_at_thresholds[0].matrix}")
