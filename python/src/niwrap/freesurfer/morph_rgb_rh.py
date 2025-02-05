# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MORPH_RGB_RH_METADATA = Metadata(
    id="d9ff451dc5d9779a26edbf9b5422cc9aac7df58e.boutiques",
    name="morph_rgb-rh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MorphRgbRhParameters = typing.TypedDict('MorphRgbRhParameters', {
    "__STYX_TYPE__": typing.Literal["morph_rgb-rh"],
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
        "morph_rgb-rh": morph_rgb_rh_cargs,
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


class MorphRgbRhOutputs(typing.NamedTuple):
    """
    Output object returned when calling `morph_rgb_rh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def morph_rgb_rh_params(
    subject_id: str,
) -> MorphRgbRhParameters:
    """
    Build parameters.
    
    Args:
        subject_id: Subject ID for which the RGB morphing should be performed.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "morph_rgb-rh",
        "subject_id": subject_id,
    }
    return params


def morph_rgb_rh_cargs(
    params: MorphRgbRhParameters,
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
    cargs.extend([
        "-rh",
        "morph_rgb" + params.get("subject_id")
    ])
    return cargs


def morph_rgb_rh_outputs(
    params: MorphRgbRhParameters,
    execution: Execution,
) -> MorphRgbRhOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MorphRgbRhOutputs(
        root=execution.output_file("."),
    )
    return ret


def morph_rgb_rh_execute(
    params: MorphRgbRhParameters,
    execution: Execution,
) -> MorphRgbRhOutputs:
    """
    Morphs RGB values onto a FreeSurfer right hemisphere surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MorphRgbRhOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = morph_rgb_rh_cargs(params, execution)
    ret = morph_rgb_rh_outputs(params, execution)
    execution.run(cargs)
    return ret


def morph_rgb_rh(
    subject_id: str,
    runner: Runner | None = None,
) -> MorphRgbRhOutputs:
    """
    Morphs RGB values onto a FreeSurfer right hemisphere surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_id: Subject ID for which the RGB morphing should be performed.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MorphRgbRhOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MORPH_RGB_RH_METADATA)
    params = morph_rgb_rh_params(subject_id=subject_id)
    return morph_rgb_rh_execute(params, execution)


__all__ = [
    "MORPH_RGB_RH_METADATA",
    "MorphRgbRhOutputs",
    "MorphRgbRhParameters",
    "morph_rgb_rh",
    "morph_rgb_rh_params",
]
