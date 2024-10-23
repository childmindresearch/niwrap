# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSL_FIX_TEXT_METADATA = Metadata(
    id="3a1a122eff10e692a02c0555487f33ce5188b31a.boutiques",
    name="fslFixText",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class FslFixTextOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_fix_text(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_text_file: OutputPathType
    """Output text file with standard UNIX line endings"""


def fsl_fix_text(
    input_text_file: InputPathType,
    output_text_file: str,
    runner: Runner | None = None,
) -> FslFixTextOutputs:
    """
    Ensures standard UNIX line endings in the output text file.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_text_file: Input text file.
        output_text_file: Output text file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslFixTextOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_FIX_TEXT_METADATA)
    cargs = []
    cargs.append("fslFixText")
    cargs.append(execution.input_file(input_text_file))
    cargs.append(output_text_file)
    ret = FslFixTextOutputs(
        root=execution.output_file("."),
        output_text_file=execution.output_file(output_text_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSL_FIX_TEXT_METADATA",
    "FslFixTextOutputs",
    "fsl_fix_text",
]
