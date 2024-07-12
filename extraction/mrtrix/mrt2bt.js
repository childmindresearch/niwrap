const fs = require('fs');
const path = require('path');



function make_descriptor(obj) {

    // boutiques descriptor skeleton
    const descriptor = {
        "name": "tool_name",
        "description": "description",
        "author": "author",
        "tool-version": "1.0.0",
        "schema-version": "0.5",
        "container-image": {
          "image": "mrtrix3/mrtrix3:3.0.4",
          "type": "docker"
        },
        "command-line": "tool",
        "inputs": [],
        "output-files": []
    };

    // fill the descriptor with the object
    descriptor.name = obj.name;
    descriptor.description = obj.synopsis + '.\n\n' + obj.description.join('\n\n') + '\n\nReferences:\n\n' + obj.references.join('\n\n');
    descriptor.author = obj.author;
    descriptor['tool-version'] = obj.version;
    descriptor.url = 'https://mrtrix.readthedocs.io/en/latest/reference/commands/' + obj.name + '.html';
    descriptor['command-line'] = obj.name;
    if (!obj.name) {
        throw new Error('No name for the tool');
    }

    // Options

    function set_type(argument, boutiques_input, comma_separated = false) {
        if (argument.type == 'integer') {
            boutiques_input.type = 'Number';
            boutiques_input.integer = true;
            return false;
        } else if (argument.type == 'float') {
            boutiques_input.type = 'Number';
            boutiques_input.integer = false;
            return false;
        } else if (argument.type == 'text') {
            boutiques_input.type = 'String';
            return false;
        } else if (argument.type == 'file in') {
            boutiques_input.type = 'File';
            return false;
        } else if (argument.type == 'file out') {
            boutiques_input.type = 'String';
            return true;
        } else if (argument.type == 'directory in') {
            boutiques_input.type = 'File';
            return false;
        } else if (argument.type == 'directory out') {
            boutiques_input.type = 'String';
            return true;
        } else if (argument.type == 'image in') {
            boutiques_input.type = 'File';
            return false;
        } else if (argument.type == 'image out') {
            boutiques_input.type = 'String';
            return true;
        } else if (argument.type == 'choice') {
            boutiques_input.type = 'String';
            // split by / to get the choices
            //boutiques_input['value-choices'] = argument.id.split('/');
            // note: this is not always correct, e.g. dwi2fod algorithm
            // so lets just keep it as a str for now
            return false;
        } else if (argument.type == 'int seq') {
            boutiques_input.type = 'Number';
            boutiques_input.integer = true;
            boutiques_input.list = true;
            if (comma_separated) {
                boutiques_input["list-separator"] = ',';
            }
            return false;
        } else if (argument.type == 'float seq') {
            boutiques_input.type = 'Number';
            boutiques_input.integer = false;
            boutiques_input.list = true;
            if (comma_separated) {
                boutiques_input["list-separator"] = ',';
            }
            return false;
        } else if (argument.type == 'tracks in') {
            boutiques_input.type = 'File';
            return false;
        } else if (argument.type == 'tracks out') {
            boutiques_input.type = 'String';
            return true;
        } else if (argument.type == 'various') {
            boutiques_input.type = 'String';
            return false;
        } else if (argument.type == 'undefined') {
            // E.g. dcmedit tag elements have this type - not sure what it is
            boutiques_input.type = 'String';
            return false;
        } else {
            throw new Error('Unknown type: ' + argument.type);
        }
    }

    for (const option_group of obj.option_groups) {
        for (const option of option_group.options) {

            const id = (option_group.name + "_" + option.id).replace(/[^a-zA-Z0-9]/g, '_');
            const template_key = `[${id.toUpperCase()}]`;
            const input = {
                "id": option.id.replace(/[^a-zA-Z0-9]/g, '_'),
                "name": option.id.replace(/[^a-zA-Z0-9]/g, '_'),
                "command-line-flag": "-" + option.id,
                "value-key": template_key,
                "description": option.description,
                "type": "?",
                "optional": option.optional
            };
            descriptor.inputs.push(input);
            descriptor['command-line'] += ' ' + template_key;

            if (option.arguments.length > 1 || option.allow_multiple) { // needs subcommand

                input['command-line-flag'] = undefined; // we pull the flag into the subcommand

                if (option.allow_multiple) {
                    input.list = true;
                }

                // make the subcommand descriptor
                const subcommand_descriptor = {
                    "id": option.id.replace(/[^a-zA-Z0-9]/g, '_'),
                    "name": option.id.replace(/[^a-zA-Z0-9]/g, '_'),
                    "description": option.description,
                    "command-line": "-" + option.id,
                    "inputs": [],
                    "output-files": []
                };
                input.type = subcommand_descriptor;

                for (const argument of option.arguments) {
                    const id = argument.id.replace(/[^a-zA-Z0-9]/g, '_');
                    const template_key = `[${id.toUpperCase()}]`;
                    const input = {
                        "id": id,
                        "name": id,
                        "value-key": template_key,
                        "description": argument.description || option.description,
                        "type": "?",
                        "optional": argument.optional
                    };
                    if (argument.allow_multiple) {
                        input.list = true;
                    }

                    const comma_separated = option.description.includes("comma-separated");
                    const has_output = set_type(argument, input, comma_separated);
                    subcommand_descriptor['command-line'] += ' ' + template_key;
                    if (has_output) {
                        subcommand_descriptor['output-files'].push({
                            "id": id,
                            "name": id,
                            "path-template": template_key,
                            "description": argument.description || option.description
                        });
                    }

                    subcommand_descriptor.inputs.push(input);
                }

            } else if (option.arguments.length == 0) {
                // no argument
                input.type = 'Flag';
            } else if (option.arguments.length == 1 && !option.allow_multiple) {
                const argument = option.arguments[0];

                if (argument.allow_multiple) {
                    // raise error
                    throw new Error('Argument "' + argument.id + '" has allow_multiple set to true');
                }

                if (argument.optional) {
                    // raise error
                    throw new Error('Argument "' + argument.id + '" has optional set to true (expected only the option could be optional)');
                }

                const comma_separated = option.description.includes("comma-separated");
                const has_output = set_type(argument, input, comma_separated);
                if (has_output) {
                    descriptor['output-files'].push({
                        "id": option.id,
                        "name": option.id,
                        "path-template": template_key,
                        "description": option.description + ((' ' + argument.description) || '')
                    });
                }
            } else {
                // raise error
                throw new Error('This should not be able to happen');
            }

        }
    }

    // Positional arguments

    // remove options so that they are added at the end
    const option_inputs = descriptor.inputs;
    descriptor.inputs = [];
    const option_outputs = descriptor['output-files'];
    descriptor['output-files'] = [];

    for (const argument of obj.arguments) {
        const id = argument.id.replace(/[^a-zA-Z0-9]/g, '_');
        const template_key = `[${id.toUpperCase()}]`;
        const input = {
            "id": id,
            "name": id,
            "value-key": template_key,
            "description": argument.description,
            "type": "?",
            "optional": argument.optional
        };
        if (argument.allow_multiple) {
            input.list = true;
        }

        const comma_separated = obj.description.includes("comma-separated");
        const has_output = set_type(argument, input, comma_separated);
        descriptor['command-line'] += ' ' + template_key;
        if (has_output) {
            if (input.list) {
                input.list = false;
                // styx cant handle list output argument replacements
                // todo: promote argument to subcommand list
                console.log('Warning: promoting output argument to subcommand list ' + id + ' for ' + obj.name + ' due to list output argument replacement limitation in styx.');
            }
            descriptor['output-files'].push({
                "id": id,
                "name": id,
                "path-template": template_key,
                "description": argument.description
            });
        }

        descriptor.inputs.push(input);
    }

    // Re-add options at the end
    descriptor.inputs = descriptor.inputs.concat(option_inputs);
    descriptor['output-files'] = descriptor['output-files'].concat(option_outputs);

    return descriptor;
}

