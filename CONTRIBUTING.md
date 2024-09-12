# Contributing to NiWrap

> [!WARNING]
> Contributing Guidelines are a work in progress.

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
