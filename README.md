> [!NOTE]  
> In early development and is not yet ready for production use.

# CPAC Boutiques Descriptor Collection

This repository contains a collection of Boutiques descriptors for all command line brain imaging tools called by C-PAC. The descriptors are stored in the `descriptors` directory and are organized by the brain imaging software framework they belong to.

## Python package

Install the `niwrap` Python package to use the generated Python wrappers.

See the [niwrap Python package README](./python/README.md) for more installation instructions and usage information.

## Style guide

### Output file prefixes

Hardcode the output file names/prefixes in the descriptor.

Exposing the output file prefixes as inputs in the descriptor will result in meaningless verbosity of the interface. Users will grab the output file paths from the output tuple so there is no value in being able to change them.

Don't do this:

```json
{
    "command-line": "tool [IN] [OUT]",
    "inputs": [{
        "id": "output_file_prefix",
        "type": "string",
        "value-key": "[OUT]",
        "command-line-flag": "-o",
        "optional": false
    }],
    "output-files": [{
        "id": "output_file",
        "path-template": "[OUT].nii.gz"
    }]
}
```

Do this:

```json
{
    "command-line": "tool [IN] -o out",
    "output-files": [{
        "id": "output_file",
        "path-template": "out.nii.gz"
    }]
}
```

## VSCode JSON schema

Add the following entry to your `./.vscode/settings.json` file to enable in-editor JSON schema validation for this project for VSCode.

```json
{
    "json.schemas": [
        {
            "fileMatch": [
                "descriptors/**/*.json"
            ],
            "url": "./schemas/descriptor.schema.json"
        }
    ]
}
```

## Helpful resources

- [Greg's Intro to Boutiques slideshow](https://docs.google.com/presentation/d/17ktohcT1iH6MX1DNklljlHnNaD8YH8u-FauKuopmugY/edit?usp=sharing)
- [Flo's Boutiques Tutorial slideshow](https://docs.google.com/presentation/d/1pVjWzubcoY1WuE0g09xV6K8yx7asklMGJKyMS2rDZ_w/edit?usp=sharing)
- [Boutiques documentation](https://boutiques.github.io/)
- [Boutiques schema](https://github.com/boutiques/boutiques/blob/master/boutiques/schema/descriptor.schema.json)
- [FSL help pages](https://childmindresearch.github.io/help-pages-fsl/)
- [FSL wiki](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki)
- [Freesurfer wiki](https://surfer.nmr.mgh.harvard.edu/fswiki)
- [AFNI documentation](https://afni.nimh.nih.gov/pub/dist/doc/htmldoc/index.html)
