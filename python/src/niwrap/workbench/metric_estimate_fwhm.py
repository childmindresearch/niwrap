# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

METRIC_ESTIMATE_FWHM_METADATA = Metadata(
    id="93d4c4a8c6da0ee8cc2cc4c3da48da105c37ad7e.boutiques",
    name="metric-estimate-fwhm",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
MetricEstimateFwhmWholeFileParameters = typing.TypedDict('MetricEstimateFwhmWholeFileParameters', {
    "__STYX_TYPE__": typing.Literal["whole_file"],
    "opt_demean": bool,
})
MetricEstimateFwhmParameters = typing.TypedDict('MetricEstimateFwhmParameters', {
    "__STYX_TYPE__": typing.Literal["metric-estimate-fwhm"],
    "surface": InputPathType,
    "metric_in": InputPathType,
    "opt_roi_roi_metric": typing.NotRequired[InputPathType | None],
    "opt_column_column": typing.NotRequired[str | None],
    "whole_file": typing.NotRequired[MetricEstimateFwhmWholeFileParameters | None],
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
        "metric-estimate-fwhm": metric_estimate_fwhm_cargs,
        "whole_file": metric_estimate_fwhm_whole_file_cargs,
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


def metric_estimate_fwhm_whole_file_params(
    opt_demean: bool = False,
) -> MetricEstimateFwhmWholeFileParameters:
    """
    Build parameters.
    
    Args:
        opt_demean: subtract the mean image before estimating smoothness.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "whole_file",
        "opt_demean": opt_demean,
    }
    return params


def metric_estimate_fwhm_whole_file_cargs(
    params: MetricEstimateFwhmWholeFileParameters,
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
    cargs.append("-whole-file")
    if params.get("opt_demean"):
        cargs.append("-demean")
    return cargs


class MetricEstimateFwhmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_estimate_fwhm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def metric_estimate_fwhm_params(
    surface: InputPathType,
    metric_in: InputPathType,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    whole_file: MetricEstimateFwhmWholeFileParameters | None = None,
) -> MetricEstimateFwhmParameters:
    """
    Build parameters.
    
    Args:
        surface: the surface to use for distance and neighbor information.
        metric_in: the input metric.
        opt_roi_roi_metric: use only data within an ROI: the metric file to use\
            as an ROI.
        opt_column_column: select a single column to estimate smoothness of:\
            the column number or name.
        whole_file: estimate for the whole file at once, not each column\
            separately.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "metric-estimate-fwhm",
        "surface": surface,
        "metric_in": metric_in,
    }
    if opt_roi_roi_metric is not None:
        params["opt_roi_roi_metric"] = opt_roi_roi_metric
    if opt_column_column is not None:
        params["opt_column_column"] = opt_column_column
    if whole_file is not None:
        params["whole_file"] = whole_file
    return params


def metric_estimate_fwhm_cargs(
    params: MetricEstimateFwhmParameters,
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
    cargs.append("-metric-estimate-fwhm")
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(execution.input_file(params.get("metric_in")))
    if params.get("opt_roi_roi_metric") is not None:
        cargs.extend([
            "-roi",
            execution.input_file(params.get("opt_roi_roi_metric"))
        ])
    if params.get("opt_column_column") is not None:
        cargs.extend([
            "-column",
            params.get("opt_column_column")
        ])
    if params.get("whole_file") is not None:
        cargs.extend(dyn_cargs(params.get("whole_file")["__STYXTYPE__"])(params.get("whole_file"), execution))
    return cargs


def metric_estimate_fwhm_outputs(
    params: MetricEstimateFwhmParameters,
    execution: Execution,
) -> MetricEstimateFwhmOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MetricEstimateFwhmOutputs(
        root=execution.output_file("."),
    )
    return ret


def metric_estimate_fwhm_execute(
    params: MetricEstimateFwhmParameters,
    execution: Execution,
) -> MetricEstimateFwhmOutputs:
    """
    Estimate fwhm smoothness of a metric file.
    
    Estimates the smoothness of the metric columns, printing the estimates to
    standard output. These estimates ignore variation in vertex spacing.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MetricEstimateFwhmOutputs`).
    """
    params = execution.params(params)
    cargs = metric_estimate_fwhm_cargs(params, execution)
    ret = metric_estimate_fwhm_outputs(params, execution)
    execution.run(cargs)
    return ret


def metric_estimate_fwhm(
    surface: InputPathType,
    metric_in: InputPathType,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    whole_file: MetricEstimateFwhmWholeFileParameters | None = None,
    runner: Runner | None = None,
) -> MetricEstimateFwhmOutputs:
    """
    Estimate fwhm smoothness of a metric file.
    
    Estimates the smoothness of the metric columns, printing the estimates to
    standard output. These estimates ignore variation in vertex spacing.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface: the surface to use for distance and neighbor information.
        metric_in: the input metric.
        opt_roi_roi_metric: use only data within an ROI: the metric file to use\
            as an ROI.
        opt_column_column: select a single column to estimate smoothness of:\
            the column number or name.
        whole_file: estimate for the whole file at once, not each column\
            separately.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricEstimateFwhmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_ESTIMATE_FWHM_METADATA)
    params = metric_estimate_fwhm_params(surface=surface, metric_in=metric_in, opt_roi_roi_metric=opt_roi_roi_metric, opt_column_column=opt_column_column, whole_file=whole_file)
    return metric_estimate_fwhm_execute(params, execution)


__all__ = [
    "METRIC_ESTIMATE_FWHM_METADATA",
    "MetricEstimateFwhmOutputs",
    "MetricEstimateFwhmParameters",
    "MetricEstimateFwhmWholeFileParameters",
    "metric_estimate_fwhm",
    "metric_estimate_fwhm_params",
    "metric_estimate_fwhm_whole_file_params",
]
