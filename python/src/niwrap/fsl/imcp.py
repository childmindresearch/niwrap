# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

IMCP_METADATA = Metadata(
    id="94e6449f7e297fbc91d61628d282d1e78df28b82.boutiques",
    name="imcp",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class ImcpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `imcp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfiles: OutputPathType
    """Output file or directory"""


def imcp(
    infiles: list[InputPathType],
    output_location: str,
    runner: Runner | None = None,
) -> ImcpOutputs:
    """
    Copy images from one location to another.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        infiles: Input image files (e.g. img1.nii.gz, img2.nii.gz).
        output_location: Output file or directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImcpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMCP_METADATA)
    cargs = []
    cargs.append("imcp")
    cargs.extend([execution.input_file(f) for f in infiles])
    cargs.append(output_location)
    ret = ImcpOutputs(
        root=execution.output_file("."),
        outfiles=execution.output_file(output_location),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "IMCP_METADATA",
    "ImcpOutputs",
    "imcp",
]
