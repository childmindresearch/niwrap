# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SEGMENT_SUBJECT_T2_AUTO_ESTIMATE_ALVEUS_ML_METADATA = Metadata(
    id="8a6a12eb1eae4567d49625f69155e84f68466b3c.boutiques",
    name="segmentSubjectT2_autoEstimateAlveusML",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
SegmentSubjectT2AutoEstimateAlveusMlParameters = typing.TypedDict('SegmentSubjectT2AutoEstimateAlveusMlParameters', {
    "__STYX_TYPE__": typing.Literal["segmentSubjectT2_autoEstimateAlveusML"],
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
        "segmentSubjectT2_autoEstimateAlveusML": segment_subject_t2_auto_estimate_alveus_ml_cargs,
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


class SegmentSubjectT2AutoEstimateAlveusMlOutputs(typing.NamedTuple):
    """
    Output object returned when calling `segment_subject_t2_auto_estimate_alveus_ml(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def segment_subject_t2_auto_estimate_alveus_ml_params(
) -> SegmentSubjectT2AutoEstimateAlveusMlParameters:
    """
    Build parameters.
    
    Args:
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "segmentSubjectT2_autoEstimateAlveusML",
    }
    return params


def segment_subject_t2_auto_estimate_alveus_ml_cargs(
    params: SegmentSubjectT2AutoEstimateAlveusMlParameters,
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
    cargs.append("segmentSubjectT2_autoEstimateAlveusML")
    return cargs


def segment_subject_t2_auto_estimate_alveus_ml_outputs(
    params: SegmentSubjectT2AutoEstimateAlveusMlParameters,
    execution: Execution,
) -> SegmentSubjectT2AutoEstimateAlveusMlOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SegmentSubjectT2AutoEstimateAlveusMlOutputs(
        root=execution.output_file("."),
    )
    return ret


def segment_subject_t2_auto_estimate_alveus_ml_execute(
    params: SegmentSubjectT2AutoEstimateAlveusMlParameters,
    execution: Execution,
) -> SegmentSubjectT2AutoEstimateAlveusMlOutputs:
    """
    A Freesurfer tool to segment T2 subjects with automatic alveus ML estimation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SegmentSubjectT2AutoEstimateAlveusMlOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = segment_subject_t2_auto_estimate_alveus_ml_cargs(params, execution)
    ret = segment_subject_t2_auto_estimate_alveus_ml_outputs(params, execution)
    execution.run(cargs)
    return ret


def segment_subject_t2_auto_estimate_alveus_ml(
    runner: Runner | None = None,
) -> SegmentSubjectT2AutoEstimateAlveusMlOutputs:
    """
    A Freesurfer tool to segment T2 subjects with automatic alveus ML estimation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SegmentSubjectT2AutoEstimateAlveusMlOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SEGMENT_SUBJECT_T2_AUTO_ESTIMATE_ALVEUS_ML_METADATA)
    params = segment_subject_t2_auto_estimate_alveus_ml_params()
    return segment_subject_t2_auto_estimate_alveus_ml_execute(params, execution)


__all__ = [
    "SEGMENT_SUBJECT_T2_AUTO_ESTIMATE_ALVEUS_ML_METADATA",
    "SegmentSubjectT2AutoEstimateAlveusMlOutputs",
    "SegmentSubjectT2AutoEstimateAlveusMlParameters",
    "segment_subject_t2_auto_estimate_alveus_ml",
    "segment_subject_t2_auto_estimate_alveus_ml_params",
]
