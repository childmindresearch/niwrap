import json
import os
import glob
import shlex


def override_from_command_list(file_command_list, file_package_json, prefix=''):
    with open(file_package_json, 'r') as f:
        package = json.load(f)
    
    new_endpoints = []

    with open(file_command_list, 'r') as f:
        for line in f:
            subcommand = line.strip()
            if len(subcommand) > 0:
                new_endpoints.append(f"{prefix}{subcommand}")

    old_endpoints = [x['target'] for x in package["api"]["endpoints"]]

    for endpoint in old_endpoints:
        if endpoint not in new_endpoints:
            del package["api"]["endpoints"][old_endpoints.index(endpoint)]
            print(f"Removed {endpoint} from {file_package_json}")
    
    for endpoint in new_endpoints:
        if endpoint not in old_endpoints:
            package["api"]["endpoints"].append({
                'target': f"{endpoint}",
                'status': 'missing',
            })
            print(f"Added {endpoint} to {file_package_json}")

    # Collect list of command line invocations
    # Read all descriptors/{package}/*.json files and extract field 'command-line'
    command_invocations = []
    for descriptor_file in glob.glob(f'descriptors/{package["id"]}/*.json'):
        with open(descriptor_file, 'r') as f:
            descriptor = json.load(f)
            command_args = shlex.split(descriptor["command-line"])
            command_invocations.append((descriptor_file, command_args))

    def _find_command_invocation(invocation):
        invocation = invocation.split(' ')[-1]
        for file, command in command_invocations:
            if invocation in command:
                return file
        return None

    # Check if a descriptor is available for any endpoint
    for endpoint in package["api"]["endpoints"]:
        if endpoint["status"] == "ignore":
            continue

        hit = _find_command_invocation(endpoint["target"])

        if hit and (endpoint["status"] == "missing" or "descriptor" not in endpoint):
            endpoint["status"] = "done"
            endpoint["descriptor"] = hit.replace('\\', '/')
            print(f"Updated status of {endpoint['target']} to done in {file_package_json}")
        if not hit and endpoint["status"] == "done":
            print(f"INFO: {endpoint['target']} is marked as done but no trivially matching descriptor found in {file_package_json} (this might be a false positive)")

    with open(file_package_json, 'w') as f:
        json.dump(package, f, indent=2)
        f.write("\n")


if __name__ == '__main__':
    # set wd to the root of the project
    os.chdir(os.path.join(os.path.dirname(__file__), "../.."))
    assert os.path.exists('packages/fsl.json')
    assert os.path.exists('packages/afni.json')
    
    override_from_command_list('packages/commands/afni_commands.txt', 'packages/afni.json')
    override_from_command_list('packages/commands/ants_commands.txt', 'packages/ants.json')
    override_from_command_list('packages/commands/fsl_commands.txt', 'packages/fsl.json')
    override_from_command_list('packages/commands/freesurfer_commands.txt', 'packages/freesurfer.json')
    override_from_command_list('packages/commands/mrtrix_commands.txt', 'packages/mrtrix.json')
    override_from_command_list('packages/commands/c3d_commands.txt', 'packages/c3d.json')
    override_from_command_list('extraction/workbench/out_commands.txt', 'packages/workbench.json', prefix='wb_command ')
    override_from_command_list('packages/commands/niftyreg_commands.txt', 'packages/niftyreg.json')
