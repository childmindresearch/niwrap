# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

INSTALL_NIH_MARMOSET_METADATA = Metadata(
    id="d2f2dac7258e2499a64b704625be9a44e218e7a2",
    name="Install_NIH_Marmoset",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class InstallNihMarmosetOutputs(typing.NamedTuple):
    """
    Output object returned when calling `install_nih_marmoset(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def install_nih_marmoset(
    wget: bool = False,
    curl: bool = False,
    runner: Runner | None = None,
) -> InstallNihMarmosetOutputs:
    """
    Install_NIH_Marmoset by AFNI Team.
    
    Installs the NIH marmoset template and atlases.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@Install_NIH_Marmoset.html
    
    Args:
        wget: Use wget to download archive. Script chooses by default with\
            preference for curl.
        curl: Use curl to download archive. Script chooses by default with\
            preference for curl.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `InstallNihMarmosetOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INSTALL_NIH_MARMOSET_METADATA)
    cargs = []
    cargs.append("@Install_NIH_Marmoset")
    if wget:
        cargs.append("-wget")
    if curl:
        cargs.append("-curl")
    ret = InstallNihMarmosetOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "INSTALL_NIH_MARMOSET_METADATA",
    "InstallNihMarmosetOutputs",
    "install_nih_marmoset",
]
