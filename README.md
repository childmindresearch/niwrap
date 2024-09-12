
# NiWrap <img src="logo.png" align="right" width="25%"/>

NiWrap is an extensive collection of neuroimaging command line tool metadata used for generating modern, ideomatic Python wrappers.

Metadata is partly hand-written and partly extracted from the source code of the tools themselves.
NiWrap is based on the [Boutiques Descriptor Schema](https://github.com/boutiques/boutiques) and powered by the [Styx Boutiques-to-Python compiler](https://github.com/childmindresearch/styx).

## Supported packages

<!-- START_PACKAGES_TABLE -->

| Package | Status | Version | API Coverage |
| --- | --- | --- | --- |
| [AFNI](https://afni.nimh.nih.gov/) | In progress | [`AFNI_24.2.06`](https://hub.docker.com/r/afni/afni_make_build) | 561/621 (90.3%) |
| [ANTs](https://github.com/ANTsX/ANTs) | In progress | [`v2.5.3`](https://hub.docker.com/r/antsx/ants) | 9/120 (7.5%) |
| [Connectome Workbench](https://github.com/Washington-University/workbench) | Testing | [`1.5.0-freesurfer-update`](https://hub.docker.com/r/brainlife/connectome_workbench) | 202/202 (100% 🎉) |
| [Convert3D](http://www.itksnap.org/pmwiki/pmwiki.php?n=Convert3D.Convert3D) | In progress | [`v3.8.2`](https://hub.docker.com/r/pyushkevich/itksnap) | 2/4 (50.0%) |
| [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki) | In progress | [`6.0.5`](https://hub.docker.com/r/mcin/fsl) | 221/376 (58.8%) |
| [FreeSurfer](https://github.com/freesurfer/freesurfer) | In progress | [`7.4.1`](https://hub.docker.com/r/freesurfer/freesurfer) | 2/104 (1.9%) |
| [Greedy](https://sites.google.com/view/greedyreg/about) | In progress | [`v3.8.2`](https://hub.docker.com/r/pyushkevich/itksnap) | 1/1 (100% 🎉) |
| [MRTrix3](https://www.mrtrix.org/) | Testing | [`3.0.4`](https://hub.docker.com/r/mrtrix3/mrtrix3) | 116/125 (92.8%) |
| [NiftyReg](http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg) | In progress | [`20220819`](https://hub.docker.com/r/vnmd/niftyreg_1.4.0) | 7/7 (100% 🎉) |

<!-- END_PACKAGES_TABLE -->

> [!NOTE] 
> *API Coverage* is defined as the percentage of individual binaries for which a descriptor is available in NiWrap. This is not a measure of the completeness of the descriptors themselves nor is reaching 100% strictly necessary as e.g. FSL and AFNI contain many small utilities for which Python offers much easier standard library functions. One way to increase coverage is to mark known-irrelevant binaries as `"status": "ignore"` in `packages/`.

## Repository structure

| Directory | Description |
| --- | --- |
| `/descriptors` | Boutiques descriptors |
| `/schemas` | JSON schema for Boutiques descriptors |
| `/python` | Generated `niwrap` Python package |
| `/extraction` | Source metadata extraction |
| `/packages` | Package-specific metadata |

## Python package

Install the `niwrap` Python package to use the generated Python wrappers.

See the [niwrap Python package README](./python/README.md) for installation instructions and usage information.

## Contributing

See the [CONTRIBUTING.md](./CONTRIBUTING.md) file for information on how to contribute to NiWrap.
































