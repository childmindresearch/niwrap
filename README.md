
# NiWrap <img src="logo.png" align="right" width="25%"/>

NiWrap is an extensive collection of neuroimaging command line tool metadata used for generating modern, ideomatic Python wrappers.

Metadata is partly hand-written and partly extracted from existing tools.

NiWrap is based on the Boutiques Descriptor Schema and powered by the Styx Boutiques-to-Python compiler.

## Supported frameworks

| Framework | Approach | Status | Coverage |
| --- | --- | --- | --- |
| AFNI | Manual | In progress | ?% (?/?) |
| ANTs | Manual | In progress | ?% (?/?) |
| Convert3D | Manual | In progress | ?% (?/?) |
| FSL | Manual | In progress | ?% (?/?) |
| Freesurfer | Manual | In progress | ?% (?/?) |
| MRtrix3 | Source extration | Testing | 100% (112/112) |
| Connectome Workbench | Source extraction | Testing | 100% (202/202) |

## Repository structure

| Directory | Description |
| --- | --- |
| `/descriptors` | Boutiques descriptors |
| `/schemas` | JSON schema for Boutiques descriptors |
| `/python` | Generated `niwrap` Python package |
| `/extraction` | Source metadata extraction |

## Python package

Install the `niwrap` Python package to use the generated Python wrappers.

See the [niwrap Python package README](./python/README.md) for installation instructions and usage information.

## Contributing

See the [CONTRIBUTING.md](./CONTRIBUTING.md) file for information on how to contribute to NiWrap.
