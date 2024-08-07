# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

METRIC_REMOVE_ISLANDS_METADATA = Metadata(
    id="440d12a75637613f30664d272f6058985f089df7",
    name="metric-remove-islands",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class MetricRemoveIslandsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_remove_islands(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output ROI metric"""


def metric_remove_islands(
    surface: InputPathType,
    metric_in: InputPathType,
    metric_out: str,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    runner: Runner | None = None,
) -> MetricRemoveIslandsOutputs:
    """
    metric-remove-islands by Washington University School of Medicin.
    
    Remove islands from an roi metric.
    
    Finds all connected areas in the ROI, and zeros out all but the largest one,
    in terms of surface area.
    
    Args:
        surface: the surface to use for neighbor information.
        metric_in: the input ROI metric.
        metric_out: the output ROI metric.
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricRemoveIslandsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_REMOVE_ISLANDS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-remove-islands")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(metric_in))
    cargs.append(metric_out)
    if opt_corrected_areas_area_metric is not None:
        cargs.extend(["-corrected-areas", execution.input_file(opt_corrected_areas_area_metric)])
    ret = MetricRemoveIslandsOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(f"{metric_out}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "METRIC_REMOVE_ISLANDS_METADATA",
    "MetricRemoveIslandsOutputs",
    "metric_remove_islands",
]
