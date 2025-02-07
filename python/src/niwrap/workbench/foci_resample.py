# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FOCI_RESAMPLE_METADATA = Metadata(
    id="d25e8eee3893055f474c3819282ad3f943c97a1d.boutiques",
    name="foci-resample",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
FociResampleLeftSurfacesParameters = typing.TypedDict('FociResampleLeftSurfacesParameters', {
    "__STYX_TYPE__": typing.Literal["left_surfaces"],
    "current_surf": InputPathType,
    "new_surf": InputPathType,
})
FociResampleRightSurfacesParameters = typing.TypedDict('FociResampleRightSurfacesParameters', {
    "__STYX_TYPE__": typing.Literal["right_surfaces"],
    "current_surf": InputPathType,
    "new_surf": InputPathType,
})
FociResampleCerebellumSurfacesParameters = typing.TypedDict('FociResampleCerebellumSurfacesParameters', {
    "__STYX_TYPE__": typing.Literal["cerebellum_surfaces"],
    "current_surf": InputPathType,
    "new_surf": InputPathType,
})
FociResampleParameters = typing.TypedDict('FociResampleParameters', {
    "__STYX_TYPE__": typing.Literal["foci-resample"],
    "foci_in": InputPathType,
    "foci_out": str,
    "left_surfaces": typing.NotRequired[FociResampleLeftSurfacesParameters | None],
    "right_surfaces": typing.NotRequired[FociResampleRightSurfacesParameters | None],
    "cerebellum_surfaces": typing.NotRequired[FociResampleCerebellumSurfacesParameters | None],
    "opt_discard_distance_from_surface": bool,
    "opt_restore_xyz": bool,
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
        "foci-resample": foci_resample_cargs,
        "left_surfaces": foci_resample_left_surfaces_cargs,
        "right_surfaces": foci_resample_right_surfaces_cargs,
        "cerebellum_surfaces": foci_resample_cerebellum_surfaces_cargs,
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
        "foci-resample": foci_resample_outputs,
        "left_surfaces": foci_resample_left_surfaces_outputs,
        "right_surfaces": foci_resample_right_surfaces_outputs,
        "cerebellum_surfaces": foci_resample_cerebellum_surfaces_outputs,
    }.get(t)


def foci_resample_left_surfaces_params(
    current_surf: InputPathType,
    new_surf: InputPathType,
) -> FociResampleLeftSurfacesParameters:
    """
    Build parameters.
    
    Args:
        current_surf: the surface the foci are currently projected on.
        new_surf: the surface to project the foci onto.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "left_surfaces",
        "current_surf": current_surf,
        "new_surf": new_surf,
    }
    return params


def foci_resample_left_surfaces_cargs(
    params: FociResampleLeftSurfacesParameters,
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
    cargs.append("-left-surfaces")
    cargs.append(execution.input_file(params.get("current_surf")))
    cargs.append(execution.input_file(params.get("new_surf")))
    return cargs


def foci_resample_right_surfaces_params(
    current_surf: InputPathType,
    new_surf: InputPathType,
) -> FociResampleRightSurfacesParameters:
    """
    Build parameters.
    
    Args:
        current_surf: the surface the foci are currently projected on.
        new_surf: the surface to project the foci onto.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "right_surfaces",
        "current_surf": current_surf,
        "new_surf": new_surf,
    }
    return params


def foci_resample_right_surfaces_cargs(
    params: FociResampleRightSurfacesParameters,
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
    cargs.append("-right-surfaces")
    cargs.append(execution.input_file(params.get("current_surf")))
    cargs.append(execution.input_file(params.get("new_surf")))
    return cargs


def foci_resample_cerebellum_surfaces_params(
    current_surf: InputPathType,
    new_surf: InputPathType,
) -> FociResampleCerebellumSurfacesParameters:
    """
    Build parameters.
    
    Args:
        current_surf: the surface the foci are currently projected on.
        new_surf: the surface to project the foci onto.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cerebellum_surfaces",
        "current_surf": current_surf,
        "new_surf": new_surf,
    }
    return params


def foci_resample_cerebellum_surfaces_cargs(
    params: FociResampleCerebellumSurfacesParameters,
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
    cargs.append("-cerebellum-surfaces")
    cargs.append(execution.input_file(params.get("current_surf")))
    cargs.append(execution.input_file(params.get("new_surf")))
    return cargs


class FociResampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `foci_resample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    foci_out: OutputPathType
    """the output foci file"""


def foci_resample_params(
    foci_in: InputPathType,
    foci_out: str,
    left_surfaces: FociResampleLeftSurfacesParameters | None = None,
    right_surfaces: FociResampleRightSurfacesParameters | None = None,
    cerebellum_surfaces: FociResampleCerebellumSurfacesParameters | None = None,
    opt_discard_distance_from_surface: bool = False,
    opt_restore_xyz: bool = False,
) -> FociResampleParameters:
    """
    Build parameters.
    
    Args:
        foci_in: the input foci file.
        foci_out: the output foci file.
        left_surfaces: the left surfaces for resampling.
        right_surfaces: the right surfaces for resampling.
        cerebellum_surfaces: the cerebellum surfaces for resampling.
        opt_discard_distance_from_surface: ignore the distance the foci are\
            above or below the current surface.
        opt_restore_xyz: put the original xyz coordinates into the foci, rather\
            than the coordinates obtained from unprojection.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "foci-resample",
        "foci_in": foci_in,
        "foci_out": foci_out,
        "opt_discard_distance_from_surface": opt_discard_distance_from_surface,
        "opt_restore_xyz": opt_restore_xyz,
    }
    if left_surfaces is not None:
        params["left_surfaces"] = left_surfaces
    if right_surfaces is not None:
        params["right_surfaces"] = right_surfaces
    if cerebellum_surfaces is not None:
        params["cerebellum_surfaces"] = cerebellum_surfaces
    return params


