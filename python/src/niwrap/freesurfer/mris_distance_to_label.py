# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_DISTANCE_TO_LABEL_METADATA = Metadata(
    id="0538a932ce0052cc0bb4e77e20e1d20d65106c51.boutiques",
    name="mris_distance_to_label",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisDistanceToLabelParameters = typing.TypedDict('MrisDistanceToLabelParameters', {
    "__STYX_TYPE__": typing.Literal["mris_distance_to_label"],
    "hemisphere": str,
    "subject_1": str,
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
        "mris_distance_to_label": mris_distance_to_label_cargs,
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


class MrisDistanceToLabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_distance_to_label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_distance_to_label_params(
    hemisphere: str,
    subject_1: str,
) -> MrisDistanceToLabelParameters:
    """
    Build parameters.
    
    Args:
        hemisphere: Hemisphere to process (e.g., 'lh' for left hemisphere or\
            'rh' for right hemisphere).
        subject_1: Subject identifier or path to the subject directory.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_distance_to_label",
        "hemisphere": hemisphere,
        "subject_1": subject_1,
    }
    return params


def mris_distance_to_label_cargs(
    params: MrisDistanceToLabelParameters,
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
    cargs.append("mris_distance_to_label")
    cargs.append(params.get("hemisphere"))
    cargs.append(params.get("subject_1"))
    return cargs


def mris_distance_to_label_outputs(
    params: MrisDistanceToLabelParameters,
    execution: Execution,
) -> MrisDistanceToLabelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisDistanceToLabelOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_distance_to_label_execute(
    params: MrisDistanceToLabelParameters,
    execution: Execution,
) -> MrisDistanceToLabelOutputs:
    """
    A tool for measuring the distance between vertices on a surface and a labeled
    region.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisDistanceToLabelOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_distance_to_label_cargs(params, execution)
    ret = mris_distance_to_label_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_distance_to_label(
    hemisphere: str,
    subject_1: str,
    runner: Runner | None = None,
) -> MrisDistanceToLabelOutputs:
    """
    A tool for measuring the distance between vertices on a surface and a labeled
    region.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        hemisphere: Hemisphere to process (e.g., 'lh' for left hemisphere or\
            'rh' for right hemisphere).
        subject_1: Subject identifier or path to the subject directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisDistanceToLabelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_DISTANCE_TO_LABEL_METADATA)
    params = mris_distance_to_label_params(hemisphere=hemisphere, subject_1=subject_1)
    return mris_distance_to_label_execute(params, execution)


__all__ = [
    "MRIS_DISTANCE_TO_LABEL_METADATA",
    "MrisDistanceToLabelOutputs",
    "mris_distance_to_label",
    "mris_distance_to_label_params",
]
