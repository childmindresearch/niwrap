# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

REMOVE_TALAIRACH_METADATA = Metadata(
    id="4b227d57c6cc0632758ead5783a3cd254592158b.boutiques",
    name="remove_talairach",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
RemoveTalairachParameters = typing.TypedDict('RemoveTalairachParameters', {
    "__STYX_TYPE__": typing.Literal["remove_talairach"],
    "input_file": InputPathType,
    "output_file": str,
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
        "remove_talairach": remove_talairach_cargs,
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
        "remove_talairach": remove_talairach_outputs,
    }.get(t)


class RemoveTalairachOutputs(typing.NamedTuple):
    """
    Output object returned when calling `remove_talairach(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume: OutputPathType
    """Output volume with Talairach transformation removed"""


def remove_talairach_params(
    input_file: InputPathType,
    output_file: str,
) -> RemoveTalairachParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input volume with Talairach transformation (e.g.,\
            volume.nii).
        output_file: Output volume after removing Talairach transformation\
            (e.g., volume_notal.nii).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "remove_talairach",
        "input_file": input_file,
        "output_file": output_file,
    }
    return params


def remove_talairach_cargs(
    params: RemoveTalairachParameters,
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
    cargs.append("remove_talairach")
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(params.get("output_file"))
    return cargs


def remove_talairach_outputs(
    params: RemoveTalairachParameters,
    execution: Execution,
) -> RemoveTalairachOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RemoveTalairachOutputs(
        root=execution.output_file("."),
        output_volume=execution.output_file(params.get("output_file")),
    )
    return ret


def remove_talairach_execute(
    params: RemoveTalairachParameters,
    execution: Execution,
) -> RemoveTalairachOutputs:
    """
    A tool for removing the Talairach transformation from a volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RemoveTalairachOutputs`).
    """
    params = execution.params(params)
    cargs = remove_talairach_cargs(params, execution)
    ret = remove_talairach_outputs(params, execution)
    execution.run(cargs)
    return ret


def remove_talairach(
    input_file: InputPathType,
    output_file: str,
    runner: Runner | None = None,
) -> RemoveTalairachOutputs:
    """
    A tool for removing the Talairach transformation from a volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input volume with Talairach transformation (e.g.,\
            volume.nii).
        output_file: Output volume after removing Talairach transformation\
            (e.g., volume_notal.nii).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RemoveTalairachOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REMOVE_TALAIRACH_METADATA)
    params = remove_talairach_params(input_file=input_file, output_file=output_file)
    return remove_talairach_execute(params, execution)


__all__ = [
    "REMOVE_TALAIRACH_METADATA",
    "RemoveTalairachOutputs",
    "RemoveTalairachParameters",
    "remove_talairach",
    "remove_talairach_params",
]
