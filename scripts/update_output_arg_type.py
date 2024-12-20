import glob
import json
import re

out_regex = re.compile(r"\b(?:\w*_)?(?:output|out)(?:_\w*)?\b", re.IGNORECASE)

# Path to folder with JSON descriptors
json_files = glob.glob("descriptors/*/*.json")

for json_file in json_files:
    with open(json_file, "r") as f:
        data = json.load(f)

    changes_made = False

    if "inputs" in data:
        # Grab only the part that would match the value-key
        outputs = (
            [
                re.split("\]", output["path-template"])[0] + "]"
                for output in data["output-files"]
            ]
            if "output-files" in data
            else []
        )
        for input_obj in data["inputs"]:
            if "id" in input_obj and "type" in input_obj:
                if (
                    out_regex.search(input_obj["id"])
                    and input_obj["type"] == "File"
                    and input_obj["value-key"] in outputs
                ):
                    input_obj["type"] = "String"
                    changes_made = True
                    print(
                        f"Changed type to 'String' for '{input_obj['name']}' in {json_file}"
                    )
            else:
                print(f"Warning missing 'name' and / or 'type' in {json_file}")

    if changes_made:
        with open(json_file, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Updated {json_file} output argument types.")
