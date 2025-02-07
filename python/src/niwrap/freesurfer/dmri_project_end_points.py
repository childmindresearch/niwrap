# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DMRI_PROJECT_END_POINTS_METADATA = Metadata(
    id="93cde90208fae7700f6f02d3a5122b37ae3a77f6.boutiques",
    name="dmri_projectEndPoints",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
DmriProjectEndPointsParameters = typing.TypedDict('DmriProjectEndPointsParameters', {
    "__STYX_TYPE__": typing.Literal["dmri_projectEndPoints"],
    "streamline_file": InputPathType,
    "left_surface_file": InputPathType,
    "right_surface_file": InputPathType,
    "left_overlay_file": str,
    "right_overlay_file": str,
    "reference_image": InputPathType,
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
        "dmri_projectEndPoints": dmri_project_end_points_cargs,
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
        "dmri_projectEndPoints": dmri_project_end_points_outputs,
    }.get(t)


class DmriProjectEndPointsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dmri_project_end_points(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_left_overlay: OutputPathType
    """Overlay file for left hemisphere surface"""
    out_right_overlay: OutputPathType
    """Overlay file for right hemisphere surface"""


def dmri_project_end_points_params(
    streamline_file: InputPathType,
    left_surface_file: InputPathType,
    right_surface_file: InputPathType,
    left_overlay_file: str,
    right_overlay_file: str,
    reference_image: InputPathType,
) -> DmriProjectEndPointsParameters:
    """
    Build parameters.
    
    Args:
        streamline_file: Input streamline file (e.g. streamlineFile.trk).
        left_surface_file: Left hemisphere surface file (e.g.\
            surfaceFile_lh.orig).
        right_surface_file: Right hemisphere surface file (e.g.\
            surfaceFile_rh.orig).
        left_overlay_file: Output overlay file for left hemisphere.
        right_overlay_file: Output overlay file for right hemisphere.
        reference_image: Reference image for the projections.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dmri_projectEndPoints",
        "streamline_file": streamline_file,
        "left_surface_file": left_surface_file,
        "right_surface_file": right_surface_file,
        "left_overlay_file": left_overlay_file,
        "right_overlay_file": right_overlay_file,
        "reference_image": reference_image,
    }
    return params


def dmri_project_end_points_cargs(
    params: DmriProjectEndPointsParameters,
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
    cargs.append("dmri_projectEndPoints")
    cargs.extend([
        "-i",
        execution.input_file(params.get("streamline_file"))
    ])
    cargs.extend([
        "-sl",
        execution.input_file(params.get("left_surface_file"))
    ])
    cargs.extend([
        "-sr",
        execution.input_file(params.get("right_surface_file"))
    ])
    cargs.extend([
        "-ol",
        params.get("left_overlay_file")
    ])
    cargs.extend([
        "-or",
        params.get("right_overlay_file")
    ])
    cargs.extend([
        "-ri",
        execution.input_file(params.get("reference_image"))
    ])
    return cargs


def dmri_project_end_points_outputs(
    params: DmriProjectEndPointsParameters,
    execution: Execution,
) -> DmriProjectEndPointsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DmriProjectEndPointsOutputs(
        root=execution.output_file("."),
        out_left_overlay=execution.output_file(params.get("left_overlay_file")),
        out_right_overlay=execution.output_file(params.get("right_overlay_file")),
    )
    return ret


def dmri_project_end_points_execute(
    params: DmriProjectEndPointsParameters,
    execution: Execution,
) -> DmriProjectEndPointsOutputs:
    """
    A tool for projecting the endpoints of streamlines onto cortical surfaces,
    producing overlay files for visualization.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DmriProjectEndPointsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = dmri_project_end_points_cargs(params, execution)
    ret = dmri_project_end_points_outputs(params, execution)
    execution.run(cargs)
    return ret


def dmri_project_end_points(
    streamline_file: InputPathType,
    left_surface_file: InputPathType,
    right_surface_file: InputPathType,
    left_overlay_file: str,
    right_overlay_file: str,
    reference_image: InputPathType,
    runner: Runner | None = None,
) -> DmriProjectEndPointsOutputs:
    """
    A tool for projecting the endpoints of streamlines onto cortical surfaces,
    producing overlay files for visualization.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        streamline_file: Input streamline file (e.g. streamlineFile.trk).
        left_surface_file: Left hemisphere surface file (e.g.\
            surfaceFile_lh.orig).
        right_surface_file: Right hemisphere surface file (e.g.\
            surfaceFile_rh.orig).
        left_overlay_file: Output overlay file for left hemisphere.
        right_overlay_file: Output overlay file for right hemisphere.
        reference_image: Reference image for the projections.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DmriProjectEndPointsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DMRI_PROJECT_END_POINTS_METADATA)
    params = dmri_project_end_points_params(streamline_file=streamline_file, left_surface_file=left_surface_file, right_surface_file=right_surface_file, left_overlay_file=left_overlay_file, right_overlay_file=right_overlay_file, reference_image=reference_image)
    return dmri_project_end_points_execute(params, execution)


__all__ = [
    "DMRI_PROJECT_END_POINTS_METADATA",
    "DmriProjectEndPointsOutputs",
    "DmriProjectEndPointsParameters",
    "dmri_project_end_points",
    "dmri_project_end_points_params",
]
