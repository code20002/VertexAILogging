import pandas as pd
import json

# create example dataframe
df = pd.DataFrame({
    'resource_name': ['resource_1', 'resource_2'],
    'version_id': [1, 2],
    'create_time': ['2022-01-01', '2022-01-01'],
    'update_time': ['2022-01-10', '2022-01-10'],
    'EvaluationMetrics': ['auRoc', 'confidenceMetrics'],
    'Actual_Values': ['0.8', '{"falsepositive":1.0,"falseNegative":0.9,"f1Score":0.0767}']
})

# convert Actual_Values column to separate rows
df = pd.concat([df.drop('Actual_Values', axis=1), 
                df['Actual_Values'].apply(lambda x: pd.Series(json.loads(x)))], 
               axis=1).melt(id_vars=['resource_name', 'version_id', 'create_time', 'update_time', 'EvaluationMetrics'],
                            var_name='Metric_Type', value_name='Metric_Value')
# filter out rows where EvaluationMetrics is not 'confidenceMetrics'
df = df[df['EvaluationMetrics'] == 'confidenceMetrics']
# rename Metric_Type values to match the desired output
df['Metric_Type'] = df['Metric_Type'].replace({'falsepositive': 'FalsePositive', 'falseNegative': 'FalseNegative', 'f1Score': 'F1Score'})
# sort by resource_name and version_id
df = df.sort_values(['resource_name', 'version_id'])

# display final output
print(df)


"""
This script will first split the 'Actual_Values' column into separate rows for each key-value pair using the json.loads() method to convert the JSON string to a dictionary and the pd.Series() method to convert the dictionary to separate columns. It will then filter out rows where 'EvaluationMetrics' is not 'confidenceMetrics' and rename the 'Metric_Type' values to match the desired output. Finally, it will sort the rows by 'resource_name' and 'version_id'.
"""