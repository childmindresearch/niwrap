# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_MS_REFINE_METADATA = Metadata(
    id="cf2b3ea87eceab7f469060c4f74f2742bb3ca22f.boutiques",
    name="mris_ms_refine",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisMsRefineOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_ms_refine(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    white_surface: OutputPathType
    """Generated white matter surface file"""
    pial_surface: OutputPathType
    """Generated gray matter surface file"""
    curvature_file: OutputPathType
    """Curvature file for cortical thickness"""
    layer_iv_surface: OutputPathType
    """Surface file approximating layer IV of the cortical sheet"""


def mris_ms_refine(
    subject_name: str,
    hemisphere: str,
    xform: InputPathType,
    flash_files: list[InputPathType],
    residuals: InputPathType,
    omit_self_intersection: bool = False,
    create_curvature_files: bool = False,
    average_curvature: float | None = 10,
    white_only: bool = False,
    runner: Runner | None = None,
) -> MrisMsRefineOutputs:
    """
    This program positions the tessellation of the cortical surface at the white
    matter surface, then the gray matter surface. It generates surface files for
    these surfaces as well as a 'curvature' file for the cortical thickness, and a
    surface file which approximates layer IV of the cortical sheet.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: The name of the subject.
        hemisphere: The hemisphere to process ('lh' or 'rh').
        xform: The transform file.
        flash_files: Flash images.
        residuals: Residuals file.
        omit_self_intersection: Omit self-intersection and only generate\
            gray/white surface.
        create_curvature_files: Create curvature and area files from white\
            matter surface.
        average_curvature: Average curvature values a specified number of\
            times.
        white_only: Only generate white matter surface.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisMsRefineOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_MS_REFINE_METADATA)
    cargs = []
    cargs.append("mris_ms_refine")
    cargs.append(subject_name)
    cargs.append(hemisphere)
    cargs.append(execution.input_file(xform))
    cargs.extend([execution.input_file(f) for f in flash_files])
    cargs.append(execution.input_file(residuals))
    if omit_self_intersection:
        cargs.append("-q")
    if create_curvature_files:
        cargs.append("-c")
    if average_curvature is not None:
        cargs.extend([
            "-a",
            str(average_curvature)
        ])
    if white_only:
        cargs.append("-whiteonly")
    ret = MrisMsRefineOutputs(
        root=execution.output_file("."),
        white_surface=execution.output_file("<subject name>/<hemisphere>.white"),
        pial_surface=execution.output_file("<subject name>/<hemisphere>.pial"),
        curvature_file=execution.output_file("<subject name>/<hemisphere>.curv"),
        layer_iv_surface=execution.output_file("<subject name>/<hemisphere>.layerIV"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_MS_REFINE_METADATA",
    "MrisMsRefineOutputs",
    "mris_ms_refine",
]
