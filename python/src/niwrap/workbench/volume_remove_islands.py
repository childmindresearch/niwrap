# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

VOLUME_REMOVE_ISLANDS_METADATA = Metadata(
    id="a915b7fc618e0a145c90d97ad0abe25a3af42c2f.boutiques",
    name="volume-remove-islands",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
VolumeRemoveIslandsParameters = typing.TypedDict('VolumeRemoveIslandsParameters', {
    "__STYX_TYPE__": typing.Literal["volume-remove-islands"],
    "volume_in": InputPathType,
    "volume_out": str,
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
        "volume-remove-islands": volume_remove_islands_cargs,
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
        "volume-remove-islands": volume_remove_islands_outputs,
    }.get(t)


class VolumeRemoveIslandsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_remove_islands(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output ROI volume"""


def volume_remove_islands_params(
    volume_in: InputPathType,
    volume_out: str,
) -> VolumeRemoveIslandsParameters:
    """
    Build parameters.
    
    Args:
        volume_in: the input ROI volume.
        volume_out: the output ROI volume.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume-remove-islands",
        "volume_in": volume_in,
        "volume_out": volume_out,
    }
    return params


def volume_remove_islands_cargs(
    params: VolumeRemoveIslandsParameters,
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
    cargs.append("-volume-remove-islands")
    cargs.append(execution.input_file(params.get("volume_in")))
    cargs.append(params.get("volume_out"))
    return cargs


def volume_remove_islands_outputs(
    params: VolumeRemoveIslandsParameters,
    execution: Execution,
) -> VolumeRemoveIslandsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VolumeRemoveIslandsOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(params.get("volume_out")),
    )
    return ret


def volume_remove_islands_execute(
    params: VolumeRemoveIslandsParameters,
    execution: Execution,
) -> VolumeRemoveIslandsOutputs:
    """
    Remove islands from an roi volume.
    
    Finds all face-connected parts of the ROI, and zeros out all but the largest
    one.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VolumeRemoveIslandsOutputs`).
    """
    cargs = volume_remove_islands_cargs(params, execution)
    ret = volume_remove_islands_outputs(params, execution)
    execution.run(cargs)
    return ret


def volume_remove_islands(
    volume_in: InputPathType,
    volume_out: str,
    runner: Runner | None = None,
) -> VolumeRemoveIslandsOutputs:
    """
    Remove islands from an roi volume.
    
    Finds all face-connected parts of the ROI, and zeros out all but the largest
    one.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        volume_in: the input ROI volume.
        volume_out: the output ROI volume.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeRemoveIslandsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_REMOVE_ISLANDS_METADATA)
    params = volume_remove_islands_params(volume_in=volume_in, volume_out=volume_out)
    return volume_remove_islands_execute(params, execution)


__all__ = [
    "VOLUME_REMOVE_ISLANDS_METADATA",
    "VolumeRemoveIslandsOutputs",
    "VolumeRemoveIslandsParameters",
    "volume_remove_islands",
    "volume_remove_islands_params",
]
