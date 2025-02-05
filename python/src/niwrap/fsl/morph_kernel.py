# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MORPH_KERNEL_METADATA = Metadata(
    id="68541ec7748d8d13f5c268560fc3b05f625b4dae.boutiques",
    name="morph_kernel",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
MorphKernelParameters = typing.TypedDict('MorphKernelParameters', {
    "__STYX_TYPE__": typing.Literal["morph_kernel"],
    "cube_side_length": float,
    "sphere_radius": float,
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
        "morph_kernel": morph_kernel_cargs,
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
    vt = {
        "morph_kernel": morph_kernel_outputs,
    }
    return vt.get(t)


class MorphKernelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `morph_kernel(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    morph_kernel_output: OutputPathType
    """Output morphological kernel file"""


def morph_kernel_params(
    cube_side_length: float,
    sphere_radius: float,
) -> MorphKernelParameters:
    """
    Build parameters.
    
    Args:
        cube_side_length: Side length of the cube (e.g., 11).
        sphere_radius: Radius of the sphere (e.g., 5.5).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "morph_kernel",
        "cube_side_length": cube_side_length,
        "sphere_radius": sphere_radius,
    }
    return params


def morph_kernel_cargs(
    params: MorphKernelParameters,
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
    cargs.append("morph_kernel")
    cargs.append(str(params.get("cube_side_length")))
    cargs.append(str(params.get("sphere_radius")))
    return cargs


def morph_kernel_outputs(
    params: MorphKernelParameters,
    execution: Execution,
) -> MorphKernelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MorphKernelOutputs(
        root=execution.output_file("."),
        morph_kernel_output=execution.output_file("sphere[OUTPUT_PREFIX].ker"),
    )
    return ret


def morph_kernel_execute(
    params: MorphKernelParameters,
    execution: Execution,
) -> MorphKernelOutputs:
    """
    Tool to generate morphological kernels.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MorphKernelOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = morph_kernel_cargs(params, execution)
    ret = morph_kernel_outputs(params, execution)
    execution.run(cargs)
    return ret


def morph_kernel(
    cube_side_length: float,
    sphere_radius: float,
    runner: Runner | None = None,
) -> MorphKernelOutputs:
    """
    Tool to generate morphological kernels.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        cube_side_length: Side length of the cube (e.g., 11).
        sphere_radius: Radius of the sphere (e.g., 5.5).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MorphKernelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MORPH_KERNEL_METADATA)
    params = morph_kernel_params(cube_side_length=cube_side_length, sphere_radius=sphere_radius)
    return morph_kernel_execute(params, execution)


__all__ = [
    "MORPH_KERNEL_METADATA",
    "MorphKernelOutputs",
    "MorphKernelParameters",
    "morph_kernel",
    "morph_kernel_params",
]
