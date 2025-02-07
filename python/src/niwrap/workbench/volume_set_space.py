# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

VOLUME_SET_SPACE_METADATA = Metadata(
    id="cc06a5ed74f7b2995a9e56b76a45660865d0ab11.boutiques",
    name="volume-set-space",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
VolumeSetSpacePlumbParameters = typing.TypedDict('VolumeSetSpacePlumbParameters', {
    "__STYX_TYPE__": typing.Literal["plumb"],
    "axis_order": str,
    "x_spacing": float,
    "y_spacing": float,
    "z_spacing": float,
    "x_offset": float,
    "y_offset": float,
    "z_offset": float,
})
VolumeSetSpaceSformParameters = typing.TypedDict('VolumeSetSpaceSformParameters', {
    "__STYX_TYPE__": typing.Literal["sform"],
    "xi_spacing": float,
    "xj_spacing": float,
    "xk_spacing": float,
    "x_offset": float,
    "yi_spacing": float,
    "yj_spacing": float,
    "yk_spacing": float,
    "y_offset": float,
    "zi_spacing": float,
    "zj_spacing": float,
    "zk_spacing": float,
    "z_offset": float,
})
VolumeSetSpaceFileParameters = typing.TypedDict('VolumeSetSpaceFileParameters', {
    "__STYX_TYPE__": typing.Literal["file"],
    "volume_ref": str,
    "opt_ignore_dims": bool,
})
VolumeSetSpaceParameters = typing.TypedDict('VolumeSetSpaceParameters', {
    "__STYX_TYPE__": typing.Literal["volume-set-space"],
    "volume_in": InputPathType,
    "volume_out": str,
    "plumb": typing.NotRequired[VolumeSetSpacePlumbParameters | None],
    "sform": typing.NotRequired[VolumeSetSpaceSformParameters | None],
    "file": typing.NotRequired[VolumeSetSpaceFileParameters | None],
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
        "volume-set-space": volume_set_space_cargs,
        "plumb": volume_set_space_plumb_cargs,
        "sform": volume_set_space_sform_cargs,
        "file": volume_set_space_file_cargs,
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
        "volume-set-space": volume_set_space_outputs,
        "plumb": volume_set_space_plumb_outputs,
        "sform": volume_set_space_sform_outputs,
        "file": volume_set_space_file_outputs,
    }.get(t)


def volume_set_space_plumb_params(
    axis_order: str,
    x_spacing: float,
    y_spacing: float,
    z_spacing: float,
    x_offset: float,
    y_offset: float,
    z_offset: float,
) -> VolumeSetSpacePlumbParameters:
    """
    Build parameters.
    
    Args:
        axis_order: a string like 'XYZ' that specifies which index is along\
            which spatial dimension.
        x_spacing: change in x-coordinate from incrementing the relevant index.
        y_spacing: change in y-coordinate from incrementing the relevant index.
        z_spacing: change in z-coordinate from incrementing the relevant index.
        x_offset: the x-coordinate of the first voxel.
        y_offset: the y-coordinate of the first voxel.
        z_offset: the z-coordinate of the first voxel.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "plumb",
        "axis_order": axis_order,
        "x_spacing": x_spacing,
        "y_spacing": y_spacing,
        "z_spacing": z_spacing,
        "x_offset": x_offset,
        "y_offset": y_offset,
        "z_offset": z_offset,
    }
    return params


def volume_set_space_plumb_cargs(
    params: VolumeSetSpacePlumbParameters,
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
    cargs.append("-plumb")
    cargs.append(params.get("axis_order"))
    cargs.append(str(params.get("x_spacing")))
    cargs.append(str(params.get("y_spacing")))
    cargs.append(str(params.get("z_spacing")))
    cargs.append(str(params.get("x_offset")))
    cargs.append(str(params.get("y_offset")))
    cargs.append(str(params.get("z_offset")))
    return cargs


def volume_set_space_sform_params(
    xi_spacing: float,
    xj_spacing: float,
    xk_spacing: float,
    x_offset: float,
    yi_spacing: float,
    yj_spacing: float,
    yk_spacing: float,
    y_offset: float,
    zi_spacing: float,
    zj_spacing: float,
    zk_spacing: float,
    z_offset: float,
) -> VolumeSetSpaceSformParameters:
    """
    Build parameters.
    
    Args:
        xi_spacing: increase in x coordinate from incrementing the i index.
        xj_spacing: increase in x coordinate from incrementing the j index.
        xk_spacing: increase in x coordinate from incrementing the k index.
        x_offset: x coordinate of first voxel.
        yi_spacing: increase in y coordinate from incrementing the i index.
        yj_spacing: increase in y coordinate from incrementing the j index.
        yk_spacing: increase in y coordinate from incrementing the k index.
        y_offset: y coordinate of first voxel.
        zi_spacing: increase in z coordinate from incrementing the i index.
        zj_spacing: increase in z coordinate from incrementing the j index.
        zk_spacing: increase in z coordinate from incrementing the k index.
        z_offset: z coordinate of first voxel.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "sform",
        "xi_spacing": xi_spacing,
        "xj_spacing": xj_spacing,
        "xk_spacing": xk_spacing,
        "x_offset": x_offset,
        "yi_spacing": yi_spacing,
        "yj_spacing": yj_spacing,
        "yk_spacing": yk_spacing,
        "y_offset": y_offset,
        "zi_spacing": zi_spacing,
        "zj_spacing": zj_spacing,
        "zk_spacing": zk_spacing,
        "z_offset": z_offset,
    }
    return params


def volume_set_space_sform_cargs(
    params: VolumeSetSpaceSformParameters,
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
    cargs.append("-sform")
    cargs.append(str(params.get("xi_spacing")))
    cargs.append(str(params.get("xj_spacing")))
    cargs.append(str(params.get("xk_spacing")))
    cargs.append(str(params.get("x_offset")))
    cargs.append(str(params.get("yi_spacing")))
    cargs.append(str(params.get("yj_spacing")))
    cargs.append(str(params.get("yk_spacing")))
    cargs.append(str(params.get("y_offset")))
    cargs.append(str(params.get("zi_spacing")))
    cargs.append(str(params.get("zj_spacing")))
    cargs.append(str(params.get("zk_spacing")))
    cargs.append(str(params.get("z_offset")))
    return cargs


def volume_set_space_file_params(
    volume_ref: str,
    opt_ignore_dims: bool = False,
) -> VolumeSetSpaceFileParameters:
    """
    Build parameters.
    
    Args:
        volume_ref: volume file to use for reference space.
        opt_ignore_dims: copy the spacing info even if the dimensions don't\
            match.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "file",
        "volume_ref": volume_ref,
        "opt_ignore_dims": opt_ignore_dims,
    }
    return params


def volume_set_space_file_cargs(
    params: VolumeSetSpaceFileParameters,
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
    cargs.append("-file")
    cargs.append(params.get("volume_ref"))
    if params.get("opt_ignore_dims"):
        cargs.append("-ignore-dims")
    return cargs


class VolumeSetSpaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_set_space(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def volume_set_space_params(
    volume_in: InputPathType,
    volume_out: str,
    plumb: VolumeSetSpacePlumbParameters | None = None,
    sform: VolumeSetSpaceSformParameters | None = None,
    file: VolumeSetSpaceFileParameters | None = None,
) -> VolumeSetSpaceParameters:
    """
    Build parameters.
    
    Args:
        volume_in: the input volume.
        volume_out: output - the output volume.
        plumb: set via axis order and spacing/offset.
        sform: set via a nifti sform.
        file: copy spacing info from volume file with matching dimensions.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume-set-space",
        "volume_in": volume_in,
        "volume_out": volume_out,
    }
    if plumb is not None:
        params["plumb"] = plumb
    if sform is not None:
        params["sform"] = sform
    if file is not None:
        params["file"] = file
    return params


def volume_set_space_cargs(
    params: VolumeSetSpaceParameters,
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
    cargs.append("wb_command")
    cargs.append("-volume-set-space")
    cargs.append(execution.input_file(params.get("volume_in")))
    cargs.append(params.get("volume_out"))
    if params.get("plumb") is not None:
        cargs.extend(dyn_cargs(params.get("plumb")["__STYXTYPE__"])(params.get("plumb"), execution))
    if params.get("sform") is not None:
        cargs.extend(dyn_cargs(params.get("sform")["__STYXTYPE__"])(params.get("sform"), execution))
    if params.get("file") is not None:
        cargs.extend(dyn_cargs(params.get("file")["__STYXTYPE__"])(params.get("file"), execution))
    return cargs


def volume_set_space_outputs(
    params: VolumeSetSpaceParameters,
    execution: Execution,
) -> VolumeSetSpaceOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VolumeSetSpaceOutputs(
        root=execution.output_file("."),
    )
    return ret


def volume_set_space_execute(
    params: VolumeSetSpaceParameters,
    execution: Execution,
) -> VolumeSetSpaceOutputs:
    """
    Change volume space information.
    
    Writes a copy of the volume file, with the spacing information changed as
    specified. No reordering of the voxel data occurs, see -volume-reorient to
    change the volume indexing order and reorder the voxels to match. Exactly
    one of -plumb, -sform, or -file must be specified.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VolumeSetSpaceOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = volume_set_space_cargs(params, execution)
    ret = volume_set_space_outputs(params, execution)
    execution.run(cargs)
    return ret


def volume_set_space(
    volume_in: InputPathType,
    volume_out: str,
    plumb: VolumeSetSpacePlumbParameters | None = None,
    sform: VolumeSetSpaceSformParameters | None = None,
    file: VolumeSetSpaceFileParameters | None = None,
    runner: Runner | None = None,
) -> VolumeSetSpaceOutputs:
    """
    Change volume space information.
    
    Writes a copy of the volume file, with the spacing information changed as
    specified. No reordering of the voxel data occurs, see -volume-reorient to
    change the volume indexing order and reorder the voxels to match. Exactly
    one of -plumb, -sform, or -file must be specified.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        volume_in: the input volume.
        volume_out: output - the output volume.
        plumb: set via axis order and spacing/offset.
        sform: set via a nifti sform.
        file: copy spacing info from volume file with matching dimensions.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeSetSpaceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_SET_SPACE_METADATA)
    params = volume_set_space_params(volume_in=volume_in, volume_out=volume_out, plumb=plumb, sform=sform, file=file)
    return volume_set_space_execute(params, execution)


__all__ = [
    "VOLUME_SET_SPACE_METADATA",
    "VolumeSetSpaceFileParameters",
    "VolumeSetSpaceOutputs",
    "VolumeSetSpaceParameters",
    "VolumeSetSpacePlumbParameters",
    "VolumeSetSpaceSformParameters",
    "volume_set_space",
    "volume_set_space_file_params",
    "volume_set_space_params",
    "volume_set_space_plumb_params",
    "volume_set_space_sform_params",
]
