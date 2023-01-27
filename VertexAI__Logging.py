import logging
import vertexai

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the model
model = vertexai.load("path/to/model")

# Log information about the model
logger.info("Model loaded successfully")
logger.info("Model name: %s", model.name)
logger.info("Model version: %s", model.version)

# Use the model to make predictions
output = model.predict(input_data)

# Log the output
logger.info("Prediction output: %s", output)


#batch predictions

import logging
import vertexai

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the model
model = vertexai.load("path/to/model")

# Log information about the model
logger.info("Model loaded successfully")
logger.info("Model name: %s", model.name)
logger.info("Model version: %s", model.version)

# Prepare input data for batch predictions
batch_input_data = [input1, input2, input3, ...]

# Make batch predictions
output = model.predict(batch_input_data)

# Log the output
logger.info("Batch prediction output: %s", output)

# Iterate over the output and log individual predictions
for i, prediction in enumerate(output):
    logger.info("Prediction %d: %s", i, prediction)



#Batch predictions track error messages:
import logging
import vertexai

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# Load the model
try:
    model = vertexai.load("path/to/model")
except Exception as e:
    logger.error("Error loading model: %s", str(e))
    exit()

# Log information about the model
logger.info("Model loaded successfully")
logger.info("Model name: %s", model.name)
logger.info("Model version: %s", model.version)

# Prepare input data for batch predictions
batch_input_data = [input1, input2, input3, ...]

# Make batch predictions
try:
    output = model.predict(batch_input_data)
except Exception as e:
    logger.error("Error making batch predictions: %s", str(e))
    exit()

# Log the output
logger.info("Batch prediction output: %s", output)

# Iterate over the output and log individual predictions
for i, prediction in enumerate(output):
    try:
        logger.info("Prediction %d: %s", i, prediction)
    except Exception as e:
        logger.error("Error logging prediction %d: %s", i, str(e))



#batch predictions success logs

import logging
import vertexai

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the model
try:
    model = vertexai.load("path/to/model")
    logger.info("Model loaded successfully")
    logger.info("Model name: %s", model.name)
    logger.info("Model version: %s", model.version)
except Exception as e:
    logger.error("Error loading model: %s", str(e))
    exit()

# Prepare input data for batch predictions
batch_input_data = [input1, input2, input3, ...]

# Make batch predictions
try:
    output = model.predict(batch_input_data)
    logger.info("Batch predictions made successfully")
except Exception as e:
    logger.error("Error making batch predictions: %s", str(e))
    exit()

# Log the output
logger.info("Batch prediction output: %s", output)

# Iterate over the output and log individual predictions
for i, prediction in enumerate(output):
    try:
        logger.info("Prediction %d: %s", i, prediction)
    except Exception as e:
        logger.error("Error logging prediction %d: %s", i, str(e))

