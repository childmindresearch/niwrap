# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

INFLATE_SUBJECT_NEW_RH_METADATA = Metadata(
    id="6ededf15eee0d58308af964a359eb602b1b300a0.boutiques",
    name="inflate_subject_new-rh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
InflateSubjectNewRhParameters = typing.TypedDict('InflateSubjectNewRhParameters', {
    "__STYX_TYPE__": typing.Literal["inflate_subject_new-rh"],
    "args": typing.NotRequired[str | None],
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
        "inflate_subject_new-rh": inflate_subject_new_rh_cargs,
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


class InflateSubjectNewRhOutputs(typing.NamedTuple):
    """
    Output object returned when calling `inflate_subject_new_rh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def inflate_subject_new_rh_params(
    args: str | None = None,
) -> InflateSubjectNewRhParameters:
    """
    Build parameters.
    
    Args:
        args: Additional command-line arguments for inflate_subject_new-rh.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "inflate_subject_new-rh",
    }
    if args is not None:
        params["args"] = args
    return params


def inflate_subject_new_rh_cargs(
    params: InflateSubjectNewRhParameters,
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
    if params.get("args") is not None:
        cargs.extend([
            "-rh",
            "inflate_subject_new" + params.get("args")
        ])
    return cargs


def inflate_subject_new_rh_outputs(
    params: InflateSubjectNewRhParameters,
    execution: Execution,
) -> InflateSubjectNewRhOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = InflateSubjectNewRhOutputs(
        root=execution.output_file("."),
    )
    return ret


def inflate_subject_new_rh_execute(
    params: InflateSubjectNewRhParameters,
    execution: Execution,
) -> InflateSubjectNewRhOutputs:
    """
    This is a placeholder descriptor for the 'inflate_subject_new-rh' command. The
    tool appears to be part of FreeSurfer but the specific inputs, outputs or
    options couldn't be extracted from the help text.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `InflateSubjectNewRhOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = inflate_subject_new_rh_cargs(params, execution)
    ret = inflate_subject_new_rh_outputs(params, execution)
    execution.run(cargs)
    return ret


def inflate_subject_new_rh(
    args: str | None = None,
    runner: Runner | None = None,
) -> InflateSubjectNewRhOutputs:
    """
    This is a placeholder descriptor for the 'inflate_subject_new-rh' command. The
    tool appears to be part of FreeSurfer but the specific inputs, outputs or
    options couldn't be extracted from the help text.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        args: Additional command-line arguments for inflate_subject_new-rh.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `InflateSubjectNewRhOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INFLATE_SUBJECT_NEW_RH_METADATA)
    params = inflate_subject_new_rh_params(args=args)
    return inflate_subject_new_rh_execute(params, execution)


__all__ = [
    "INFLATE_SUBJECT_NEW_RH_METADATA",
    "InflateSubjectNewRhOutputs",
    "inflate_subject_new_rh",
    "inflate_subject_new_rh_params",
]
