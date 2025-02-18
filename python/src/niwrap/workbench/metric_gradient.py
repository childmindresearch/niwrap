# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

METRIC_GRADIENT_METADATA = Metadata(
    id="f4530e09758cb38a6a09de62a78168104a151cfb.boutiques",
    name="metric-gradient",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
MetricGradientPresmoothParameters = typing.TypedDict('MetricGradientPresmoothParameters', {
    "__STYX_TYPE__": typing.Literal["presmooth"],
    "kernel": float,
    "opt_fwhm": bool,
})
MetricGradientRoiParameters = typing.TypedDict('MetricGradientRoiParameters', {
    "__STYX_TYPE__": typing.Literal["roi"],
    "roi_metric": InputPathType,
    "opt_match_columns": bool,
})
MetricGradientParameters = typing.TypedDict('MetricGradientParameters', {
    "__STYX_TYPE__": typing.Literal["metric-gradient"],
    "surface": InputPathType,
    "metric_in": InputPathType,
    "metric_out": str,
    "presmooth": typing.NotRequired[MetricGradientPresmoothParameters | None],
    "roi": typing.NotRequired[MetricGradientRoiParameters | None],
    "opt_vectors_vector_metric_out": typing.NotRequired[str | None],
    "opt_column_column": typing.NotRequired[str | None],
    "opt_corrected_areas_area_metric": typing.NotRequired[InputPathType | None],
    "opt_average_normals": bool,
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
        "metric-gradient": metric_gradient_cargs,
        "presmooth": metric_gradient_presmooth_cargs,
        "roi": metric_gradient_roi_cargs,
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
        "metric-gradient": metric_gradient_outputs,
    }.get(t)


def metric_gradient_presmooth_params(
    kernel: float,
    opt_fwhm: bool = False,
) -> MetricGradientPresmoothParameters:
    """
    Build parameters.
    
    Args:
        kernel: the size of the gaussian smoothing kernel in mm, as sigma by\
            default.
        opt_fwhm: kernel size is FWHM, not sigma.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "presmooth",
        "kernel": kernel,
        "opt_fwhm": opt_fwhm,
    }
    return params


def metric_gradient_presmooth_cargs(
    params: MetricGradientPresmoothParameters,
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
    cargs.append("-presmooth")
    cargs.append(str(params.get("kernel")))
    if params.get("opt_fwhm"):
        cargs.append("-fwhm")
    return cargs


def metric_gradient_roi_params(
    roi_metric: InputPathType,
    opt_match_columns: bool = False,
) -> MetricGradientRoiParameters:
    """
    Build parameters.
    
    Args:
        roi_metric: the area to take the gradient within, as a metric.
        opt_match_columns: for each input column, use the corresponding column\
            from the roi.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "roi",
        "roi_metric": roi_metric,
        "opt_match_columns": opt_match_columns,
    }
    return params


def metric_gradient_roi_cargs(
    params: MetricGradientRoiParameters,
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
    cargs.append("-roi")
    cargs.append(execution.input_file(params.get("roi_metric")))
    if params.get("opt_match_columns"):
        cargs.append("-match-columns")
    return cargs


class MetricGradientOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_gradient(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the magnitude of the gradient"""
    opt_vectors_vector_metric_out: OutputPathType | None
    """output gradient vectors: the vectors as a metric file"""


def metric_gradient_params(
    surface: InputPathType,
    metric_in: InputPathType,
    metric_out: str,
    presmooth: MetricGradientPresmoothParameters | None = None,
    roi: MetricGradientRoiParameters | None = None,
    opt_vectors_vector_metric_out: str | None = None,
    opt_column_column: str | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    opt_average_normals: bool = False,
) -> MetricGradientParameters:
    """
    Build parameters.
    
    Args:
        surface: the surface to compute the gradient on.
        metric_in: the metric to compute the gradient of.
        metric_out: the magnitude of the gradient.
        presmooth: smooth the metric before computing the gradient.
        roi: select a region of interest to take the gradient of.
        opt_vectors_vector_metric_out: output gradient vectors: the vectors as\
            a metric file.
        opt_column_column: select a single column to compute the gradient of:\
            the column number or name.
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
        opt_average_normals: average the normals of each vertex with its\
            neighbors before using them to compute the gradient.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "metric-gradient",
        "surface": surface,
        "metric_in": metric_in,
        "metric_out": metric_out,
        "opt_average_normals": opt_average_normals,
    }
    if presmooth is not None:
        params["presmooth"] = presmooth
    if roi is not None:
        params["roi"] = roi
    if opt_vectors_vector_metric_out is not None:
        params["opt_vectors_vector_metric_out"] = opt_vectors_vector_metric_out
    if opt_column_column is not None:
        params["opt_column_column"] = opt_column_column
    if opt_corrected_areas_area_metric is not None:
        params["opt_corrected_areas_area_metric"] = opt_corrected_areas_area_metric
    return params


def metric_gradient_cargs(
    params: MetricGradientParameters,
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
    cargs.append("-metric-gradient")
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(execution.input_file(params.get("metric_in")))
    cargs.append(params.get("metric_out"))
    if params.get("presmooth") is not None:
        cargs.extend(dyn_cargs(params.get("presmooth")["__STYXTYPE__"])(params.get("presmooth"), execution))
    if params.get("roi") is not None:
        cargs.extend(dyn_cargs(params.get("roi")["__STYXTYPE__"])(params.get("roi"), execution))
    if params.get("opt_vectors_vector_metric_out") is not None:
        cargs.extend([
            "-vectors",
            params.get("opt_vectors_vector_metric_out")
        ])
    if params.get("opt_column_column") is not None:
        cargs.extend([
            "-column",
            params.get("opt_column_column")
        ])
    if params.get("opt_corrected_areas_area_metric") is not None:
        cargs.extend([
            "-corrected-areas",
            execution.input_file(params.get("opt_corrected_areas_area_metric"))
        ])
    if params.get("opt_average_normals"):
        cargs.append("-average-normals")
    return cargs


def metric_gradient_outputs(
    params: MetricGradientParameters,
    execution: Execution,
) -> MetricGradientOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MetricGradientOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(params.get("metric_out")),
        opt_vectors_vector_metric_out=execution.output_file(params.get("opt_vectors_vector_metric_out")) if (params.get("opt_vectors_vector_metric_out") is not None) else None,
    )
    return ret


def metric_gradient_execute(
    params: MetricGradientParameters,
    execution: Execution,
) -> MetricGradientOutputs:
    """
    Surface gradient of a metric file.
    
    At each vertex, the immediate neighbors are unfolded onto a plane tangent to
    the surface at the vertex (specifically, perpendicular to the normal). The
    gradient is computed using a regression between the unfolded positions of
    the vertices and their values. The gradient is then given by the slopes of
    the regression, and reconstructed as a 3D gradient vector. By default, takes
    the gradient of all columns, with no presmoothing, across the whole surface,
    without averaging the normals of the surface among neighbors.
    
    When using -corrected-areas, note that it is an approximate correction.
    Doing smoothing on individual surfaces before averaging/gradient is
    preferred, when possible, in order to make use of the original surface
    structure.
    
    Specifying an ROI will restrict the gradient to only use data from where the
    ROI metric is positive, and output zeros anywhere the ROI metric is not
    positive.
    
    By default, the first column of the roi metric is used for all input
    columns. When -match-columns is specified to the -roi option, the input and
    roi metrics must have the same number of columns, and for each input
    column's index, the same column index is used in the roi metric. If the
    -match-columns option to -roi is used while the -column option is also used,
    the number of columns of the roi metric must match the input metric, and it
    will use the roi column with the index of the selected input column.
    
    The vector output metric is organized such that the X, Y, and Z components
    from a single input column are consecutive columns.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MetricGradientOutputs`).
    """
    params = execution.params(params)
    cargs = metric_gradient_cargs(params, execution)
    ret = metric_gradient_outputs(params, execution)
    execution.run(cargs)
    return ret


def metric_gradient(
    surface: InputPathType,
    metric_in: InputPathType,
    metric_out: str,
    presmooth: MetricGradientPresmoothParameters | None = None,
    roi: MetricGradientRoiParameters | None = None,
    opt_vectors_vector_metric_out: str | None = None,
    opt_column_column: str | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    opt_average_normals: bool = False,
    runner: Runner | None = None,
) -> MetricGradientOutputs:
    """
    Surface gradient of a metric file.
    
    At each vertex, the immediate neighbors are unfolded onto a plane tangent to
    the surface at the vertex (specifically, perpendicular to the normal). The
    gradient is computed using a regression between the unfolded positions of
    the vertices and their values. The gradient is then given by the slopes of
    the regression, and reconstructed as a 3D gradient vector. By default, takes
    the gradient of all columns, with no presmoothing, across the whole surface,
    without averaging the normals of the surface among neighbors.
    
    When using -corrected-areas, note that it is an approximate correction.
    Doing smoothing on individual surfaces before averaging/gradient is
    preferred, when possible, in order to make use of the original surface
    structure.
    
    Specifying an ROI will restrict the gradient to only use data from where the
    ROI metric is positive, and output zeros anywhere the ROI metric is not
    positive.
    
    By default, the first column of the roi metric is used for all input
    columns. When -match-columns is specified to the -roi option, the input and
    roi metrics must have the same number of columns, and for each input
    column's index, the same column index is used in the roi metric. If the
    -match-columns option to -roi is used while the -column option is also used,
    the number of columns of the roi metric must match the input metric, and it
    will use the roi column with the index of the selected input column.
    
    The vector output metric is organized such that the X, Y, and Z components
    from a single input column are consecutive columns.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface: the surface to compute the gradient on.
        metric_in: the metric to compute the gradient of.
        metric_out: the magnitude of the gradient.
        presmooth: smooth the metric before computing the gradient.
        roi: select a region of interest to take the gradient of.
        opt_vectors_vector_metric_out: output gradient vectors: the vectors as\
            a metric file.
        opt_column_column: select a single column to compute the gradient of:\
            the column number or name.
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
        opt_average_normals: average the normals of each vertex with its\
            neighbors before using them to compute the gradient.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricGradientOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_GRADIENT_METADATA)
    params = metric_gradient_params(surface=surface, metric_in=metric_in, metric_out=metric_out, presmooth=presmooth, roi=roi, opt_vectors_vector_metric_out=opt_vectors_vector_metric_out, opt_column_column=opt_column_column, opt_corrected_areas_area_metric=opt_corrected_areas_area_metric, opt_average_normals=opt_average_normals)
    return metric_gradient_execute(params, execution)


__all__ = [
    "METRIC_GRADIENT_METADATA",
    "MetricGradientOutputs",
    "MetricGradientParameters",
    "MetricGradientPresmoothParameters",
    "MetricGradientRoiParameters",
    "metric_gradient",
    "metric_gradient_params",
    "metric_gradient_presmooth_params",
    "metric_gradient_roi_params",
]
