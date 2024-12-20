# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_THICKNESS_METADATA = Metadata(
    id="1f70790c09e2a07e9627e797f2437c49106bcce2.boutiques",
    name="mris_thickness",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisThicknessOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_thickness(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_thickness_file: OutputPathType
    """Output curvature file containing thickness measurements."""


def mris_thickness(
    subject_name: str,
    hemi: str,
    thickness_file: str,
    max_threshold: float | None = None,
    fill_holes: list[str] | None = None,
    thickness_from_seg: list[str] | None = None,
    vector: bool = False,
    runner: Runner | None = None,
) -> MrisThicknessOutputs:
    """
    Measures the thickness of the cortical surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: The subject name for processing.
        hemi: The hemisphere to process (e.g., lh or rh).
        thickness_file: Output file for thickness measurements.
        max_threshold: Use a maximum threshold for thickness (default is 5mm).
        fill_holes: Fill in thickness in holes in the cortex label using\
            fsaverage cortex label.
        thickness_from_seg: Compute thickness from segmentation. Requires the\
            following parameters: surf label, seg.mgz, dmaxmm, ddeltamm, and\
            output.mgz.
        vector: Compute the thickness using a variationally derived vector\
            field.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisThicknessOutputs`).
    """
    if fill_holes is not None and (len(fill_holes) != 2): 
        raise ValueError(f"Length of 'fill_holes' must be 2 but was {len(fill_holes)}")
    if thickness_from_seg is not None and (len(thickness_from_seg) != 5): 
        raise ValueError(f"Length of 'thickness_from_seg' must be 5 but was {len(thickness_from_seg)}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_THICKNESS_METADATA)
    cargs = []
    cargs.append("mris_thickness")
    cargs.append(subject_name)
    cargs.append(hemi)
    cargs.append(thickness_file)
    if max_threshold is not None:
        cargs.extend([
            "-max",
            str(max_threshold)
        ])
    if fill_holes is not None:
        cargs.extend([
            "-fill_holes",
            *fill_holes
        ])
    if thickness_from_seg is not None:
        cargs.extend([
            "-thickness-from-seg",
            *thickness_from_seg
        ])
    if vector:
        cargs.append("-vector")
    ret = MrisThicknessOutputs(
        root=execution.output_file("."),
        output_thickness_file=execution.output_file(thickness_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_THICKNESS_METADATA",
    "MrisThicknessOutputs",
    "mris_thickness",
]
