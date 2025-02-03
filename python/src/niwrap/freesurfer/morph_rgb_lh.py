# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MORPH_RGB_LH_METADATA = Metadata(
    id="8a27176b135c7e00506bbb223dc33d4f8b5c331f.boutiques",
    name="morph_rgb-lh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MorphRgbLhParameters = typing.TypedDict('MorphRgbLhParameters', {
    "__STYX_TYPE__": typing.Literal["morph_rgb-lh"],
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
        "morph_rgb-lh": morph_rgb_lh_cargs,
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


class MorphRgbLhOutputs(typing.NamedTuple):
    """
    Output object returned when calling `morph_rgb_lh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def morph_rgb_lh_params(
    subject_id: str,
) -> MorphRgbLhParameters:
    """
    Build parameters.
    
    Args:
        subject_id: The subject ID to process. This refers to the sub-directory\
            within $SUBJECTS_DIR containing the FreeSurfer processed data for the\
            subject.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "morph_rgb-lh",
        "subject_id": subject_id,
    }
    return params


def morph_rgb_lh_cargs(
    params: MorphRgbLhParameters,
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
        "-lh",
        "morph_rgb" + params.get("subject_id")
    ])
    return cargs


def morph_rgb_lh_outputs(
    params: MorphRgbLhParameters,
    execution: Execution,
) -> MorphRgbLhOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MorphRgbLhOutputs(
        root=execution.output_file("."),
    )
    return ret


def morph_rgb_lh_execute(
    params: MorphRgbLhParameters,
    execution: Execution,
) -> MorphRgbLhOutputs:
    """
    Tool for working with and generating RGB images of morphometric data for the
    left hemisphere in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MorphRgbLhOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = morph_rgb_lh_cargs(params, execution)
    ret = morph_rgb_lh_outputs(params, execution)
    execution.run(cargs)
    return ret


def morph_rgb_lh(
    subject_id: str,
    runner: Runner | None = None,
) -> MorphRgbLhOutputs:
    """
    Tool for working with and generating RGB images of morphometric data for the
    left hemisphere in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_id: The subject ID to process. This refers to the sub-directory\
            within $SUBJECTS_DIR containing the FreeSurfer processed data for the\
            subject.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MorphRgbLhOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MORPH_RGB_LH_METADATA)
    params = morph_rgb_lh_params(subject_id=subject_id)
    return morph_rgb_lh_execute(params, execution)


__all__ = [
    "MORPH_RGB_LH_METADATA",
    "MorphRgbLhOutputs",
    "morph_rgb_lh",
    "morph_rgb_lh_params",
]
