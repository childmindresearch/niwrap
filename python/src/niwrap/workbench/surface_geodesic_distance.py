# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURFACE_GEODESIC_DISTANCE_METADATA = Metadata(
    id="ed6ff5cde669a2d85c0c8b429448c5425d4354ad.boutiques",
    name="surface-geodesic-distance",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
SurfaceGeodesicDistanceParameters = typing.TypedDict('SurfaceGeodesicDistanceParameters', {
    "__STYX_TYPE__": typing.Literal["surface-geodesic-distance"],
    "surface": InputPathType,
    "vertex": int,
    "metric_out": str,
    "opt_naive": bool,
    "opt_limit_limit_mm": typing.NotRequired[float | None],
    "opt_corrected_areas_area_metric": typing.NotRequired[InputPathType | None],
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
        "surface-geodesic-distance": surface_geodesic_distance_cargs,
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
        "surface-geodesic-distance": surface_geodesic_distance_outputs,
    }.get(t)


class SurfaceGeodesicDistanceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_geodesic_distance(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def surface_geodesic_distance_params(
    surface: InputPathType,
    vertex: int,
    metric_out: str,
    opt_naive: bool = False,
    opt_limit_limit_mm: float | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
) -> SurfaceGeodesicDistanceParameters:
    """
    Build parameters.
    
    Args:
        surface: the surface to compute on.
        vertex: the vertex to compute geodesic distance from.
        metric_out: the output metric.
        opt_naive: use only neighbors, don't crawl triangles (not recommended).
        opt_limit_limit_mm: stop at a certain distance: distance in mm to stop\
            at.
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surface-geodesic-distance",
        "surface": surface,
        "vertex": vertex,
        "metric_out": metric_out,
        "opt_naive": opt_naive,
    }
    if opt_limit_limit_mm is not None:
        params["opt_limit_limit_mm"] = opt_limit_limit_mm
    if opt_corrected_areas_area_metric is not None:
        params["opt_corrected_areas_area_metric"] = opt_corrected_areas_area_metric
    return params


def surface_geodesic_distance_cargs(
    params: SurfaceGeodesicDistanceParameters,
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
    cargs.append("-surface-geodesic-distance")
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(str(params.get("vertex")))
    cargs.append(params.get("metric_out"))
    if params.get("opt_naive"):
        cargs.append("-naive")
    if params.get("opt_limit_limit_mm") is not None:
        cargs.extend([
            "-limit",
            str(params.get("opt_limit_limit_mm"))
        ])
    if params.get("opt_corrected_areas_area_metric") is not None:
        cargs.extend([
            "-corrected-areas",
            execution.input_file(params.get("opt_corrected_areas_area_metric"))
        ])
    return cargs


def surface_geodesic_distance_outputs(
    params: SurfaceGeodesicDistanceParameters,
    execution: Execution,
) -> SurfaceGeodesicDistanceOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfaceGeodesicDistanceOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(params.get("metric_out")),
    )
    return ret


def surface_geodesic_distance_execute(
    params: SurfaceGeodesicDistanceParameters,
    execution: Execution,
) -> SurfaceGeodesicDistanceOutputs:
    """
    Compute geodesic distance from one vertex to the entire surface.
    
    Unless -limit is specified, computes the geodesic distance from the
    specified vertex to all others. The result is output as a single column
    metric file, with a value of -1 for vertices that the distance was not
    computed for.
    
    The -corrected-areas option should be used when the input is a group average
    surface - group average surfaces have significantly less surface area than
    individual surfaces do, and therefore distances measured on them would be
    smaller than measuring them on individual surfaces. In this case, the input
    to this option should be a group average of the output of
    -surface-vertex-areas for each subject.
    
    If -naive is not specified, the algorithm uses not just immediate neighbors,
    but also neighbors derived from crawling across pairs of triangles that
    share an edge.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfaceGeodesicDistanceOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = surface_geodesic_distance_cargs(params, execution)
    ret = surface_geodesic_distance_outputs(params, execution)
    execution.run(cargs)
    return ret


def surface_geodesic_distance(
    surface: InputPathType,
    vertex: int,
    metric_out: str,
    opt_naive: bool = False,
    opt_limit_limit_mm: float | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    runner: Runner | None = None,
) -> SurfaceGeodesicDistanceOutputs:
    """
    Compute geodesic distance from one vertex to the entire surface.
    
    Unless -limit is specified, computes the geodesic distance from the
    specified vertex to all others. The result is output as a single column
    metric file, with a value of -1 for vertices that the distance was not
    computed for.
    
    The -corrected-areas option should be used when the input is a group average
    surface - group average surfaces have significantly less surface area than
    individual surfaces do, and therefore distances measured on them would be
    smaller than measuring them on individual surfaces. In this case, the input
    to this option should be a group average of the output of
    -surface-vertex-areas for each subject.
    
    If -naive is not specified, the algorithm uses not just immediate neighbors,
    but also neighbors derived from crawling across pairs of triangles that
    share an edge.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface: the surface to compute on.
        vertex: the vertex to compute geodesic distance from.
        metric_out: the output metric.
        opt_naive: use only neighbors, don't crawl triangles (not recommended).
        opt_limit_limit_mm: stop at a certain distance: distance in mm to stop\
            at.
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceGeodesicDistanceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_GEODESIC_DISTANCE_METADATA)
    params = surface_geodesic_distance_params(surface=surface, vertex=vertex, metric_out=metric_out, opt_naive=opt_naive, opt_limit_limit_mm=opt_limit_limit_mm, opt_corrected_areas_area_metric=opt_corrected_areas_area_metric)
    return surface_geodesic_distance_execute(params, execution)


__all__ = [
    "SURFACE_GEODESIC_DISTANCE_METADATA",
    "SurfaceGeodesicDistanceOutputs",
    "SurfaceGeodesicDistanceParameters",
    "surface_geodesic_distance",
    "surface_geodesic_distance_params",
]