def foci_resample_cargs(
    params: FociResampleParameters,
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
    cargs.append("wb_command")
    cargs.append("-foci-resample")
    cargs.append(execution.input_file(params.get("foci_in")))
    cargs.append(params.get("foci_out"))
    if params.get("left_surfaces") is not None:
        cargs.extend(dyn_cargs(params.get("left_surfaces")["__STYXTYPE__"])(params.get("left_surfaces"), execution))
    if params.get("right_surfaces") is not None:
        cargs.extend(dyn_cargs(params.get("right_surfaces")["__STYXTYPE__"])(params.get("right_surfaces"), execution))
    if params.get("cerebellum_surfaces") is not None:
        cargs.extend(dyn_cargs(params.get("cerebellum_surfaces")["__STYXTYPE__"])(params.get("cerebellum_surfaces"), execution))
    if params.get("opt_discard_distance_from_surface"):
        cargs.append("-discard-distance-from-surface")
    if params.get("opt_restore_xyz"):
        cargs.append("-restore-xyz")
    return cargs


def foci_resample_outputs(
    params: FociResampleParameters,
    execution: Execution,
) -> FociResampleOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FociResampleOutputs(
        root=execution.output_file("."),
        foci_out=execution.output_file(params.get("foci_out")),
    )
    return ret


def foci_resample_execute(
    params: FociResampleParameters,
    execution: Execution,
) -> FociResampleOutputs:
    """
    Project foci to a different surface.
    
    Unprojects foci from the <current-surf> for the structure, then projects
    them to <new-surf>. If the foci have meaningful distances above or below the
    surface, use anatomical surfaces. If the foci should be on the surface, use
    registered spheres and the options -discard-distance-from-surface and
    -restore-xyz.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FociResampleOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = foci_resample_cargs(params, execution)
    ret = foci_resample_outputs(params, execution)
    execution.run(cargs)
    return ret


def foci_resample(
    foci_in: InputPathType,
    foci_out: str,
    left_surfaces: FociResampleLeftSurfacesParameters | None = None,
    right_surfaces: FociResampleRightSurfacesParameters | None = None,
    cerebellum_surfaces: FociResampleCerebellumSurfacesParameters | None = None,
    opt_discard_distance_from_surface: bool = False,
    opt_restore_xyz: bool = False,
    runner: Runner | None = None,
) -> FociResampleOutputs:
    """
    Project foci to a different surface.
    
    Unprojects foci from the <current-surf> for the structure, then projects
    them to <new-surf>. If the foci have meaningful distances above or below the
    surface, use anatomical surfaces. If the foci should be on the surface, use
    registered spheres and the options -discard-distance-from-surface and
    -restore-xyz.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        foci_in: the input foci file.
        foci_out: the output foci file.
        left_surfaces: the left surfaces for resampling.
        right_surfaces: the right surfaces for resampling.
        cerebellum_surfaces: the cerebellum surfaces for resampling.
        opt_discard_distance_from_surface: ignore the distance the foci are\
            above or below the current surface.
        opt_restore_xyz: put the original xyz coordinates into the foci, rather\
            than the coordinates obtained from unprojection.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FociResampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FOCI_RESAMPLE_METADATA)
    params = foci_resample_params(foci_in=foci_in, foci_out=foci_out, left_surfaces=left_surfaces, right_surfaces=right_surfaces, cerebellum_surfaces=cerebellum_surfaces, opt_discard_distance_from_surface=opt_discard_distance_from_surface, opt_restore_xyz=opt_restore_xyz)
    return foci_resample_execute(params, execution)


__all__ = [
    "FOCI_RESAMPLE_METADATA",
    "FociResampleCerebellumSurfacesParameters",
    "FociResampleLeftSurfacesParameters",
    "FociResampleOutputs",
    "FociResampleParameters",
    "FociResampleRightSurfacesParameters",
    "foci_resample",
    "foci_resample_cerebellum_surfaces_params",
    "foci_resample_left_surfaces_params",
    "foci_resample_params",
    "foci_resample_right_surfaces_params",
]
