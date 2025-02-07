# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_SMOOTH_INTRACORTICAL_METADATA = Metadata(
    id="2d913141d3a964703c9f9e1365f71235771f5c17.boutiques",
    name="mris_smooth_intracortical",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisSmoothIntracorticalParameters = typing.TypedDict('MrisSmoothIntracorticalParameters', {
    "__STYX_TYPE__": typing.Literal["mris_smooth_intracortical"],
    "surf_dir": str,
    "surf_name": str,
    "overlay_dir": str,
    "overlay_name": str,
    "output_dir": typing.NotRequired[str | None],
    "output_name": typing.NotRequired[str | None],
    "tan_size": typing.NotRequired[int | None],
    "rad_size": typing.NotRequired[float | None],
    "rad_start": typing.NotRequired[float | None],
    "tan_weights": typing.NotRequired[str | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "mris_smooth_intracortical": mris_smooth_intracortical_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "mris_smooth_intracortical": mris_smooth_intracortical_outputs,
    }.get(t)


class MrisSmoothIntracorticalOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_smooth_intracortical(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_overlay: OutputPathType | None
    """Output overlay file."""


def mris_smooth_intracortical_params(
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
) -> MrisSmoothIntracorticalParameters:
    """
    Build parameters.
    
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
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_smooth_intracortical",
        "surf_dir": surf_dir,
        "surf_name": surf_name,
        "overlay_dir": overlay_dir,
        "overlay_name": overlay_name,
    }
    if output_dir is not None:
        params["output_dir"] = output_dir
    if output_name is not None:
        params["output_name"] = output_name
    if tan_size is not None:
        params["tan_size"] = tan_size
    if rad_size is not None:
        params["rad_size"] = rad_size
    if rad_start is not None:
        params["rad_start"] = rad_start
    if tan_weights is not None:
        params["tan_weights"] = tan_weights
    return params


def mris_smooth_intracortical_cargs(
    params: MrisSmoothIntracorticalParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("mris_smooth_intracortical")
    cargs.extend([
        "--surf_dir",
        params.get("surf_dir")
    ])
    cargs.extend([
        "--surf_name",
        params.get("surf_name")
    ])
    cargs.extend([
        "--overlay_dir",
        params.get("overlay_dir")
    ])
    cargs.extend([
        "--overlay_name",
        params.get("overlay_name")
    ])
    if params.get("output_dir") is not None:
        cargs.extend([
            "--output_dir",
            "[" + params.get("output_dir") + "]"
        ])
    if params.get("output_name") is not None:
        cargs.extend([
            "--output_name",
            "[" + params.get("output_name") + "]"
        ])
    if params.get("tan_size") is not None:
        cargs.extend([
            "--tan-size",
            "[" + str(params.get("tan_size")) + "]"
        ])
    if params.get("rad_size") is not None:
        cargs.extend([
            "--rad-size",
            "[" + str(params.get("rad_size")) + "]"
        ])
    if params.get("rad_start") is not None:
        cargs.extend([
            "--rad-start",
            "[" + str(params.get("rad_start")) + "]"
        ])
    if params.get("tan_weights") is not None:
        cargs.extend([
            "--tan-weights",
            "[" + params.get("tan_weights") + "]"
        ])
    return cargs


def mris_smooth_intracortical_outputs(
    params: MrisSmoothIntracorticalParameters,
    execution: Execution,
) -> MrisSmoothIntracorticalOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisSmoothIntracorticalOutputs(
        root=execution.output_file("."),
        output_overlay=execution.output_file(params.get("output_dir") + "/" + params.get("output_name")) if (params.get("output_dir") is not None and params.get("output_name") is not None) else None,
    )
    return ret


def mris_smooth_intracortical_execute(
    params: MrisSmoothIntracorticalParameters,
    execution: Execution,
) -> MrisSmoothIntracorticalOutputs:
    """
    Smooths data overlaid onto cortical surface meshes using specified tangential
    and radial extents.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisSmoothIntracorticalOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_smooth_intracortical_cargs(params, execution)
    ret = mris_smooth_intracortical_outputs(params, execution)
    execution.run(cargs)
    return ret


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
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_SMOOTH_INTRACORTICAL_METADATA)
    params = mris_smooth_intracortical_params(surf_dir=surf_dir, surf_name=surf_name, overlay_dir=overlay_dir, overlay_name=overlay_name, output_dir=output_dir, output_name=output_name, tan_size=tan_size, rad_size=rad_size, rad_start=rad_start, tan_weights=tan_weights)
    return mris_smooth_intracortical_execute(params, execution)


__all__ = [
    "MRIS_SMOOTH_INTRACORTICAL_METADATA",
    "MrisSmoothIntracorticalOutputs",
    "MrisSmoothIntracorticalParameters",
    "mris_smooth_intracortical",
    "mris_smooth_intracortical_params",
]
