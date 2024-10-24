# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SEGMENT_SUBJECT_T1_AUTO_ESTIMATE_ALVEUS_ML_METADATA = Metadata(
    id="43b0001ab86e4ffd97c64d3a223a099dafddc2e9.boutiques",
    name="segmentSubjectT1_autoEstimateAlveusML",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class SegmentSubjectT1AutoEstimateAlveusMlOutputs(typing.NamedTuple):
    """
    Output object returned when calling `segment_subject_t1_auto_estimate_alveus_ml(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    segmentation_output: OutputPathType
    """The file containing segmented MRI data."""


def segment_subject_t1_auto_estimate_alveus_ml(
    t1_file: InputPathType,
    output_folder: str,
    runner: Runner | None = None,
) -> SegmentSubjectT1AutoEstimateAlveusMlOutputs:
    """
    A tool that segments T1-weighted MRI data and automatically estimates the
    Alveus.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        t1_file: Input T1-weighted MRI file to be segmented.
        output_folder: Path to the folder where the outputs will be saved.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SegmentSubjectT1AutoEstimateAlveusMlOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SEGMENT_SUBJECT_T1_AUTO_ESTIMATE_ALVEUS_ML_METADATA)
    cargs = []
    cargs.append("segmentSubjectT1_autoEstimateAlveusML")
    cargs.append(execution.input_file(t1_file))
    cargs.append(output_folder)
    ret = SegmentSubjectT1AutoEstimateAlveusMlOutputs(
        root=execution.output_file("."),
        segmentation_output=execution.output_file(output_folder + "/segmented_output.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SEGMENT_SUBJECT_T1_AUTO_ESTIMATE_ALVEUS_ML_METADATA",
    "SegmentSubjectT1AutoEstimateAlveusMlOutputs",
    "segment_subject_t1_auto_estimate_alveus_ml",
]
