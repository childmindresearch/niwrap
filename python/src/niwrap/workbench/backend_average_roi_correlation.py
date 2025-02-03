# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

BACKEND_AVERAGE_ROI_CORRELATION_METADATA = Metadata(
    id="92d29c21c9c3c279b64b735c2a3ea9a41a57d6cd.boutiques",
    name="backend-average-roi-correlation",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
BackendAverageRoiCorrelationParameters = typing.TypedDict('BackendAverageRoiCorrelationParameters', {
    "__STYX_TYPE__": typing.Literal["backend-average-roi-correlation"],
    "index_list": str,
    "out_file": str,
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
        "backend-average-roi-correlation": backend_average_roi_correlation_cargs,
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


class BackendAverageRoiCorrelationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `backend_average_roi_correlation(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def backend_average_roi_correlation_params(
    index_list: str,
    out_file: str,
) -> BackendAverageRoiCorrelationParameters:
    """
    Build parameters.
    
    Args:
        index_list: comma separated list of cifti indexes to average and then\
            correlate.
        out_file: file to write the average row to.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "backend-average-roi-correlation",
        "index_list": index_list,
        "out_file": out_file,
    }
    return params


def backend_average_roi_correlation_cargs(
    params: BackendAverageRoiCorrelationParameters,
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
    cargs.append("-backend-average-roi-correlation")
    cargs.append(params.get("index_list"))
    cargs.append(params.get("out_file"))
    return cargs


def backend_average_roi_correlation_outputs(
    params: BackendAverageRoiCorrelationParameters,
    execution: Execution,
) -> BackendAverageRoiCorrelationOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BackendAverageRoiCorrelationOutputs(
        root=execution.output_file("."),
    )
    return ret


def backend_average_roi_correlation_execute(
    params: BackendAverageRoiCorrelationParameters,
    execution: Execution,
) -> BackendAverageRoiCorrelationOutputs:
    """
    Connectome db backend command for cifti average roi correlation.
    
    This command is probably not the one you are looking for, try
    -cifti-average-roi-correlation. It takes the list of cifti files to average
    from standard input, and writes its output as little endian, 32-bit integer
    of row size followed by the row as 32-bit floats.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BackendAverageRoiCorrelationOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = backend_average_roi_correlation_cargs(params, execution)
    ret = backend_average_roi_correlation_outputs(params, execution)
    execution.run(cargs)
    return ret


def backend_average_roi_correlation(
    index_list: str,
    out_file: str,
    runner: Runner | None = None,
) -> BackendAverageRoiCorrelationOutputs:
    """
    Connectome db backend command for cifti average roi correlation.
    
    This command is probably not the one you are looking for, try
    -cifti-average-roi-correlation. It takes the list of cifti files to average
    from standard input, and writes its output as little endian, 32-bit integer
    of row size followed by the row as 32-bit floats.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        index_list: comma separated list of cifti indexes to average and then\
            correlate.
        out_file: file to write the average row to.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BackendAverageRoiCorrelationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BACKEND_AVERAGE_ROI_CORRELATION_METADATA)
    params = backend_average_roi_correlation_params(index_list=index_list, out_file=out_file)
    return backend_average_roi_correlation_execute(params, execution)


__all__ = [
    "BACKEND_AVERAGE_ROI_CORRELATION_METADATA",
    "BackendAverageRoiCorrelationOutputs",
    "backend_average_roi_correlation",
    "backend_average_roi_correlation_params",
]
