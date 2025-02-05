# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DIFFUSION_UTILS_METADATA = Metadata(
    id="644c1194ddc618947bb21fc39f90ede191a80b94.boutiques",
    name="diffusionUtils",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
DiffusionUtilsParameters = typing.TypedDict('DiffusionUtilsParameters', {
    "__STYX_TYPE__": typing.Literal["diffusionUtils"],
    "dummy_flag": bool,
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
        "diffusionUtils": diffusion_utils_cargs,
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


class DiffusionUtilsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `diffusion_utils(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def diffusion_utils_params(
    dummy_flag: bool = False,
) -> DiffusionUtilsParameters:
    """
    Build parameters.
    
    Args:
        dummy_flag: Dummy input as no valid help information is provided due to\
            missing module.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "diffusionUtils",
        "dummy_flag": dummy_flag,
    }
    return params


def diffusion_utils_cargs(
    params: DiffusionUtilsParameters,
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
    cargs.append("diffusionUtils")
    if params.get("dummy_flag"):
        cargs.append("--dummy")
    return cargs


def diffusion_utils_outputs(
    params: DiffusionUtilsParameters,
    execution: Execution,
) -> DiffusionUtilsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DiffusionUtilsOutputs(
        root=execution.output_file("."),
    )
    return ret


def diffusion_utils_execute(
    params: DiffusionUtilsParameters,
    execution: Execution,
) -> DiffusionUtilsOutputs:
    """
    A utility related to diffusion data, potentially using the DIPY library.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DiffusionUtilsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = diffusion_utils_cargs(params, execution)
    ret = diffusion_utils_outputs(params, execution)
    execution.run(cargs)
    return ret


def diffusion_utils(
    dummy_flag: bool = False,
    runner: Runner | None = None,
) -> DiffusionUtilsOutputs:
    """
    A utility related to diffusion data, potentially using the DIPY library.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        dummy_flag: Dummy input as no valid help information is provided due to\
            missing module.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DiffusionUtilsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DIFFUSION_UTILS_METADATA)
    params = diffusion_utils_params(dummy_flag=dummy_flag)
    return diffusion_utils_execute(params, execution)


__all__ = [
    "DIFFUSION_UTILS_METADATA",
    "DiffusionUtilsOutputs",
    "DiffusionUtilsParameters",
    "diffusion_utils",
    "diffusion_utils_params",
]
