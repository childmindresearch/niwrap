# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RENORMALIZE_T1_SUBJECT_METADATA = Metadata(
    id="fd1b560cfb5855fbdac004ecaa45cd6e0aa37abf.boutiques",
    name="renormalize_T1_subject",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
RenormalizeT1SubjectParameters = typing.TypedDict('RenormalizeT1SubjectParameters', {
    "__STYX_TYPE__": typing.Literal["renormalize_T1_subject"],
    "subject_dir": str,
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
        "renormalize_T1_subject": renormalize_t1_subject_cargs,
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
        "renormalize_T1_subject": renormalize_t1_subject_outputs,
    }.get(t)


class RenormalizeT1SubjectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `renormalize_t1_subject(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def renormalize_t1_subject_params(
    subject_dir: str,
) -> RenormalizeT1SubjectParameters:
    """
    Build parameters.
    
    Args:
        subject_dir: Directory of the subject containing T1 images to\
            renormalize.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "renormalize_T1_subject",
        "subject_dir": subject_dir,
    }
    return params


def renormalize_t1_subject_cargs(
    params: RenormalizeT1SubjectParameters,
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
    cargs.append("renormalize_T1_subject")
    cargs.append(params.get("subject_dir"))
    return cargs


def renormalize_t1_subject_outputs(
    params: RenormalizeT1SubjectParameters,
    execution: Execution,
) -> RenormalizeT1SubjectOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RenormalizeT1SubjectOutputs(
        root=execution.output_file("."),
    )
    return ret


def renormalize_t1_subject_execute(
    params: RenormalizeT1SubjectParameters,
    execution: Execution,
) -> RenormalizeT1SubjectOutputs:
    """
    Renormalize T1 subject images using FreeSurfer scripts.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RenormalizeT1SubjectOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = renormalize_t1_subject_cargs(params, execution)
    ret = renormalize_t1_subject_outputs(params, execution)
    execution.run(cargs)
    return ret


def renormalize_t1_subject(
    subject_dir: str,
    runner: Runner | None = None,
) -> RenormalizeT1SubjectOutputs:
    """
    Renormalize T1 subject images using FreeSurfer scripts.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_dir: Directory of the subject containing T1 images to\
            renormalize.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RenormalizeT1SubjectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RENORMALIZE_T1_SUBJECT_METADATA)
    params = renormalize_t1_subject_params(subject_dir=subject_dir)
    return renormalize_t1_subject_execute(params, execution)


__all__ = [
    "RENORMALIZE_T1_SUBJECT_METADATA",
    "RenormalizeT1SubjectOutputs",
    "RenormalizeT1SubjectParameters",
    "renormalize_t1_subject",
    "renormalize_t1_subject_params",
]
