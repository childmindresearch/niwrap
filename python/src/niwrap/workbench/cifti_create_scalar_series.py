# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CIFTI_CREATE_SCALAR_SERIES_METADATA = Metadata(
    id="baeec4f19b77cff9ac7b9fbc51ea7e84c97983f3.boutiques",
    name="cifti-create-scalar-series",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
CiftiCreateScalarSeriesSeriesParameters = typing.TypedDict('CiftiCreateScalarSeriesSeriesParameters', {
    "__STYX_TYPE__": typing.Literal["series"],
    "unit": str,
    "start": float,
    "step": float,
})
CiftiCreateScalarSeriesParameters = typing.TypedDict('CiftiCreateScalarSeriesParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-create-scalar-series"],
    "input": str,
    "cifti_out": str,
    "opt_transpose": bool,
    "opt_name_file_file": typing.NotRequired[str | None],
    "series": typing.NotRequired[CiftiCreateScalarSeriesSeriesParameters | None],
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
        "cifti-create-scalar-series": cifti_create_scalar_series_cargs,
        "series": cifti_create_scalar_series_series_cargs,
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
        "cifti-create-scalar-series": cifti_create_scalar_series_outputs,
    }.get(t)


def cifti_create_scalar_series_series_params(
    unit: str,
    start: float,
    step: float,
) -> CiftiCreateScalarSeriesSeriesParameters:
    """
    Build parameters.
    
    Args:
        unit: the unit to use.
        start: the value at the first series point.
        step: the interval between series points.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "series",
        "unit": unit,
        "start": start,
        "step": step,
    }
    return params


def cifti_create_scalar_series_series_cargs(
    params: CiftiCreateScalarSeriesSeriesParameters,
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
    cargs.append("-series")
    cargs.append(params.get("unit"))
    cargs.append(str(params.get("start")))
    cargs.append(str(params.get("step")))
    return cargs


class CiftiCreateScalarSeriesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_create_scalar_series(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """output cifti file"""


def cifti_create_scalar_series_params(
    input_: str,
    cifti_out: str,
    opt_transpose: bool = False,
    opt_name_file_file: str | None = None,
    series: CiftiCreateScalarSeriesSeriesParameters | None = None,
) -> CiftiCreateScalarSeriesParameters:
    """
    Build parameters.
    
    Args:
        input_: input file.
        cifti_out: output cifti file.
        opt_transpose: use if the rows of the text file are along the scalar\
            dimension.
        opt_name_file_file: use a text file to set names on scalar dimension:\
            text file containing names, one per line.
        series: set the units and values of the series.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-create-scalar-series",
        "input": input_,
        "cifti_out": cifti_out,
        "opt_transpose": opt_transpose,
    }
    if opt_name_file_file is not None:
        params["opt_name_file_file"] = opt_name_file_file
    if series is not None:
        params["series"] = series
    return params


def cifti_create_scalar_series_cargs(
    params: CiftiCreateScalarSeriesParameters,
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
    cargs.append("-cifti-create-scalar-series")
    cargs.append(params.get("input"))
    cargs.append(params.get("cifti_out"))
    if params.get("opt_transpose"):
        cargs.append("-transpose")
    if params.get("opt_name_file_file") is not None:
        cargs.extend([
            "-name-file",
            params.get("opt_name_file_file")
        ])
    if params.get("series") is not None:
        cargs.extend(dyn_cargs(params.get("series")["__STYXTYPE__"])(params.get("series"), execution))
    return cargs


def cifti_create_scalar_series_outputs(
    params: CiftiCreateScalarSeriesParameters,
    execution: Execution,
) -> CiftiCreateScalarSeriesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiCreateScalarSeriesOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(params.get("cifti_out")),
    )
    return ret


def cifti_create_scalar_series_execute(
    params: CiftiCreateScalarSeriesParameters,
    execution: Execution,
) -> CiftiCreateScalarSeriesOutputs:
    """
    Import series data into cifti.
    
    Convert a text file containing series of equal length into a cifti file. The
    text file should have lines made up of numbers separated by whitespace, with
    no extra newlines between lines.
    
    The <unit> argument must be one of the following:
    
    SECOND
    HERTZ
    METER
    RADIAN.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiCreateScalarSeriesOutputs`).
    """
    params = execution.params(params)
    cargs = cifti_create_scalar_series_cargs(params, execution)
    ret = cifti_create_scalar_series_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_create_scalar_series(
    input_: str,
    cifti_out: str,
    opt_transpose: bool = False,
    opt_name_file_file: str | None = None,
    series: CiftiCreateScalarSeriesSeriesParameters | None = None,
    runner: Runner | None = None,
) -> CiftiCreateScalarSeriesOutputs:
    """
    Import series data into cifti.
    
    Convert a text file containing series of equal length into a cifti file. The
    text file should have lines made up of numbers separated by whitespace, with
    no extra newlines between lines.
    
    The <unit> argument must be one of the following:
    
    SECOND
    HERTZ
    METER
    RADIAN.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        input_: input file.
        cifti_out: output cifti file.
        opt_transpose: use if the rows of the text file are along the scalar\
            dimension.
        opt_name_file_file: use a text file to set names on scalar dimension:\
            text file containing names, one per line.
        series: set the units and values of the series.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiCreateScalarSeriesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_CREATE_SCALAR_SERIES_METADATA)
    params = cifti_create_scalar_series_params(input_=input_, cifti_out=cifti_out, opt_transpose=opt_transpose, opt_name_file_file=opt_name_file_file, series=series)
    return cifti_create_scalar_series_execute(params, execution)


__all__ = [
    "CIFTI_CREATE_SCALAR_SERIES_METADATA",
    "CiftiCreateScalarSeriesOutputs",
    "CiftiCreateScalarSeriesParameters",
    "CiftiCreateScalarSeriesSeriesParameters",
    "cifti_create_scalar_series",
    "cifti_create_scalar_series_params",
    "cifti_create_scalar_series_series_params",
]
