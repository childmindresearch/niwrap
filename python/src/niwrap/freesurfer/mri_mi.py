# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_MI_METADATA = Metadata(
    id="a8192108178632d862688e0dfe4e9538ca88d9ad.boutiques",
    name="mri_mi",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriMiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_mi(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_mi(
    input_file1: InputPathType,
    input_file2: InputPathType,
    bins: str | None = None,
    silent: bool = False,
    runner: Runner | None = None,
) -> MriMiOutputs:
    """
    Computes mutual information (mi) between two input volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file1: First input file name.
        input_file2: Second input file name.
        bins: Specifies the number of bins for the two input volumes. Default\
            is 64x64.
        silent: Write out only the final mutual information result.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriMiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_MI_METADATA)
    cargs = []
    cargs.append("mri_mi")
    cargs.append(execution.input_file(input_file1))
    cargs.append(execution.input_file(input_file2))
    if bins is not None:
        cargs.extend([
            "--bins",
            bins
        ])
    if silent:
        cargs.append("--silent")
    ret = MriMiOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_MI_METADATA",
    "MriMiOutputs",
    "mri_mi",
]
