# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

INSTALL_MBM_MARMOSET_METADATA = Metadata(
    id="2327a5e2de45f4f986bd00b298d6a23ede32654a",
    name="Install_MBM_Marmoset",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class InstallMbmMarmosetOutputs(typing.NamedTuple):
    """
    Output object returned when calling `install_mbm_marmoset(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def install_mbm_marmoset(
    wget: bool = False,
    curl: bool = False,
    runner: Runner | None = None,
) -> InstallMbmMarmosetOutputs:
    """
    Install_MBM_Marmoset by AFNI Team.
    
    Installs the NIH marmoset template and atlases.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@Install_MBM_Marmoset.html
    
    Args:
        wget: Use wget to download archive. Script chooses by default with\
            preference for curl.
        curl: Use curl to download archive. Script chooses by default with\
            preference for curl.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `InstallMbmMarmosetOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INSTALL_MBM_MARMOSET_METADATA)
    cargs = []
    cargs.append("@Install_MBM_Marmoset")
    if wget:
        cargs.append("-wget")
    if curl:
        cargs.append("-curl")
    ret = InstallMbmMarmosetOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "INSTALL_MBM_MARMOSET_METADATA",
    "InstallMbmMarmosetOutputs",
    "install_mbm_marmoset",
]
