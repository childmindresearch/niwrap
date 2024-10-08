# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__4_DAVERAGE_METADATA = Metadata(
    id="ba3901e216b33f7527ed78d8041df8aa00991c26.boutiques",
    name="@4Daverage",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V4DaverageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__4_daverage(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__4_daverage(
    output_prefix: str,
    runner: Runner | None = None,
) -> V4DaverageOutputs:
    """
    Script for computing average 3D+time bricks using 3Dcalc.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/@4Daverage.html
    
    Args:
        output_prefix: Prefix for the output 3D+t brick.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V4DaverageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__4_DAVERAGE_METADATA)
    cargs = []
    cargs.append("@4Daverage")
    cargs.append(output_prefix)
    cargs.append("[INPUT_FILES...]")
    ret = V4DaverageOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V4DaverageOutputs",
    "V__4_DAVERAGE_METADATA",
    "v__4_daverage",
]
