# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SEGMENT_SUBJECT_NOTAL2_METADATA = Metadata(
    id="6303522667922b1bee80bfcf692f9907c22c58f7.boutiques",
    name="segment_subject_notal2",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
SegmentSubjectNotal2Parameters = typing.TypedDict('SegmentSubjectNotal2Parameters', {
    "__STYX_TYPE__": typing.Literal["segment_subject_notal2"],
    "license_file": InputPathType,
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
        "segment_subject_notal2": segment_subject_notal2_cargs,
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
        "segment_subject_notal2": segment_subject_notal2_outputs,
    }.get(t)


class SegmentSubjectNotal2Outputs(typing.NamedTuple):
    """
    Output object returned when calling `segment_subject_notal2(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dir: OutputPathType
    """Output directory containing the segmented results"""


def segment_subject_notal2_params(
    license_file: InputPathType,
) -> SegmentSubjectNotal2Parameters:
    """
    Build parameters.
    
    Args:
        license_file: FreeSurfer license file is required to run the\
            application. Obtain from\
            http://surfer.nmr.mgh.harvard.edu/registration.html.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "segment_subject_notal2",
        "license_file": license_file,
    }
    return params


def segment_subject_notal2_cargs(
    params: SegmentSubjectNotal2Parameters,
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
    cargs.append("segment_subject_notal2")
    cargs.extend([
        "--fs-license-file",
        execution.input_file(params.get("license_file"))
    ])
    return cargs


def segment_subject_notal2_outputs(
    params: SegmentSubjectNotal2Parameters,
    execution: Execution,
) -> SegmentSubjectNotal2Outputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SegmentSubjectNotal2Outputs(
        root=execution.output_file("."),
        output_dir=execution.output_file("segmented_output"),
    )
    return ret


def segment_subject_notal2_execute(
    params: SegmentSubjectNotal2Parameters,
    execution: Execution,
) -> SegmentSubjectNotal2Outputs:
    """
    FreeSurfer tool for segmenting subject data using notal2 algorithm.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SegmentSubjectNotal2Outputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = segment_subject_notal2_cargs(params, execution)
    ret = segment_subject_notal2_outputs(params, execution)
    execution.run(cargs)
    return ret


def segment_subject_notal2(
    license_file: InputPathType,
    runner: Runner | None = None,
) -> SegmentSubjectNotal2Outputs:
    """
    FreeSurfer tool for segmenting subject data using notal2 algorithm.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        license_file: FreeSurfer license file is required to run the\
            application. Obtain from\
            http://surfer.nmr.mgh.harvard.edu/registration.html.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SegmentSubjectNotal2Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SEGMENT_SUBJECT_NOTAL2_METADATA)
    params = segment_subject_notal2_params(license_file=license_file)
    return segment_subject_notal2_execute(params, execution)


__all__ = [
    "SEGMENT_SUBJECT_NOTAL2_METADATA",
    "SegmentSubjectNotal2Outputs",
    "SegmentSubjectNotal2Parameters",
    "segment_subject_notal2",
    "segment_subject_notal2_params",
]
