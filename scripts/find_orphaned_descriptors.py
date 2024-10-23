import os
import json

def find_orphaned_descriptors(package_dir, descriptors_dir):
    orphaned_files = []

    # Collect all listed descriptor files from package endpoints
    listed_descriptors = {}

    # Iterate through all JSON files in the packages directory
    for package_file in os.listdir(package_dir):
        if package_file.endswith(".json"):
            package_path = os.path.join(package_dir, package_file)
            
            # Load the package JSON file
            with open(package_path, 'r', encoding='utf-8') as f:
                package_data = json.load(f)
            
            package_id = package_data.get('id')
            if not package_id:
                print(f"Missing 'id' in {package_file}")
                continue
            
            # Collect the listed descriptor files from the endpoints
            listed_descriptors[package_id] = set()
            for endpoint in package_data.get('api', {}).get('endpoints', []):
                descriptor_path = endpoint.get('descriptor')
                if descriptor_path:
                    descriptor_file = os.path.basename(descriptor_path)
                    listed_descriptors[package_id].add(descriptor_file)

    # Now look for orphaned descriptor files
    for package_id in listed_descriptors:
        descriptor_path = os.path.join(descriptors_dir, package_id)
        if os.path.exists(descriptor_path):
            for file in os.listdir(descriptor_path):
                if file.endswith(".json"):
                    # Check if the file is listed in the corresponding package's endpoints
                    if file not in listed_descriptors[package_id]:
                        orphaned_files.append(os.path.join(descriptor_path, file))

    # Print the orphaned descriptor files
    if orphaned_files:
        print("Orphaned descriptor files found:")
        for orphan in orphaned_files:
            print(f"  {orphan}")
    else:
        print("No orphaned descriptor files found.")

find_orphaned_descriptors("packages", "descriptors")
