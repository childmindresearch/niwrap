# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SEGMENT_HA_T1_LONG_SH_METADATA = Metadata(
    id="e6413cb2b0b0c7d6ddbeca885e2ef04a50aea294.boutiques",
    name="segmentHA_T1_long.sh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
SegmentHaT1LongShParameters = typing.TypedDict('SegmentHaT1LongShParameters', {
    "__STYX_TYPE__": typing.Literal["segmentHA_T1_long.sh"],
    "subject_dir": str,
    "subject_id": str,
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
        "segmentHA_T1_long.sh": segment_ha_t1_long_sh_cargs,
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
    vt = {
        "segmentHA_T1_long.sh": segment_ha_t1_long_sh_outputs,
    }
    return vt.get(t)


class SegmentHaT1LongShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `segment_ha_t1_long_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dir: OutputPathType
    """Output directory containing segmentation results"""


def segment_ha_t1_long_sh_params(
    subject_dir: str,
    subject_id: str,
) -> SegmentHaT1LongShParameters:
    """
    Build parameters.
    
    Args:
        subject_dir: Directory containing subject data.
        subject_id: Identifier for the subject within the subject directory.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "segmentHA_T1_long.sh",
        "subject_dir": subject_dir,
        "subject_id": subject_id,
    }
    return params


def segment_ha_t1_long_sh_cargs(
    params: SegmentHaT1LongShParameters,
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
    cargs.append("segmentHA_T1_long.sh")
    cargs.append(params.get("subject_dir"))
    cargs.append(params.get("subject_id"))
    return cargs


def segment_ha_t1_long_sh_outputs(
    params: SegmentHaT1LongShParameters,
    execution: Execution,
) -> SegmentHaT1LongShOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SegmentHaT1LongShOutputs(
        root=execution.output_file("."),
        output_dir=execution.output_file(params.get("subject_dir") + "/" + params.get("subject_id") + "_long_segment/output"),
    )
    return ret


def segment_ha_t1_long_sh_execute(
    params: SegmentHaT1LongShParameters,
    execution: Execution,
) -> SegmentHaT1LongShOutputs:
    """
    A script for longitudinal segmentation of the hippocampal/amygdala regions.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SegmentHaT1LongShOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = segment_ha_t1_long_sh_cargs(params, execution)
    ret = segment_ha_t1_long_sh_outputs(params, execution)
    execution.run(cargs)
    return ret


def segment_ha_t1_long_sh(
    subject_dir: str,
    subject_id: str,
    runner: Runner | None = None,
) -> SegmentHaT1LongShOutputs:
    """
    A script for longitudinal segmentation of the hippocampal/amygdala regions.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_dir: Directory containing subject data.
        subject_id: Identifier for the subject within the subject directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SegmentHaT1LongShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SEGMENT_HA_T1_LONG_SH_METADATA)
    params = segment_ha_t1_long_sh_params(subject_dir=subject_dir, subject_id=subject_id)
    return segment_ha_t1_long_sh_execute(params, execution)


__all__ = [
    "SEGMENT_HA_T1_LONG_SH_METADATA",
    "SegmentHaT1LongShOutputs",
    "SegmentHaT1LongShParameters",
    "segment_ha_t1_long_sh",
    "segment_ha_t1_long_sh_params",
]
