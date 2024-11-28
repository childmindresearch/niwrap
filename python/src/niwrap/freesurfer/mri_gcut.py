# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_GCUT_METADATA = Metadata(
    id="2d7a317ffc88d0aa0b30756aff0cdbaa297fc3a1.boutiques",
    name="mri_gcut",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriGcutOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_gcut(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_mask_file: OutputPathType
    """The output file containing the skull-stripped brain volume."""


def mri_gcut(
    infile: InputPathType,
    outfile: str,
    wmmask_110: bool = False,
    mult_file: InputPathType | None = None,
    threshold_value: float | None = None,
    runner: Runner | None = None,
) -> MriGcutOutputs:
    """
    Skull stripping algorithm based on graph cuts.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        infile: Input brain volume file, e.g. T1.mgz.
        outfile: Output file name, e.g. brainmask.auto.mgz.
        wmmask_110: Use voxels with intensity 110 as white matter mask (when\
            applied on T1.mgz, FreeSurfer only).
        mult_file: Intersect the skull-stripped 'in_filename' and an existing\
            skull-stripped volume specified by 'filename', storing the result in\
            'out_filename'.
        threshold_value: Set threshold to value (%) of WM intensity, where the\
            value should be >0 and <1; defaults to 0.40.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriGcutOutputs`).
    """
    if threshold_value is not None and not (0 <= threshold_value <= 1): 
        raise ValueError(f"'threshold_value' must be between 0 <= x <= 1 but was {threshold_value}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_GCUT_METADATA)
    cargs = []
    cargs.append("mri_gcut")
    if wmmask_110:
        cargs.append("-110")
    if mult_file is not None:
        cargs.extend([
            "-mult",
            execution.input_file(mult_file)
        ])
    if threshold_value is not None:
        cargs.extend([
            "-T",
            str(threshold_value)
        ])
    cargs.append(execution.input_file(infile))
    cargs.append(outfile)
    ret = MriGcutOutputs(
        root=execution.output_file("."),
        output_mask_file=execution.output_file(outfile),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_GCUT_METADATA",
    "MriGcutOutputs",
    "mri_gcut",
]
