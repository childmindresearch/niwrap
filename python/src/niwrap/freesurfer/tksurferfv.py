# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TKSURFERFV_METADATA = Metadata(
    id="5f6c49af2e657ea2532d217b90ff0a44fe817bc6.boutiques",
    name="tksurferfv",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
TksurferfvParameters = typing.TypedDict('TksurferfvParameters', {
    "__STYX_TYPE__": typing.Literal["tksurferfv"],
    "subject": str,
    "hemi": str,
    "surface": str,
    "tksurfer": bool,
    "all_surfaces": bool,
    "vgl": bool,
    "no_vgl": bool,
    "no_outline": bool,
    "neuro_orientation": bool,
    "rotate_around_cursor": bool,
    "heat_scale": typing.NotRequired[str | None],
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
        "tksurferfv": tksurferfv_cargs,
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
    }.get(t)


class TksurferfvOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tksurferfv(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def tksurferfv_params(
    subject: str,
    hemi: str,
    surface: str,
    tksurfer: bool = False,
    all_surfaces: bool = False,
    vgl: bool = False,
    no_vgl: bool = False,
    no_outline: bool = False,
    neuro_orientation: bool = False,
    rotate_around_cursor: bool = False,
    heat_scale: str | None = "min_to_max",
) -> TksurferfvParameters:
    """
    Build parameters.
    
    Args:
        subject: Subject identifier.
        hemi: Hemisphere (e.g., lh or rh).
        surface: Surface type.
        tksurfer: Use tksurfer instead of freeview.
        all_surfaces: Load white, pial, and inflated surfaces.
        vgl: Run freeview with /usr/pubsw/bin/vglrun.
        no_vgl: Do not run freeview with /usr/pubsw/bin/vglrun.
        no_outline: Do not show annotations as outlines.
        neuro_orientation: Use neurological orientation instead of\
            radiological.
        rotate_around_cursor: Rotate around cursor in 3D view.
        heat_scale: Overlay heat scale (options: linear, linearopaque,\
            piecewise, min_to_max).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "tksurferfv",
        "subject": subject,
        "hemi": hemi,
        "surface": surface,
        "tksurfer": tksurfer,
        "all_surfaces": all_surfaces,
        "vgl": vgl,
        "no_vgl": no_vgl,
        "no_outline": no_outline,
        "neuro_orientation": neuro_orientation,
        "rotate_around_cursor": rotate_around_cursor,
    }
    if heat_scale is not None:
        params["heat_scale"] = heat_scale
    return params


def tksurferfv_cargs(
    params: TksurferfvParameters,
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
    cargs.append("tksurferfv")
    cargs.append(params.get("subject"))
    cargs.append(params.get("hemi"))
    cargs.append(params.get("surface"))
    if params.get("tksurfer"):
        cargs.append("-tksurfer")
    if params.get("all_surfaces"):
        cargs.append("-all")
    if params.get("vgl"):
        cargs.append("-vgl")
    if params.get("no_vgl"):
        cargs.append("-no-vgl")
    if params.get("no_outline"):
        cargs.append("-no-outline")
    if params.get("neuro_orientation"):
        cargs.append("-neuro")
    if params.get("rotate_around_cursor"):
        cargs.append("-rca")
    if params.get("heat_scale") is not None:
        cargs.append(params.get("heat_scale"))
    return cargs


def tksurferfv_outputs(
    params: TksurferfvParameters,
    execution: Execution,
) -> TksurferfvOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TksurferfvOutputs(
        root=execution.output_file("."),
    )
    return ret


def tksurferfv_execute(
    params: TksurferfvParameters,
    execution: Execution,
) -> TksurferfvOutputs:
    """
    A script that runs freeview with arguments similar to tksurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TksurferfvOutputs`).
    """
    params = execution.params(params)
    cargs = tksurferfv_cargs(params, execution)
    ret = tksurferfv_outputs(params, execution)
    execution.run(cargs)
    return ret


def tksurferfv(
    subject: str,
    hemi: str,
    surface: str,
    tksurfer: bool = False,
    all_surfaces: bool = False,
    vgl: bool = False,
    no_vgl: bool = False,
    no_outline: bool = False,
    neuro_orientation: bool = False,
    rotate_around_cursor: bool = False,
    heat_scale: str | None = "min_to_max",
    runner: Runner | None = None,
) -> TksurferfvOutputs:
    """
    A script that runs freeview with arguments similar to tksurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject identifier.
        hemi: Hemisphere (e.g., lh or rh).
        surface: Surface type.
        tksurfer: Use tksurfer instead of freeview.
        all_surfaces: Load white, pial, and inflated surfaces.
        vgl: Run freeview with /usr/pubsw/bin/vglrun.
        no_vgl: Do not run freeview with /usr/pubsw/bin/vglrun.
        no_outline: Do not show annotations as outlines.
        neuro_orientation: Use neurological orientation instead of\
            radiological.
        rotate_around_cursor: Rotate around cursor in 3D view.
        heat_scale: Overlay heat scale (options: linear, linearopaque,\
            piecewise, min_to_max).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TksurferfvOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TKSURFERFV_METADATA)
    params = tksurferfv_params(subject=subject, hemi=hemi, surface=surface, tksurfer=tksurfer, all_surfaces=all_surfaces, vgl=vgl, no_vgl=no_vgl, no_outline=no_outline, neuro_orientation=neuro_orientation, rotate_around_cursor=rotate_around_cursor, heat_scale=heat_scale)
    return tksurferfv_execute(params, execution)


__all__ = [
    "TKSURFERFV_METADATA",
    "TksurferfvOutputs",
    "TksurferfvParameters",
    "tksurferfv",
    "tksurferfv_params",
]
