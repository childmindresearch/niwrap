# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

POINTFLIRT_METADATA = Metadata(
    id="460b6d9bdf4517e6ada68203b2bdc3886e4c92c3.boutiques",
    name="pointflirt",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
PointflirtParameters = typing.TypedDict('PointflirtParameters', {
    "__STYX_TYPE__": typing.Literal["pointflirt"],
    "invol_coords": InputPathType,
    "refvol_coords": InputPathType,
    "out_matrix": typing.NotRequired[str | None],
    "use_vox": bool,
    "vol_input": typing.NotRequired[InputPathType | None],
    "vol_ref": typing.NotRequired[InputPathType | None],
    "verbose_flag": bool,
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
        "pointflirt": pointflirt_cargs,
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
        "pointflirt": pointflirt_outputs,
    }.get(t)


class PointflirtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `pointflirt(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_matrix_file: OutputPathType | None
    """Affine matrix output file"""


def pointflirt_params(
    invol_coords: InputPathType,
    refvol_coords: InputPathType,
    out_matrix: str | None = None,
    use_vox: bool = False,
    vol_input: InputPathType | None = None,
    vol_ref: InputPathType | None = None,
    verbose_flag: bool = False,
) -> PointflirtParameters:
    """
    Build parameters.
    
    Args:
        invol_coords: Filename of input volume coordinates.
        refvol_coords: Filename of reference volume coordinates.
        out_matrix: Filename of affine matrix output.
        use_vox: Use voxel coordinates, not mm, for input.
        vol_input: Filename of input volume (needed for --vox option).
        vol_ref: Filename of reference volume (needed for --vox option).
        verbose_flag: Switch on diagnostic messages.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "pointflirt",
        "invol_coords": invol_coords,
        "refvol_coords": refvol_coords,
        "use_vox": use_vox,
        "verbose_flag": verbose_flag,
    }
    if out_matrix is not None:
        params["out_matrix"] = out_matrix
    if vol_input is not None:
        params["vol_input"] = vol_input
    if vol_ref is not None:
        params["vol_ref"] = vol_ref
    return params


def pointflirt_cargs(
    params: PointflirtParameters,
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
    cargs.append("pointflirt")
    cargs.extend([
        "-i",
        execution.input_file(params.get("invol_coords"))
    ])
    cargs.extend([
        "-r",
        execution.input_file(params.get("refvol_coords"))
    ])
    if params.get("out_matrix") is not None:
        cargs.extend([
            "-o",
            params.get("out_matrix")
        ])
    if params.get("use_vox"):
        cargs.append("--vox")
    if params.get("vol_input") is not None:
        cargs.extend([
            "--invol",
            execution.input_file(params.get("vol_input"))
        ])
    if params.get("vol_ref") is not None:
        cargs.extend([
            "--refvol",
            execution.input_file(params.get("vol_ref"))
        ])
    if params.get("verbose_flag"):
        cargs.append("-v")
    return cargs


def pointflirt_outputs(
    params: PointflirtParameters,
    execution: Execution,
) -> PointflirtOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = PointflirtOutputs(
        root=execution.output_file("."),
        output_matrix_file=execution.output_file(params.get("out_matrix")) if (params.get("out_matrix") is not None) else None,
    )
    return ret


def pointflirt_execute(
    params: PointflirtParameters,
    execution: Execution,
) -> PointflirtOutputs:
    """
    A tool to align point coordinates between volumes and compute affine
    transformation matrices.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `PointflirtOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = pointflirt_cargs(params, execution)
    ret = pointflirt_outputs(params, execution)
    execution.run(cargs)
    return ret


def pointflirt(
    invol_coords: InputPathType,
    refvol_coords: InputPathType,
    out_matrix: str | None = None,
    use_vox: bool = False,
    vol_input: InputPathType | None = None,
    vol_ref: InputPathType | None = None,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> PointflirtOutputs:
    """
    A tool to align point coordinates between volumes and compute affine
    transformation matrices.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        invol_coords: Filename of input volume coordinates.
        refvol_coords: Filename of reference volume coordinates.
        out_matrix: Filename of affine matrix output.
        use_vox: Use voxel coordinates, not mm, for input.
        vol_input: Filename of input volume (needed for --vox option).
        vol_ref: Filename of reference volume (needed for --vox option).
        verbose_flag: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PointflirtOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(POINTFLIRT_METADATA)
    params = pointflirt_params(invol_coords=invol_coords, refvol_coords=refvol_coords, out_matrix=out_matrix, use_vox=use_vox, vol_input=vol_input, vol_ref=vol_ref, verbose_flag=verbose_flag)
    return pointflirt_execute(params, execution)


__all__ = [
    "POINTFLIRT_METADATA",
    "PointflirtOutputs",
    "PointflirtParameters",
    "pointflirt",
    "pointflirt_params",
]
