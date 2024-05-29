# Update frameworks/workbench.json api endpoint list from out_commands.txt

import json
import os

# set wd to the root of the project
os.chdir(os.path.join(os.path.dirname(__file__), "../.."))
assert os.path.exists('frameworks/workbench.json')

# Load the current workbench.json
with open('frameworks/workbench.json', 'r') as f:
    workbench = json.load(f)

workbench["api"]["endpoints"] = []

# Update the api endpoint list
with open('extraction/workbench/out_commands.txt', 'r') as f:
    for line in f:
        subcommand = line.strip()
        if len(subcommand) > 0:
            workbench["api"]["endpoints"].append({
                'target': f"wb_command {subcommand}",
                'status': 'done',
            })

# Write the updated workbench.json

with open('frameworks/workbench.json', 'w') as f:
    json.dump(workbench, f, indent=2)
    f.write("\n")
