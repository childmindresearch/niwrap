# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_BALL_MATCH_METADATA = Metadata(
    id="fe3fd0a09e1cb0531678dcf999710e6d7163d194.boutiques",
    name="3dBallMatch",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dBallMatchParameters = typing.TypedDict('V3dBallMatchParameters', {
    "__STYX_TYPE__": typing.Literal["3dBallMatch"],
    "input_dataset": InputPathType,
    "radius": typing.NotRequired[float | None],
    "dataset_option": typing.NotRequired[str | None],
    "ball_radius": typing.NotRequired[float | None],
    "spheroid_axes": typing.NotRequired[list[float] | None],
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
        "3dBallMatch": v_3d_ball_match_cargs,
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
        "3dBallMatch": v_3d_ball_match_outputs,
    }.get(t)


class V3dBallMatchOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_ball_match(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_stdout: OutputPathType
    """Output containing matching coordinates and related data"""


def v_3d_ball_match_params(
    input_dataset: InputPathType,
    radius: float | None = None,
    dataset_option: str | None = None,
    ball_radius: float | None = None,
    spheroid_axes: list[float] | None = None,
) -> V3dBallMatchParameters:
    """
    Build parameters.
    
    Args:
        input_dataset: Input dataset (e.g., Fred.nii).
        radius: Radius of the 3D ball to match (in mm).
        dataset_option: Specifies the input dataset.
        ball_radius: Set the radius of the 3D ball to match (mm).
        spheroid_axes: Match with a spheroid of revolution, with principal axis\
            radius 'a' and secondary axes radii 'b'.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dBallMatch",
        "input_dataset": input_dataset,
    }
    if radius is not None:
        params["radius"] = radius
    if dataset_option is not None:
        params["dataset_option"] = dataset_option
    if ball_radius is not None:
        params["ball_radius"] = ball_radius
    if spheroid_axes is not None:
        params["spheroid_axes"] = spheroid_axes
    return params


def v_3d_ball_match_cargs(
    params: V3dBallMatchParameters,
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
    cargs.append("3dBallMatch")
    cargs.append(execution.input_file(params.get("input_dataset")))
    if params.get("radius") is not None:
        cargs.append(str(params.get("radius")))
    if params.get("dataset_option") is not None:
        cargs.extend([
            "-input",
            params.get("dataset_option")
        ])
    if params.get("ball_radius") is not None:
        cargs.extend([
            "-ball",
            str(params.get("ball_radius"))
        ])
    if params.get("spheroid_axes") is not None:
        cargs.extend([
            "-spheroid",
            *map(str, params.get("spheroid_axes"))
        ])
    return cargs


def v_3d_ball_match_outputs(
    params: V3dBallMatchParameters,
    execution: Execution,
) -> V3dBallMatchOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dBallMatchOutputs(
        root=execution.output_file("."),
        output_stdout=execution.output_file("stdout"),
    )
    return ret


def v_3d_ball_match_execute(
    params: V3dBallMatchParameters,
    execution: Execution,
) -> V3dBallMatchOutputs:
    """
    A tool to find a good match between a ball (filled sphere) of the given radius
    and a dataset to determine a crude approximate center of the brain quickly.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dBallMatchOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_ball_match_cargs(params, execution)
    ret = v_3d_ball_match_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_ball_match(
    input_dataset: InputPathType,
    radius: float | None = None,
    dataset_option: str | None = None,
    ball_radius: float | None = None,
    spheroid_axes: list[float] | None = None,
    runner: Runner | None = None,
) -> V3dBallMatchOutputs:
    """
    A tool to find a good match between a ball (filled sphere) of the given radius
    and a dataset to determine a crude approximate center of the brain quickly.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Input dataset (e.g., Fred.nii).
        radius: Radius of the 3D ball to match (in mm).
        dataset_option: Specifies the input dataset.
        ball_radius: Set the radius of the 3D ball to match (mm).
        spheroid_axes: Match with a spheroid of revolution, with principal axis\
            radius 'a' and secondary axes radii 'b'.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dBallMatchOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_BALL_MATCH_METADATA)
    params = v_3d_ball_match_params(input_dataset=input_dataset, radius=radius, dataset_option=dataset_option, ball_radius=ball_radius, spheroid_axes=spheroid_axes)
    return v_3d_ball_match_execute(params, execution)


__all__ = [
    "V3dBallMatchOutputs",
    "V3dBallMatchParameters",
    "V_3D_BALL_MATCH_METADATA",
    "v_3d_ball_match",
    "v_3d_ball_match_params",
]
