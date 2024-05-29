# MRTrix3 metadata extraction

## Build

Build `buildenv.Dockerfile`, then run or use devcontainer:

```json
{
    "image": "mrtrix_buildenv:latest"
}
```

Build MRTrix3:

```bash
./configure
./build
```

## Extract metadata

```bash
./generate_json_docs.sh
node mrt2bt.js
```

## Implementation details

All changes are in `extraction\mrtrix\source\core\app.cpp`.
