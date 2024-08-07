# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

INSTALL_IBT_DATASETS_METADATA = Metadata(
    id="8609c9fc71946a34e7ce07736528cb9c1bfa9094",
    name="Install_IBT_DATASETS",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class InstallIbtDatasetsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `install_ibt_datasets(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def install_ibt_datasets(
    wget_flag: bool = False,
    curl_flag: bool = False,
    runner: Runner | None = None,
) -> InstallIbtDatasetsOutputs:
    """
    Install_IBT_DATASETS by AFNI Team.
    
    Installs the demo archive for AFNI's macaque-analysis demo.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@Install_IBT_DATASETS.html
    
    Args:
        wget_flag: Use wget to download archive. Script chooses by default with\
            preference for curl.
        curl_flag: Use curl to download archive. Script chooses by default with\
            preference for curl.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `InstallIbtDatasetsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INSTALL_IBT_DATASETS_METADATA)
    cargs = []
    cargs.append("Install_IBT_DATASETS")
    if wget_flag:
        cargs.append("-wget")
    if curl_flag:
        cargs.append("-curl")
    ret = InstallIbtDatasetsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "INSTALL_IBT_DATASETS_METADATA",
    "InstallIbtDatasetsOutputs",
    "install_ibt_datasets",
]
