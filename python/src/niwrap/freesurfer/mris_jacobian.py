# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_JACOBIAN_METADATA = Metadata(
    id="f32baf37cb24be970160e497e65bff0c90b9d331.boutiques",
    name="mris_jacobian",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisJacobianParameters = typing.TypedDict('MrisJacobianParameters', {
    "__STYX_TYPE__": typing.Literal["mris_jacobian"],
    "original_surface": InputPathType,
    "mapped_surface": InputPathType,
    "jacobian_file": str,
    "log": bool,
    "noscale": bool,
    "invert": bool,
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
        "mris_jacobian": mris_jacobian_cargs,
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
        "mris_jacobian": mris_jacobian_outputs,
    }.get(t)


class MrisJacobianOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_jacobian(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_jacobian_file: OutputPathType
    """Output file containing the Jacobian of the surface mapping."""


def mris_jacobian_params(
    original_surface: InputPathType,
    mapped_surface: InputPathType,
    jacobian_file: str,
    log: bool = False,
    noscale: bool = False,
    invert: bool = False,
) -> MrisJacobianParameters:
    """
    Build parameters.
    
    Args:
        original_surface: The original surface file.
        mapped_surface: The mapped surface file.
        jacobian_file: The output file name for the Jacobian.
        log: Compute and write out log of Jacobian.
        noscale: Don't scale Jacobian by total surface areas.
        invert: Compute -1/Jacobian for Jacobian < 1.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_jacobian",
        "original_surface": original_surface,
        "mapped_surface": mapped_surface,
        "jacobian_file": jacobian_file,
        "log": log,
        "noscale": noscale,
        "invert": invert,
    }
    return params


def mris_jacobian_cargs(
    params: MrisJacobianParameters,
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
    cargs.append("mris_jacobian")
    cargs.append(execution.input_file(params.get("original_surface")))
    cargs.append(execution.input_file(params.get("mapped_surface")))
    cargs.append(params.get("jacobian_file"))
    if params.get("log"):
        cargs.append("-log")
    if params.get("noscale"):
        cargs.append("-noscale")
    if params.get("invert"):
        cargs.append("-invert")
    return cargs


def mris_jacobian_outputs(
    params: MrisJacobianParameters,
    execution: Execution,
) -> MrisJacobianOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisJacobianOutputs(
        root=execution.output_file("."),
        output_jacobian_file=execution.output_file(params.get("jacobian_file")),
    )
    return ret


def mris_jacobian_execute(
    params: MrisJacobianParameters,
    execution: Execution,
) -> MrisJacobianOutputs:
    """
    This program computes the Jacobian of a surface mapping.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisJacobianOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_jacobian_cargs(params, execution)
    ret = mris_jacobian_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_jacobian(
    original_surface: InputPathType,
    mapped_surface: InputPathType,
    jacobian_file: str,
    log: bool = False,
    noscale: bool = False,
    invert: bool = False,
    runner: Runner | None = None,
) -> MrisJacobianOutputs:
    """
    This program computes the Jacobian of a surface mapping.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        original_surface: The original surface file.
        mapped_surface: The mapped surface file.
        jacobian_file: The output file name for the Jacobian.
        log: Compute and write out log of Jacobian.
        noscale: Don't scale Jacobian by total surface areas.
        invert: Compute -1/Jacobian for Jacobian < 1.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisJacobianOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_JACOBIAN_METADATA)
    params = mris_jacobian_params(original_surface=original_surface, mapped_surface=mapped_surface, jacobian_file=jacobian_file, log=log, noscale=noscale, invert=invert)
    return mris_jacobian_execute(params, execution)


__all__ = [
    "MRIS_JACOBIAN_METADATA",
    "MrisJacobianOutputs",
    "MrisJacobianParameters",
    "mris_jacobian",
    "mris_jacobian_params",
]
