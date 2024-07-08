import pathlib
import json
import re


PATH_WB_DUMP = pathlib.Path(__file__).parent / "outs"
PATH_WB_BOUTIQUES = pathlib.Path(__file__).parent.parent.parent / "descriptors" / "workbench"

assert PATH_WB_DUMP.exists(), "Workbench dump not found."
assert PATH_WB_BOUTIQUES.exists(), "Boutiques directory not found."



def set_wb_type(wb_type, input_):
    if wb_type == "String":
        input_["type"] = "String"
    
    elif wb_type == "Surface File":
        input_["type"] = "File"
    elif wb_type == "Border File":
        input_["type"] = "File"
    elif wb_type == "Metric File":
        input_["type"] = "File"
    elif wb_type == "Annotation File":
        input_["type"] = "File"
    elif wb_type == "Cifti File":
        input_["type"] = "File"
    elif wb_type == "Volume File":
        input_["type"] = "File"
    elif wb_type == "Label File":
        input_["type"] = "File"
    elif wb_type == "Foci File":
        input_["type"] = "File"
    
    elif wb_type == "Floating Point":
        input_["type"] = "Number"
        input_["integer"] = False
    elif wb_type == "Integer":
        input_["type"] = "Number"
        input_["integer"] = True
    
    elif wb_type == "Boolean":
        input_["type"] = "String"
        input_["value-choices"] = ["true", "false"]
    
    else:
        raise ValueError(f"Unknown type: {wb_type}")
    
    return input_


def as_bt_id(s):
    if s.startswith("-"):
        s = s[1:]
    s = re.sub(r"\W", "_", s).lower()
    return s


def as_value_key(s):
    if s.startswith("-"):
        s = s[1:]
    s = re.sub(r"\W", "_", s).upper()
    return f'[{s}]'


def unallcaps(s):
    """Converts "ALL CAPS" to "All caps"."""
    if len(s) <= 1:
        return s
    return s[0] + s[1:].lower()


def make_param(param, bt_inputs, bt_descriptor):
    input_id = as_bt_id(param["short_name"])
    value_key = as_value_key(param['short_name'])
    bt_inputs.append(set_wb_type(param["type"],{
        "id": input_id,
        "name": input_id,
        "description": param["description"],
        "optional": False,
        "value-key": value_key
    }))
    bt_descriptor['command-line'] += f" {value_key}"


def make_output(out, bt_inputs, bt_outputs, bt_descriptor):
    input_id = as_bt_id(out["short_name"])
    value_key = as_value_key(out['short_name'])
    bt_inputs.append({
        "id": input_id,
        "name": input_id,
        "type": "String",
        "description": out["description"],
        "optional": False,
        "value-key": value_key
    })

    bt_outputs.append({
        "id": input_id,
        "name": input_id,
        "path-template": value_key,
        "description": out["description"],
        "optional": False
    })
    
    bt_descriptor["command-line"] += f" {value_key}"


def make_poor(opt, bt_inputs, bt_outputs, bt_descriptor, repeatable=False):
    assert "params" in opt
    assert "options" in opt
    assert "outputs" in opt
    assert "repeatable_options" in opt
    assert "description" in opt
    assert "option_switch" in opt
    assert "key" in opt

    
    if repeatable or (len(opt["params"]) + len(opt["outputs"]) + len(opt["options"]) + len(opt["repeatable_options"])) > 1:
        # subcommand needed
        input_id = as_bt_id(opt["option_switch"])
        value_key = as_value_key(opt["option_switch"])
        new_descriptor = {
            "id": as_bt_id(opt["option_switch"]),
            "name": as_bt_id(opt["option_switch"]),
            "description": opt["description"],
            "command-line": opt["option_switch"],
            "inputs": [],
            "output-files": [],
        }
        bt_inputs.append({
            "id": input_id,
            "name": input_id,
            "description": opt["description"],
            #"command-line-flag": opt["option_switch"],
            "type": new_descriptor,
            "optional": True,
            "value-key": value_key,
            "list": repeatable
        })
        bt_descriptor["command-line"] += f" {value_key}"
        bt_inputs = new_descriptor["inputs"]
        bt_outputs = new_descriptor["output-files"]
        bt_descriptor = new_descriptor

        for param in opt["params"]:
            make_param(param, bt_inputs, bt_descriptor)

    elif len(opt["params"]) == 0:
        # command line flag

        input_id = as_bt_id("opt"+opt["option_switch"])
        value_key = as_value_key(input_id)
        bt_inputs.append({
            "id": input_id,
            "name": input_id,
            "command-line-flag": opt["option_switch"],
            "description": opt["description"],
            "type": "Flag",
            "optional": True,
            "value-key": value_key
        })
        bt_descriptor["command-line"] += f" {value_key}"

    elif len(opt["params"]) == 1:
        param = opt["params"][0]

        input_id = as_bt_id(f"opt{opt['option_switch']}-{param['short_name']}")
        value_key = as_value_key(input_id)
        bt_inputs.append(set_wb_type(param["type"],{
            "id": input_id,
            "name": input_id,
            "command-line-flag": opt["option_switch"],
            "description": opt["description"] + ": " + param["description"],
            "optional": True,
            "value-key": value_key
        }))
        bt_descriptor["command-line"] += f" {value_key}"
    else:
        for param in opt["params"]:
            make_param(param, bt_inputs, bt_descriptor)

    for out in opt["outputs"]:
        make_output(out, bt_inputs, bt_outputs, bt_descriptor)

    for sub_opt in opt["options"]:
        make_poor(sub_opt, bt_inputs, bt_outputs, bt_descriptor, repeatable=False)

    for sub_opt in opt["repeatable_options"]:
        make_poor(sub_opt, bt_inputs, bt_outputs, bt_descriptor, repeatable=True)


    if ("inputs" in bt_descriptor) and (len(bt_descriptor["inputs"]) == 0):
        del bt_descriptor["inputs"]
    if ("output-files" in bt_descriptor) and (len(bt_descriptor["output-files"]) == 0):
        del bt_descriptor["output-files"]
    if ("groups" in bt_descriptor) and (len(bt_descriptor["groups"]) == 0):
        del bt_descriptor["groups"]



