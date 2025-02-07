# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

METRIC_ROIS_TO_BORDER_METADATA = Metadata(
    id="7055195b90d96406ade3173df1aa38a66c4c45c1.boutiques",
    name="metric-rois-to-border",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
MetricRoisToBorderParameters = typing.TypedDict('MetricRoisToBorderParameters', {
    "__STYX_TYPE__": typing.Literal["metric-rois-to-border"],
    "surface": InputPathType,
    "metric": InputPathType,
    "class_name": str,
    "border_out": str,
    "opt_placement_fraction": typing.NotRequired[float | None],
    "opt_column_column": typing.NotRequired[str | None],
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
        "metric-rois-to-border": metric_rois_to_border_cargs,
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
        "metric-rois-to-border": metric_rois_to_border_outputs,
    }.get(t)


class MetricRoisToBorderOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_rois_to_border(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    border_out: OutputPathType
    """the output border file"""


def metric_rois_to_border_params(
    surface: InputPathType,
    metric: InputPathType,
    class_name: str,
    border_out: str,
    opt_placement_fraction: float | None = None,
    opt_column_column: str | None = None,
) -> MetricRoisToBorderParameters:
    """
    Build parameters.
    
    Args:
        surface: the surface to use for neighbor information.
        metric: the input metric containing ROIs.
        class_name: the name to use for the class of the output borders.
        border_out: the output border file.
        opt_placement_fraction: set how far along the edge border points are\
            drawn: fraction along edge from inside vertex (default 0.33).
        opt_column_column: select a single column: the column number or name.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "metric-rois-to-border",
        "surface": surface,
        "metric": metric,
        "class_name": class_name,
        "border_out": border_out,
    }
    if opt_placement_fraction is not None:
        params["opt_placement_fraction"] = opt_placement_fraction
    if opt_column_column is not None:
        params["opt_column_column"] = opt_column_column
    return params


def metric_rois_to_border_cargs(
    params: MetricRoisToBorderParameters,
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
    cargs.append("-metric-rois-to-border")
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(execution.input_file(params.get("metric")))
    cargs.append(params.get("class_name"))
    cargs.append(params.get("border_out"))
    if params.get("opt_placement_fraction") is not None:
        cargs.extend([
            "-placement",
            str(params.get("opt_placement_fraction"))
        ])
    if params.get("opt_column_column") is not None:
        cargs.extend([
            "-column",
            params.get("opt_column_column")
        ])
    return cargs


def metric_rois_to_border_outputs(
    params: MetricRoisToBorderParameters,
    execution: Execution,
) -> MetricRoisToBorderOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MetricRoisToBorderOutputs(
        root=execution.output_file("."),
        border_out=execution.output_file(params.get("border_out")),
    )
    return ret


def metric_rois_to_border_execute(
    params: MetricRoisToBorderParameters,
    execution: Execution,
) -> MetricRoisToBorderOutputs:
    """
    Draw borders around metric rois.
    
    For each ROI column, finds all edges on the mesh that cross the boundary of
    the ROI, and draws borders through them. By default, this is done on all
    columns in the input file, using the map name as the name for the border.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MetricRoisToBorderOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = metric_rois_to_border_cargs(params, execution)
    ret = metric_rois_to_border_outputs(params, execution)
    execution.run(cargs)
    return ret


def metric_rois_to_border(
    surface: InputPathType,
    metric: InputPathType,
    class_name: str,
    border_out: str,
    opt_placement_fraction: float | None = None,
    opt_column_column: str | None = None,
    runner: Runner | None = None,
) -> MetricRoisToBorderOutputs:
    """
    Draw borders around metric rois.
    
    For each ROI column, finds all edges on the mesh that cross the boundary of
    the ROI, and draws borders through them. By default, this is done on all
    columns in the input file, using the map name as the name for the border.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface: the surface to use for neighbor information.
        metric: the input metric containing ROIs.
        class_name: the name to use for the class of the output borders.
        border_out: the output border file.
        opt_placement_fraction: set how far along the edge border points are\
            drawn: fraction along edge from inside vertex (default 0.33).
        opt_column_column: select a single column: the column number or name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricRoisToBorderOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_ROIS_TO_BORDER_METADATA)
    params = metric_rois_to_border_params(surface=surface, metric=metric, class_name=class_name, border_out=border_out, opt_placement_fraction=opt_placement_fraction, opt_column_column=opt_column_column)
    return metric_rois_to_border_execute(params, execution)


__all__ = [
    "METRIC_ROIS_TO_BORDER_METADATA",
    "MetricRoisToBorderOutputs",
    "MetricRoisToBorderParameters",
    "metric_rois_to_border",
    "metric_rois_to_border_params",
]
