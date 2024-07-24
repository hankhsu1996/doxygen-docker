import json
import os

with open('versions.json', 'r') as file:
    versions = json.load(file)

# Write the versions to the GitHub output environment file
with open(os.environ['GITHUB_OUTPUT'], 'a') as output_file:
    output_file.write(f"matrix={json.dumps(versions['versions'])}\n")