def make_descriptor(j):

    inputs = []
    output_files = []
    groups = []

    bt_descriptor = {
        "tool-version": "1.5.0 2e663bdff57597d5d1fb251dc4740d14d9cf11dd",
        "name": j["command"][1:],
        "author": "Washington University School of Medicin",
        #"descriptor-url": "https://github.com/aces/cbrain-plugins-neuro/blob/master/cbrain_task_descriptors/fsl_bet.json",
        "command-line": f"wb_command {j['command']}",
        "container-image": {
            "image": "fcpindi/c-pac:latest",
            "type": "docker"
        },
        "description": unallcaps(j["short_description"]) + ".\n\n" + j["help_text"],
        "schema-version": "0.5",
        "tags": {},
        "inputs": inputs,
        "output-files": output_files,
        "groups": groups,
    }

    for i in j["params"]:
        make_param(i, inputs, bt_descriptor)

    for o in j["outputs"]:
        make_output(o, inputs, output_files, bt_descriptor)

    for o in j["options"]:
        make_poor(o, inputs, output_files, bt_descriptor, repeatable=False)
    
    for o in j["repeatable_options"]:
        make_poor(o, inputs, output_files, bt_descriptor, repeatable=True)


    if ("inputs" in bt_descriptor) and (len(bt_descriptor["inputs"]) == 0):
        del bt_descriptor["inputs"]
    if ("output-files" in bt_descriptor) and (len(bt_descriptor["output-files"]) == 0):
        del bt_descriptor["output-files"]
    if ("groups" in bt_descriptor) and (len(bt_descriptor["groups"]) == 0):
        del bt_descriptor["groups"]

    return bt_descriptor

def main():

    for idx_p, p in enumerate(PATH_WB_DUMP.glob("*_output.txt")):
        if p.stem in [
            "-class-add-member_output",
            "-class-create-algorithm_output", 
            "-class-create-enum_output", 
            "-class-create_output", 
            "-class-create-operation_output", 
            "-unit-test_output"
        ]:
            print(f"Skipping {p}")
            continue

        #if idx_p < 10:
        #    continue
        #if idx_p > 10:
        #    break
        print(f"Processing {p}")
        # load into string
        with open(p, "r") as f:
            txt = f.read()
        # remove trailing commas
        #--txt = re.sub(r",\s*([}\]])", r"\g<1>", txt)
        # add missing commas
        #--txt = re.sub(r'"\s+("[a-z]+"):', r'",\g<1>:', txt)

        # to json
        try:
            j = json.loads(txt)
        except json.JSONDecodeError as e:
            print(txt)
            raise e

        descriptor = make_descriptor(j)

        # write to file
        out_path = pathlib.Path("descriptors/workbench") / (descriptor["name"] + ".json")
        with open(out_path, "w") as f:
            json.dump(descriptor, f, indent=2)
            f.write("\n")
        # print as json
        #print(json.dumps(descriptor, indent=2))


if __name__ == "__main__":
    main()
