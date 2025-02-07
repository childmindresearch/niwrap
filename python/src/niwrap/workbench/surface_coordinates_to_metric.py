# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURFACE_COORDINATES_TO_METRIC_METADATA = Metadata(
    id="0f7e2511cce185227bdef48e1289a112b38532ef.boutiques",
    name="surface-coordinates-to-metric",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
SurfaceCoordinatesToMetricParameters = typing.TypedDict('SurfaceCoordinatesToMetricParameters', {
    "__STYX_TYPE__": typing.Literal["surface-coordinates-to-metric"],
    "surface": InputPathType,
    "metric_out": str,
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
        "surface-coordinates-to-metric": surface_coordinates_to_metric_cargs,
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
        "surface-coordinates-to-metric": surface_coordinates_to_metric_outputs,
    }.get(t)


class SurfaceCoordinatesToMetricOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_coordinates_to_metric(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def surface_coordinates_to_metric_params(
    surface: InputPathType,
    metric_out: str,
) -> SurfaceCoordinatesToMetricParameters:
    """
    Build parameters.
    
    Args:
        surface: the surface to use the coordinates of.
        metric_out: the output metric.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surface-coordinates-to-metric",
        "surface": surface,
        "metric_out": metric_out,
    }
    return params


def surface_coordinates_to_metric_cargs(
    params: SurfaceCoordinatesToMetricParameters,
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
    cargs.append("-surface-coordinates-to-metric")
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(params.get("metric_out"))
    return cargs


def surface_coordinates_to_metric_outputs(
    params: SurfaceCoordinatesToMetricParameters,
    execution: Execution,
) -> SurfaceCoordinatesToMetricOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfaceCoordinatesToMetricOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(params.get("metric_out")),
    )
    return ret


def surface_coordinates_to_metric_execute(
    params: SurfaceCoordinatesToMetricParameters,
    execution: Execution,
) -> SurfaceCoordinatesToMetricOutputs:
    """
    Make metric file of surface coordinates.
    
    Puts the coordinates of the surface into a 3-map metric file, as x, y, z.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfaceCoordinatesToMetricOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = surface_coordinates_to_metric_cargs(params, execution)
    ret = surface_coordinates_to_metric_outputs(params, execution)
    execution.run(cargs)
    return ret


def surface_coordinates_to_metric(
    surface: InputPathType,
    metric_out: str,
    runner: Runner | None = None,
) -> SurfaceCoordinatesToMetricOutputs:
    """
    Make metric file of surface coordinates.
    
    Puts the coordinates of the surface into a 3-map metric file, as x, y, z.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface: the surface to use the coordinates of.
        metric_out: the output metric.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceCoordinatesToMetricOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_COORDINATES_TO_METRIC_METADATA)
    params = surface_coordinates_to_metric_params(surface=surface, metric_out=metric_out)
    return surface_coordinates_to_metric_execute(params, execution)


__all__ = [
    "SURFACE_COORDINATES_TO_METRIC_METADATA",
    "SurfaceCoordinatesToMetricOutputs",
    "SurfaceCoordinatesToMetricParameters",
    "surface_coordinates_to_metric",
    "surface_coordinates_to_metric_params",
]
