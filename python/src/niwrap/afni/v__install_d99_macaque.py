# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V__INSTALL_D99_MACAQUE_METADATA = Metadata(
    id="026f9857534ab285e688283f3be2563144e7b8b2",
    name="@Install_D99_macaque",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VInstallD99MacaqueOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__install_d99_macaque(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    readme_file: OutputPathType
    """Readme file with details about the installed atlas."""
    atlas_files: OutputPathType
    """Installed D99 macaque version 2 atlas files."""


def v__install_d99_macaque(
    wget_download: bool = False,
    curl_download: bool = False,
    runner: Runner | None = None,
) -> VInstallD99MacaqueOutputs:
    """
    @Install_D99_macaque by AFNI Team.
    
    Installs the D99 macaque version 2 atlases for subcortical regions in the
    macaque monkey.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@Install_D99_macaque.html
    
    Args:
        wget_download: Use wget to download archive. Script chooses by default\
            with preference for curl.
        curl_download: Use curl to download archive. Script chooses by default\
            with preference for curl.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VInstallD99MacaqueOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__INSTALL_D99_MACAQUE_METADATA)
    cargs = []
    cargs.append("@Install_D99_macaque")
    if wget_download:
        cargs.append("-wget")
    if curl_download:
        cargs.append("-curl")
    ret = VInstallD99MacaqueOutputs(
        root=execution.output_file("."),
        readme_file=execution.output_file(f"README.txt", optional=True),
        atlas_files=execution.output_file(f"D99_macaque_v2/*", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VInstallD99MacaqueOutputs",
    "V__INSTALL_D99_MACAQUE_METADATA",
    "v__install_d99_macaque",
]
