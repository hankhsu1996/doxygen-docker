import yaml
import json

with open('versions.yml', 'r') as file:
    versions = yaml.safe_load(file)

# Print the versions in the required format for GitHub Actions output
print(f"::set-output name=matrix::{json.dumps(versions['versions'])}")
