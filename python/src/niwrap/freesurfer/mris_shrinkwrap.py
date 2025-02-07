# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_SHRINKWRAP_METADATA = Metadata(
    id="12ec14d079d6b626e78773a4c0b060c225cdd33f.boutiques",
    name="mris_shrinkwrap",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisShrinkwrapParameters = typing.TypedDict('MrisShrinkwrapParameters', {
    "__STYX_TYPE__": typing.Literal["mris_shrinkwrap"],
    "volume": InputPathType,
    "output_name": str,
    "threshold": typing.NotRequired[float | None],
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
        "mris_shrinkwrap": mris_shrinkwrap_cargs,
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
        "mris_shrinkwrap": mris_shrinkwrap_outputs,
    }.get(t)


class MrisShrinkwrapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_shrinkwrap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    inner_skull: OutputPathType
    """Output surface file representing the inner skull."""
    outer_skull: OutputPathType
    """Output surface file representing the outer skull."""
    outer_skin: OutputPathType
    """Output surface file representing the outer skin."""


def mris_shrinkwrap_params(
    volume: InputPathType,
    output_name: str,
    threshold: float | None = None,
) -> MrisShrinkwrapParameters:
    """
    Build parameters.
    
    Args:
        volume: Input image volume for shrink wrap.
        output_name: Base name for output surface files.
        threshold: Apply threshold to image before deforming on distance\
            transform.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_shrinkwrap",
        "volume": volume,
        "output_name": output_name,
    }
    if threshold is not None:
        params["threshold"] = threshold
    return params


def mris_shrinkwrap_cargs(
    params: MrisShrinkwrapParameters,
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
    cargs.append("mris_shrinkwrap")
    cargs.append(execution.input_file(params.get("volume")))
    cargs.append(params.get("output_name"))
    if params.get("threshold") is not None:
        cargs.extend([
            "-t",
            str(params.get("threshold"))
        ])
    return cargs


def mris_shrinkwrap_outputs(
    params: MrisShrinkwrapParameters,
    execution: Execution,
) -> MrisShrinkwrapOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisShrinkwrapOutputs(
        root=execution.output_file("."),
        inner_skull=execution.output_file(params.get("output_name") + "_inner_skull.tri"),
        outer_skull=execution.output_file(params.get("output_name") + "_outer_skull.tri"),
        outer_skin=execution.output_file(params.get("output_name") + "_outer_skin.tri"),
    )
    return ret


def mris_shrinkwrap_execute(
    params: MrisShrinkwrapParameters,
    execution: Execution,
) -> MrisShrinkwrapOutputs:
    """
    Generate shrink-wrapped tessellations of the input volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisShrinkwrapOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_shrinkwrap_cargs(params, execution)
    ret = mris_shrinkwrap_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_shrinkwrap(
    volume: InputPathType,
    output_name: str,
    threshold: float | None = None,
    runner: Runner | None = None,
) -> MrisShrinkwrapOutputs:
    """
    Generate shrink-wrapped tessellations of the input volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        volume: Input image volume for shrink wrap.
        output_name: Base name for output surface files.
        threshold: Apply threshold to image before deforming on distance\
            transform.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisShrinkwrapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_SHRINKWRAP_METADATA)
    params = mris_shrinkwrap_params(volume=volume, output_name=output_name, threshold=threshold)
    return mris_shrinkwrap_execute(params, execution)


__all__ = [
    "MRIS_SHRINKWRAP_METADATA",
    "MrisShrinkwrapOutputs",
    "MrisShrinkwrapParameters",
    "mris_shrinkwrap",
    "mris_shrinkwrap_params",
]
