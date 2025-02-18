# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

METADATA_REMOVE_PROVENANCE_METADATA = Metadata(
    id="477bbc80e00e51f900e75625d9c13d64da765e46.boutiques",
    name="metadata-remove-provenance",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
MetadataRemoveProvenanceParameters = typing.TypedDict('MetadataRemoveProvenanceParameters', {
    "__STYX_TYPE__": typing.Literal["metadata-remove-provenance"],
    "input_file": str,
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
        "metadata-remove-provenance": metadata_remove_provenance_cargs,
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
    }.get(t)


class MetadataRemoveProvenanceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metadata_remove_provenance(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def metadata_remove_provenance_params(
    input_file: str,
    output_file: str,
) -> MetadataRemoveProvenanceParameters:
    """
    Build parameters.
    
    Args:
        input_file: the file to remove provenance information from.
        output_file: output - the name to save the modified file as.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "metadata-remove-provenance",
        "input_file": input_file,
        "output_file": output_file,
    }
    return params


def metadata_remove_provenance_cargs(
    params: MetadataRemoveProvenanceParameters,
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
    cargs.append("-metadata-remove-provenance")
    cargs.append(params.get("input_file"))
    cargs.append(params.get("output_file"))
    return cargs


def metadata_remove_provenance_outputs(
    params: MetadataRemoveProvenanceParameters,
    execution: Execution,
) -> MetadataRemoveProvenanceOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MetadataRemoveProvenanceOutputs(
        root=execution.output_file("."),
    )
    return ret


def metadata_remove_provenance_execute(
    params: MetadataRemoveProvenanceParameters,
    execution: Execution,
) -> MetadataRemoveProvenanceOutputs:
    """
    Remove provenance information from file metadata.
    
    Removes the provenance metadata fields added by workbench during processing.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MetadataRemoveProvenanceOutputs`).
    """
    params = execution.params(params)
    cargs = metadata_remove_provenance_cargs(params, execution)
    ret = metadata_remove_provenance_outputs(params, execution)
    execution.run(cargs)
    return ret


def metadata_remove_provenance(
    input_file: str,
    output_file: str,
    runner: Runner | None = None,
) -> MetadataRemoveProvenanceOutputs:
    """
    Remove provenance information from file metadata.
    
    Removes the provenance metadata fields added by workbench during processing.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        input_file: the file to remove provenance information from.
        output_file: output - the name to save the modified file as.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetadataRemoveProvenanceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METADATA_REMOVE_PROVENANCE_METADATA)
    params = metadata_remove_provenance_params(input_file=input_file, output_file=output_file)
    return metadata_remove_provenance_execute(params, execution)


__all__ = [
    "METADATA_REMOVE_PROVENANCE_METADATA",
    "MetadataRemoveProvenanceOutputs",
    "MetadataRemoveProvenanceParameters",
    "metadata_remove_provenance",
    "metadata_remove_provenance_params",
]
