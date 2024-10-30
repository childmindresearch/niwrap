# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_CONCATENATE_GCAM_METADATA = Metadata(
    id="fd466778d5618f979eb973c0e7ee2af83aa44e4d.boutiques",
    name="mri_concatenate_gcam",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriConcatenateGcamOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_concatenate_gcam(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Composite LTA or M3Z transform, depending on input."""


def mri_concatenate_gcam(
    inputs: list[InputPathType],
    output: str,
    source_image: InputPathType | None = None,
    target_image: InputPathType | None = None,
    reduce: bool = False,
    invert: bool = False,
    downsample: bool = False,
    runner: Runner | None = None,
) -> MriConcatenateGcamOutputs:
    """
    Concatenate a combination of input LTAs (linear transform array) and GCAMs
    (Gaussian classifier atlas, M3Z).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        inputs: Combination of input LTAs and M3Zs.
        output: Concatenated output transform, saved as an LTA or M3Z depending\
            on the input transforms.
        source_image: Change source image geometry of output M3Z, useful for\
            GCAM inversion if the path of the original source volume changed.
        target_image: Change destination image geometry of output M3Z.
        reduce: Reduce output LTA to single LT.
        invert: Invert the output transform.
        downsample: Downsample output M3Z to spacing of 2; by default, the\
            output spacing is that of the rightmost input M3Z.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriConcatenateGcamOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_CONCATENATE_GCAM_METADATA)
    cargs = []
    cargs.append("mri_concatenate_gcam")
    cargs.extend([execution.input_file(f) for f in inputs])
    cargs.append(output)
    if source_image is not None:
        cargs.extend([
            "-s",
            execution.input_file(source_image)
        ])
    if target_image is not None:
        cargs.extend([
            "-t",
            execution.input_file(target_image)
        ])
    if reduce:
        cargs.append("-r")
    if invert:
        cargs.append("-i")
    if downsample:
        cargs.append("-d")
    ret = MriConcatenateGcamOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(output),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_CONCATENATE_GCAM_METADATA",
    "MriConcatenateGcamOutputs",
    "mri_concatenate_gcam",
]