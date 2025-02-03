# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

METRIC_WEIGHTED_STATS_METADATA = Metadata(
    id="18f091ded19df25622a8ba5fd28dcde188252609.boutiques",
    name="metric-weighted-stats",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
MetricWeightedStatsRoiParameters = typing.TypedDict('MetricWeightedStatsRoiParameters', {
    "__STYX_TYPE__": typing.Literal["roi"],
    "roi_metric": InputPathType,
    "opt_match_maps": bool,
})
MetricWeightedStatsStdevParameters = typing.TypedDict('MetricWeightedStatsStdevParameters', {
    "__STYX_TYPE__": typing.Literal["stdev"],
    "opt_sample": bool,
})
MetricWeightedStatsParameters = typing.TypedDict('MetricWeightedStatsParameters', {
    "__STYX_TYPE__": typing.Literal["metric-weighted-stats"],
    "metric_in": InputPathType,
    "opt_area_surface_area_surface": typing.NotRequired[InputPathType | None],
    "opt_weight_metric_weight_metric": typing.NotRequired[InputPathType | None],
    "opt_column_column": typing.NotRequired[str | None],
    "roi": typing.NotRequired[MetricWeightedStatsRoiParameters | None],
    "opt_mean": bool,
    "stdev": typing.NotRequired[MetricWeightedStatsStdevParameters | None],
    "opt_percentile_percent": typing.NotRequired[float | None],
    "opt_sum": bool,
    "opt_show_map_name": bool,
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
        "metric-weighted-stats": metric_weighted_stats_cargs,
        "roi": metric_weighted_stats_roi_cargs,
        "stdev": metric_weighted_stats_stdev_cargs,
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
    vt = {}
    return vt.get(t)


def metric_weighted_stats_roi_params(
    roi_metric: InputPathType,
    opt_match_maps: bool = False,
) -> MetricWeightedStatsRoiParameters:
    """
    Build parameters.
    
    Args:
        roi_metric: the roi, as a metric file.
        opt_match_maps: each column of input uses the corresponding column from\
            the roi file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "roi",
        "roi_metric": roi_metric,
        "opt_match_maps": opt_match_maps,
    }
    return params


def metric_weighted_stats_roi_cargs(
    params: MetricWeightedStatsRoiParameters,
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
    if params.get("opt_match_maps"):
        cargs.append("-match-maps")
    return cargs


def metric_weighted_stats_stdev_params(
    opt_sample: bool = False,
) -> MetricWeightedStatsStdevParameters:
    """
    Build parameters.
    
    Args:
        opt_sample: estimate population stdev from the sample.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "stdev",
        "opt_sample": opt_sample,
    }
    return params


def metric_weighted_stats_stdev_cargs(
    params: MetricWeightedStatsStdevParameters,
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
    cargs.append("-stdev")
    if params.get("opt_sample"):
        cargs.append("-sample")
    return cargs


class MetricWeightedStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_weighted_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def metric_weighted_stats_params(
    metric_in: InputPathType,
    opt_area_surface_area_surface: InputPathType | None = None,
    opt_weight_metric_weight_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    roi: MetricWeightedStatsRoiParameters | None = None,
    opt_mean: bool = False,
    stdev: MetricWeightedStatsStdevParameters | None = None,
    opt_percentile_percent: float | None = None,
    opt_sum: bool = False,
    opt_show_map_name: bool = False,
) -> MetricWeightedStatsParameters:
    """
    Build parameters.
    
    Args:
        metric_in: the input metric.
        opt_area_surface_area_surface: use vertex areas as weights: the surface\
            to use for vertex areas.
        opt_weight_metric_weight_metric: use weights from a metric file: metric\
            file containing the weights.
        opt_column_column: only display output for one column: the column\
            number or name.
        roi: only consider data inside an roi.
        opt_mean: compute weighted mean.
        stdev: compute weighted standard deviation.
        opt_percentile_percent: compute weighted percentile: the percentile to\
            find, must be between 0 and 100.
        opt_sum: compute weighted sum.
        opt_show_map_name: print map index and name before each output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "metric-weighted-stats",
        "metric_in": metric_in,
        "opt_mean": opt_mean,
        "opt_sum": opt_sum,
        "opt_show_map_name": opt_show_map_name,
    }
    if opt_area_surface_area_surface is not None:
        params["opt_area_surface_area_surface"] = opt_area_surface_area_surface
    if opt_weight_metric_weight_metric is not None:
        params["opt_weight_metric_weight_metric"] = opt_weight_metric_weight_metric
    if opt_column_column is not None:
        params["opt_column_column"] = opt_column_column
    if roi is not None:
        params["roi"] = roi
    if stdev is not None:
        params["stdev"] = stdev
    if opt_percentile_percent is not None:
        params["opt_percentile_percent"] = opt_percentile_percent
    return params


def metric_weighted_stats_cargs(
    params: MetricWeightedStatsParameters,
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
    cargs.append("-metric-weighted-stats")
    cargs.append(execution.input_file(params.get("metric_in")))
    if params.get("opt_area_surface_area_surface") is not None:
        cargs.extend([
            "-area-surface",
            execution.input_file(params.get("opt_area_surface_area_surface"))
        ])
    if params.get("opt_weight_metric_weight_metric") is not None:
        cargs.extend([
            "-weight-metric",
            execution.input_file(params.get("opt_weight_metric_weight_metric"))
        ])
    if params.get("opt_column_column") is not None:
        cargs.extend([
            "-column",
            params.get("opt_column_column")
        ])
    if params.get("roi") is not None:
        cargs.extend(dyn_cargs(params.get("roi")["__STYXTYPE__"])(params.get("roi"), execution))
    if params.get("opt_mean"):
        cargs.append("-mean")
    if params.get("stdev") is not None:
        cargs.extend(dyn_cargs(params.get("stdev")["__STYXTYPE__"])(params.get("stdev"), execution))
    if params.get("opt_percentile_percent") is not None:
        cargs.extend([
            "-percentile",
            str(params.get("opt_percentile_percent"))
        ])
    if params.get("opt_sum"):
        cargs.append("-sum")
    if params.get("opt_show_map_name"):
        cargs.append("-show-map-name")
    return cargs


def metric_weighted_stats_outputs(
    params: MetricWeightedStatsParameters,
    execution: Execution,
) -> MetricWeightedStatsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MetricWeightedStatsOutputs(
        root=execution.output_file("."),
    )
    return ret


def metric_weighted_stats_execute(
    params: MetricWeightedStatsParameters,
    execution: Execution,
) -> MetricWeightedStatsOutputs:
    """
    Weighted spatial statistics on a metric file.
    
    For each column of the input, a line of text is printed, resulting from the
    specified operation. You must specify exactly one of -area-surface or
    -weight-metric. Use -column to only give output for a single column. If the
    -roi option is used without -match-maps, then each line will contain as many
    numbers as there are maps in the ROI file, separated by tab characters.
    Exactly one of -mean, -stdev, -percentile or -sum must be specified.
    
    Using -sum with -area-surface (or -weight-metric with a metric containing
    similar data) is equivalent to integrating with respect to surface area. For
    example, if you want to find the surface area within an roi, do this:
    
    $ wb_command -metric-weighted-stats roi.func.gii -sum -area-surface
    midthickness.surf.gii.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MetricWeightedStatsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = metric_weighted_stats_cargs(params, execution)
    ret = metric_weighted_stats_outputs(params, execution)
    execution.run(cargs)
    return ret


def metric_weighted_stats(
    metric_in: InputPathType,
    opt_area_surface_area_surface: InputPathType | None = None,
    opt_weight_metric_weight_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    roi: MetricWeightedStatsRoiParameters | None = None,
    opt_mean: bool = False,
    stdev: MetricWeightedStatsStdevParameters | None = None,
    opt_percentile_percent: float | None = None,
    opt_sum: bool = False,
    opt_show_map_name: bool = False,
    runner: Runner | None = None,
) -> MetricWeightedStatsOutputs:
    """
    Weighted spatial statistics on a metric file.
    
    For each column of the input, a line of text is printed, resulting from the
    specified operation. You must specify exactly one of -area-surface or
    -weight-metric. Use -column to only give output for a single column. If the
    -roi option is used without -match-maps, then each line will contain as many
    numbers as there are maps in the ROI file, separated by tab characters.
    Exactly one of -mean, -stdev, -percentile or -sum must be specified.
    
    Using -sum with -area-surface (or -weight-metric with a metric containing
    similar data) is equivalent to integrating with respect to surface area. For
    example, if you want to find the surface area within an roi, do this:
    
    $ wb_command -metric-weighted-stats roi.func.gii -sum -area-surface
    midthickness.surf.gii.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        metric_in: the input metric.
        opt_area_surface_area_surface: use vertex areas as weights: the surface\
            to use for vertex areas.
        opt_weight_metric_weight_metric: use weights from a metric file: metric\
            file containing the weights.
        opt_column_column: only display output for one column: the column\
            number or name.
        roi: only consider data inside an roi.
        opt_mean: compute weighted mean.
        stdev: compute weighted standard deviation.
        opt_percentile_percent: compute weighted percentile: the percentile to\
            find, must be between 0 and 100.
        opt_sum: compute weighted sum.
        opt_show_map_name: print map index and name before each output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricWeightedStatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_WEIGHTED_STATS_METADATA)
    params = metric_weighted_stats_params(metric_in=metric_in, opt_area_surface_area_surface=opt_area_surface_area_surface, opt_weight_metric_weight_metric=opt_weight_metric_weight_metric, opt_column_column=opt_column_column, roi=roi, opt_mean=opt_mean, stdev=stdev, opt_percentile_percent=opt_percentile_percent, opt_sum=opt_sum, opt_show_map_name=opt_show_map_name)
    return metric_weighted_stats_execute(params, execution)


__all__ = [
    "METRIC_WEIGHTED_STATS_METADATA",
    "MetricWeightedStatsOutputs",
    "metric_weighted_stats",
    "metric_weighted_stats_params",
    "metric_weighted_stats_roi_params",
    "metric_weighted_stats_stdev_params",
]
