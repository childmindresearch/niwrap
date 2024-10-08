# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__INSTALL_MACAQUE_DEMO_METADATA = Metadata(
    id="861d78308cd21c85f350630038319cdae517c027.boutiques",
    name="@Install_MACAQUE_DEMO",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VInstallMacaqueDemoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__install_macaque_demo(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__install_macaque_demo(
    wget: bool = False,
    curl: bool = False,
    runner: Runner | None = None,
) -> VInstallMacaqueDemoOutputs:
    """
    Installs the demo archive for AFNI's macaque-analysis demo.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@Install_MACAQUE_DEMO.html
    
    Args:
        wget: Use wget to download archive. Script chooses by default with\
            preference for curl.
        curl: Use curl to download archive. Script chooses by default with\
            preference for curl.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VInstallMacaqueDemoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__INSTALL_MACAQUE_DEMO_METADATA)
    cargs = []
    cargs.append("Install_MACAQUE_DEMO")
    if wget:
        cargs.append("-wget")
    if curl:
        cargs.append("-curl")
    ret = VInstallMacaqueDemoOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VInstallMacaqueDemoOutputs",
    "V__INSTALL_MACAQUE_DEMO_METADATA",
    "v__install_macaque_demo",
]
