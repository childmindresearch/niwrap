# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

APPLYWARP_METADATA = Metadata(
    id="feff959ede39bc32c46956ed391232146e709478.boutiques",
    name="applywarp",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class ApplywarpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `applywarp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    warped_output_file: OutputPathType
    """Warped output image"""


def applywarp(
    input_file: InputPathType,
    output_file: str,
    reference_file: InputPathType,
    warp_coeff_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> ApplywarpOutputs:
    """
    Apply a warp to an image using FSL's applywarp utility.
    
    Author: University of Oxford (Jesper Andersson)
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FNIRT/Applywarp
    
    Args:
        input_file: Filename of input image (to be warped).
        output_file: Filename for output (warped) image.
        reference_file: Filename for reference image.
        warp_coeff_file: Filename for warp/coefficient (volume).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ApplywarpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(APPLYWARP_METADATA)
    cargs = []
    cargs.append("applywarp")
    cargs.append("-i")
    cargs.extend([
        "-i",
        execution.input_file(input_file)
    ])
    cargs.append("-o")
    cargs.extend([
        "-o",
        output_file
    ])
    cargs.append("-r")
    cargs.extend([
        "-r",
        execution.input_file(reference_file)
    ])
    cargs.append("-w")
    if warp_coeff_file is not None:
        cargs.extend([
            "-w",
            execution.input_file(warp_coeff_file)
        ])
    cargs.append("--usesqform")
    ret = ApplywarpOutputs(
        root=execution.output_file("."),
        warped_output_file=execution.output_file(output_file + ".nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "APPLYWARP_METADATA",
    "ApplywarpOutputs",
    "applywarp",
]
