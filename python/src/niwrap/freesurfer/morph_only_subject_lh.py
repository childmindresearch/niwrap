# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MORPH_ONLY_SUBJECT_LH_METADATA = Metadata(
    id="352935372f9b953d29e77e48bc48053d0bb7123b.boutiques",
    name="morph_only_subject-lh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MorphOnlySubjectLhOutputs(typing.NamedTuple):
    """
    Output object returned when calling `morph_only_subject_lh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    morph_results: OutputPathType
    """Output directory with morphological results."""


def morph_only_subject_lh(
    subject_dir: str,
    runner: Runner | None = None,
) -> MorphOnlySubjectLhOutputs:
    """
    A tool for morphological processing for the left hemisphere.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_dir: Directory of the subject to process.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MorphOnlySubjectLhOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MORPH_ONLY_SUBJECT_LH_METADATA)
    cargs = []
    cargs.extend([
        "-lh",
        "morph_only_subject" + subject_dir
    ])
    ret = MorphOnlySubjectLhOutputs(
        root=execution.output_file("."),
        morph_results=execution.output_file(subject_dir + "/morph_results"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MORPH_ONLY_SUBJECT_LH_METADATA",
    "MorphOnlySubjectLhOutputs",
    "morph_only_subject_lh",
]
