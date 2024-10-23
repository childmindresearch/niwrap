
# NiWrap <img src="logo.png" align="right" width="25%"/>

🧠 Modern Python wrappers for neuroimaging tools


## 🚀 Features

- Extensive collection of neuroimaging command line tool metadata
- Generates idiomatic Python wrappers for popular neuroimaging tools
- Based on [Boutiques Descriptor Schema](https://github.com/boutiques/boutiques)
- Powered by [Styx compiler](https://github.com/childmindresearch/styx)

## 🧰 Supported Packages

<!-- START_PACKAGES_TABLE -->

| Package | Status | Version | API Coverage |
| --- | --- | --- | --- |
| [AFNI](https://afni.nimh.nih.gov/) | In progress | [`24.2.06`](https://hub.docker.com/r/afni/afni_make_build) | 532/658 (80.9%) |
| [ANTs](https://github.com/ANTsX/ANTs) | In progress | [`2.5.3`](https://hub.docker.com/r/antsx/ants) | 71/113 (62.8%) |
| [Connectome Workbench](https://github.com/Washington-University/workbench) | Testing | [`1.5.0`](https://hub.docker.com/r/brainlife/connectome_workbench) | 202/202 (100% 🎉) |
| [Convert3D](http://www.itksnap.org/pmwiki/pmwiki.php?n=Convert3D.Convert3D) | In progress | [`1.1.0`](https://hub.docker.com/r/pyushkevich/itksnap) | 2/4 (50.0%) |
| [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki) | In progress | [`6.0.5`](https://hub.docker.com/r/mcin/fsl) | 254/338 (75.1%) |
| [FreeSurfer](https://github.com/freesurfer/freesurfer) | In progress | [`7.4.1`](https://hub.docker.com/r/freesurfer/freesurfer) | 713/806 (88.5%) |
| [Greedy](https://sites.google.com/view/greedyreg/about) | In progress | [`1.0.1`](https://hub.docker.com/r/pyushkevich/itksnap) | 1/1 (100% 🎉) |
| [MRTrix3](https://www.mrtrix.org/) | Testing | [`3.0.4`](https://hub.docker.com/r/mrtrix3/mrtrix3) | 117/125 (93.6%) |
| [MRTrix3Tissue](https://3tissue.github.io/) | Testing | [`5.2.8`](https://hub.docker.com/r/brainlife/3tissue) | 1/1 (100% 🎉) |
| [NiftyReg](http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg) | In progress | [`1.4.0`](https://hub.docker.com/r/vnmd/niftyreg_1.4.0) | 7/7 (100% 🎉) |

<!-- END_PACKAGES_TABLE -->

> 📊 **API Coverage Explained**
> - Represents the percentage of tool binaries with available NiWrap descriptors
> - Does not indicate descriptor completeness
> - 100% coverage isn't always necessary (e.g., some FSL/AFNI utilities have Python stdlib equivalents)
> - To improve coverage:
>   - Add missing descriptor in `descriptors/`
>   - Mark irrelevant binaries as `"status": "ignore"` in `packages/`

## 🗂 Repository Structure

```
niwrap/
├── descriptors/    # Boutiques descriptors
├── schemas/        # JSON schema for Boutiques descriptors
├── python/         # Generated niwrap Python package
├── extraction/     # Source metadata extraction
└── packages/       # Package-specific metadata
```

## 🐍 [Python Package](https://github.com/childmindresearch/niwrap/blob/main/python/README.md)

Install the `niwrap` Python package to use the generated wrappers:

```bash
pip install niwrap
```

See the [NiWrap Python package readme](https://github.com/childmindresearch/niwrap/blob/main/python/README.md) for more details.

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](./CONTRIBUTING.md) for ways to get started.


## 📄 License

The NiWrap project itself, including all metadata and generated Python wrappers, is licensed under the MIT License. See the LICENSE file for details.

> **⚠️ Important**: The neuroimaging tools wrapped by NiWrap each have their own licenses. Using NiWrap does not grant any rights to use these tools beyond what their respective licenses allow. Users are responsible for complying with the licenses of the underlying tools they use through NiWrap.

## 🙋‍♀️ Support

For support, please open an issue in the [GitHub issue tracker](https://github.com/childmindresearch/niwrap/issues).
