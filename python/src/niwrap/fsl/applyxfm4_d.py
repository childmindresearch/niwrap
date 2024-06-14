# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

APPLYXFM4_D_METADATA = Metadata(
    id="e23b3d7680990ca17bc457d7c3c766a1e5b11934",
    name="applyxfm4D",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class Applyxfm4DOutputs(typing.NamedTuple):
    """
    Output object returned when calling `applyxfm4_d(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Transformed 4D volume output"""


def applyxfm4_d(
    input_volume: InputPathType,
    ref_volume: InputPathType,
    output_volume: str,
    transformation_matrix: str,
    interpolation_method: str | None = "sinc",
    single_matrix_flag: bool = False,
    four_digit_flag: bool = False,
    user_prefix: str | None = None,
    runner: Runner = None,
) -> Applyxfm4DOutputs:
    """
    applyxfm4D by Unknown.
    
    Applies 4D transformation matrices to 4D volumes.
    
    Args:
        input_volume: Input 4D volume (e.g. img.nii.gz).
        ref_volume: Reference volume (e.g. ref.nii.gz).
        output_volume: Output volume after applying transformation (e.g.\
            output.nii.gz).
        transformation_matrix: Transformation matrix file or directory.
        interpolation_method: Interpolation method; options are\
            nearestneighbour (or nn), trilinear, spline, sinc; default is sinc.
        single_matrix_flag: Flag to specify a single transformation matrix.
        four_digit_flag: Flag to use four digits in naming files.
        user_prefix: User-defined prefix for output files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Applyxfm4DOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(APPLYXFM4_D_METADATA)
    cargs = []
    cargs.append("applyxfm4D")
    cargs.append(execution.input_file(input_volume))
    cargs.append(execution.input_file(ref_volume))
    cargs.append(output_volume)
    cargs.append(transformation_matrix)
    ret = Applyxfm4DOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"{output_volume}.nii.gz", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "APPLYXFM4_D_METADATA",
    "Applyxfm4DOutputs",
    "applyxfm4_d",
]