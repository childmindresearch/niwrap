# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_THRESHOLD_METADATA = Metadata(
    id="18dd783d6c61c6360f3439c48e74d88d1a862887.boutiques",
    name="mri_threshold",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriThresholdOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_threshold(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_vol_file: OutputPathType
    """Thresholded output volume"""


def mri_threshold(
    input_vol: InputPathType,
    threshold: float,
    output_vol: str,
    binarize: float | None = None,
    upper_threshold: bool = False,
    frame_number: float | None = None,
    runner: Runner | None = None,
) -> MriThresholdOutputs:
    """
    This program will lower threshold an input volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_vol: Input volume file.
        threshold: Threshold value for the volume.
        output_vol: Output volume file.
        binarize: Binarize the output volume with specified bval.
        upper_threshold: Upper threshold the volume instead of lower\
            thresholding.
        frame_number: Apply thresholding to a specific frame indexed by fnum.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriThresholdOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_THRESHOLD_METADATA)
    cargs = []
    cargs.append("mri_threshold")
    cargs.append(execution.input_file(input_vol))
    cargs.append(str(threshold))
    cargs.append(output_vol)
    if binarize is not None:
        cargs.extend([
            "-B",
            str(binarize)
        ])
    if upper_threshold:
        cargs.append("-U")
    if frame_number is not None:
        cargs.extend([
            "-F",
            str(frame_number)
        ])
    ret = MriThresholdOutputs(
        root=execution.output_file("."),
        output_vol_file=execution.output_file(output_vol),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_THRESHOLD_METADATA",
    "MriThresholdOutputs",
    "mri_threshold",
]
