import requests as r
import pandas as pd

access_token =""

#list docker images

project_name = "anbc-pdev"
location = "us-east4"
repository = "io-docker"

url = f"https://artifactregistry.googleapis.com/vi/projects/{project_name}/locations/{location}/repositories/{repository}/dockerImages"
headers = {"Authorization" : f"Bearer {access_token}", "Accept" : "application/json", "x-goog-user-project" : project_name }
res = r.get(url, headers=headers)
res.json

df = pd.DataFrame.from_dict(res.json()['dockerImages'])
df
