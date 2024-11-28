# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

PERFUSION_SUBTRACT_METADATA = Metadata(
    id="8a0b5c252cd2198e9f3ba22398f35e5e42e86246.boutiques",
    name="perfusion_subtract",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class PerfusionSubtractOutputs(typing.NamedTuple):
    """
    Output object returned when calling `perfusion_subtract(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output 4D image with subtraction results"""


def perfusion_subtract(
    four_d_input: InputPathType,
    four_d_output: str,
    control_first_flag: bool = False,
    runner: Runner | None = None,
) -> PerfusionSubtractOutputs:
    """
    Subtract control images from tag images in 4D perfusion data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        four_d_input: Input 4D perfusion image (e.g. perfusion.nii.gz).
        four_d_output: Output 4D image with subtraction results (e.g.\
            perfusion_subtracted.nii.gz).
        control_first_flag: First timepoint is control instead of tag. Default\
            is tag first.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PerfusionSubtractOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PERFUSION_SUBTRACT_METADATA)
    cargs = []
    cargs.append("perfusion_subtract")
    cargs.append(execution.input_file(four_d_input))
    cargs.append(four_d_output)
    if control_first_flag:
        cargs.append("-c")
    ret = PerfusionSubtractOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(four_d_output + ".nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "PERFUSION_SUBTRACT_METADATA",
    "PerfusionSubtractOutputs",
    "perfusion_subtract",
]
