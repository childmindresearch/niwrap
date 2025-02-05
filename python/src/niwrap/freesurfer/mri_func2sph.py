# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_FUNC2SPH_METADATA = Metadata(
    id="07527586a882465863cf7ef1f979d3d044731e6d.boutiques",
    name="mri-func2sph",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriFunc2sphParameters = typing.TypedDict('MriFunc2sphParameters', {
    "__STYX_TYPE__": typing.Literal["mri-func2sph"],
    "instem": str,
    "outstem": str,
    "hemisphere": typing.Literal["lh", "rh"],
    "fvitdir": str,
    "hole_filling_iters": typing.NotRequired[float | None],
    "icosahedron_size": typing.NotRequired[float | None],
    "input_type": typing.NotRequired[str | None],
    "umask": typing.NotRequired[str | None],
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
        "mri-func2sph": mri_func2sph_cargs,
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


class MriFunc2sphOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_func2sph(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_func2sph_params(
    instem: str,
    outstem: str,
    hemisphere: typing.Literal["lh", "rh"],
    fvitdir: str,
    hole_filling_iters: float | None = 100,
    icosahedron_size: float | None = 10242,
    input_type: str | None = None,
    umask: str | None = None,
) -> MriFunc2sphParameters:
    """
    Build parameters.
    
    Args:
        instem: Input file stem.
        outstem: Output file stem.
        hemisphere: Hemisphere to process, can be 'lh' or 'rh'.
        fvitdir: Functional vertex information directory.
        hole_filling_iters: Number of hole-filling iterations.
        icosahedron_size: Size of the icosahedron.
        input_type: Type of input data, will be auto-detected if not specified.
        umask: New umask value.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri-func2sph",
        "instem": instem,
        "outstem": outstem,
        "hemisphere": hemisphere,
        "fvitdir": fvitdir,
    }
    if hole_filling_iters is not None:
        params["hole_filling_iters"] = hole_filling_iters
    if icosahedron_size is not None:
        params["icosahedron_size"] = icosahedron_size
    if input_type is not None:
        params["input_type"] = input_type
    if umask is not None:
        params["umask"] = umask
    return params


def mri_func2sph_cargs(
    params: MriFunc2sphParameters,
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
    cargs.append("mri-func2sph")
    cargs.extend([
        "-i",
        params.get("instem")
    ])
    cargs.extend([
        "-o",
        params.get("outstem")
    ])
    cargs.extend([
        "-hemi",
        params.get("hemisphere")
    ])
    cargs.extend([
        "-fvitdir",
        params.get("fvitdir")
    ])
    if params.get("hole_filling_iters") is not None:
        cargs.extend([
            "-niters",
            str(params.get("hole_filling_iters"))
        ])
    if params.get("icosahedron_size") is not None:
        cargs.extend([
            "-icosize",
            str(params.get("icosahedron_size"))
        ])
    if params.get("input_type") is not None:
        cargs.extend([
            "-intype",
            params.get("input_type")
        ])
    if params.get("umask") is not None:
        cargs.extend([
            "-umask",
            params.get("umask")
        ])
    return cargs


def mri_func2sph_outputs(
    params: MriFunc2sphParameters,
    execution: Execution,
) -> MriFunc2sphOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriFunc2sphOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_func2sph_execute(
    params: MriFunc2sphParameters,
    execution: Execution,
) -> MriFunc2sphOutputs:
    """
    Maps functional data from volume space to spherical surface space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriFunc2sphOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_func2sph_cargs(params, execution)
    ret = mri_func2sph_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_func2sph(
    instem: str,
    outstem: str,
    hemisphere: typing.Literal["lh", "rh"],
    fvitdir: str,
    hole_filling_iters: float | None = 100,
    icosahedron_size: float | None = 10242,
    input_type: str | None = None,
    umask: str | None = None,
    runner: Runner | None = None,
) -> MriFunc2sphOutputs:
    """
    Maps functional data from volume space to spherical surface space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        instem: Input file stem.
        outstem: Output file stem.
        hemisphere: Hemisphere to process, can be 'lh' or 'rh'.
        fvitdir: Functional vertex information directory.
        hole_filling_iters: Number of hole-filling iterations.
        icosahedron_size: Size of the icosahedron.
        input_type: Type of input data, will be auto-detected if not specified.
        umask: New umask value.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriFunc2sphOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_FUNC2SPH_METADATA)
    params = mri_func2sph_params(instem=instem, outstem=outstem, hemisphere=hemisphere, fvitdir=fvitdir, hole_filling_iters=hole_filling_iters, icosahedron_size=icosahedron_size, input_type=input_type, umask=umask)
    return mri_func2sph_execute(params, execution)


__all__ = [
    "MRI_FUNC2SPH_METADATA",
    "MriFunc2sphOutputs",
    "MriFunc2sphParameters",
    "mri_func2sph",
    "mri_func2sph_params",
]
