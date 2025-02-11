# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CIFTI_DILATE_METADATA = Metadata(
    id="907e475cef6dbf3556c5c8ea8d183b2219169bf5.boutiques",
    name="cifti-dilate",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
CiftiDilateLeftSurfaceParameters = typing.TypedDict('CiftiDilateLeftSurfaceParameters', {
    "__STYX_TYPE__": typing.Literal["left_surface"],
    "surface": InputPathType,
    "opt_left_corrected_areas_area_metric": typing.NotRequired[InputPathType | None],
})
CiftiDilateRightSurfaceParameters = typing.TypedDict('CiftiDilateRightSurfaceParameters', {
    "__STYX_TYPE__": typing.Literal["right_surface"],
    "surface": InputPathType,
    "opt_right_corrected_areas_area_metric": typing.NotRequired[InputPathType | None],
})
CiftiDilateCerebellumSurfaceParameters = typing.TypedDict('CiftiDilateCerebellumSurfaceParameters', {
    "__STYX_TYPE__": typing.Literal["cerebellum_surface"],
    "surface": InputPathType,
    "opt_cerebellum_corrected_areas_area_metric": typing.NotRequired[InputPathType | None],
})
CiftiDilateParameters = typing.TypedDict('CiftiDilateParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-dilate"],
    "cifti_in": InputPathType,
    "direction": str,
    "surface_distance": float,
    "volume_distance": float,
    "cifti_out": str,
    "left_surface": typing.NotRequired[CiftiDilateLeftSurfaceParameters | None],
    "right_surface": typing.NotRequired[CiftiDilateRightSurfaceParameters | None],
    "cerebellum_surface": typing.NotRequired[CiftiDilateCerebellumSurfaceParameters | None],
    "opt_bad_brainordinate_roi_roi_cifti": typing.NotRequired[InputPathType | None],
    "opt_nearest": bool,
    "opt_merged_volume": bool,
    "opt_legacy_mode": bool,
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
        "cifti-dilate": cifti_dilate_cargs,
        "left_surface": cifti_dilate_left_surface_cargs,
        "right_surface": cifti_dilate_right_surface_cargs,
        "cerebellum_surface": cifti_dilate_cerebellum_surface_cargs,
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
        "cifti-dilate": cifti_dilate_outputs,
    }.get(t)


def cifti_dilate_left_surface_params(
    surface: InputPathType,
    opt_left_corrected_areas_area_metric: InputPathType | None = None,
) -> CiftiDilateLeftSurfaceParameters:
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


