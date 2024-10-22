# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

INSTALL_INSTA_CORR_DEMO_METADATA = Metadata(
    id="e1895643d8f47b7d5e0eaf075bdeed5156edf2bb.boutiques",
    name="Install_InstaCorr_Demo",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class InstallInstaCorrDemoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `install_insta_corr_demo(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def install_insta_corr_demo(
    wget: bool = False,
    curl: bool = False,
    full: bool = False,
    mini: bool = False,
    runner: Runner | None = None,
) -> InstallInstaCorrDemoOutputs:
    """
    Installs and sets up AFNI's InstaCorr demo archive.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        wget: Use wget to download archive. Script chooses by default with\
            preference for curl.
        curl: Use curl to download archive. Script chooses by default with\
            preference for curl.
        full: Install the full version of the demo. Downloads all subject\
            surfaces, resting state volume time series, etc. The script processes\
            the data and produces the files needed for running the various\
            interactive InstaCorr demos.
        mini: Install the mini version of the demo. Downloads only the files\
            needed for running the various interactive InstaCorr demos.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `InstallInstaCorrDemoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INSTALL_INSTA_CORR_DEMO_METADATA)
    cargs = []
    cargs.append("@Install_InstaCorr_Demo")
    if wget:
        cargs.append("-wget")
    if curl:
        cargs.append("-curl")
    if full:
        cargs.append("-full")
    if mini:
        cargs.append("-mini")
    ret = InstallInstaCorrDemoOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "INSTALL_INSTA_CORR_DEMO_METADATA",
    "InstallInstaCorrDemoOutputs",
    "install_insta_corr_demo",
]