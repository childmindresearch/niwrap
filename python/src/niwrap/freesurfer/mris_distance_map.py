# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_DISTANCE_MAP_METADATA = Metadata(
    id="3d8e889c4b656344736f94614b767e1d77d78242.boutiques",
    name="mris_distance_map",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisDistanceMapParameters = typing.TypedDict('MrisDistanceMapParameters', {
    "__STYX_TYPE__": typing.Literal["mris_distance_map"],
    "input_surface_file": InputPathType,
    "output_scalar_field": str,
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
        "mris_distance_map": mris_distance_map_cargs,
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
        "mris_distance_map": mris_distance_map_outputs,
    }.get(t)


class MrisDistanceMapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_distance_map(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output scalar field file"""


def mris_distance_map_params(
    input_surface_file: InputPathType,
    output_scalar_field: str,
) -> MrisDistanceMapParameters:
    """
    Build parameters.
    
    Args:
        input_surface_file: Input surface file.
        output_scalar_field: Output scalar field (.mgz).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_distance_map",
        "input_surface_file": input_surface_file,
        "output_scalar_field": output_scalar_field,
    }
    return params


def mris_distance_map_cargs(
    params: MrisDistanceMapParameters,
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
    cargs.append("mris_distance_map")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(params.get("input_surface_file")))
    cargs.append(params.get("output_scalar_field"))
    return cargs


def mris_distance_map_outputs(
    params: MrisDistanceMapParameters,
    execution: Execution,
) -> MrisDistanceMapOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisDistanceMapOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_scalar_field") + ".mgz"),
    )
    return ret


def mris_distance_map_execute(
    params: MrisDistanceMapParameters,
    execution: Execution,
) -> MrisDistanceMapOutputs:
    """
    Tool to compute a distance map of each point on the surface to a reference
    point.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisDistanceMapOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_distance_map_cargs(params, execution)
    ret = mris_distance_map_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_distance_map(
    input_surface_file: InputPathType,
    output_scalar_field: str,
    runner: Runner | None = None,
) -> MrisDistanceMapOutputs:
    """
    Tool to compute a distance map of each point on the surface to a reference
    point.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface_file: Input surface file.
        output_scalar_field: Output scalar field (.mgz).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisDistanceMapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_DISTANCE_MAP_METADATA)
    params = mris_distance_map_params(input_surface_file=input_surface_file, output_scalar_field=output_scalar_field)
    return mris_distance_map_execute(params, execution)


__all__ = [
    "MRIS_DISTANCE_MAP_METADATA",
    "MrisDistanceMapOutputs",
    "MrisDistanceMapParameters",
    "mris_distance_map",
    "mris_distance_map_params",
]
