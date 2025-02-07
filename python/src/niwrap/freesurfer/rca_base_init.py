# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RCA_BASE_INIT_METADATA = Metadata(
    id="40035e4c6889519a8062b007d6e932c3e18ff078.boutiques",
    name="rca-base-init",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
RcaBaseInitParameters = typing.TypedDict('RcaBaseInitParameters', {
    "__STYX_TYPE__": typing.Literal["rca-base-init"],
    "log_file": typing.NotRequired[str | None],
    "status_file": typing.NotRequired[str | None],
    "cmd_file": typing.NotRequired[str | None],
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
        "rca-base-init": rca_base_init_cargs,
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
        "rca-base-init": rca_base_init_outputs,
    }.get(t)


class RcaBaseInitOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rca_base_init(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def rca_base_init_params(
    log_file: str | None = None,
    status_file: str | None = None,
    cmd_file: str | None = None,
) -> RcaBaseInitParameters:
    """
    Build parameters.
    
    Args:
        log_file: Path to the local log file for output.
        status_file: Path to the status file to append logs.
        cmd_file: Path to the command file to append execution commands.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "rca-base-init",
    }
    if log_file is not None:
        params["log_file"] = log_file
    if status_file is not None:
        params["status_file"] = status_file
    if cmd_file is not None:
        params["cmd_file"] = cmd_file
    return params


def rca_base_init_cargs(
    params: RcaBaseInitParameters,
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
    if params.get("log_file") is not None:
        cargs.extend([
            "-init",
            "rca-base" + params.get("log_file")
        ])
    if params.get("status_file") is not None:
        cargs.append(params.get("status_file"))
    if params.get("cmd_file") is not None:
        cargs.append(params.get("cmd_file"))
    return cargs


def rca_base_init_outputs(
    params: RcaBaseInitParameters,
    execution: Execution,
) -> RcaBaseInitOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RcaBaseInitOutputs(
        root=execution.output_file("."),
    )
    return ret


def rca_base_init_execute(
    params: RcaBaseInitParameters,
    execution: Execution,
) -> RcaBaseInitOutputs:
    """
    Initialize base subject for recon-all processing.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RcaBaseInitOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = rca_base_init_cargs(params, execution)
    ret = rca_base_init_outputs(params, execution)
    execution.run(cargs)
    return ret


def rca_base_init(
    log_file: str | None = None,
    status_file: str | None = None,
    cmd_file: str | None = None,
    runner: Runner | None = None,
) -> RcaBaseInitOutputs:
    """
    Initialize base subject for recon-all processing.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        log_file: Path to the local log file for output.
        status_file: Path to the status file to append logs.
        cmd_file: Path to the command file to append execution commands.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RcaBaseInitOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RCA_BASE_INIT_METADATA)
    params = rca_base_init_params(log_file=log_file, status_file=status_file, cmd_file=cmd_file)
    return rca_base_init_execute(params, execution)


__all__ = [
    "RCA_BASE_INIT_METADATA",
    "RcaBaseInitOutputs",
    "RcaBaseInitParameters",
    "rca_base_init",
    "rca_base_init_params",
]
