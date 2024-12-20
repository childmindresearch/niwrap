# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_REFINE_SEG_METADATA = Metadata(
    id="cb7729fa49160d260ecc58552917a2760053175e.boutiques",
    name="mri_refine_seg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriRefineSegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_refine_seg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    refined_output: OutputPathType
    """Refined segmentation output file."""


def mri_refine_seg(
    input_segmentation: InputPathType,
    output_segmentation: str,
    debug: bool = False,
    runner: Runner | None = None,
) -> MriRefineSegOutputs:
    """
    Refines a messy segmentation by recoding stray voxels.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_segmentation: Input segmentation file.
        output_segmentation: Refined segmentation output name.
        debug: Save the original segmentation, a mask of the refined voxels,\
            and a pointset of the refined clusters to the output directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriRefineSegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_REFINE_SEG_METADATA)
    cargs = []
    cargs.append("mri_refine_seg")
    cargs.extend([
        "-i",
        execution.input_file(input_segmentation)
    ])
    cargs.extend([
        "-o",
        output_segmentation
    ])
    if debug:
        cargs.append("--debug")
    ret = MriRefineSegOutputs(
        root=execution.output_file("."),
        refined_output=execution.output_file(output_segmentation),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_REFINE_SEG_METADATA",
    "MriRefineSegOutputs",
    "mri_refine_seg",
]
