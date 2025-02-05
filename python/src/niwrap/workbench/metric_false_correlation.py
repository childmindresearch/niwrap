# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

METRIC_FALSE_CORRELATION_METADATA = Metadata(
    id="1caaae17d3f0c5a13c0d0ecb9b74ca6b5a6dc29b.boutiques",
    name="metric-false-correlation",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
MetricFalseCorrelationParameters = typing.TypedDict('MetricFalseCorrelationParameters', {
    "__STYX_TYPE__": typing.Literal["metric-false-correlation"],
    "surface": InputPathType,
    "metric_in": InputPathType,
    "3d_dist": float,
    "geo_outer": float,
    "geo_inner": float,
    "metric_out": str,
    "opt_roi_roi_metric": typing.NotRequired[InputPathType | None],
    "opt_dump_text_text_out": typing.NotRequired[str | None],
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
        "metric-false-correlation": metric_false_correlation_cargs,
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
        "metric-false-correlation": metric_false_correlation_outputs,
    }
    return vt.get(t)


class MetricFalseCorrelationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_false_correlation(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def metric_false_correlation_params(
    surface: InputPathType,
    metric_in: InputPathType,
    v_3d_dist: float,
    geo_outer: float,
    geo_inner: float,
    metric_out: str,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_dump_text_text_out: str | None = None,
) -> MetricFalseCorrelationParameters:
    """
    Build parameters.
    
    Args:
        surface: the surface to compute geodesic and 3D distance with.
        metric_in: the metric to correlate.
        v_3d_dist: maximum 3D distance to check around each vertex.
        geo_outer: maximum geodesic distance to use for neighboring correlation.
        geo_inner: minimum geodesic distance to use for neighboring correlation.
        metric_out: the output metric.
        opt_roi_roi_metric: select a region of interest that has data: the\
            region, as a metric file.
        opt_dump_text_text_out: dump the raw measures used to a text file: the\
            output text file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "metric-false-correlation",
        "surface": surface,
        "metric_in": metric_in,
        "3d_dist": v_3d_dist,
        "geo_outer": geo_outer,
        "geo_inner": geo_inner,
        "metric_out": metric_out,
    }
    if opt_roi_roi_metric is not None:
        params["opt_roi_roi_metric"] = opt_roi_roi_metric
    if opt_dump_text_text_out is not None:
        params["opt_dump_text_text_out"] = opt_dump_text_text_out
    return params


def metric_false_correlation_cargs(
    params: MetricFalseCorrelationParameters,
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
    cargs.append("-metric-false-correlation")
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(execution.input_file(params.get("metric_in")))
    cargs.append(str(params.get("3d_dist")))
    cargs.append(str(params.get("geo_outer")))
    cargs.append(str(params.get("geo_inner")))
    cargs.append(params.get("metric_out"))
    if params.get("opt_roi_roi_metric") is not None:
        cargs.extend([
            "-roi",
            execution.input_file(params.get("opt_roi_roi_metric"))
        ])
    if params.get("opt_dump_text_text_out") is not None:
        cargs.extend([
            "-dump-text",
            params.get("opt_dump_text_text_out")
        ])
    return cargs


def metric_false_correlation_outputs(
    params: MetricFalseCorrelationParameters,
    execution: Execution,
) -> MetricFalseCorrelationOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MetricFalseCorrelationOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(params.get("metric_out")),
    )
    return ret


def metric_false_correlation_execute(
    params: MetricFalseCorrelationParameters,
    execution: Execution,
) -> MetricFalseCorrelationOutputs:
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
        NamedTuple of outputs (described in `MetricFalseCorrelationOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = metric_false_correlation_cargs(params, execution)
    ret = metric_false_correlation_outputs(params, execution)
    execution.run(cargs)
    return ret


def metric_false_correlation(
    surface: InputPathType,
    metric_in: InputPathType,
    v_3d_dist: float,
    geo_outer: float,
    geo_inner: float,
    metric_out: str,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_dump_text_text_out: str | None = None,
    runner: Runner | None = None,
) -> MetricFalseCorrelationOutputs:
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
        surface: the surface to compute geodesic and 3D distance with.
        metric_in: the metric to correlate.
        v_3d_dist: maximum 3D distance to check around each vertex.
        geo_outer: maximum geodesic distance to use for neighboring correlation.
        geo_inner: minimum geodesic distance to use for neighboring correlation.
        metric_out: the output metric.
        opt_roi_roi_metric: select a region of interest that has data: the\
            region, as a metric file.
        opt_dump_text_text_out: dump the raw measures used to a text file: the\
            output text file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricFalseCorrelationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_FALSE_CORRELATION_METADATA)
    params = metric_false_correlation_params(surface=surface, metric_in=metric_in, v_3d_dist=v_3d_dist, geo_outer=geo_outer, geo_inner=geo_inner, metric_out=metric_out, opt_roi_roi_metric=opt_roi_roi_metric, opt_dump_text_text_out=opt_dump_text_text_out)
    return metric_false_correlation_execute(params, execution)


__all__ = [
    "METRIC_FALSE_CORRELATION_METADATA",
    "MetricFalseCorrelationOutputs",
    "MetricFalseCorrelationParameters",
    "metric_false_correlation",
    "metric_false_correlation_params",
]