// read all json files in "json_docs\reference\commands\*.json"
const jsonPath = "json_docs/reference/commands";
const outputPath = "C:/Users/floru/Projects/cmi/nopype/descriptors/mrtrix";

// create the output directory if it does not exist
if (!fs.existsSync(outputPath)) {
    fs.mkdirSync(outputPath);
}

for (const file of fs.readdirSync(jsonPath)) {
    if (path.extname(file) !== '.json') {
        continue;
    }
    console.log(jsonPath + "/" + file);

    const json = fs.readFileSync(path.join(jsonPath, file), 'utf8');
    const obj = JSON.parse(json);

    // make the descriptor
    const descriptor = make_descriptor(obj);

    // special cases
    if (descriptor.name === 'dwi2fod') {
        descriptor.inputs[2].type = {
            "id": "response_odf",
            "name": "response_odf",
            "description": "pairs of input tissue response and output ODF images",
            "command-line": "[RESPONSE] [ODF]",
            "inputs": [
              {
                "id": "response",
                "name": "response",
                "value-key": "[RESPONSE]",
                "description": "input tissue response",
                "type": "File",
                "optional": false
              },
              {
                "id": "odf",
                "name": "odf",
                "value-key": "[ODF]",
                "description": "output ODF image",
                "type": "String",
                "optional": false
              }
            ],
            "output-files": [
              {
                "id": "odf",
                "name": "odf",
                "path-template": "[ODF]",
                "description": "output ODF image"
              }
            ]
          };
    }
    else if (descriptor.name === 'mtnormalise') {
        descriptor.inputs[0].type = {
            "id": "input_output",
            "name": "input_output",
            "description": "list of all input and output tissue compartment files (see example usage).",
            "command-line": "[INPUT] [OUTPUT]",
            "inputs": [
              {
                "id": "input",
                "name": "input",
                "value-key": "[INPUT]",
                "description": "input tissue compartment image.",
                "type": "File",
                "optional": false
              },
              {
                "id": "output",
                "name": "output",
                "value-key": "[OUTPUT]",
                "description": "output normalised tissue compartment image.",
                "type": "String",
                "optional": false
              }
            ],
            "output-files": [
              {
                "id": "output",
                "name": "output",
                "path-template": "[OUTPUT]",
                "description": "output normalised tissue compartment image."
              }
            ]
          };
    }

    console.log(" done");

    // write the descriptor to a file
    const descriptorPath = path.join(outputPath, obj.name + ".json");
    fs.writeFileSync
        (descriptorPath,
            JSON.stringify(descriptor, null, 2) + '\n',
            'utf8');
}