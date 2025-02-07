# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_SEGCENTROIDS_METADATA = Metadata(
    id="60e55d3e62c17ddebe1721176cd1445c815b5c8c.boutiques",
    name="mri_segcentroids",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriSegcentroidsParameters = typing.TypedDict('MriSegcentroidsParameters', {
    "__STYX_TYPE__": typing.Literal["mri_segcentroids"],
    "input_segmentation": InputPathType,
    "output_file": str,
    "pointset_flag": bool,
    "registration_file": typing.NotRequired[InputPathType | None],
    "weights_file": typing.NotRequired[InputPathType | None],
    "lut_file": typing.NotRequired[InputPathType | None],
    "default_lut_flag": bool,
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
        "mri_segcentroids": mri_segcentroids_cargs,
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
        "mri_segcentroids": mri_segcentroids_outputs,
    }.get(t)


class MriSegcentroidsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_segcentroids(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_centroids: OutputPathType
    """Output text file containing the centroids."""


def mri_segcentroids_params(
    input_segmentation: InputPathType,
    output_file: str,
    pointset_flag: bool = False,
    registration_file: InputPathType | None = None,
    weights_file: InputPathType | None = None,
    lut_file: InputPathType | None = None,
    default_lut_flag: bool = False,
) -> MriSegcentroidsParameters:
    """
    Build parameters.
    
    Args:
        input_segmentation: Input segmentation volume file.
        output_file: Output text file for centroids.
        pointset_flag: Save centroids as a Freeview pointset (json).
        registration_file: Apply a linear registration (lta).
        weights_file: Compute weighted centroids with provided voxel weights.
        lut_file: Specify label lookup table.
        default_lut_flag: Use default FreeSurferColorLUT.txt for lookup table.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_segcentroids",
        "input_segmentation": input_segmentation,
        "output_file": output_file,
        "pointset_flag": pointset_flag,
        "default_lut_flag": default_lut_flag,
    }
    if registration_file is not None:
        params["registration_file"] = registration_file
    if weights_file is not None:
        params["weights_file"] = weights_file
    if lut_file is not None:
        params["lut_file"] = lut_file
    return params


def mri_segcentroids_cargs(
    params: MriSegcentroidsParameters,
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
    cargs.append("mri_segcentroids")
    cargs.extend([
        "--i",
        execution.input_file(params.get("input_segmentation"))
    ])
    cargs.extend([
        "--o",
        params.get("output_file")
    ])
    if params.get("pointset_flag"):
        cargs.append("--p")
    if params.get("registration_file") is not None:
        cargs.extend([
            "--reg",
            execution.input_file(params.get("registration_file"))
        ])
    if params.get("weights_file") is not None:
        cargs.extend([
            "--weights",
            execution.input_file(params.get("weights_file"))
        ])
    if params.get("lut_file") is not None:
        cargs.extend([
            "--ctab",
            execution.input_file(params.get("lut_file"))
        ])
    if params.get("default_lut_flag"):
        cargs.append("--ctab-default")
    return cargs


def mri_segcentroids_outputs(
    params: MriSegcentroidsParameters,
    execution: Execution,
) -> MriSegcentroidsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriSegcentroidsOutputs(
        root=execution.output_file("."),
        output_centroids=execution.output_file(params.get("output_file")),
    )
    return ret


def mri_segcentroids_execute(
    params: MriSegcentroidsParameters,
    execution: Execution,
) -> MriSegcentroidsOutputs:
    """
    Computes the center of mass for individual structures in a segmentation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriSegcentroidsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_segcentroids_cargs(params, execution)
    ret = mri_segcentroids_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_segcentroids(
    input_segmentation: InputPathType,
    output_file: str,
    pointset_flag: bool = False,
    registration_file: InputPathType | None = None,
    weights_file: InputPathType | None = None,
    lut_file: InputPathType | None = None,
    default_lut_flag: bool = False,
    runner: Runner | None = None,
) -> MriSegcentroidsOutputs:
    """
    Computes the center of mass for individual structures in a segmentation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_segmentation: Input segmentation volume file.
        output_file: Output text file for centroids.
        pointset_flag: Save centroids as a Freeview pointset (json).
        registration_file: Apply a linear registration (lta).
        weights_file: Compute weighted centroids with provided voxel weights.
        lut_file: Specify label lookup table.
        default_lut_flag: Use default FreeSurferColorLUT.txt for lookup table.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriSegcentroidsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_SEGCENTROIDS_METADATA)
    params = mri_segcentroids_params(input_segmentation=input_segmentation, output_file=output_file, pointset_flag=pointset_flag, registration_file=registration_file, weights_file=weights_file, lut_file=lut_file, default_lut_flag=default_lut_flag)
    return mri_segcentroids_execute(params, execution)


__all__ = [
    "MRI_SEGCENTROIDS_METADATA",
    "MriSegcentroidsOutputs",
    "MriSegcentroidsParameters",
    "mri_segcentroids",
    "mri_segcentroids_params",
]
