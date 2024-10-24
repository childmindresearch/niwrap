# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DMRIRC_EXAMPLE_METADATA = Metadata(
    id="826786cb87aa325721cea94d4b8ca2bed3f5b212.boutiques",
    name="dmrirc.example",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class DmrircExampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dmrirc_example(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def dmrirc_example(
    runner: Runner | None = None,
) -> DmrircExampleOutputs:
    """
    Example script for DTI processing in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DmrircExampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DMRIRC_EXAMPLE_METADATA)
    cargs = []
    cargs.append("dmrirc.example")
    cargs.append("[ARGS]")
    ret = DmrircExampleOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DMRIRC_EXAMPLE_METADATA",
    "DmrircExampleOutputs",
    "dmrirc_example",
]
