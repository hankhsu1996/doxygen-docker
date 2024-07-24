import json
import os

with open('versions.json', 'r') as file:
    versions = json.load(file)

# Write the versions to the GitHub output environment file
with open(os.environ['GITHUB_OUTPUT'], 'a') as output_file:
    output_file.write(f"matrix={json.dumps(versions['versions'])}\n")

# Write the summary to the GITHUB_STEP_SUMMARY file
with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as summary_file:
    summary_file.write("## Versions to be built 🚀\n")
    for version in versions['versions']:
        summary_file.write(f"- {version}\n")
