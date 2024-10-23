# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSLORIENT_METADATA = Metadata(
    id="4a390fd943cefbf5c66914c99ef4a58956833f7f.boutiques",
    name="fslorient",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class FslorientOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslorient(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fslorient(
    filename: InputPathType,
    swap_orient: bool = False,
    runner: Runner | None = None,
) -> FslorientOutputs:
    """
    FSL tool to manipulate NIfTI header orientation information.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        filename: Filename of the image to operate on (e.g. img.nii.gz).
        swap_orient: Swaps FSL radiological and FSL neurological.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslorientOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLORIENT_METADATA)
    cargs = []
    cargs.append("fslorient")
    if swap_orient:
        cargs.append("-swaporient")
    cargs.append(execution.input_file(filename))
    ret = FslorientOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLORIENT_METADATA",
    "FslorientOutputs",
    "fslorient",
]
