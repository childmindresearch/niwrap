# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSR_GETXOPTS_METADATA = Metadata(
    id="224fcae72cefe1195f88d86eb1986d98d2293a58.boutiques",
    name="fsr-getxopts",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class FsrGetxoptsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsr_getxopts(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fsr_getxopts(
    help_: bool = False,
    runner: Runner | None = None,
) -> FsrGetxoptsOutputs:
    """
    Tool to retrieve extended options for a specific context or configuration.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        help_: Display the help message and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FsrGetxoptsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSR_GETXOPTS_METADATA)
    cargs = []
    cargs.append("fsr-getxopts")
    if help_:
        cargs.append("--help")
    ret = FsrGetxoptsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSR_GETXOPTS_METADATA",
    "FsrGetxoptsOutputs",
    "fsr_getxopts",
]
