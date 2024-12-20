# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

INFLATE_SUBJECT_METADATA = Metadata(
    id="0f453fc5ea15ce4839c856ec25b28572898bd123.boutiques",
    name="inflate_subject",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class InflateSubjectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `inflate_subject(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """Output of inflate_subject command"""


def inflate_subject(
    args: str | None = None,
    runner: Runner | None = None,
) -> InflateSubjectOutputs:
    """
    Inflate subject script for FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        args: Arguments for the inflate_subject command.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `InflateSubjectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INFLATE_SUBJECT_METADATA)
    cargs = []
    cargs.append("inflate_subject")
    if args is not None:
        cargs.append(args)
    ret = InflateSubjectOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(args + "_output.txt") if (args is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "INFLATE_SUBJECT_METADATA",
    "InflateSubjectOutputs",
    "inflate_subject",
]
