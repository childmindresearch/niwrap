# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:56:52.639002

import typing

from ..styxdefs import *


METRIC_FILL_HOLES_METADATA = Metadata(
    id="5819f20642f4257428e8d52990862e461e56c9a7",
    name="metric-fill-holes",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class MetricFillHolesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_fill_holes(...)`.
    """
    metric_out: OutputPathType
    """the output ROI metric"""


def metric_fill_holes(
    runner: Runner,
    surface: InputPathType,
    metric_in: InputPathType,
    metric_out: InputPathType,
    opt_corrected_areas_area_metric: InputPathType | None = None,
) -> MetricFillHolesOutputs:
    """
    FILL HOLES IN AN ROI METRIC.
    
    Finds all connected areas that are not included in the ROI, and writes ones
    into all but the largest one, in terms of surface area.
    
    Args:
        runner: Command runner
        surface: the surface to use for neighbor information
        metric_in: the input ROI metric
        metric_out: the output ROI metric
        opt_corrected_areas_area_metric: vertex areas to use instead of
            computing them from the surface: the corrected vertex areas, as a metric
    Returns:
        NamedTuple of outputs (described in `MetricFillHolesOutputs`).
    """
    execution = runner.start_execution(METRIC_FILL_HOLES_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-fill-holes")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(metric_in))
    cargs.append(execution.input_file(metric_out))
    if opt_corrected_areas_area_metric is not None:
        cargs.extend(["-corrected-areas", execution.input_file(opt_corrected_areas_area_metric)])
    ret = MetricFillHolesOutputs(
        metric_out=execution.output_file(f"{metric_out}"),
    )
    execution.run(cargs)
    return ret
