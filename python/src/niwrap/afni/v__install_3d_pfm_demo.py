# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

INSTALL_3D_PFM_DEMO_METADATA = Metadata(
    id="eee949a22334c9cd763bb1acd0d5e3e7918b016d",
    name="Install_3dPFM_Demo",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class Install3dPfmDemoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `install_3d_pfm_demo(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    readme_file: OutputPathType
    """Instructions for demo usage"""


def install_3d_pfm_demo(
    output_directory: str,
    runner: Runner | None = None,
) -> Install3dPfmDemoOutputs:
    """
    Install_3dPFM_Demo by AFNI Team.
    
    Installs the demo archive for the 3dPFM function.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@Install_3dPFM_Demo.html
    
    Args:
        output_directory: Output directory where the demo archive will be\
            downloaded and unpacked.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Install3dPfmDemoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INSTALL_3D_PFM_DEMO_METADATA)
    cargs = []
    cargs.append("Install_3dPFM_Demo")
    cargs.append(output_directory)
    ret = Install3dPfmDemoOutputs(
        root=execution.output_file("."),
        readme_file=execution.output_file(f"{output_directory}/README.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "INSTALL_3D_PFM_DEMO_METADATA",
    "Install3dPfmDemoOutputs",
    "install_3d_pfm_demo",
]
