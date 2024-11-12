# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

REINFLATE_SUBJECT_RH_METADATA = Metadata(
    id="540bde89fe45baa657d26fcfdea3dd14ef5a0717.boutiques",
    name="reinflate_subject-rh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class ReinflateSubjectRhOutputs(typing.NamedTuple):
    """
    Output object returned when calling `reinflate_subject_rh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def reinflate_subject_rh(
    subject_dir: str,
    additional_options: str | None = None,
    runner: Runner | None = None,
) -> ReinflateSubjectRhOutputs:
    """
    A tool for reinflating the cortical surfaces for a given subject in FreeSurfer,
    specifically for the right hemisphere.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_dir: Directory of the subject within FreeSurfer environment.
        additional_options: Additional options for the reinflate_subject-rh\
            command.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ReinflateSubjectRhOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REINFLATE_SUBJECT_RH_METADATA)
    cargs = []
    cargs.append("reinflate_subject-rh")
    cargs.append(subject_dir)
    if additional_options is not None:
        cargs.append(additional_options)
    ret = ReinflateSubjectRhOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "REINFLATE_SUBJECT_RH_METADATA",
    "ReinflateSubjectRhOutputs",
    "reinflate_subject_rh",
]