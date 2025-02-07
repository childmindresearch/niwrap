# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

BACKEND_AVERAGE_DENSE_ROI_METADATA = Metadata(
    id="8daccd3e1d4e01fd363a65e41aec0093bc0081b4.boutiques",
    name="backend-average-dense-roi",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
BackendAverageDenseRoiParameters = typing.TypedDict('BackendAverageDenseRoiParameters', {
    "__STYX_TYPE__": typing.Literal["backend-average-dense-roi"],
    "index_list": str,
    "out_file": str,
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
        "backend-average-dense-roi": backend_average_dense_roi_cargs,
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
        "backend-average-dense-roi": backend_average_dense_roi_outputs,
    }.get(t)


class BackendAverageDenseRoiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `backend_average_dense_roi(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def backend_average_dense_roi_params(
    index_list: str,
    out_file: str,
) -> BackendAverageDenseRoiParameters:
    """
    Build parameters.
    
    Args:
        index_list: comma separated list of cifti indexes to average.
        out_file: file to write the average row to.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "backend-average-dense-roi",
        "index_list": index_list,
        "out_file": out_file,
    }
    return params


def backend_average_dense_roi_cargs(
    params: BackendAverageDenseRoiParameters,
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
    cargs.append("-backend-average-dense-roi")
    cargs.append(params.get("index_list"))
    cargs.append(params.get("out_file"))
    return cargs


def backend_average_dense_roi_outputs(
    params: BackendAverageDenseRoiParameters,
    execution: Execution,
) -> BackendAverageDenseRoiOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BackendAverageDenseRoiOutputs(
        root=execution.output_file("."),
    )
    return ret


def backend_average_dense_roi_execute(
    params: BackendAverageDenseRoiParameters,
    execution: Execution,
) -> BackendAverageDenseRoiOutputs:
    """
    Connectome db backend command for cifti average dense roi.
    
    This command is probably not the one you are looking for, try
    -cifti-average-dense-roi. It takes the list of cifti files to average from
    standard input, and writes its output as little endian, 32-bit integer of
    row size followed by the row as 32-bit floats.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BackendAverageDenseRoiOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = backend_average_dense_roi_cargs(params, execution)
    ret = backend_average_dense_roi_outputs(params, execution)
    execution.run(cargs)
    return ret


def backend_average_dense_roi(
    index_list: str,
    out_file: str,
    runner: Runner | None = None,
) -> BackendAverageDenseRoiOutputs:
    """
    Connectome db backend command for cifti average dense roi.
    
    This command is probably not the one you are looking for, try
    -cifti-average-dense-roi. It takes the list of cifti files to average from
    standard input, and writes its output as little endian, 32-bit integer of
    row size followed by the row as 32-bit floats.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        index_list: comma separated list of cifti indexes to average.
        out_file: file to write the average row to.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BackendAverageDenseRoiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BACKEND_AVERAGE_DENSE_ROI_METADATA)
    params = backend_average_dense_roi_params(index_list=index_list, out_file=out_file)
    return backend_average_dense_roi_execute(params, execution)


__all__ = [
    "BACKEND_AVERAGE_DENSE_ROI_METADATA",
    "BackendAverageDenseRoiOutputs",
    "BackendAverageDenseRoiParameters",
    "backend_average_dense_roi",
    "backend_average_dense_roi_params",
]
