# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FS_TIME_METADATA = Metadata(
    id="ca61b3d7c09ab70471b0b19e87ec76f60e282835.boutiques",
    name="fs_time",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
FsTimeParameters = typing.TypedDict('FsTimeParameters', {
    "__STYX_TYPE__": typing.Literal["fs_time"],
    "output_file": typing.NotRequired[str | None],
    "key": typing.NotRequired[str | None],
    "load_avg": bool,
    "command": str,
    "args": typing.NotRequired[list[str] | None],
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
        "fs_time": fs_time_cargs,
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
        "fs_time": fs_time_outputs,
    }.get(t)


class FsTimeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fs_time(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    resource_output: OutputPathType | None
    """File containing resource usage information."""


def fs_time_params(
    command: str,
    output_file: str | None = None,
    key: str | None = None,
    load_avg: bool = False,
    args: list[str] | None = None,
) -> FsTimeParameters:
    """
    Build parameters.
    
    Args:
        command: The command to be timed with fs_time.
        output_file: Save resource info into output file.
        key: Specify a key for the resource information.
        load_avg: Report on load averages as from uptime.
        args: Arguments for the command.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fs_time",
        "load_avg": load_avg,
        "command": command,
    }
    if output_file is not None:
        params["output_file"] = output_file
    if key is not None:
        params["key"] = key
    if args is not None:
        params["args"] = args
    return params


def fs_time_cargs(
    params: FsTimeParameters,
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
    cargs.append("fs_time")
    if params.get("output_file") is not None:
        cargs.extend([
            "-o",
            params.get("output_file")
        ])
    if params.get("key") is not None:
        cargs.extend([
            "-k",
            params.get("key")
        ])
    if params.get("load_avg"):
        cargs.append("-l")
    cargs.append(params.get("command"))
    if params.get("args") is not None:
        cargs.extend(params.get("args"))
    return cargs


def fs_time_outputs(
    params: FsTimeParameters,
    execution: Execution,
) -> FsTimeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FsTimeOutputs(
        root=execution.output_file("."),
        resource_output=execution.output_file(params.get("output_file")) if (params.get("output_file") is not None) else None,
    )
    return ret


def fs_time_execute(
    params: FsTimeParameters,
    execution: Execution,
) -> FsTimeOutputs:
    """
    A frontend for the unix /usr/bin/time program to track resource usage by a
    process.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FsTimeOutputs`).
    """
    cargs = fs_time_cargs(params, execution)
    ret = fs_time_outputs(params, execution)
    execution.run(cargs)
    return ret


def fs_time(
    command: str,
    output_file: str | None = None,
    key: str | None = None,
    load_avg: bool = False,
    args: list[str] | None = None,
    runner: Runner | None = None,
) -> FsTimeOutputs:
    """
    A frontend for the unix /usr/bin/time program to track resource usage by a
    process.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        command: The command to be timed with fs_time.
        output_file: Save resource info into output file.
        key: Specify a key for the resource information.
        load_avg: Report on load averages as from uptime.
        args: Arguments for the command.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FsTimeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FS_TIME_METADATA)
    params = fs_time_params(output_file=output_file, key=key, load_avg=load_avg, command=command, args=args)
    return fs_time_execute(params, execution)


__all__ = [
    "FS_TIME_METADATA",
    "FsTimeOutputs",
    "FsTimeParameters",
    "fs_time",
    "fs_time_params",
]
