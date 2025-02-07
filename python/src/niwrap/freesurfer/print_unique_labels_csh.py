# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

PRINT_UNIQUE_LABELS_CSH_METADATA = Metadata(
    id="e9fb80f03f3d4d6c2fbe65561d9c32f6e16bc580.boutiques",
    name="print_unique_labels.csh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
PrintUniqueLabelsCshParameters = typing.TypedDict('PrintUniqueLabelsCshParameters', {
    "__STYX_TYPE__": typing.Literal["print_unique_labels.csh"],
    "label_volume": InputPathType,
    "list_only": bool,
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
        "print_unique_labels.csh": print_unique_labels_csh_cargs,
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
        "print_unique_labels.csh": print_unique_labels_csh_outputs,
    }.get(t)


class PrintUniqueLabelsCshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `print_unique_labels_csh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    results_file: OutputPathType
    """Output file with the list of unique labels"""


def print_unique_labels_csh_params(
    label_volume: InputPathType,
    list_only: bool = False,
) -> PrintUniqueLabelsCshParameters:
    """
    Build parameters.
    
    Args:
        label_volume: Label volume to be analyzed.
        list_only: Only list the labels.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "print_unique_labels.csh",
        "label_volume": label_volume,
        "list_only": list_only,
    }
    return params


def print_unique_labels_csh_cargs(
    params: PrintUniqueLabelsCshParameters,
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
    cargs.append("print_unique_labels.csh")
    cargs.extend([
        "--vol",
        execution.input_file(params.get("label_volume"))
    ])
    if params.get("list_only"):
        cargs.append("--list")
    return cargs


def print_unique_labels_csh_outputs(
    params: PrintUniqueLabelsCshParameters,
    execution: Execution,
) -> PrintUniqueLabelsCshOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = PrintUniqueLabelsCshOutputs(
        root=execution.output_file("."),
        results_file=execution.output_file("[OUTPUT_FILE]"),
    )
    return ret


def print_unique_labels_csh_execute(
    params: PrintUniqueLabelsCshParameters,
    execution: Execution,
) -> PrintUniqueLabelsCshOutputs:
    """
    Prints the list of unique labels (with structure name) in the input volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `PrintUniqueLabelsCshOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = print_unique_labels_csh_cargs(params, execution)
    ret = print_unique_labels_csh_outputs(params, execution)
    execution.run(cargs)
    return ret


def print_unique_labels_csh(
    label_volume: InputPathType,
    list_only: bool = False,
    runner: Runner | None = None,
) -> PrintUniqueLabelsCshOutputs:
    """
    Prints the list of unique labels (with structure name) in the input volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        label_volume: Label volume to be analyzed.
        list_only: Only list the labels.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PrintUniqueLabelsCshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PRINT_UNIQUE_LABELS_CSH_METADATA)
    params = print_unique_labels_csh_params(label_volume=label_volume, list_only=list_only)
    return print_unique_labels_csh_execute(params, execution)


__all__ = [
    "PRINT_UNIQUE_LABELS_CSH_METADATA",
    "PrintUniqueLabelsCshOutputs",
    "PrintUniqueLabelsCshParameters",
    "print_unique_labels_csh",
    "print_unique_labels_csh_params",
]
