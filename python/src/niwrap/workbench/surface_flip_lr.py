# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURFACE_FLIP_LR_METADATA = Metadata(
    id="ee8ef63d7e751c54f67f811c70c07449c11152b4.boutiques",
    name="surface-flip-lr",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
SurfaceFlipLrParameters = typing.TypedDict('SurfaceFlipLrParameters', {
    "__STYX_TYPE__": typing.Literal["surface-flip-lr"],
    "surface": InputPathType,
    "surface_out": str,
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
        "surface-flip-lr": surface_flip_lr_cargs,
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
        "surface-flip-lr": surface_flip_lr_outputs,
    }.get(t)


class SurfaceFlipLrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_flip_lr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    surface_out: OutputPathType
    """the output flipped surface"""


def surface_flip_lr_params(
    surface: InputPathType,
    surface_out: str,
) -> SurfaceFlipLrParameters:
    """
    Build parameters.
    
    Args:
        surface: the surface to flip.
        surface_out: the output flipped surface.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surface-flip-lr",
        "surface": surface,
        "surface_out": surface_out,
    }
    return params


def surface_flip_lr_cargs(
    params: SurfaceFlipLrParameters,
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
    cargs.append("-surface-flip-lr")
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(params.get("surface_out"))
    return cargs


def surface_flip_lr_outputs(
    params: SurfaceFlipLrParameters,
    execution: Execution,
) -> SurfaceFlipLrOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfaceFlipLrOutputs(
        root=execution.output_file("."),
        surface_out=execution.output_file(params.get("surface_out")),
    )
    return ret


def surface_flip_lr_execute(
    params: SurfaceFlipLrParameters,
    execution: Execution,
) -> SurfaceFlipLrOutputs:
    """
    Mirror a surface through the yz plane.
    
    This command negates the x coordinate of each vertex, and flips the surface
    normals, so that you have a surface of opposite handedness with the same
    features and vertex correspondence, with normals consistent with the
    original surface. That is, if the input surface has normals facing outward,
    the output surface will also have normals facing outward.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfaceFlipLrOutputs`).
    """
    cargs = surface_flip_lr_cargs(params, execution)
    ret = surface_flip_lr_outputs(params, execution)
    execution.run(cargs)
    return ret


def surface_flip_lr(
    surface: InputPathType,
    surface_out: str,
    runner: Runner | None = None,
) -> SurfaceFlipLrOutputs:
    """
    Mirror a surface through the yz plane.
    
    This command negates the x coordinate of each vertex, and flips the surface
    normals, so that you have a surface of opposite handedness with the same
    features and vertex correspondence, with normals consistent with the
    original surface. That is, if the input surface has normals facing outward,
    the output surface will also have normals facing outward.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface: the surface to flip.
        surface_out: the output flipped surface.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceFlipLrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_FLIP_LR_METADATA)
    params = surface_flip_lr_params(surface=surface, surface_out=surface_out)
    return surface_flip_lr_execute(params, execution)


__all__ = [
    "SURFACE_FLIP_LR_METADATA",
    "SurfaceFlipLrOutputs",
    "SurfaceFlipLrParameters",
    "surface_flip_lr",
    "surface_flip_lr_params",
]
