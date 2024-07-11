
# NiWrap <img src="logo.png" align="right" width="25%"/>

NiWrap is an extensive collection of neuroimaging command line tool metadata used for generating modern, ideomatic Python wrappers.

Metadata is partly hand-written and partly extracted from the source code of the tools themselves.
NiWrap is based on the [Boutiques Descriptor Schema](https://github.com/boutiques/boutiques) and powered by the [Styx Boutiques-to-Python compiler](https://github.com/childmindresearch/styx).

## Supported frameworks

<!-- START_FRAMEWORKS_TABLE -->

| Framework | Approach | Status | API Coverage |
| --- | --- | --- | --- |
| [AFNI](https://afni.nimh.nih.gov/) | Manual | In progress | 23/621 (3.7%) |
| [ANTs](https://github.com/ANTsX/ANTs) | Manual | In progress | 9/120 (7.5%) |
| [Connectome Workbench](https://github.com/Washington-University/workbench) | Source extraction | Testing | 202/202 (100% 🎉) |
| [Convert3D](http://www.itksnap.org/pmwiki/pmwiki.php?n=Convert3D.Convert3D) | Manual | In progress | 2/4 (50.0%) |
| [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki) | Manual | In progress | 221/376 (58.8%) |
| [FreeSurfer](https://github.com/freesurfer/freesurfer) | Manual | In progress | 2/104 (1.9%) |
| [MRTrix3](https://www.mrtrix.org/) | Source extraction | Testing | 116/125 (92.8%) |
| [NiftyReg](http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg) | Manual | In progress | 7/7 (100% 🎉) |

<!-- END_FRAMEWORKS_TABLE -->

> [!NOTE] 
> *API Coverage* is defined as the percentage of individual binaries for which a descriptor is available in NiWrap. This is not a measure of the completeness of the descriptors themselves nor is reaching 100% strictly necessary as e.g. FSL and AFNI contain many small utilities for which Python offers much easier standard library functions. One way to increase coverage is to mark known-irrelevant binaries as `"status": "ignore"` in `frameworks/`.

## Repository structure

| Directory | Description |
| --- | --- |
| `/descriptors` | Boutiques descriptors |
| `/schemas` | JSON schema for Boutiques descriptors |
| `/python` | Generated `niwrap` Python package |
| `/extraction` | Source metadata extraction |
| `/frameworks` | Framework-specific metadata |

## Python package

Install the `niwrap` Python package to use the generated Python wrappers.

See the [niwrap Python package README](./python/README.md) for installation instructions and usage information.

## Contributing

See the [CONTRIBUTING.md](./CONTRIBUTING.md) file for information on how to contribute to NiWrap.




















