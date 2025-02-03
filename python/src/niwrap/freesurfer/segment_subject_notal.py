# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SEGMENT_SUBJECT_NOTAL_METADATA = Metadata(
    id="a7a96a3826fdc962ee75d09bc6629b89ee8c17d9.boutiques",
    name="segment_subject_notal",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
SegmentSubjectNotalParameters = typing.TypedDict('SegmentSubjectNotalParameters', {
    "__STYX_TYPE__": typing.Literal["segment_subject_notal"],
    "subject_path": str,
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
        "segment_subject_notal": segment_subject_notal_cargs,
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


class SegmentSubjectNotalOutputs(typing.NamedTuple):
    """
    Output object returned when calling `segment_subject_notal(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def segment_subject_notal_params(
    subject_path: str,
) -> SegmentSubjectNotalParameters:
    """
    Build parameters.
    
    Args:
        subject_path: Path to the subject's directory.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "segment_subject_notal",
        "subject_path": subject_path,
    }
    return params


def segment_subject_notal_cargs(
    params: SegmentSubjectNotalParameters,
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
    cargs.append("segment_subject_notal")
    cargs.append(params.get("subject_path"))
    return cargs


def segment_subject_notal_outputs(
    params: SegmentSubjectNotalParameters,
    execution: Execution,
) -> SegmentSubjectNotalOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SegmentSubjectNotalOutputs(
        root=execution.output_file("."),
    )
    return ret


def segment_subject_notal_execute(
    params: SegmentSubjectNotalParameters,
    execution: Execution,
) -> SegmentSubjectNotalOutputs:
    """
    A script to segment subjects (notal).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SegmentSubjectNotalOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = segment_subject_notal_cargs(params, execution)
    ret = segment_subject_notal_outputs(params, execution)
    execution.run(cargs)
    return ret


def segment_subject_notal(
    subject_path: str,
    runner: Runner | None = None,
) -> SegmentSubjectNotalOutputs:
    """
    A script to segment subjects (notal).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_path: Path to the subject's directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SegmentSubjectNotalOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SEGMENT_SUBJECT_NOTAL_METADATA)
    params = segment_subject_notal_params(subject_path=subject_path)
    return segment_subject_notal_execute(params, execution)


__all__ = [
    "SEGMENT_SUBJECT_NOTAL_METADATA",
    "SegmentSubjectNotalOutputs",
    "segment_subject_notal",
    "segment_subject_notal_params",
]
