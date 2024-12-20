# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TALAIRACH_MGH_METADATA = Metadata(
    id="470f9a508abcecfbd0c30650fa66adee5d4d661f.boutiques",
    name="talairach_mgh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class TalairachMghOutputs(typing.NamedTuple):
    """
    Output object returned when calling `talairach_mgh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    transformed_output: OutputPathType
    """Transformed output volume aligned with Talairach reference brain"""


def talairach_mgh(
    input_volume: InputPathType,
    output_volume: str,
    runner: Runner | None = None,
) -> TalairachMghOutputs:
    """
    A tool for aligning brain volume with Talairach reference brain.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume file for the talairach transformation.
        output_volume: Output volume file for the talairach transformation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TalairachMghOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TALAIRACH_MGH_METADATA)
    cargs = []
    cargs.append("talairach_mgh")
    cargs.append(execution.input_file(input_volume))
    cargs.append(output_volume)
    ret = TalairachMghOutputs(
        root=execution.output_file("."),
        transformed_output=execution.output_file(output_volume),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TALAIRACH_MGH_METADATA",
    "TalairachMghOutputs",
    "talairach_mgh",
]
