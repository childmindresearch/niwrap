# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURFACE_SMOOTHING_METADATA = Metadata(
    id="5893cea5d893eb8491f51d6b37d8233414b94239.boutiques",
    name="surface-smoothing",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
SurfaceSmoothingParameters = typing.TypedDict('SurfaceSmoothingParameters', {
    "__STYX_TYPE__": typing.Literal["surface-smoothing"],
    "surface_in": InputPathType,
    "smoothing_strength": float,
    "smoothing_iterations": int,
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
        "surface-smoothing": surface_smoothing_cargs,
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
        "surface-smoothing": surface_smoothing_outputs,
    }.get(t)


class SurfaceSmoothingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_smoothing(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    surface_out: OutputPathType
    """output surface file"""


def surface_smoothing_params(
    surface_in: InputPathType,
    smoothing_strength: float,
    smoothing_iterations: int,
    surface_out: str,
) -> SurfaceSmoothingParameters:
    """
    Build parameters.
    
    Args:
        surface_in: the surface file to smooth.
        smoothing_strength: smoothing strength (ranges [0.0 - 1.0]).
        smoothing_iterations: smoothing iterations.
        surface_out: output surface file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surface-smoothing",
        "surface_in": surface_in,
        "smoothing_strength": smoothing_strength,
        "smoothing_iterations": smoothing_iterations,
        "surface_out": surface_out,
    }
    return params


def surface_smoothing_cargs(
    params: SurfaceSmoothingParameters,
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
    cargs.append("-surface-smoothing")
    cargs.append(execution.input_file(params.get("surface_in")))
    cargs.append(str(params.get("smoothing_strength")))
    cargs.append(str(params.get("smoothing_iterations")))
    cargs.append(params.get("surface_out"))
    return cargs


def surface_smoothing_outputs(
    params: SurfaceSmoothingParameters,
    execution: Execution,
) -> SurfaceSmoothingOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfaceSmoothingOutputs(
        root=execution.output_file("."),
        surface_out=execution.output_file(params.get("surface_out")),
    )
    return ret


def surface_smoothing_execute(
    params: SurfaceSmoothingParameters,
    execution: Execution,
) -> SurfaceSmoothingOutputs:
    """
    Surface smoothing.
    
    Smooths a surface by averaging vertex coordinates with those of the
    neighboring vertices.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfaceSmoothingOutputs`).
    """
    cargs = surface_smoothing_cargs(params, execution)
    ret = surface_smoothing_outputs(params, execution)
    execution.run(cargs)
    return ret


def surface_smoothing(
    surface_in: InputPathType,
    smoothing_strength: float,
    smoothing_iterations: int,
    surface_out: str,
    runner: Runner | None = None,
) -> SurfaceSmoothingOutputs:
    """
    Surface smoothing.
    
    Smooths a surface by averaging vertex coordinates with those of the
    neighboring vertices.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface_in: the surface file to smooth.
        smoothing_strength: smoothing strength (ranges [0.0 - 1.0]).
        smoothing_iterations: smoothing iterations.
        surface_out: output surface file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceSmoothingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_SMOOTHING_METADATA)
    params = surface_smoothing_params(surface_in=surface_in, smoothing_strength=smoothing_strength, smoothing_iterations=smoothing_iterations, surface_out=surface_out)
    return surface_smoothing_execute(params, execution)


__all__ = [
    "SURFACE_SMOOTHING_METADATA",
    "SurfaceSmoothingOutputs",
    "SurfaceSmoothingParameters",
    "surface_smoothing",
    "surface_smoothing_params",
]
