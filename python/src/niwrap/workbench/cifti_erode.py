# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CIFTI_ERODE_METADATA = Metadata(
    id="bc74c026585faa5731c32e77b9b8935b7ad2dc76.boutiques",
    name="cifti-erode",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
CiftiErodeLeftSurfaceParameters = typing.TypedDict('CiftiErodeLeftSurfaceParameters', {
    "__STYX_TYPE__": typing.Literal["left_surface"],
    "surface": InputPathType,
    "opt_left_corrected_areas_area_metric": typing.NotRequired[InputPathType | None],
})
CiftiErodeRightSurfaceParameters = typing.TypedDict('CiftiErodeRightSurfaceParameters', {
    "__STYX_TYPE__": typing.Literal["right_surface"],
    "surface": InputPathType,
    "opt_right_corrected_areas_area_metric": typing.NotRequired[InputPathType | None],
})
CiftiErodeCerebellumSurfaceParameters = typing.TypedDict('CiftiErodeCerebellumSurfaceParameters', {
    "__STYX_TYPE__": typing.Literal["cerebellum_surface"],
    "surface": InputPathType,
    "opt_cerebellum_corrected_areas_area_metric": typing.NotRequired[InputPathType | None],
})
CiftiErodeParameters = typing.TypedDict('CiftiErodeParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-erode"],
    "cifti_in": InputPathType,
    "direction": str,
    "surface_distance": float,
    "volume_distance": float,
    "cifti_out": str,
    "left_surface": typing.NotRequired[CiftiErodeLeftSurfaceParameters | None],
    "right_surface": typing.NotRequired[CiftiErodeRightSurfaceParameters | None],
    "cerebellum_surface": typing.NotRequired[CiftiErodeCerebellumSurfaceParameters | None],
    "opt_merged_volume": bool,
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
        "cifti-erode": cifti_erode_cargs,
        "left_surface": cifti_erode_left_surface_cargs,
        "right_surface": cifti_erode_right_surface_cargs,
        "cerebellum_surface": cifti_erode_cerebellum_surface_cargs,
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
        "cifti-erode": cifti_erode_outputs,
        "left_surface": cifti_erode_left_surface_outputs,
        "right_surface": cifti_erode_right_surface_outputs,
        "cerebellum_surface": cifti_erode_cerebellum_surface_outputs,
    }.get(t)


def cifti_erode_left_surface_params(
    surface: InputPathType,
    opt_left_corrected_areas_area_metric: InputPathType | None = None,
) -> CiftiErodeLeftSurfaceParameters:
    """
    Build parameters.
    
    Args:
        surface: the left surface file.
        opt_left_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the left surface: the corrected vertex areas, as a\
            metric.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "left_surface",
        "surface": surface,
    }
    if opt_left_corrected_areas_area_metric is not None:
        params["opt_left_corrected_areas_area_metric"] = opt_left_corrected_areas_area_metric
    return params


def cifti_erode_left_surface_cargs(
    params: CiftiErodeLeftSurfaceParameters,
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
    cargs.append("-left-surface")
    cargs.append(execution.input_file(params.get("surface")))
    if params.get("opt_left_corrected_areas_area_metric") is not None:
        cargs.extend([
            "-left-corrected-areas",
            execution.input_file(params.get("opt_left_corrected_areas_area_metric"))
        ])
    return cargs


def cifti_erode_right_surface_params(
    surface: InputPathType,
    opt_right_corrected_areas_area_metric: InputPathType | None = None,
) -> CiftiErodeRightSurfaceParameters:
    """
    Build parameters.
    
    Args:
        surface: the right surface file.
        opt_right_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the right surface: the corrected vertex areas, as a\
            metric.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "right_surface",
        "surface": surface,
    }
    if opt_right_corrected_areas_area_metric is not None:
        params["opt_right_corrected_areas_area_metric"] = opt_right_corrected_areas_area_metric
    return params


def cifti_erode_right_surface_cargs(
    params: CiftiErodeRightSurfaceParameters,
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
    cargs.append("-right-surface")
    cargs.append(execution.input_file(params.get("surface")))
    if params.get("opt_right_corrected_areas_area_metric") is not None:
        cargs.extend([
            "-right-corrected-areas",
            execution.input_file(params.get("opt_right_corrected_areas_area_metric"))
        ])
    return cargs


def cifti_erode_cerebellum_surface_params(
    surface: InputPathType,
    opt_cerebellum_corrected_areas_area_metric: InputPathType | None = None,
) -> CiftiErodeCerebellumSurfaceParameters:
    """
    Build parameters.
    
    Args:
        surface: the cerebellum surface file.
        opt_cerebellum_corrected_areas_area_metric: vertex areas to use instead\
            of computing them from the cerebellum surface: the corrected vertex\
            areas, as a metric.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cerebellum_surface",
        "surface": surface,
    }
    if opt_cerebellum_corrected_areas_area_metric is not None:
        params["opt_cerebellum_corrected_areas_area_metric"] = opt_cerebellum_corrected_areas_area_metric
    return params


def cifti_erode_cerebellum_surface_cargs(
    params: CiftiErodeCerebellumSurfaceParameters,
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
    cargs.append("-cerebellum-surface")
    cargs.append(execution.input_file(params.get("surface")))
    if params.get("opt_cerebellum_corrected_areas_area_metric") is not None:
        cargs.extend([
            "-cerebellum-corrected-areas",
            execution.input_file(params.get("opt_cerebellum_corrected_areas_area_metric"))
        ])
    return cargs


class CiftiErodeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_erode(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_erode_params(
    cifti_in: InputPathType,
    direction: str,
    surface_distance: float,
    volume_distance: float,
    cifti_out: str,
    left_surface: CiftiErodeLeftSurfaceParameters | None = None,
    right_surface: CiftiErodeRightSurfaceParameters | None = None,
    cerebellum_surface: CiftiErodeCerebellumSurfaceParameters | None = None,
    opt_merged_volume: bool = False,
) -> CiftiErodeParameters:
    """
    Build parameters.
    
    Args:
        cifti_in: the input cifti file.
        direction: which dimension to dilate along, ROW or COLUMN.
        surface_distance: the distance to dilate on surfaces, in mm.
        volume_distance: the distance to dilate in the volume, in mm.
        cifti_out: the output cifti file.
        left_surface: specify the left surface to use.
        right_surface: specify the right surface to use.
        cerebellum_surface: specify the cerebellum surface to use.
        opt_merged_volume: treat volume components as if they were a single\
            component.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-erode",
        "cifti_in": cifti_in,
        "direction": direction,
        "surface_distance": surface_distance,
        "volume_distance": volume_distance,
        "cifti_out": cifti_out,
        "opt_merged_volume": opt_merged_volume,
    }
    if left_surface is not None:
        params["left_surface"] = left_surface
    if right_surface is not None:
        params["right_surface"] = right_surface
    if cerebellum_surface is not None:
        params["cerebellum_surface"] = cerebellum_surface
    return params


