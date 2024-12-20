# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_SMOOTH_INTRACORTICAL_METADATA = Metadata(
    id="2d913141d3a964703c9f9e1365f71235771f5c17.boutiques",
    name="mris_smooth_intracortical",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisSmoothIntracorticalOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_smooth_intracortical(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_overlay: OutputPathType | None
    """Output overlay file."""


def mris_smooth_intracortical(
    surf_dir: str,
    surf_name: str,
    overlay_dir: str,
    overlay_name: str,
    output_dir: str | None = "[OVERLAY_DIR]",
    output_name: str | None = None,
    tan_size: int | None = None,
    rad_size: float | None = None,
    rad_start: float | None = None,
    tan_weights: str | None = None,
    runner: Runner | None = None,
) -> MrisSmoothIntracorticalOutputs:
    """
    Smooths data overlaid onto cortical surface meshes using specified tangential
    and radial extents.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surf_dir: Directory with surface meshes.
        surf_name: Name of a surface file(s). Use * and ? to pass multiple\
            names (max 20).
        overlay_dir: Directory with surface mesh overlays.
        overlay_name: Name of an overlay file(s). Use * and ? to pass multiple\
            names (max 20).
        output_dir: Path to the output directory. Default is same as overlay\
            directory.
        output_name: Name of the output overlay file.
        tan_size: Tangential extent of the smoothing kernel. Default = 0, Max =\
            6.
        rad_size: Radial extent of the intracortical smoothing kernel.
        rad_start: Starting surface mesh of the intracortical smoothing kernel\
            in the radial direction.
        tan_weights: Weighting function for tangential smoothing. 'gauss' or\
            'distance'.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisSmoothIntracorticalOutputs`).
    """
    if tan_size is not None and not (0 <= tan_size <= 6): 
        raise ValueError(f"'tan_size' must be between 0 <= x <= 6 but was {tan_size}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_SMOOTH_INTRACORTICAL_METADATA)
    cargs = []
    cargs.append("mris_smooth_intracortical")
    cargs.extend([
        "--surf_dir",
        surf_dir
    ])
    cargs.extend([
        "--surf_name",
        surf_name
    ])
    cargs.extend([
        "--overlay_dir",
        overlay_dir
    ])
    cargs.extend([
        "--overlay_name",
        overlay_name
    ])
    if output_dir is not None:
        cargs.extend([
            "--output_dir",
            "[" + output_dir + "]"
        ])
    if output_name is not None:
        cargs.extend([
            "--output_name",
            "[" + output_name + "]"
        ])
    if tan_size is not None:
        cargs.extend([
            "--tan-size",
            "[" + str(tan_size) + "]"
        ])
    if rad_size is not None:
        cargs.extend([
            "--rad-size",
            "[" + str(rad_size) + "]"
        ])
    if rad_start is not None:
        cargs.extend([
            "--rad-start",
            "[" + str(rad_start) + "]"
        ])
    if tan_weights is not None:
        cargs.extend([
            "--tan-weights",
            "[" + tan_weights + "]"
        ])
    ret = MrisSmoothIntracorticalOutputs(
        root=execution.output_file("."),
        output_overlay=execution.output_file(output_dir + "/" + output_name) if (output_dir is not None and output_name is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_SMOOTH_INTRACORTICAL_METADATA",
    "MrisSmoothIntracorticalOutputs",
    "mris_smooth_intracortical",
]
