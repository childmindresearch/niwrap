# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DEFACE_SUBJECT_METADATA = Metadata(
    id="274e5ad239a83bd50707ef1a9dcf8ce7c5e84775.boutiques",
    name="deface_subject",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
DefaceSubjectParameters = typing.TypedDict('DefaceSubjectParameters', {
    "__STYX_TYPE__": typing.Literal["deface_subject"],
    "subjects_dir": str,
    "subject_id": str,
    "volume_input": InputPathType,
    "volume_output": str,
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
        "deface_subject": deface_subject_cargs,
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
        "deface_subject": deface_subject_outputs,
    }.get(t)


class DefaceSubjectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `deface_subject(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume: OutputPathType
    """Defaced output volume."""


def deface_subject_params(
    subjects_dir: str,
    subject_id: str,
    volume_input: InputPathType,
    volume_output: str,
) -> DefaceSubjectParameters:
    """
    Build parameters.
    
    Args:
        subjects_dir: Directory containing FreeSurfer subject directories.
        subject_id: Subject ID that specifies the subject directory.
        volume_input: Input volume to be defaced.
        volume_output: Output volume after defacing.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "deface_subject",
        "subjects_dir": subjects_dir,
        "subject_id": subject_id,
        "volume_input": volume_input,
        "volume_output": volume_output,
    }
    return params


def deface_subject_cargs(
    params: DefaceSubjectParameters,
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
    cargs.append("deface_subject")
    cargs.extend([
        "-sdir",
        params.get("subjects_dir")
    ])
    cargs.extend([
        "-id",
        params.get("subject_id")
    ])
    cargs.extend([
        "-i",
        execution.input_file(params.get("volume_input"))
    ])
    cargs.extend([
        "-o",
        params.get("volume_output")
    ])
    return cargs


def deface_subject_outputs(
    params: DefaceSubjectParameters,
    execution: Execution,
) -> DefaceSubjectOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DefaceSubjectOutputs(
        root=execution.output_file("."),
        output_volume=execution.output_file(params.get("volume_output")),
    )
    return ret


def deface_subject_execute(
    params: DefaceSubjectParameters,
    execution: Execution,
) -> DefaceSubjectOutputs:
    """
    Tool for defacing MRI images to anonymize patient data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DefaceSubjectOutputs`).
    """
    cargs = deface_subject_cargs(params, execution)
    ret = deface_subject_outputs(params, execution)
    execution.run(cargs)
    return ret


def deface_subject(
    subjects_dir: str,
    subject_id: str,
    volume_input: InputPathType,
    volume_output: str,
    runner: Runner | None = None,
) -> DefaceSubjectOutputs:
    """
    Tool for defacing MRI images to anonymize patient data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjects_dir: Directory containing FreeSurfer subject directories.
        subject_id: Subject ID that specifies the subject directory.
        volume_input: Input volume to be defaced.
        volume_output: Output volume after defacing.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DefaceSubjectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DEFACE_SUBJECT_METADATA)
    params = deface_subject_params(subjects_dir=subjects_dir, subject_id=subject_id, volume_input=volume_input, volume_output=volume_output)
    return deface_subject_execute(params, execution)


__all__ = [
    "DEFACE_SUBJECT_METADATA",
    "DefaceSubjectOutputs",
    "DefaceSubjectParameters",
    "deface_subject",
    "deface_subject_params",
]
