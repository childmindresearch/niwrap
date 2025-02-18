# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_ROTATE_METADATA = Metadata(
    id="ef8f8112c666b20f57f67d98677ecae66ab493de.boutiques",
    name="mris_rotate",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisRotateParameters = typing.TypedDict('MrisRotateParameters', {
    "__STYX_TYPE__": typing.Literal["mris_rotate"],
    "input_surface": InputPathType,
    "alpha_deg": float,
    "beta_deg": float,
    "gamma_deg": float,
    "output_surface": str,
    "regfile": typing.NotRequired[InputPathType | None],
    "invalidate_geometry": bool,
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
        "mris_rotate": mris_rotate_cargs,
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
        "mris_rotate": mris_rotate_outputs,
    }.get(t)


class MrisRotateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_rotate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    rotated_surface: OutputPathType
    """The rotated output surface."""


def mris_rotate_params(
    input_surface: InputPathType,
    alpha_deg: float,
    beta_deg: float,
    gamma_deg: float,
    output_surface: str,
    regfile: InputPathType | None = None,
    invalidate_geometry: bool = False,
) -> MrisRotateParameters:
    """
    Build parameters.
    
    Args:
        input_surface: Input surface file to be rotated.
        alpha_deg: Rotation angle in degrees around the X-axis.
        beta_deg: Rotation angle in degrees around the Y-axis.
        gamma_deg: Rotation angle in degrees around the Z-axis.
        output_surface: Output surface file after rotation.
        regfile: Extract angles from registration file, ignores alpha, beta,\
            gamma.
        invalidate_geometry: Invalidate volume geometry in output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_rotate",
        "input_surface": input_surface,
        "alpha_deg": alpha_deg,
        "beta_deg": beta_deg,
        "gamma_deg": gamma_deg,
        "output_surface": output_surface,
        "invalidate_geometry": invalidate_geometry,
    }
    if regfile is not None:
        params["regfile"] = regfile
    return params


def mris_rotate_cargs(
    params: MrisRotateParameters,
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
    cargs.append("mris_rotate")
    cargs.append(execution.input_file(params.get("input_surface")))
    cargs.append(str(params.get("alpha_deg")))
    cargs.append(str(params.get("beta_deg")))
    cargs.append(str(params.get("gamma_deg")))
    cargs.append(params.get("output_surface"))
    if params.get("regfile") is not None:
        cargs.extend([
            "-r",
            execution.input_file(params.get("regfile"))
        ])
    if params.get("invalidate_geometry"):
        cargs.append("-n")
    return cargs


def mris_rotate_outputs(
    params: MrisRotateParameters,
    execution: Execution,
) -> MrisRotateOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisRotateOutputs(
        root=execution.output_file("."),
        rotated_surface=execution.output_file(params.get("output_surface")),
    )
    return ret


def mris_rotate_execute(
    params: MrisRotateParameters,
    execution: Execution,
) -> MrisRotateOutputs:
    """
    Rotate a surface given three angles.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisRotateOutputs`).
    """
    params = execution.params(params)
    cargs = mris_rotate_cargs(params, execution)
    ret = mris_rotate_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_rotate(
    input_surface: InputPathType,
    alpha_deg: float,
    beta_deg: float,
    gamma_deg: float,
    output_surface: str,
    regfile: InputPathType | None = None,
    invalidate_geometry: bool = False,
    runner: Runner | None = None,
) -> MrisRotateOutputs:
    """
    Rotate a surface given three angles.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: Input surface file to be rotated.
        alpha_deg: Rotation angle in degrees around the X-axis.
        beta_deg: Rotation angle in degrees around the Y-axis.
        gamma_deg: Rotation angle in degrees around the Z-axis.
        output_surface: Output surface file after rotation.
        regfile: Extract angles from registration file, ignores alpha, beta,\
            gamma.
        invalidate_geometry: Invalidate volume geometry in output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisRotateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_ROTATE_METADATA)
    params = mris_rotate_params(input_surface=input_surface, alpha_deg=alpha_deg, beta_deg=beta_deg, gamma_deg=gamma_deg, output_surface=output_surface, regfile=regfile, invalidate_geometry=invalidate_geometry)
    return mris_rotate_execute(params, execution)


__all__ = [
    "MRIS_ROTATE_METADATA",
    "MrisRotateOutputs",
    "MrisRotateParameters",
    "mris_rotate",
    "mris_rotate_params",
]
