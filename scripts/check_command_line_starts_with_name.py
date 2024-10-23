import os
import json

def check_command_line(directory):

    mismatches = 0
    missing_fields = 0

    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                
                # Open and load the JSON file
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                    # Get the 'name' and 'command-line' fields
                    name = data.get('name', None)
                    command_line = data.get('command-line', None)
                    
                    if name and command_line:
                        # Check if 'command-line' starts with 'name' followed by a space
                        if not command_line.startswith(f"{name} ") and not command_line.startswith(f"wb_command -{name} "):
                            print(f"Mismatch found in {file_path}:")
                            print(f"  Name: {name}")
                            print(f"  Command-line: {command_line}")
                            print("-"*80)
                            mismatches += 1
                    else:
                        print(f"Missing 'name' or 'command-line' in {file_path}")
                        print("-"*80)
                        missing_fields += 1
    print(f"Total mismatches: {mismatches}")
    print(f"Total missing fields: {missing_fields}")

check_command_line('descriptors')
