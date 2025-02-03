# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CHECK_SUBJECT_METADATA = Metadata(
    id="a469eabd7979354cb8f4da4909edfba7eca4707c.boutiques",
    name="check_subject",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
CheckSubjectParameters = typing.TypedDict('CheckSubjectParameters', {
    "__STYX_TYPE__": typing.Literal["check_subject"],
    "subject_dir": str,
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
        "check_subject": check_subject_cargs,
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


class CheckSubjectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `check_subject(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def check_subject_params(
    subject_dir: str,
) -> CheckSubjectParameters:
    """
    Build parameters.
    
    Args:
        subject_dir: Path to the subject directory to check.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "check_subject",
        "subject_dir": subject_dir,
    }
    return params


def check_subject_cargs(
    params: CheckSubjectParameters,
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
    cargs.append("check_subject")
    cargs.append(params.get("subject_dir"))
    return cargs


def check_subject_outputs(
    params: CheckSubjectParameters,
    execution: Execution,
) -> CheckSubjectOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CheckSubjectOutputs(
        root=execution.output_file("."),
    )
    return ret


def check_subject_execute(
    params: CheckSubjectParameters,
    execution: Execution,
) -> CheckSubjectOutputs:
    """
    Checks a subject directory for the existence of a surf directory.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CheckSubjectOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = check_subject_cargs(params, execution)
    ret = check_subject_outputs(params, execution)
    execution.run(cargs)
    return ret


def check_subject(
    subject_dir: str,
    runner: Runner | None = None,
) -> CheckSubjectOutputs:
    """
    Checks a subject directory for the existence of a surf directory.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_dir: Path to the subject directory to check.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CheckSubjectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CHECK_SUBJECT_METADATA)
    params = check_subject_params(subject_dir=subject_dir)
    return check_subject_execute(params, execution)


__all__ = [
    "CHECK_SUBJECT_METADATA",
    "CheckSubjectOutputs",
    "check_subject",
    "check_subject_params",
]
