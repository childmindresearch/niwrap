# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__AFNI_RUN_ME_METADATA = Metadata(
    id="aeac26149fa34d0c42e1c07c261b19ac0706d90b.boutiques",
    name="@afni.run.me",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VAfniRunMeParameters = typing.TypedDict('VAfniRunMeParameters', {
    "__STYX_TYPE__": typing.Literal["@afni.run.me"],
    "go": bool,
    "curl": bool,
    "help": bool,
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
        "@afni.run.me": v__afni_run_me_cargs,
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
    }.get(t)


class VAfniRunMeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__afni_run_me(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__afni_run_me_params(
    go: bool = False,
    curl: bool = False,
    help_: bool = False,
) -> VAfniRunMeParameters:
    """
    Build parameters.
    
    Args:
        go: Execute the work.
        curl: Default to curl instead of wget.
        help_: Show help message.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@afni.run.me",
        "go": go,
        "curl": curl,
        "help": help_,
    }
    return params


def v__afni_run_me_cargs(
    params: VAfniRunMeParameters,
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
    cargs.append("@afni.run.me")
    if params.get("go"):
        cargs.append("-go")
    if params.get("curl"):
        cargs.append("-curl")
    if params.get("help"):
        cargs.append("-help")
    return cargs


def v__afni_run_me_outputs(
    params: VAfniRunMeParameters,
    execution: Execution,
) -> VAfniRunMeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VAfniRunMeOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__afni_run_me_execute(
    params: VAfniRunMeParameters,
    execution: Execution,
) -> VAfniRunMeOutputs:
    """
    A tool to execute a specific command.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VAfniRunMeOutputs`).
    """
    params = execution.params(params)
    cargs = v__afni_run_me_cargs(params, execution)
    ret = v__afni_run_me_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__afni_run_me(
    go: bool = False,
    curl: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> VAfniRunMeOutputs:
    """
    A tool to execute a specific command.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        go: Execute the work.
        curl: Default to curl instead of wget.
        help_: Show help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VAfniRunMeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__AFNI_RUN_ME_METADATA)
    params = v__afni_run_me_params(go=go, curl=curl, help_=help_)
    return v__afni_run_me_execute(params, execution)


__all__ = [
    "VAfniRunMeOutputs",
    "VAfniRunMeParameters",
    "V__AFNI_RUN_ME_METADATA",
    "v__afni_run_me",
    "v__afni_run_me_params",
]
