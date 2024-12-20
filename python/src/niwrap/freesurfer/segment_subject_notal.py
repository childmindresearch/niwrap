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


class SegmentSubjectNotalOutputs(typing.NamedTuple):
    """
    Output object returned when calling `segment_subject_notal(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


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
    cargs = []
    cargs.append("segment_subject_notal")
    cargs.append(subject_path)
    ret = SegmentSubjectNotalOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SEGMENT_SUBJECT_NOTAL_METADATA",
    "SegmentSubjectNotalOutputs",
    "segment_subject_notal",
]
