# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_NWARP_APPLY_METADATA = Metadata(
    id="0a5385bf1fc9acdee0016adc133f63a8ec8a4e36.boutiques",
    name="3dNwarpApply",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dNwarpApplyParameters = typing.TypedDict('V3dNwarpApplyParameters', {
    "__STYX_TYPE__": typing.Literal["3dNwarpApply"],
    "nwarp": str,
    "iwarp": bool,
    "source": str,
    "master": typing.NotRequired[str | None],
    "newgrid": typing.NotRequired[str | None],
    "dxyz": typing.NotRequired[str | None],
    "interp": typing.NotRequired[str | None],
    "ainterp": typing.NotRequired[str | None],
    "prefix": typing.NotRequired[str | None],
    "suffix": typing.NotRequired[str | None],
    "short": bool,
    "wprefix": typing.NotRequired[str | None],
    "quiet": bool,
    "verb": bool,
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
        "3dNwarpApply": v_3d_nwarp_apply_cargs,
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
        "3dNwarpApply": v_3d_nwarp_apply_outputs,
    }.get(t)


class V3dNwarpApplyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_nwarp_apply(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    warped_output: OutputPathType | None
    """Warped output dataset"""
    generated_warp: OutputPathType | None
    """Warp dataset generated during application"""


def v_3d_nwarp_apply_params(
    nwarp: str,
    source: str,
    iwarp: bool = False,
    master: str | None = None,
    newgrid: str | None = None,
    dxyz: str | None = None,
    interp: str | None = None,
    ainterp: str | None = None,
    prefix: str | None = None,
    suffix: str | None = None,
    short: bool = False,
    wprefix: str | None = None,
    quiet: bool = False,
    verb: bool = False,
) -> V3dNwarpApplyParameters:
    """
    Build parameters.
    
    Args:
        nwarp: The name of the 3D warp dataset. Multiple warps can be\
            catenated.
        source: The name of the source dataset to be warped. Multiple datasets\
            can be supplied.
        iwarp: Invert the warp specified in '-nwarp'.
        master: The name of the master dataset which defines the output grid.
        newgrid: The new grid spacing (cubical voxels, in mm).
        dxyz: Specify a different grid spacing (cubical voxels, in mm).
        interp: The interpolation mode ('NN', 'linear', 'cubic', 'quintic',\
            'wsinc5').
        ainterp: Specify a different interpolation mode for the data than the\
            warp.
        prefix: The name of the new output dataset. Multiple names can be\
            supplied if more than one source dataset is input.
        suffix: Change the default suffix '_Nwarp' to a user-defined suffix.
        short: Write output dataset using 16-bit short integers rather than the\
            usual 32-bit floats.
        wprefix: Save every warp generated in the process to a separate\
            dataset.
        quiet: Don't be verbose.
        verb: Be extra verbose.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dNwarpApply",
        "nwarp": nwarp,
        "iwarp": iwarp,
        "source": source,
        "short": short,
        "quiet": quiet,
        "verb": verb,
    }
    if master is not None:
        params["master"] = master
    if newgrid is not None:
        params["newgrid"] = newgrid
    if dxyz is not None:
        params["dxyz"] = dxyz
    if interp is not None:
        params["interp"] = interp
    if ainterp is not None:
        params["ainterp"] = ainterp
    if prefix is not None:
        params["prefix"] = prefix
    if suffix is not None:
        params["suffix"] = suffix
    if wprefix is not None:
        params["wprefix"] = wprefix
    return params


def v_3d_nwarp_apply_cargs(
    params: V3dNwarpApplyParameters,
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
    cargs.append("3dNwarpApply")
    cargs.extend([
        "-nwarp",
        params.get("nwarp")
    ])
    if params.get("iwarp"):
        cargs.append("-iwarp")
    cargs.extend([
        "-source",
        params.get("source")
    ])
    if params.get("master") is not None:
        cargs.extend([
            "-master",
            params.get("master")
        ])
    if params.get("newgrid") is not None:
        cargs.extend([
            "-newgrid",
            params.get("newgrid")
        ])
    if params.get("dxyz") is not None:
        cargs.extend([
            "-dxyz",
            params.get("dxyz")
        ])
    if params.get("interp") is not None:
        cargs.extend([
            "-interp",
            params.get("interp")
        ])
    if params.get("ainterp") is not None:
        cargs.extend([
            "-ainterp",
            params.get("ainterp")
        ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("suffix") is not None:
        cargs.extend([
            "-suffix",
            params.get("suffix")
        ])
    if params.get("short"):
        cargs.append("-short")
    if params.get("wprefix") is not None:
        cargs.extend([
            "-wprefix",
            params.get("wprefix")
        ])
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("verb"):
        cargs.append("-verb")
    return cargs


def v_3d_nwarp_apply_outputs(
    params: V3dNwarpApplyParameters,
    execution: Execution,
) -> V3dNwarpApplyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dNwarpApplyOutputs(
        root=execution.output_file("."),
        warped_output=execution.output_file(params.get("prefix") + "_" + params.get("source") + "_warped.nii.gz") if (params.get("prefix") is not None) else None,
        generated_warp=execution.output_file(params.get("wprefix") + "_warp_????.nii.gz") if (params.get("wprefix") is not None) else None,
    )
    return ret


def v_3d_nwarp_apply_execute(
    params: V3dNwarpApplyParameters,
    execution: Execution,
) -> V3dNwarpApplyOutputs:
    """
    Program to apply a nonlinear 3D warp saved from 3dQwarp (or 3dNwarpCat, etc.) to
    a 3D dataset, to produce a warped version of the source dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dNwarpApplyOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_nwarp_apply_cargs(params, execution)
    ret = v_3d_nwarp_apply_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_nwarp_apply(
    nwarp: str,
    source: str,
    iwarp: bool = False,
    master: str | None = None,
    newgrid: str | None = None,
    dxyz: str | None = None,
    interp: str | None = None,
    ainterp: str | None = None,
    prefix: str | None = None,
    suffix: str | None = None,
    short: bool = False,
    wprefix: str | None = None,
    quiet: bool = False,
    verb: bool = False,
    runner: Runner | None = None,
) -> V3dNwarpApplyOutputs:
    """
    Program to apply a nonlinear 3D warp saved from 3dQwarp (or 3dNwarpCat, etc.) to
    a 3D dataset, to produce a warped version of the source dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        nwarp: The name of the 3D warp dataset. Multiple warps can be\
            catenated.
        source: The name of the source dataset to be warped. Multiple datasets\
            can be supplied.
        iwarp: Invert the warp specified in '-nwarp'.
        master: The name of the master dataset which defines the output grid.
        newgrid: The new grid spacing (cubical voxels, in mm).
        dxyz: Specify a different grid spacing (cubical voxels, in mm).
        interp: The interpolation mode ('NN', 'linear', 'cubic', 'quintic',\
            'wsinc5').
        ainterp: Specify a different interpolation mode for the data than the\
            warp.
        prefix: The name of the new output dataset. Multiple names can be\
            supplied if more than one source dataset is input.
        suffix: Change the default suffix '_Nwarp' to a user-defined suffix.
        short: Write output dataset using 16-bit short integers rather than the\
            usual 32-bit floats.
        wprefix: Save every warp generated in the process to a separate\
            dataset.
        quiet: Don't be verbose.
        verb: Be extra verbose.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dNwarpApplyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_NWARP_APPLY_METADATA)
    params = v_3d_nwarp_apply_params(nwarp=nwarp, iwarp=iwarp, source=source, master=master, newgrid=newgrid, dxyz=dxyz, interp=interp, ainterp=ainterp, prefix=prefix, suffix=suffix, short=short, wprefix=wprefix, quiet=quiet, verb=verb)
    return v_3d_nwarp_apply_execute(params, execution)


__all__ = [
    "V3dNwarpApplyOutputs",
    "V3dNwarpApplyParameters",
    "V_3D_NWARP_APPLY_METADATA",
    "v_3d_nwarp_apply",
    "v_3d_nwarp_apply_params",
]
