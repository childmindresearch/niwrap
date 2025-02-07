# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_AUTOBOX_METADATA = Metadata(
    id="614b8e391ea136b04b4fe49d62f798c0eada766e.boutiques",
    name="3dAutobox",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dAutoboxParameters = typing.TypedDict('V3dAutoboxParameters', {
    "__STYX_TYPE__": typing.Literal["3dAutobox"],
    "input": InputPathType,
    "prefix": typing.NotRequired[str | None],
    "alt_input": typing.NotRequired[InputPathType | None],
    "noclust": bool,
    "extent": bool,
    "extent_ijk": bool,
    "extent_ijk_to_file": typing.NotRequired[str | None],
    "extent_ijk_midslice": bool,
    "extent_ijkord": bool,
    "extent_ijkord_to_file": typing.NotRequired[str | None],
    "extent_xyz_to_file": typing.NotRequired[str | None],
    "extent_xyz_midslice": bool,
    "npad": typing.NotRequired[float | None],
    "npad_safety_on": bool,
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
        "3dAutobox": v_3d_autobox_cargs,
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
        "3dAutobox": v_3d_autobox_outputs,
    }.get(t)


class V3dAutoboxOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_autobox(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3d_autobox_params(
    input_: InputPathType,
    prefix: str | None = None,
    alt_input: InputPathType | None = None,
    noclust: bool = False,
    extent: bool = False,
    extent_ijk: bool = False,
    extent_ijk_to_file: str | None = None,
    extent_ijk_midslice: bool = False,
    extent_ijkord: bool = False,
    extent_ijkord_to_file: str | None = None,
    extent_xyz_to_file: str | None = None,
    extent_xyz_midslice: bool = False,
    npad: float | None = None,
    npad_safety_on: bool = False,
) -> V3dAutoboxParameters:
    """
    Build parameters.
    
    Args:
        input_: Input dataset.
        prefix: Crop the input dataset to the size of the box, and write an\
            output dataset with PREFIX for the name. If not used, no new volume is\
            written out.
        alt_input: An alternate way to specify the input dataset.
        noclust: Don't do any clustering to find the box. Any non-zero voxel\
            will be preserved in the cropped volume.
        extent: Write to standard out the spatial extent of the box.
        extent_ijk: Write out the 6 auto bbox ijk slice numbers to screen: imin\
            imax jmin jmax kmin kmax.
        extent_ijk_to_file: Write out the 6 auto bbox ijk slice numbers to a\
            simple-formatted text file FF: imin imax jmin jmax kmin kmax.
        extent_ijk_midslice: Write out the 3 ijk midslices of the autobox to\
            the screen: imid jmid kmid.
        extent_ijkord: Write out the 6 auto bbox ijk slice numbers to screen in\
            a particular order and format. Useful for scripting.
        extent_ijkord_to_file: Write out the 6 auto bbox ijk slice numbers to a\
            file in a particular order and format. Useful for 3dcalc expressions.
        extent_xyz_to_file: Write out the 6 auto bbox xyz coordinates to a\
            simple-formatted text file GG: xmin xmax ymin ymax zmin zmax.
        extent_xyz_midslice: Write out the 3 xyz midslices of the autobox to\
            the screen: xmid ymid zmid.
        npad: Number of extra voxels to pad on each side of box.
        npad_safety_on: Constrain npad-ded extents to be within dataset.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dAutobox",
        "input": input_,
        "noclust": noclust,
        "extent": extent,
        "extent_ijk": extent_ijk,
        "extent_ijk_midslice": extent_ijk_midslice,
        "extent_ijkord": extent_ijkord,
        "extent_xyz_midslice": extent_xyz_midslice,
        "npad_safety_on": npad_safety_on,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if alt_input is not None:
        params["alt_input"] = alt_input
    if extent_ijk_to_file is not None:
        params["extent_ijk_to_file"] = extent_ijk_to_file
    if extent_ijkord_to_file is not None:
        params["extent_ijkord_to_file"] = extent_ijkord_to_file
    if extent_xyz_to_file is not None:
        params["extent_xyz_to_file"] = extent_xyz_to_file
    if npad is not None:
        params["npad"] = npad
    return params


def v_3d_autobox_cargs(
    params: V3dAutoboxParameters,
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
    cargs.append("3dAutobox")
    cargs.append(execution.input_file(params.get("input")))
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("alt_input") is not None:
        cargs.extend([
            "-input",
            execution.input_file(params.get("alt_input"))
        ])
    if params.get("noclust"):
        cargs.append("-noclust")
    if params.get("extent"):
        cargs.append("-extent")
    if params.get("extent_ijk"):
        cargs.append("-extent_ijk")
    if params.get("extent_ijk_to_file") is not None:
        cargs.extend([
            "-extent_ijk_to_file",
            params.get("extent_ijk_to_file")
        ])
    if params.get("extent_ijk_midslice"):
        cargs.append("-extent_ijk_midslice")
    if params.get("extent_ijkord"):
        cargs.append("-extent_ijkord")
    if params.get("extent_ijkord_to_file") is not None:
        cargs.extend([
            "-extent_ijkord_to_file",
            params.get("extent_ijkord_to_file")
        ])
    if params.get("extent_xyz_to_file") is not None:
        cargs.extend([
            "-extent_xyz_to_file",
            params.get("extent_xyz_to_file")
        ])
    if params.get("extent_xyz_midslice"):
        cargs.append("-extent_xyz_midslice")
    if params.get("npad") is not None:
        cargs.extend([
            "-npad",
            str(params.get("npad"))
        ])
    if params.get("npad_safety_on"):
        cargs.append("-npad_safety_on")
    return cargs


def v_3d_autobox_outputs(
    params: V3dAutoboxParameters,
    execution: Execution,
) -> V3dAutoboxOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dAutoboxOutputs(
        root=execution.output_file("."),
    )
    return ret


def v_3d_autobox_execute(
    params: V3dAutoboxParameters,
    execution: Execution,
) -> V3dAutoboxOutputs:
    """
    Computes size of a box that fits around the volume. Can also be used to crop the
    volume to that box.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dAutoboxOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_autobox_cargs(params, execution)
    ret = v_3d_autobox_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_autobox(
    input_: InputPathType,
    prefix: str | None = None,
    alt_input: InputPathType | None = None,
    noclust: bool = False,
    extent: bool = False,
    extent_ijk: bool = False,
    extent_ijk_to_file: str | None = None,
    extent_ijk_midslice: bool = False,
    extent_ijkord: bool = False,
    extent_ijkord_to_file: str | None = None,
    extent_xyz_to_file: str | None = None,
    extent_xyz_midslice: bool = False,
    npad: float | None = None,
    npad_safety_on: bool = False,
    runner: Runner | None = None,
) -> V3dAutoboxOutputs:
    """
    Computes size of a box that fits around the volume. Can also be used to crop the
    volume to that box.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_: Input dataset.
        prefix: Crop the input dataset to the size of the box, and write an\
            output dataset with PREFIX for the name. If not used, no new volume is\
            written out.
        alt_input: An alternate way to specify the input dataset.
        noclust: Don't do any clustering to find the box. Any non-zero voxel\
            will be preserved in the cropped volume.
        extent: Write to standard out the spatial extent of the box.
        extent_ijk: Write out the 6 auto bbox ijk slice numbers to screen: imin\
            imax jmin jmax kmin kmax.
        extent_ijk_to_file: Write out the 6 auto bbox ijk slice numbers to a\
            simple-formatted text file FF: imin imax jmin jmax kmin kmax.
        extent_ijk_midslice: Write out the 3 ijk midslices of the autobox to\
            the screen: imid jmid kmid.
        extent_ijkord: Write out the 6 auto bbox ijk slice numbers to screen in\
            a particular order and format. Useful for scripting.
        extent_ijkord_to_file: Write out the 6 auto bbox ijk slice numbers to a\
            file in a particular order and format. Useful for 3dcalc expressions.
        extent_xyz_to_file: Write out the 6 auto bbox xyz coordinates to a\
            simple-formatted text file GG: xmin xmax ymin ymax zmin zmax.
        extent_xyz_midslice: Write out the 3 xyz midslices of the autobox to\
            the screen: xmid ymid zmid.
        npad: Number of extra voxels to pad on each side of box.
        npad_safety_on: Constrain npad-ded extents to be within dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dAutoboxOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_AUTOBOX_METADATA)
    params = v_3d_autobox_params(input_=input_, prefix=prefix, alt_input=alt_input, noclust=noclust, extent=extent, extent_ijk=extent_ijk, extent_ijk_to_file=extent_ijk_to_file, extent_ijk_midslice=extent_ijk_midslice, extent_ijkord=extent_ijkord, extent_ijkord_to_file=extent_ijkord_to_file, extent_xyz_to_file=extent_xyz_to_file, extent_xyz_midslice=extent_xyz_midslice, npad=npad, npad_safety_on=npad_safety_on)
    return v_3d_autobox_execute(params, execution)


__all__ = [
    "V3dAutoboxOutputs",
    "V3dAutoboxParameters",
    "V_3D_AUTOBOX_METADATA",
    "v_3d_autobox",
    "v_3d_autobox_params",
]
