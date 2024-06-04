import json
import os
import glob
import shlex


def override_from_command_list(file_command_list, file_framework_json, prefix=''):
    with open(file_framework_json, 'r') as f:
        framework = json.load(f)
    
    new_endpoints = []

    with open(file_command_list, 'r') as f:
        for line in f:
            subcommand = line.strip()
            if len(subcommand) > 0:
                new_endpoints.append(f"{prefix}{subcommand}")

    old_endpoints = [x['target'] for x in framework["api"]["endpoints"]]

    for endpoint in old_endpoints:
        if endpoint not in new_endpoints:
            del framework["api"]["endpoints"][old_endpoints.index(endpoint)]
            print(f"Removed {endpoint} from {file_framework_json}")
    
    for endpoint in new_endpoints:
        if endpoint not in old_endpoints:
            framework["api"]["endpoints"].append({
                'target': f"{endpoint}",
                'status': 'missing',
            })
            print(f"Added {endpoint} to {file_framework_json}")

    # Collect list of command line invocations
    # Read all descriptors/{framework}/*.json files and extract field 'command-line'
    command_invocations = []
    for descriptor_file in glob.glob(f'descriptors/{framework["id"]}/*.json'):
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
    for endpoint in framework["api"]["endpoints"]:
        if endpoint["status"] == "ignore":
            continue

        hit = _find_command_invocation(endpoint["target"])

        if hit and (endpoint["status"] == "missing" or "descriptor" not in endpoint):
            endpoint["status"] = "done"
            endpoint["descriptor"] = hit.replace('\\', '/')
            print(f"Updated status of {endpoint['target']} to done in {file_framework_json}")
        if not hit and endpoint["status"] == "done":
            print(f"INFO: {endpoint['target']} is marked as done but no trivially matching descriptor found in {file_framework_json} (this might be a false positive)")

    with open(file_framework_json, 'w') as f:
        json.dump(framework, f, indent=2)
        f.write("\n")


if __name__ == '__main__':
    # set wd to the root of the project
    os.chdir(os.path.join(os.path.dirname(__file__), "../.."))
    assert os.path.exists('frameworks/fsl.json')
    assert os.path.exists('frameworks/afni.json')
    
    override_from_command_list('frameworks/commands/afni_commands.txt', 'frameworks/afni.json')
    override_from_command_list('frameworks/commands/ants_commands.txt', 'frameworks/ants.json')
    override_from_command_list('frameworks/commands/fsl_commands.txt', 'frameworks/fsl.json')
    override_from_command_list('frameworks/commands/freesurfer_commands.txt', 'frameworks/freesurfer.json')
    override_from_command_list('frameworks/commands/mrtrix_commands.txt', 'frameworks/mrtrix.json')
    override_from_command_list('frameworks/commands/c3d_commands.txt', 'frameworks/c3d.json')
    override_from_command_list('extraction/workbench/out_commands.txt', 'frameworks/workbench.json', prefix='wb_command ')
    override_from_command_list('frameworks/commands/niftyreg_commands.txt', 'frameworks/niftyreg.json')
