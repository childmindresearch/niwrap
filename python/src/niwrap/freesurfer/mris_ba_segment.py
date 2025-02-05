# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_BA_SEGMENT_METADATA = Metadata(
    id="b3ec206494aa6dee2d2521daa7c2af2397b82e98.boutiques",
    name="mris_BA_segment",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisBaSegmentParameters = typing.TypedDict('MrisBaSegmentParameters', {
    "__STYX_TYPE__": typing.Literal["mris_BA_segment"],
    "surface": InputPathType,
    "profiles": InputPathType,
    "prior_label": InputPathType,
    "output_label": str,
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
        "mris_BA_segment": mris_ba_segment_cargs,
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
        "mris_BA_segment": mris_ba_segment_outputs,
    }
    return vt.get(t)


class MrisBaSegmentOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_ba_segment(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_label_file: OutputPathType
    """Output label file"""


def mris_ba_segment_params(
    surface: InputPathType,
    profiles: InputPathType,
    prior_label: InputPathType,
    output_label: str,
) -> MrisBaSegmentParameters:
    """
    Build parameters.
    
    Args:
        surface: Input surface file.
        profiles: Input profiles file.
        prior_label: Input prior label file.
        output_label: Output label file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_BA_segment",
        "surface": surface,
        "profiles": profiles,
        "prior_label": prior_label,
        "output_label": output_label,
    }
    return params


def mris_ba_segment_cargs(
    params: MrisBaSegmentParameters,
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
    cargs.append("mris_BA_segment")
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(execution.input_file(params.get("profiles")))
    cargs.append(execution.input_file(params.get("prior_label")))
    cargs.append(params.get("output_label"))
    return cargs


def mris_ba_segment_outputs(
    params: MrisBaSegmentParameters,
    execution: Execution,
) -> MrisBaSegmentOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisBaSegmentOutputs(
        root=execution.output_file("."),
        output_label_file=execution.output_file(params.get("output_label")),
    )
    return ret


def mris_ba_segment_execute(
    params: MrisBaSegmentParameters,
    execution: Execution,
) -> MrisBaSegmentOutputs:
    """
    Segments a Brodmann area (MT currently) from a laminar intensity profile
    overlay.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisBaSegmentOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_ba_segment_cargs(params, execution)
    ret = mris_ba_segment_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_ba_segment(
    surface: InputPathType,
    profiles: InputPathType,
    prior_label: InputPathType,
    output_label: str,
    runner: Runner | None = None,
) -> MrisBaSegmentOutputs:
    """
    Segments a Brodmann area (MT currently) from a laminar intensity profile
    overlay.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surface: Input surface file.
        profiles: Input profiles file.
        prior_label: Input prior label file.
        output_label: Output label file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisBaSegmentOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_BA_SEGMENT_METADATA)
    params = mris_ba_segment_params(surface=surface, profiles=profiles, prior_label=prior_label, output_label=output_label)
    return mris_ba_segment_execute(params, execution)


__all__ = [
    "MRIS_BA_SEGMENT_METADATA",
    "MrisBaSegmentOutputs",
    "MrisBaSegmentParameters",
    "mris_ba_segment",
    "mris_ba_segment_params",
]
