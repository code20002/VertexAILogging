import pandas as pd
import json

# Create the DataFrame
data = {
    'resource_name': ['Resource A'],
    'version_id': [1],
    'create_time': ['2022-02-28 12:00:00'],
    'update_time': ['2022-02-28 13:00:00'],
    'eval_metrics': ['confidenceMetrics'],
    'eval_values': [{'falsepositiverate' : 1.0, 'falsepositivecount' : 0.9, 'truepositivecount' : 0.0767, 'precisionAt1' : 0.5, 'precision' : 0.5, 'f1score' : 0.667, 'recall' : 0.3}]
}

df = pd.DataFrame(data)

# Convert eval_values to JSON string
df['eval_values'] = df['eval_values'].apply(json.dumps)

# Normalize eval_values into separate columns
df = pd.json_normalize(df.to_dict(orient='records'))

# Melt the columns into rows
id_vars = ['resource_name', 'version_id', 'create_time', 'update_time']
value_vars = [col for col in df.columns if col not in id_vars]
df = pd.melt(df, id_vars=id_vars, value_vars=value_vars, var_name='metric', value_name='value')

# Filter out null values
df = df.dropna()

# Convert value column to float
#df['value'] = df['value'].astype(float)

# Sort by metric
df = df.sort_values('metric')

# Reset the index
df = df.reset_index(drop=True)
print(df)