def cifti_dilate_left_surface_cargs(
    params: CiftiDilateLeftSurfaceParameters,
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


def cifti_dilate_right_surface_params(
    surface: InputPathType,
    opt_right_corrected_areas_area_metric: InputPathType | None = None,
) -> CiftiDilateRightSurfaceParameters:
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


def cifti_dilate_right_surface_cargs(
    params: CiftiDilateRightSurfaceParameters,
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


def cifti_dilate_cerebellum_surface_params(
    surface: InputPathType,
    opt_cerebellum_corrected_areas_area_metric: InputPathType | None = None,
) -> CiftiDilateCerebellumSurfaceParameters:
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


def cifti_dilate_cerebellum_surface_cargs(
    params: CiftiDilateCerebellumSurfaceParameters,
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


class CiftiDilateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_dilate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_dilate_params(
    cifti_in: InputPathType,
    direction: str,
    surface_distance: float,
    volume_distance: float,
    cifti_out: str,
    left_surface: CiftiDilateLeftSurfaceParameters | None = None,
    right_surface: CiftiDilateRightSurfaceParameters | None = None,
    cerebellum_surface: CiftiDilateCerebellumSurfaceParameters | None = None,
    opt_bad_brainordinate_roi_roi_cifti: InputPathType | None = None,
    opt_nearest: bool = False,
    opt_merged_volume: bool = False,
    opt_legacy_mode: bool = False,
) -> CiftiDilateParameters:
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
        opt_bad_brainordinate_roi_roi_cifti: specify an roi of brainordinates\
            to overwrite, rather than zeros: cifti dscalar or dtseries file,\
            positive values denote brainordinates to have their values replaced.
        opt_nearest: use nearest good value instead of a weighted average.
        opt_merged_volume: treat volume components as if they were a single\
            component.
        opt_legacy_mode: use the math from v1.3.2 and earlier for weighted\
            dilation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-dilate",
        "cifti_in": cifti_in,
        "direction": direction,
        "surface_distance": surface_distance,
        "volume_distance": volume_distance,
        "cifti_out": cifti_out,
        "opt_nearest": opt_nearest,
        "opt_merged_volume": opt_merged_volume,
        "opt_legacy_mode": opt_legacy_mode,
    }
    if left_surface is not None:
        params["left_surface"] = left_surface
    if right_surface is not None:
        params["right_surface"] = right_surface
    if cerebellum_surface is not None:
        params["cerebellum_surface"] = cerebellum_surface
    if opt_bad_brainordinate_roi_roi_cifti is not None:
        params["opt_bad_brainordinate_roi_roi_cifti"] = opt_bad_brainordinate_roi_roi_cifti
    return params


def cifti_dilate_cargs(
    params: CiftiDilateParameters,
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
    cargs.append("-cifti-dilate")
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
    if params.get("opt_bad_brainordinate_roi_roi_cifti") is not None:
        cargs.extend([
            "-bad-brainordinate-roi",
            execution.input_file(params.get("opt_bad_brainordinate_roi_roi_cifti"))
        ])
    if params.get("opt_nearest"):
        cargs.append("-nearest")
    if params.get("opt_merged_volume"):
        cargs.append("-merged-volume")
    if params.get("opt_legacy_mode"):
        cargs.append("-legacy-mode")
    return cargs


def cifti_dilate_outputs(
    params: CiftiDilateParameters,
    execution: Execution,
) -> CiftiDilateOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiDilateOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(params.get("cifti_out")),
    )
    return ret


def cifti_dilate_execute(
    params: CiftiDilateParameters,
    execution: Execution,
) -> CiftiDilateOutputs:
    """
    Dilate a cifti file.
    
    For all data values designated as bad, if they neighbor a good value or are
    within the specified distance of a good value in the same kind of model,
    replace the value with a distance weighted average of nearby good values,
    otherwise set the value to zero. If -nearest is specified, it will use the
    value from the closest good value within range instead of a weighted
    average. When the input file contains label data, nearest dilation is used
    on the surface, and weighted popularity is used in the volume.
    
    The -*-corrected-areas options are intended for dilating on group average
    surfaces, but it is only an approximate correction for the reduction of
    structure in a group average surface.
    
    If -bad-brainordinate-roi is specified, all values, including those with
    value zero, are good, except for locations with a positive value in the ROI.
    If it is not specified, only values equal to zero are bad.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiDilateOutputs`).
    """
    cargs = cifti_dilate_cargs(params, execution)
    ret = cifti_dilate_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_dilate(
    cifti_in: InputPathType,
    direction: str,
    surface_distance: float,
    volume_distance: float,
    cifti_out: str,
    left_surface: CiftiDilateLeftSurfaceParameters | None = None,
    right_surface: CiftiDilateRightSurfaceParameters | None = None,
    cerebellum_surface: CiftiDilateCerebellumSurfaceParameters | None = None,
    opt_bad_brainordinate_roi_roi_cifti: InputPathType | None = None,
    opt_nearest: bool = False,
    opt_merged_volume: bool = False,
    opt_legacy_mode: bool = False,
    runner: Runner | None = None,
) -> CiftiDilateOutputs:
    """
    Dilate a cifti file.
    
    For all data values designated as bad, if they neighbor a good value or are
    within the specified distance of a good value in the same kind of model,
    replace the value with a distance weighted average of nearby good values,
    otherwise set the value to zero. If -nearest is specified, it will use the
    value from the closest good value within range instead of a weighted
    average. When the input file contains label data, nearest dilation is used
    on the surface, and weighted popularity is used in the volume.
    
    The -*-corrected-areas options are intended for dilating on group average
    surfaces, but it is only an approximate correction for the reduction of
    structure in a group average surface.
    
    If -bad-brainordinate-roi is specified, all values, including those with
    value zero, are good, except for locations with a positive value in the ROI.
    If it is not specified, only values equal to zero are bad.
    
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
        opt_bad_brainordinate_roi_roi_cifti: specify an roi of brainordinates\
            to overwrite, rather than zeros: cifti dscalar or dtseries file,\
            positive values denote brainordinates to have their values replaced.
        opt_nearest: use nearest good value instead of a weighted average.
        opt_merged_volume: treat volume components as if they were a single\
            component.
        opt_legacy_mode: use the math from v1.3.2 and earlier for weighted\
            dilation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiDilateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_DILATE_METADATA)
    params = cifti_dilate_params(cifti_in=cifti_in, direction=direction, surface_distance=surface_distance, volume_distance=volume_distance, cifti_out=cifti_out, left_surface=left_surface, right_surface=right_surface, cerebellum_surface=cerebellum_surface, opt_bad_brainordinate_roi_roi_cifti=opt_bad_brainordinate_roi_roi_cifti, opt_nearest=opt_nearest, opt_merged_volume=opt_merged_volume, opt_legacy_mode=opt_legacy_mode)
    return cifti_dilate_execute(params, execution)


__all__ = [
    "CIFTI_DILATE_METADATA",
    "CiftiDilateCerebellumSurfaceParameters",
    "CiftiDilateLeftSurfaceParameters",
    "CiftiDilateOutputs",
    "CiftiDilateParameters",
    "CiftiDilateRightSurfaceParameters",
    "cifti_dilate",
    "cifti_dilate_cerebellum_surface_params",
    "cifti_dilate_left_surface_params",
    "cifti_dilate_params",
    "cifti_dilate_right_surface_params",
]
