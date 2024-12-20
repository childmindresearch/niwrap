# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

INFLATE_SUBJECT_SC_METADATA = Metadata(
    id="bdd6f4bcc49d0163426eb09c58fe6f94a9a23109.boutiques",
    name="inflate_subject_sc",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class InflateSubjectScOutputs(typing.NamedTuple):
    """
    Output object returned when calling `inflate_subject_sc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    inflated_output: OutputPathType
    """Inflated subject surface output."""


def inflate_subject_sc(
    runner: Runner | None = None,
) -> InflateSubjectScOutputs:
    """
    Inferred description: Tool for inflating subject surfaces, specific details
    unavailable.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `InflateSubjectScOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INFLATE_SUBJECT_SC_METADATA)
    cargs = []
    cargs.append("inflate_subject_sc")
    cargs.append("[OPTIONS]")
    ret = InflateSubjectScOutputs(
        root=execution.output_file("."),
        inflated_output=execution.output_file("[SUBJECT_DIR]/inflated_output"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "INFLATE_SUBJECT_SC_METADATA",
    "InflateSubjectScOutputs",
    "inflate_subject_sc",
]
