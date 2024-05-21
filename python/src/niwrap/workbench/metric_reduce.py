# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


METRIC_REDUCE_METADATA = Metadata(
    id="ebef5f52ff3c445e6d52533b1b4c17393368decd",
    name="metric-reduce",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class MetricReduceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_reduce(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def metric_reduce(
    metric_in: InputPathType,
    operation: str,
    metric_out: InputPathType,
    opt_only_numeric: bool = False,
    runner: Runner = None,
) -> MetricReduceOutputs:
    """
    metric-reduce by Washington University School of Medicin.
    
    PERFORM REDUCTION OPERATION ACROSS METRIC COLUMNS.
    
    For each surface vertex, takes the data across columns as a vector, and
    performs the specified reduction on it, putting the result into the single
    output column at that vertex. The reduction operators are as follows:
    
    MAX: the maximum value
    MIN: the minimum value
    INDEXMAX: the 1-based index of the maximum value
    INDEXMIN: the 1-based index of the minimum value
    SUM: add all values
    PRODUCT: multiply all values
    MEAN: the mean of the data
    STDEV: the standard deviation (N denominator)
    SAMPSTDEV: the sample standard deviation (N-1 denominator)
    VARIANCE: the variance of the data
    TSNR: mean divided by sample standard deviation (N-1 denominator)
    COV: sample standard deviation (N-1 denominator) divided by mean
    L2NORM: square root of sum of squares
    MEDIAN: the median of the data
    MODE: the mode of the data
    COUNT_NONZERO: the number of nonzero elements in the data
    .
    
    Args:
        metric_in: the metric to reduce
        operation: the reduction operator to use
        metric_out: the output metric
        opt_only_numeric: exclude non-numeric values
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `MetricReduceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_REDUCE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-reduce")
    cargs.append(execution.input_file(metric_in))
    cargs.append(operation)
    cargs.append(execution.input_file(metric_out))
    if opt_only_numeric:
        cargs.append("-only-numeric")
    ret = MetricReduceOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(f"{pathlib.Path(metric_out).stem}"),
    )
    execution.run(cargs)
    return ret
