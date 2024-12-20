# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSLMODHD_METADATA = Metadata(
    id="4d79af63e716050570a42ab303ea6efb6b7d6d71.boutiques",
    name="fslmodhd",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class FslmodhdOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslmodhd(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fslmodhd(
    image: InputPathType,
    keyword_: str,
    value: str,
    runner: Runner | None = None,
) -> FslmodhdOutputs:
    """
    A tool for modifying header information of NIfTI images.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        image: Input image file (e.g. image.nii.gz).
        keyword_: Header keyword to modify (e.g. 'dim', 'pixdim').
        value: New value for the given header keyword.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslmodhdOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLMODHD_METADATA)
    cargs = []
    cargs.append("fslmodhd")
    cargs.append(execution.input_file(image))
    cargs.append(keyword_)
    cargs.append(value)
    ret = FslmodhdOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLMODHD_METADATA",
    "FslmodhdOutputs",
    "fslmodhd",
]