def cifti_erode_cargs(
    params: CiftiErodeParameters,
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
    cargs.append("-cifti-erode")
    cargs.append(execution.input_file(params.get("cifti_in")))
    cargs.append(params.get("direction"))
    cargs.append(str(params.get("surface_distance")))
    cargs.append(str(params.get("volume_distance")))
    cargs.append(params.get("cifti_out"))
    if params.get("left_surface") is not None:
        cargs.extend(dyn_cargs(params.get("left_surface")["__STYXTYPE__"])(params.get("left_surface"), execution))
    if params.get("right_surface") is not None:
        cargs.extend(dyn_cargs(params.get("right_surface")["__STYXTYPE__"])(params.get("right_surface"), execution))
    if params.get("cerebellum_surface") is not None:
        cargs.extend(dyn_cargs(params.get("cerebellum_surface")["__STYXTYPE__"])(params.get("cerebellum_surface"), execution))
    if params.get("opt_merged_volume"):
        cargs.append("-merged-volume")
    return cargs


def cifti_erode_outputs(
    params: CiftiErodeParameters,
    execution: Execution,
) -> CiftiErodeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiErodeOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(params.get("cifti_out")),
    )
    return ret


def cifti_erode_execute(
    params: CiftiErodeParameters,
    execution: Execution,
) -> CiftiErodeOutputs:
    """
    Erode a cifti file.
    
    For all data values that are empty (for label data, unlabeled, for other
    data, zero), set the surrounding values to empty. The surrounding values are
    defined as the immediate neighbors and all values in the same structure
    within the specified distance (-merged-volume treats all voxels as one
    structure).
    
    The -*-corrected-areas options are intended for eroding on group average
    surfaces, but it is only an approximate correction.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiErodeOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = cifti_erode_cargs(params, execution)
    ret = cifti_erode_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_erode(
    cifti_in: InputPathType,
    direction: str,
    surface_distance: float,
    volume_distance: float,
    cifti_out: str,
    left_surface: CiftiErodeLeftSurfaceParameters | None = None,
    right_surface: CiftiErodeRightSurfaceParameters | None = None,
    cerebellum_surface: CiftiErodeCerebellumSurfaceParameters | None = None,
    opt_merged_volume: bool = False,
    runner: Runner | None = None,
) -> CiftiErodeOutputs:
    """
    Erode a cifti file.
    
    For all data values that are empty (for label data, unlabeled, for other
    data, zero), set the surrounding values to empty. The surrounding values are
    defined as the immediate neighbors and all values in the same structure
    within the specified distance (-merged-volume treats all voxels as one
    structure).
    
    The -*-corrected-areas options are intended for eroding on group average
    surfaces, but it is only an approximate correction.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        cifti_in: the input cifti file.
        direction: which dimension to dilate along, ROW or COLUMN.
        surface_distance: the distance to dilate on surfaces, in mm.
        volume_distance: the distance to dilate in the volume, in mm.
        cifti_out: the output cifti file.
        left_surface: specify the left surface to use.
        right_surface: specify the right surface to use.
        cerebellum_surface: specify the cerebellum surface to use.
        opt_merged_volume: treat volume components as if they were a single\
            component.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiErodeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_ERODE_METADATA)
    params = cifti_erode_params(cifti_in=cifti_in, direction=direction, surface_distance=surface_distance, volume_distance=volume_distance, cifti_out=cifti_out, left_surface=left_surface, right_surface=right_surface, cerebellum_surface=cerebellum_surface, opt_merged_volume=opt_merged_volume)
    return cifti_erode_execute(params, execution)


__all__ = [
    "CIFTI_ERODE_METADATA",
    "CiftiErodeCerebellumSurfaceParameters",
    "CiftiErodeLeftSurfaceParameters",
    "CiftiErodeOutputs",
    "CiftiErodeParameters",
    "CiftiErodeRightSurfaceParameters",
    "cifti_erode",
    "cifti_erode_cerebellum_surface_params",
    "cifti_erode_left_surface_params",
    "cifti_erode_params",
    "cifti_erode_right_surface_params",
]
