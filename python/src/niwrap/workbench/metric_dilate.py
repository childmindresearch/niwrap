# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


METRIC_DILATE_METADATA = Metadata(
    id="dfb291b57100175c109304a83ed43ba7db6d794b",
    name="metric-dilate",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class MetricDilateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_dilate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def metric_dilate(
    metric: InputPathType,
    surface: InputPathType,
    distance: float | int,
    metric_out: InputPathType,
    opt_bad_vertex_roi_roi_metric: InputPathType | None = None,
    opt_data_roi_roi_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    opt_nearest: bool = False,
    opt_linear: bool = False,
    opt_exponent_exponent: float | int | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    opt_legacy_cutoff: bool = False,
    runner: Runner = None,
) -> MetricDilateOutputs:
    """
    metric-dilate by Washington University School of Medicin.
    
    DILATE A METRIC FILE.
    
    For all metric vertices that are designated as bad, if they neighbor a
    non-bad vertex with data or are within the specified distance of such a
    vertex, replace the value with a distance-based weighted average of nearby
    non-bad vertices that have data, otherwise set the value to zero. No matter
    how small <distance> is, dilation will always use at least the immediate
    neighbor vertices. If -nearest is specified, it will use the value from the
    closest non-bad vertex with data within range instead of a weighted average.
    
    If -bad-vertex-roi is specified, all vertices with a positive ROI value are
    bad. If it is not specified, only vertices that have data, with a value of
    zero, are bad. If -data-roi is not specified, all vertices are assumed to
    have data.
    
    Note that the -corrected-areas option uses an approximate correction for the
    change in distances along a group average surface.
    
    To get the behavior of version 1.3.2 or earlier, use '-legacy-cutoff
    -exponent 2'.
    
    Args:
        metric: the metric to dilate
        surface: the surface to compute on
        distance: distance in mm to dilate
        metric_out: the output metric
        opt_bad_vertex_roi_roi_metric: specify an roi of vertices to overwrite,
            rather than vertices with value zero: metric file, positive values
            denote vertices to have their values replaced
        opt_data_roi_roi_metric: specify an roi of where there is data: metric
            file, positive values denote vertices that have data
        opt_column_column: select a single column to dilate: the column number
            or name
        opt_nearest: use the nearest good value instead of a weighted average
        opt_linear: fill in values with linear interpolation along strongest
            gradient
        opt_exponent_exponent: use a different exponent in the weighting
            function: exponent 'n' to use in (area / (distance ^ n)) as the
            weighting function (default 6)
        opt_corrected_areas_area_metric: vertex areas to use instead of
            computing them from the surface: the corrected vertex areas, as a metric
        opt_legacy_cutoff: use the v1.3.2 method of choosing how many vertices
            to use when calulating the dilated value with weighted method
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `MetricDilateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_DILATE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-dilate")
    cargs.append(execution.input_file(metric))
    cargs.append(execution.input_file(surface))
    cargs.append(str(distance))
    cargs.append(execution.input_file(metric_out))
    if opt_bad_vertex_roi_roi_metric is not None:
        cargs.extend(["-bad-vertex-roi", execution.input_file(opt_bad_vertex_roi_roi_metric)])
    if opt_data_roi_roi_metric is not None:
        cargs.extend(["-data-roi", execution.input_file(opt_data_roi_roi_metric)])
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    if opt_nearest:
        cargs.append("-nearest")
    if opt_linear:
        cargs.append("-linear")
    if opt_exponent_exponent is not None:
        cargs.extend(["-exponent", str(opt_exponent_exponent)])
    if opt_corrected_areas_area_metric is not None:
        cargs.extend(["-corrected-areas", execution.input_file(opt_corrected_areas_area_metric)])
    if opt_legacy_cutoff:
        cargs.append("-legacy-cutoff")
    ret = MetricDilateOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(f"{pathlib.Path(metric_out).stem}"),
    )
    execution.run(cargs)
    return ret
