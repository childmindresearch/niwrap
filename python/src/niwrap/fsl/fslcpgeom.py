# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSLCPGEOM_METADATA = Metadata(
    id="abfea41c33a7487bc5c6fba058aaad8f45e8d06a.boutiques",
    name="fslcpgeom",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class FslcpgeomOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslcpgeom(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fslcpgeom(
    source_file: InputPathType,
    destination_file: InputPathType,
    dimensions_flag: bool = False,
    runner: Runner | None = None,
) -> FslcpgeomOutputs:
    """
    FSL tool to copy image geometry from one file to another.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        source_file: Source image file (e.g. img1.nii.gz).
        destination_file: Destination image file (e.g. img2.nii.gz).
        dimensions_flag: Don't copy image dimensions.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslcpgeomOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLCPGEOM_METADATA)
    cargs = []
    cargs.append("fslcpgeom")
    cargs.append(execution.input_file(source_file))
    cargs.append(execution.input_file(destination_file))
    if dimensions_flag:
        cargs.append("-d")
    ret = FslcpgeomOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLCPGEOM_METADATA",
    "FslcpgeomOutputs",
    "fslcpgeom",
]
