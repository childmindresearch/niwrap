# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_EULER_NUMBER_METADATA = Metadata(
    id="0ad5734919ffe0fbdc78eddad073fdf8082b2ef3.boutiques",
    name="mris_euler_number",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisEulerNumberOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_euler_number(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType | None
    """File where the number of holes is written"""


def mris_euler_number(
    input_surface: InputPathType,
    output_file: str | None = None,
    runner: Runner | None = None,
) -> MrisEulerNumberOutputs:
    """
    This program computes EulerNumber for a cortical surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: Input surface file.
        output_file: Write number of holes to output file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisEulerNumberOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_EULER_NUMBER_METADATA)
    cargs = []
    cargs.append("mris_euler_number")
    cargs.append(execution.input_file(input_surface))
    if output_file is not None:
        cargs.extend([
            "-o",
            output_file
        ])
    ret = MrisEulerNumberOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(output_file) if (output_file is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_EULER_NUMBER_METADATA",
    "MrisEulerNumberOutputs",
    "mris_euler_number",
]
