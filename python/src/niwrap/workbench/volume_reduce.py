# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

VOLUME_REDUCE_METADATA = Metadata(
    id="00b070cbd951ede68c79c38901e32520aed29ba6.boutiques",
    name="volume-reduce",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
VolumeReduceExcludeOutliersParameters = typing.TypedDict('VolumeReduceExcludeOutliersParameters', {
    "__STYX_TYPE__": typing.Literal["exclude_outliers"],
    "sigma_below": float,
    "sigma_above": float,
})
VolumeReduceParameters = typing.TypedDict('VolumeReduceParameters', {
    "__STYX_TYPE__": typing.Literal["volume-reduce"],
    "volume_in": InputPathType,
    "operation": str,
    "volume_out": str,
    "exclude_outliers": typing.NotRequired[VolumeReduceExcludeOutliersParameters | None],
    "opt_only_numeric": bool,
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
        "volume-reduce": volume_reduce_cargs,
        "exclude_outliers": volume_reduce_exclude_outliers_cargs,
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
        "volume-reduce": volume_reduce_outputs,
    }
    return vt.get(t)


def volume_reduce_exclude_outliers_params(
    sigma_below: float,
    sigma_above: float,
) -> VolumeReduceExcludeOutliersParameters:
    """
    Build parameters.
    
    Args:
        sigma_below: number of standard deviations below the mean to include.
        sigma_above: number of standard deviations above the mean to include.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "exclude_outliers",
        "sigma_below": sigma_below,
        "sigma_above": sigma_above,
    }
    return params


def volume_reduce_exclude_outliers_cargs(
    params: VolumeReduceExcludeOutliersParameters,
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
    cargs.append("-exclude-outliers")
    cargs.append(str(params.get("sigma_below")))
    cargs.append(str(params.get("sigma_above")))
    return cargs


class VolumeReduceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_reduce(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume"""


def volume_reduce_params(
    volume_in: InputPathType,
    operation: str,
    volume_out: str,
    exclude_outliers: VolumeReduceExcludeOutliersParameters | None = None,
    opt_only_numeric: bool = False,
) -> VolumeReduceParameters:
    """
    Build parameters.
    
    Args:
        volume_in: the volume file to reduce.
        operation: the reduction operator to use.
        volume_out: the output volume.
        exclude_outliers: exclude non-numeric values and outliers by standard\
            deviation.
        opt_only_numeric: exclude non-numeric values.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume-reduce",
        "volume_in": volume_in,
        "operation": operation,
        "volume_out": volume_out,
        "opt_only_numeric": opt_only_numeric,
    }
    if exclude_outliers is not None:
        params["exclude_outliers"] = exclude_outliers
    return params


def volume_reduce_cargs(
    params: VolumeReduceParameters,
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
    cargs.append("-volume-reduce")
    cargs.append(execution.input_file(params.get("volume_in")))
    cargs.append(params.get("operation"))
    cargs.append(params.get("volume_out"))
    if params.get("exclude_outliers") is not None:
        cargs.extend(dyn_cargs(params.get("exclude_outliers")["__STYXTYPE__"])(params.get("exclude_outliers"), execution))
    if params.get("opt_only_numeric"):
        cargs.append("-only-numeric")
    return cargs


def volume_reduce_outputs(
    params: VolumeReduceParameters,
    execution: Execution,
) -> VolumeReduceOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VolumeReduceOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(params.get("volume_out")),
    )
    return ret


def volume_reduce_execute(
    params: VolumeReduceParameters,
    execution: Execution,
) -> VolumeReduceOutputs:
    """
    Perform reduction operation across subvolumes.
    
    For each voxel, takes the data across subvolumes as a vector, and performs
    the specified reduction on it, putting the result into the single output
    volume at that voxel. The reduction operators are as follows:
    
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
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VolumeReduceOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = volume_reduce_cargs(params, execution)
    ret = volume_reduce_outputs(params, execution)
    execution.run(cargs)
    return ret


def volume_reduce(
    volume_in: InputPathType,
    operation: str,
    volume_out: str,
    exclude_outliers: VolumeReduceExcludeOutliersParameters | None = None,
    opt_only_numeric: bool = False,
    runner: Runner | None = None,
) -> VolumeReduceOutputs:
    """
    Perform reduction operation across subvolumes.
    
    For each voxel, takes the data across subvolumes as a vector, and performs
    the specified reduction on it, putting the result into the single output
    volume at that voxel. The reduction operators are as follows:
    
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
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        volume_in: the volume file to reduce.
        operation: the reduction operator to use.
        volume_out: the output volume.
        exclude_outliers: exclude non-numeric values and outliers by standard\
            deviation.
        opt_only_numeric: exclude non-numeric values.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeReduceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_REDUCE_METADATA)
    params = volume_reduce_params(volume_in=volume_in, operation=operation, volume_out=volume_out, exclude_outliers=exclude_outliers, opt_only_numeric=opt_only_numeric)
    return volume_reduce_execute(params, execution)


__all__ = [
    "VOLUME_REDUCE_METADATA",
    "VolumeReduceExcludeOutliersParameters",
    "VolumeReduceOutputs",
    "VolumeReduceParameters",
    "volume_reduce",
    "volume_reduce_exclude_outliers_params",
    "volume_reduce_params",
]
