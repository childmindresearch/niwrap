# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_IMAGE2VTK_METADATA = Metadata(
    id="3a08bd2f36a3b28159141e1b2abc5ed50162d39d.boutiques",
    name="mris_image2vtk",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisImage2vtkOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_image2vtk(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_vtk_file: OutputPathType
    """Output VTK file generated by the conversion process"""


def mris_image2vtk(
    input_filename: InputPathType,
    output_filename: str,
    lower_threshold: float,
    upper_threshold: float,
    vtk_smoothing_iters: float,
    image_smoothing_size: float,
    reduction_percent: float,
    runner: Runner | None = None,
) -> MrisImage2vtkOutputs:
    """
    Convert image to VTK format with specified thresholds and smoothing parameters.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_filename: Input image file name.
        output_filename: Output VTK file name.
        lower_threshold: Lower threshold for image conversion.
        upper_threshold: Upper threshold for image conversion.
        vtk_smoothing_iters: Number of VTK smoothing iterations.
        image_smoothing_size: Image smoothing size.
        reduction_percent: Reduction percentage for the conversion.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisImage2vtkOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_IMAGE2VTK_METADATA)
    cargs = []
    cargs.append("mris_image2vtk")
    cargs.append(execution.input_file(input_filename))
    cargs.append(output_filename)
    cargs.append(str(lower_threshold))
    cargs.append(str(upper_threshold))
    cargs.append(str(vtk_smoothing_iters))
    cargs.append(str(image_smoothing_size))
    cargs.append(str(reduction_percent))
    ret = MrisImage2vtkOutputs(
        root=execution.output_file("."),
        output_vtk_file=execution.output_file(output_filename),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_IMAGE2VTK_METADATA",
    "MrisImage2vtkOutputs",
    "mris_image2vtk",
]