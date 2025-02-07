# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_REMOVE_NECK_METADATA = Metadata(
    id="8e30093031ff9f4da559f5e5f4affbdaf83b0a83.boutiques",
    name="mri_remove_neck",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriRemoveNeckParameters = typing.TypedDict('MriRemoveNeckParameters', {
    "__STYX_TYPE__": typing.Literal["mri_remove_neck"],
    "input_volume": InputPathType,
    "transform": InputPathType,
    "gca": InputPathType,
    "output_volume": str,
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
        "mri_remove_neck": mri_remove_neck_cargs,
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
        "mri_remove_neck": mri_remove_neck_outputs,
    }.get(t)


class MriRemoveNeckOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_remove_neck(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume_file: OutputPathType
    """Processed MRI volume with neck removed."""


def mri_remove_neck_params(
    input_volume: InputPathType,
    transform: InputPathType,
    gca: InputPathType,
    output_volume: str,
) -> MriRemoveNeckParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Input MRI volume.
        transform: Transformation matrix to register the volume.
        gca: GCA file needed for processing.
        output_volume: Output MRI volume with the neck removed.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_remove_neck",
        "input_volume": input_volume,
        "transform": transform,
        "gca": gca,
        "output_volume": output_volume,
    }
    return params


def mri_remove_neck_cargs(
    params: MriRemoveNeckParameters,
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
    cargs.append("mri_remove_neck")
    cargs.append(execution.input_file(params.get("input_volume")))
    cargs.append(execution.input_file(params.get("transform")))
    cargs.append(execution.input_file(params.get("gca")))
    cargs.append(params.get("output_volume"))
    return cargs


def mri_remove_neck_outputs(
    params: MriRemoveNeckParameters,
    execution: Execution,
) -> MriRemoveNeckOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriRemoveNeckOutputs(
        root=execution.output_file("."),
        output_volume_file=execution.output_file(params.get("output_volume")),
    )
    return ret


def mri_remove_neck_execute(
    params: MriRemoveNeckParameters,
    execution: Execution,
) -> MriRemoveNeckOutputs:
    """
    Tool for removing neck from MRI volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriRemoveNeckOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_remove_neck_cargs(params, execution)
    ret = mri_remove_neck_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_remove_neck(
    input_volume: InputPathType,
    transform: InputPathType,
    gca: InputPathType,
    output_volume: str,
    runner: Runner | None = None,
) -> MriRemoveNeckOutputs:
    """
    Tool for removing neck from MRI volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input MRI volume.
        transform: Transformation matrix to register the volume.
        gca: GCA file needed for processing.
        output_volume: Output MRI volume with the neck removed.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriRemoveNeckOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_REMOVE_NECK_METADATA)
    params = mri_remove_neck_params(input_volume=input_volume, transform=transform, gca=gca, output_volume=output_volume)
    return mri_remove_neck_execute(params, execution)


__all__ = [
    "MRI_REMOVE_NECK_METADATA",
    "MriRemoveNeckOutputs",
    "MriRemoveNeckParameters",
    "mri_remove_neck",
    "mri_remove_neck_params",
]
