# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FIX_SUBJECT_METADATA = Metadata(
    id="61bfaf4767ebcb038e8eec8be58f3650a3ee7f43.boutiques",
    name="fix_subject",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
FixSubjectParameters = typing.TypedDict('FixSubjectParameters', {
    "__STYX_TYPE__": typing.Literal["fix_subject"],
    "arguments": typing.NotRequired[str | None],
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
        "fix_subject": fix_subject_cargs,
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


class FixSubjectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fix_subject(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fix_subject_params(
    arguments: str | None = None,
) -> FixSubjectParameters:
    """
    Build parameters.
    
    Args:
        arguments: Arguments for fix_subject command. Currently, help output\
            shows directory errors. Ensure the correct paths are used.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fix_subject",
    }
    if arguments is not None:
        params["arguments"] = arguments
    return params


def fix_subject_cargs(
    params: FixSubjectParameters,
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
    cargs.append("fix_subject")
    if params.get("arguments") is not None:
        cargs.append(params.get("arguments"))
    return cargs


def fix_subject_outputs(
    params: FixSubjectParameters,
    execution: Execution,
) -> FixSubjectOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FixSubjectOutputs(
        root=execution.output_file("."),
    )
    return ret


def fix_subject_execute(
    params: FixSubjectParameters,
    execution: Execution,
) -> FixSubjectOutputs:
    """
    Tool to fix subjects in FreeSurfer, encountered errors due to incorrect path
    handling.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FixSubjectOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fix_subject_cargs(params, execution)
    ret = fix_subject_outputs(params, execution)
    execution.run(cargs)
    return ret


def fix_subject(
    arguments: str | None = None,
    runner: Runner | None = None,
) -> FixSubjectOutputs:
    """
    Tool to fix subjects in FreeSurfer, encountered errors due to incorrect path
    handling.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        arguments: Arguments for fix_subject command. Currently, help output\
            shows directory errors. Ensure the correct paths are used.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FixSubjectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIX_SUBJECT_METADATA)
    params = fix_subject_params(arguments=arguments)
    return fix_subject_execute(params, execution)


__all__ = [
    "FIX_SUBJECT_METADATA",
    "FixSubjectOutputs",
    "FixSubjectParameters",
    "fix_subject",
    "fix_subject_params",
]
