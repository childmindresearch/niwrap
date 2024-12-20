# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

RENORMALIZE_SUBJECT_KEEP_EDITTING_METADATA = Metadata(
    id="d1c64f0c85672d74bb2cb15852e56662e6d58c32.boutiques",
    name="renormalize_subject_keep_editting",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class RenormalizeSubjectKeepEdittingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `renormalize_subject_keep_editting(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Placeholder output file since tool details are not available."""


def renormalize_subject_keep_editting(
    runner: Runner | None = None,
) -> RenormalizeSubjectKeepEdittingOutputs:
    """
    A placeholder for the renormalize_subject_keep_editting tool, details not
    available.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RenormalizeSubjectKeepEdittingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RENORMALIZE_SUBJECT_KEEP_EDITTING_METADATA)
    cargs = []
    cargs.append("renormalize_subject_keep_editting")
    ret = RenormalizeSubjectKeepEdittingOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file("output.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "RENORMALIZE_SUBJECT_KEEP_EDITTING_METADATA",
    "RenormalizeSubjectKeepEdittingOutputs",
    "renormalize_subject_keep_editting",
]
