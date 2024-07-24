import json

with open('versions.json', 'r') as file:
    versions = json.load(file)

# Print the versions in the required format for GitHub Actions output
print(f"::set-output name=matrix::{json.dumps(versions['versions'])}")
