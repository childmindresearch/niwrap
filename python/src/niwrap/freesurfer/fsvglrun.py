# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSVGLRUN_METADATA = Metadata(
    id="5ac643a495dfd3b7b90655e3aff808accc7f76dd.boutiques",
    name="fsvglrun",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
FsvglrunParameters = typing.TypedDict('FsvglrunParameters', {
    "__STYX_TYPE__": typing.Literal["fsvglrun"],
    "zeroth_arg_name": typing.NotRequired[str | None],
    "empty_env": bool,
    "dashed_arg": bool,
    "command": str,
    "command_args": typing.NotRequired[list[str] | None],
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
        "fsvglrun": fsvglrun_cargs,
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


class FsvglrunOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsvglrun(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fsvglrun_params(
    command: str,
    zeroth_arg_name: str | None = None,
    empty_env: bool = False,
    dashed_arg: bool = False,
    command_args: list[str] | None = None,
) -> FsvglrunParameters:
    """
    Build parameters.
    
    Args:
        command: The command to be executed, replacing the shell with the\
            specified program.
        zeroth_arg_name: Pass NAME as the zeroth argument to COMMAND.
        empty_env: Execute COMMAND with an empty environment.
        dashed_arg: Place a dash in the zeroth argument to COMMAND.
        command_args: Arguments for the command executed by fsvglrun.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fsvglrun",
        "empty_env": empty_env,
        "dashed_arg": dashed_arg,
        "command": command,
    }
    if zeroth_arg_name is not None:
        params["zeroth_arg_name"] = zeroth_arg_name
    if command_args is not None:
        params["command_args"] = command_args
    return params


def fsvglrun_cargs(
    params: FsvglrunParameters,
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
    cargs.append("fsvglrun")
    if params.get("zeroth_arg_name") is not None:
        cargs.extend([
            "-a",
            params.get("zeroth_arg_name")
        ])
    if params.get("empty_env"):
        cargs.append("-c")
    if params.get("dashed_arg"):
        cargs.append("-l")
    cargs.append(params.get("command"))
    if params.get("command_args") is not None:
        cargs.extend(params.get("command_args"))
    return cargs


def fsvglrun_outputs(
    params: FsvglrunParameters,
    execution: Execution,
) -> FsvglrunOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FsvglrunOutputs(
        root=execution.output_file("."),
    )
    return ret


def fsvglrun_execute(
    params: FsvglrunParameters,
    execution: Execution,
) -> FsvglrunOutputs:
    """
    A tool to execute a command, replacing the shell with the specified program,
    typically used within FreeSurfer environment.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FsvglrunOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fsvglrun_cargs(params, execution)
    ret = fsvglrun_outputs(params, execution)
    execution.run(cargs)
    return ret


def fsvglrun(
    command: str,
    zeroth_arg_name: str | None = None,
    empty_env: bool = False,
    dashed_arg: bool = False,
    command_args: list[str] | None = None,
    runner: Runner | None = None,
) -> FsvglrunOutputs:
    """
    A tool to execute a command, replacing the shell with the specified program,
    typically used within FreeSurfer environment.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        command: The command to be executed, replacing the shell with the\
            specified program.
        zeroth_arg_name: Pass NAME as the zeroth argument to COMMAND.
        empty_env: Execute COMMAND with an empty environment.
        dashed_arg: Place a dash in the zeroth argument to COMMAND.
        command_args: Arguments for the command executed by fsvglrun.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FsvglrunOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSVGLRUN_METADATA)
    params = fsvglrun_params(zeroth_arg_name=zeroth_arg_name, empty_env=empty_env, dashed_arg=dashed_arg, command=command, command_args=command_args)
    return fsvglrun_execute(params, execution)


__all__ = [
    "FSVGLRUN_METADATA",
    "FsvglrunOutputs",
    "FsvglrunParameters",
    "fsvglrun",
    "fsvglrun_params",
]
