# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CIFTI_FALSE_CORRELATION_METADATA = Metadata(
    id="305c93f3a6d583446150f0a5829082da2a5823ee.boutiques",
    name="cifti-false-correlation",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
CiftiFalseCorrelationLeftSurfaceParameters = typing.TypedDict('CiftiFalseCorrelationLeftSurfaceParameters', {
    "__STYX_TYPE__": typing.Literal["left_surface"],
    "surface": InputPathType,
    "opt_dump_text_text_out": typing.NotRequired[str | None],
})
CiftiFalseCorrelationRightSurfaceParameters = typing.TypedDict('CiftiFalseCorrelationRightSurfaceParameters', {
    "__STYX_TYPE__": typing.Literal["right_surface"],
    "surface": InputPathType,
    "opt_dump_text_text_out": typing.NotRequired[str | None],
})
CiftiFalseCorrelationCerebellumSurfaceParameters = typing.TypedDict('CiftiFalseCorrelationCerebellumSurfaceParameters', {
    "__STYX_TYPE__": typing.Literal["cerebellum_surface"],
    "surface": InputPathType,
    "opt_dump_text_text_out": typing.NotRequired[str | None],
})
CiftiFalseCorrelationParameters = typing.TypedDict('CiftiFalseCorrelationParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-false-correlation"],
    "cifti_in": InputPathType,
    "3d_dist": float,
    "geo_outer": float,
    "geo_inner": float,
    "cifti_out": str,
    "left_surface": typing.NotRequired[CiftiFalseCorrelationLeftSurfaceParameters | None],
    "right_surface": typing.NotRequired[CiftiFalseCorrelationRightSurfaceParameters | None],
    "cerebellum_surface": typing.NotRequired[CiftiFalseCorrelationCerebellumSurfaceParameters | None],
})


def dyn_cargs(
    t: str,
) -> None:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    vt = {
        "cifti-false-correlation": cifti_false_correlation_cargs,
        "left_surface": cifti_false_correlation_left_surface_cargs,
        "right_surface": cifti_false_correlation_right_surface_cargs,
        "cerebellum_surface": cifti_false_correlation_cerebellum_surface_cargs,
    }
    return vt.get(t)


def dyn_outputs(
    t: str,
) -> None:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    vt = {
        "cifti-false-correlation": cifti_false_correlation_outputs,
    }
    return vt.get(t)


def cifti_false_correlation_left_surface_params(
    surface: InputPathType,
    opt_dump_text_text_out: str | None = None,
) -> CiftiFalseCorrelationLeftSurfaceParameters:
    """
    Build parameters.
    
    Args:
        surface: the left surface file.
        opt_dump_text_text_out: dump the raw measures used to a text file: the\
            output text file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "left_surface",
        "surface": surface,
    }
    if opt_dump_text_text_out is not None:
        params["opt_dump_text_text_out"] = opt_dump_text_text_out
    return params


def cifti_false_correlation_left_surface_cargs(
    params: CiftiFalseCorrelationLeftSurfaceParameters,
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
    if params.get("opt_dump_text_text_out") is not None:
        cargs.extend([
            "-dump-text",
            params.get("opt_dump_text_text_out")
        ])
    return cargs


def cifti_false_correlation_right_surface_params(
    surface: InputPathType,
    opt_dump_text_text_out: str | None = None,
) -> CiftiFalseCorrelationRightSurfaceParameters:
    """
    Build parameters.
    
    Args:
        surface: the right surface file.
        opt_dump_text_text_out: dump the raw measures used to a text file: the\
            output text file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "right_surface",
        "surface": surface,
    }
    if opt_dump_text_text_out is not None:
        params["opt_dump_text_text_out"] = opt_dump_text_text_out
    return params


