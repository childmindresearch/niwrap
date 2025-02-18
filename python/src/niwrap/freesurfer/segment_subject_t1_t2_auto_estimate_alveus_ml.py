# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SEGMENT_SUBJECT_T1_T2_AUTO_ESTIMATE_ALVEUS_ML_METADATA = Metadata(
    id="3610f126955ba102d4ca3bfab514b11ee60bd328.boutiques",
    name="segmentSubjectT1T2_autoEstimateAlveusML",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
SegmentSubjectT1T2AutoEstimateAlveusMlParameters = typing.TypedDict('SegmentSubjectT1T2AutoEstimateAlveusMlParameters', {
    "__STYX_TYPE__": typing.Literal["segmentSubjectT1T2_autoEstimateAlveusML"],
    "input_t1": InputPathType,
    "input_t2": InputPathType,
    "output_directory": str,
    "other_options": typing.NotRequired[str | None],
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
        "segmentSubjectT1T2_autoEstimateAlveusML": segment_subject_t1_t2_auto_estimate_alveus_ml_cargs,
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
        "segmentSubjectT1T2_autoEstimateAlveusML": segment_subject_t1_t2_auto_estimate_alveus_ml_outputs,
    }.get(t)


class SegmentSubjectT1T2AutoEstimateAlveusMlOutputs(typing.NamedTuple):
    """
    Output object returned when calling `segment_subject_t1_t2_auto_estimate_alveus_ml(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    segmentation_result: OutputPathType
    """Resultant image of the alveus segmentation."""


def segment_subject_t1_t2_auto_estimate_alveus_ml_params(
    input_t1: InputPathType,
    input_t2: InputPathType,
    output_directory: str,
    other_options: str | None = None,
) -> SegmentSubjectT1T2AutoEstimateAlveusMlParameters:
    """
    Build parameters.
    
    Args:
        input_t1: Input T1-weighted MR image.
        input_t2: Input T2-weighted MR image.
        output_directory: Directory to save the output files.
        other_options: Additional command-line options.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "segmentSubjectT1T2_autoEstimateAlveusML",
        "input_t1": input_t1,
        "input_t2": input_t2,
        "output_directory": output_directory,
    }
    if other_options is not None:
        params["other_options"] = other_options
    return params


def segment_subject_t1_t2_auto_estimate_alveus_ml_cargs(
    params: SegmentSubjectT1T2AutoEstimateAlveusMlParameters,
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
    cargs.append("segmentSubjectT1T2_autoEstimateAlveusML")
    cargs.append(execution.input_file(params.get("input_t1")))
    cargs.append(execution.input_file(params.get("input_t2")))
    cargs.append(params.get("output_directory"))
    if params.get("other_options") is not None:
        cargs.append(params.get("other_options"))
    return cargs


def segment_subject_t1_t2_auto_estimate_alveus_ml_outputs(
    params: SegmentSubjectT1T2AutoEstimateAlveusMlParameters,
    execution: Execution,
) -> SegmentSubjectT1T2AutoEstimateAlveusMlOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SegmentSubjectT1T2AutoEstimateAlveusMlOutputs(
        root=execution.output_file("."),
        segmentation_result=execution.output_file(params.get("output_directory") + "/segmentation.nii.gz"),
    )
    return ret


def segment_subject_t1_t2_auto_estimate_alveus_ml_execute(
    params: SegmentSubjectT1T2AutoEstimateAlveusMlParameters,
    execution: Execution,
) -> SegmentSubjectT1T2AutoEstimateAlveusMlOutputs:
    """
    Tool for automatic estimation of the alveus in MR images using T1 and T2
    contrast.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SegmentSubjectT1T2AutoEstimateAlveusMlOutputs`).
    """
    params = execution.params(params)
    cargs = segment_subject_t1_t2_auto_estimate_alveus_ml_cargs(params, execution)
    ret = segment_subject_t1_t2_auto_estimate_alveus_ml_outputs(params, execution)
    execution.run(cargs)
    return ret


def segment_subject_t1_t2_auto_estimate_alveus_ml(
    input_t1: InputPathType,
    input_t2: InputPathType,
    output_directory: str,
    other_options: str | None = None,
    runner: Runner | None = None,
) -> SegmentSubjectT1T2AutoEstimateAlveusMlOutputs:
    """
    Tool for automatic estimation of the alveus in MR images using T1 and T2
    contrast.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_t1: Input T1-weighted MR image.
        input_t2: Input T2-weighted MR image.
        output_directory: Directory to save the output files.
        other_options: Additional command-line options.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SegmentSubjectT1T2AutoEstimateAlveusMlOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SEGMENT_SUBJECT_T1_T2_AUTO_ESTIMATE_ALVEUS_ML_METADATA)
    params = segment_subject_t1_t2_auto_estimate_alveus_ml_params(input_t1=input_t1, input_t2=input_t2, output_directory=output_directory, other_options=other_options)
    return segment_subject_t1_t2_auto_estimate_alveus_ml_execute(params, execution)


__all__ = [
    "SEGMENT_SUBJECT_T1_T2_AUTO_ESTIMATE_ALVEUS_ML_METADATA",
    "SegmentSubjectT1T2AutoEstimateAlveusMlOutputs",
    "SegmentSubjectT1T2AutoEstimateAlveusMlParameters",
    "segment_subject_t1_t2_auto_estimate_alveus_ml",
    "segment_subject_t1_t2_auto_estimate_alveus_ml_params",
]
