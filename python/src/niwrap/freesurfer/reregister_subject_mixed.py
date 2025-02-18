# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

REREGISTER_SUBJECT_MIXED_METADATA = Metadata(
    id="0d4b2b8c11d9a393c8ab3a72de3e1875d4b1135b.boutiques",
    name="reregister_subject_mixed",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
ReregisterSubjectMixedParameters = typing.TypedDict('ReregisterSubjectMixedParameters', {
    "__STYX_TYPE__": typing.Literal["reregister_subject_mixed"],
    "input_volume": InputPathType,
    "output_directory": str,
    "threads": typing.NotRequired[float | None],
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
        "reregister_subject_mixed": reregister_subject_mixed_cargs,
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
        "reregister_subject_mixed": reregister_subject_mixed_outputs,
    }.get(t)


class ReregisterSubjectMixedOutputs(typing.NamedTuple):
    """
    Output object returned when calling `reregister_subject_mixed(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    control_points: OutputPathType
    """Transformed control points"""
    intensity_normalized: OutputPathType
    """Intensity normalized output"""
    log_file: OutputPathType
    """Log file for talairach processing"""


def reregister_subject_mixed_params(
    input_volume: InputPathType,
    output_directory: str,
    threads: float | None = 1,
) -> ReregisterSubjectMixedParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Input volume file path.
        output_directory: Output directory for transformed control points and\
            intensity normalized files.
        threads: Number of threads available to mri_em_register for OpenMP.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "reregister_subject_mixed",
        "input_volume": input_volume,
        "output_directory": output_directory,
    }
    if threads is not None:
        params["threads"] = threads
    return params


def reregister_subject_mixed_cargs(
    params: ReregisterSubjectMixedParameters,
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
    cargs.append("reregister_subject_mixed")
    cargs.append(execution.input_file(params.get("input_volume")))
    cargs.append(params.get("output_directory"))
    if params.get("threads") is not None:
        cargs.append(str(params.get("threads")))
    return cargs


def reregister_subject_mixed_outputs(
    params: ReregisterSubjectMixedParameters,
    execution: Execution,
) -> ReregisterSubjectMixedOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ReregisterSubjectMixedOutputs(
        root=execution.output_file("."),
        control_points=execution.output_file(params.get("output_directory") + "/mri/fsamples"),
        intensity_normalized=execution.output_file(params.get("output_directory") + "/mri/norm"),
        log_file=execution.output_file("talairach.log"),
    )
    return ret


def reregister_subject_mixed_execute(
    params: ReregisterSubjectMixedParameters,
    execution: Execution,
) -> ReregisterSubjectMixedOutputs:
    """
    Tool for re-registering a subject's MRI volumes using Freesurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ReregisterSubjectMixedOutputs`).
    """
    params = execution.params(params)
    cargs = reregister_subject_mixed_cargs(params, execution)
    ret = reregister_subject_mixed_outputs(params, execution)
    execution.run(cargs)
    return ret


def reregister_subject_mixed(
    input_volume: InputPathType,
    output_directory: str,
    threads: float | None = 1,
    runner: Runner | None = None,
) -> ReregisterSubjectMixedOutputs:
    """
    Tool for re-registering a subject's MRI volumes using Freesurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume file path.
        output_directory: Output directory for transformed control points and\
            intensity normalized files.
        threads: Number of threads available to mri_em_register for OpenMP.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ReregisterSubjectMixedOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REREGISTER_SUBJECT_MIXED_METADATA)
    params = reregister_subject_mixed_params(input_volume=input_volume, output_directory=output_directory, threads=threads)
    return reregister_subject_mixed_execute(params, execution)


__all__ = [
    "REREGISTER_SUBJECT_MIXED_METADATA",
    "ReregisterSubjectMixedOutputs",
    "ReregisterSubjectMixedParameters",
    "reregister_subject_mixed",
    "reregister_subject_mixed_params",
]