def cifti_false_correlation_right_surface_cargs(
    params: CiftiFalseCorrelationRightSurfaceParameters,
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
    if params.get("opt_dump_text_text_out") is not None:
        cargs.extend([
            "-dump-text",
            params.get("opt_dump_text_text_out")
        ])
    return cargs


def cifti_false_correlation_cerebellum_surface_params(
    surface: InputPathType,
    opt_dump_text_text_out: str | None = None,
) -> CiftiFalseCorrelationCerebellumSurfaceParameters:
    """
    Build parameters.
    
    Args:
        surface: the cerebellum surface file.
        opt_dump_text_text_out: dump the raw measures used to a text file: the\
            output text file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cerebellum_surface",
        "surface": surface,
    }
    if opt_dump_text_text_out is not None:
        params["opt_dump_text_text_out"] = opt_dump_text_text_out
    return params


def cifti_false_correlation_cerebellum_surface_cargs(
    params: CiftiFalseCorrelationCerebellumSurfaceParameters,
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
    if params.get("opt_dump_text_text_out") is not None:
        cargs.extend([
            "-dump-text",
            params.get("opt_dump_text_text_out")
        ])
    return cargs


class CiftiFalseCorrelationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_false_correlation(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti dscalar file"""


def cifti_false_correlation_params(
    cifti_in: InputPathType,
    v_3d_dist: float,
    geo_outer: float,
    geo_inner: float,
    cifti_out: str,
    left_surface: CiftiFalseCorrelationLeftSurfaceParameters | None = None,
    right_surface: CiftiFalseCorrelationRightSurfaceParameters | None = None,
    cerebellum_surface: CiftiFalseCorrelationCerebellumSurfaceParameters | None = None,
) -> CiftiFalseCorrelationParameters:
    """
    Build parameters.
    
    Args:
        cifti_in: the cifti file to use for correlation.
        v_3d_dist: maximum 3D distance to check around each vertex.
        geo_outer: maximum geodesic distance to use for neighboring correlation.
        geo_inner: minimum geodesic distance to use for neighboring correlation.
        cifti_out: the output cifti dscalar file.
        left_surface: specify the left surface to use.
        right_surface: specify the right surface to use.
        cerebellum_surface: specify the cerebellum surface to use.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-false-correlation",
        "cifti_in": cifti_in,
        "3d_dist": v_3d_dist,
        "geo_outer": geo_outer,
        "geo_inner": geo_inner,
        "cifti_out": cifti_out,
    }
    if left_surface is not None:
        params["left_surface"] = left_surface
    if right_surface is not None:
        params["right_surface"] = right_surface
    if cerebellum_surface is not None:
        params["cerebellum_surface"] = cerebellum_surface
    return params


def cifti_false_correlation_cargs(
    params: CiftiFalseCorrelationParameters,
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
    cargs.append("-cifti-false-correlation")
    cargs.append(execution.input_file(params.get("cifti_in")))
    cargs.append(str(params.get("3d_dist")))
    cargs.append(str(params.get("geo_outer")))
    cargs.append(str(params.get("geo_inner")))
    cargs.append(params.get("cifti_out"))
    if params.get("left_surface") is not None:
        cargs.extend(dyn_cargs(params.get("left_surface")["__STYXTYPE__"])(params.get("left_surface"), execution))
    if params.get("right_surface") is not None:
        cargs.extend(dyn_cargs(params.get("right_surface")["__STYXTYPE__"])(params.get("right_surface"), execution))
    if params.get("cerebellum_surface") is not None:
        cargs.extend(dyn_cargs(params.get("cerebellum_surface")["__STYXTYPE__"])(params.get("cerebellum_surface"), execution))
    return cargs


def cifti_false_correlation_outputs(
    params: CiftiFalseCorrelationParameters,
    execution: Execution,
) -> CiftiFalseCorrelationOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiFalseCorrelationOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(params.get("cifti_out")),
    )
    return ret


def cifti_false_correlation_execute(
    params: CiftiFalseCorrelationParameters,
    execution: Execution,
) -> CiftiFalseCorrelationOutputs:
    """
    Compare correlation locally and across/through sulci/gyri.
    
    For each vertex, compute the average correlation within a range of geodesic
    distances that don't cross a sulcus/gyrus, and the correlation to the
    closest vertex crossing a sulcus/gyrus. A vertex is considered to cross a
    sulcus/gyrus if the 3D distance is less than a third of the geodesic
    distance. The output file contains the ratio between these correlations, and
    some additional maps to help explain the ratio.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiFalseCorrelationOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = cifti_false_correlation_cargs(params, execution)
    ret = cifti_false_correlation_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_false_correlation(
    cifti_in: InputPathType,
    v_3d_dist: float,
    geo_outer: float,
    geo_inner: float,
    cifti_out: str,
    left_surface: CiftiFalseCorrelationLeftSurfaceParameters | None = None,
    right_surface: CiftiFalseCorrelationRightSurfaceParameters | None = None,
    cerebellum_surface: CiftiFalseCorrelationCerebellumSurfaceParameters | None = None,
    runner: Runner | None = None,
) -> CiftiFalseCorrelationOutputs:
    """
    Compare correlation locally and across/through sulci/gyri.
    
    For each vertex, compute the average correlation within a range of geodesic
    distances that don't cross a sulcus/gyrus, and the correlation to the
    closest vertex crossing a sulcus/gyrus. A vertex is considered to cross a
    sulcus/gyrus if the 3D distance is less than a third of the geodesic
    distance. The output file contains the ratio between these correlations, and
    some additional maps to help explain the ratio.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        cifti_in: the cifti file to use for correlation.
        v_3d_dist: maximum 3D distance to check around each vertex.
        geo_outer: maximum geodesic distance to use for neighboring correlation.
        geo_inner: minimum geodesic distance to use for neighboring correlation.
        cifti_out: the output cifti dscalar file.
        left_surface: specify the left surface to use.
        right_surface: specify the right surface to use.
        cerebellum_surface: specify the cerebellum surface to use.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiFalseCorrelationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_FALSE_CORRELATION_METADATA)
    params = cifti_false_correlation_params(cifti_in=cifti_in, v_3d_dist=v_3d_dist, geo_outer=geo_outer, geo_inner=geo_inner, cifti_out=cifti_out, left_surface=left_surface, right_surface=right_surface, cerebellum_surface=cerebellum_surface)
    return cifti_false_correlation_execute(params, execution)


__all__ = [
    "CIFTI_FALSE_CORRELATION_METADATA",
    "CiftiFalseCorrelationCerebellumSurfaceParameters",
    "CiftiFalseCorrelationLeftSurfaceParameters",
    "CiftiFalseCorrelationOutputs",
    "CiftiFalseCorrelationParameters",
    "CiftiFalseCorrelationRightSurfaceParameters",
    "cifti_false_correlation",
    "cifti_false_correlation_cerebellum_surface_params",
    "cifti_false_correlation_left_surface_params",
    "cifti_false_correlation_params",
    "cifti_false_correlation_right_surface_params",
]
