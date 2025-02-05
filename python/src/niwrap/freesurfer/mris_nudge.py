# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_NUDGE_METADATA = Metadata(
    id="6f298ed7d045a2ce709015d0cecce0980607d9d6.boutiques",
    name="mris_nudge",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisNudgeParameters = typing.TypedDict('MrisNudgeParameters', {
    "__STYX_TYPE__": typing.Literal["mris_nudge"],
    "input_surface": InputPathType,
    "input_volume": InputPathType,
    "vertex": int,
    "target_val": float,
    "nbhd": int,
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
        "mris_nudge": mris_nudge_cargs,
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
        "mris_nudge": mris_nudge_outputs,
    }
    return vt.get(t)


class MrisNudgeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_nudge(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_surface: OutputPathType
    """Output surface file after nudging"""


def mris_nudge_params(
    input_surface: InputPathType,
    input_volume: InputPathType,
    vertex: int,
    target_val: float,
    nbhd: int,
) -> MrisNudgeParameters:
    """
    Build parameters.
    
    Args:
        input_surface: Input surface file for nudging.
        input_volume: Input volume file.
        vertex: Vertex to nudge.
        target_val: Target value for nudging.
        nbhd: Neighborhood size for nudge operation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_nudge",
        "input_surface": input_surface,
        "input_volume": input_volume,
        "vertex": vertex,
        "target_val": target_val,
        "nbhd": nbhd,
    }
    return params


def mris_nudge_cargs(
    params: MrisNudgeParameters,
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
    cargs.append("mris_nudge")
    cargs.append(execution.input_file(params.get("input_surface")))
    cargs.append(execution.input_file(params.get("input_volume")))
    cargs.append(str(params.get("vertex")))
    cargs.append(str(params.get("target_val")))
    cargs.append(str(params.get("nbhd")))
    cargs.append("[OUTPUT_SURF]")
    return cargs


def mris_nudge_outputs(
    params: MrisNudgeParameters,
    execution: Execution,
) -> MrisNudgeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisNudgeOutputs(
        root=execution.output_file("."),
        output_surface=execution.output_file("[OUTPUT_SURF]"),
    )
    return ret


def mris_nudge_execute(
    params: MrisNudgeParameters,
    execution: Execution,
) -> MrisNudgeOutputs:
    """
    A tool to nudge vertex positions on a surface using a volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisNudgeOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_nudge_cargs(params, execution)
    ret = mris_nudge_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_nudge(
    input_surface: InputPathType,
    input_volume: InputPathType,
    vertex: int,
    target_val: float,
    nbhd: int,
    runner: Runner | None = None,
) -> MrisNudgeOutputs:
    """
    A tool to nudge vertex positions on a surface using a volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: Input surface file for nudging.
        input_volume: Input volume file.
        vertex: Vertex to nudge.
        target_val: Target value for nudging.
        nbhd: Neighborhood size for nudge operation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisNudgeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_NUDGE_METADATA)
    params = mris_nudge_params(input_surface=input_surface, input_volume=input_volume, vertex=vertex, target_val=target_val, nbhd=nbhd)
    return mris_nudge_execute(params, execution)


__all__ = [
    "MRIS_NUDGE_METADATA",
    "MrisNudgeOutputs",
    "MrisNudgeParameters",
    "mris_nudge",
    "mris_nudge_params",
]
