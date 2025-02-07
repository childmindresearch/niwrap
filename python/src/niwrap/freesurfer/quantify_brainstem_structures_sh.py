# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

QUANTIFY_BRAINSTEM_STRUCTURES_SH_METADATA = Metadata(
    id="bb094a739a47e09361aec760ca2b87105ebeb041.boutiques",
    name="quantifyBrainstemStructures.sh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
QuantifyBrainstemStructuresShParameters = typing.TypedDict('QuantifyBrainstemStructuresShParameters', {
    "__STYX_TYPE__": typing.Literal["quantifyBrainstemStructures.sh"],
    "output_file": str,
    "subjects_directory": typing.NotRequired[str | None],
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
        "quantifyBrainstemStructures.sh": quantify_brainstem_structures_sh_cargs,
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
        "quantifyBrainstemStructures.sh": quantify_brainstem_structures_sh_outputs,
    }.get(t)


class QuantifyBrainstemStructuresShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `quantify_brainstem_structures_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    results_file: OutputPathType
    """Output file containing the gathered results."""


def quantify_brainstem_structures_sh_params(
    output_file: str,
    subjects_directory: str | None = "/usr/local/freesurfer/subjects",
) -> QuantifyBrainstemStructuresShParameters:
    """
    Build parameters.
    
    Args:
        output_file: The path to the output file where results should be\
            written.
        subjects_directory: The directory containing subject data. Defaults to\
            '/usr/local/freesurfer/subjects' if not provided.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "quantifyBrainstemStructures.sh",
        "output_file": output_file,
    }
    if subjects_directory is not None:
        params["subjects_directory"] = subjects_directory
    return params


def quantify_brainstem_structures_sh_cargs(
    params: QuantifyBrainstemStructuresShParameters,
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
    cargs.append("quantifyBrainstemStructures.sh")
    cargs.append(params.get("output_file"))
    if params.get("subjects_directory") is not None:
        cargs.append(params.get("subjects_directory"))
    return cargs


def quantify_brainstem_structures_sh_outputs(
    params: QuantifyBrainstemStructuresShParameters,
    execution: Execution,
) -> QuantifyBrainstemStructuresShOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = QuantifyBrainstemStructuresShOutputs(
        root=execution.output_file("."),
        results_file=execution.output_file(params.get("output_file")),
    )
    return ret


def quantify_brainstem_structures_sh_execute(
    params: QuantifyBrainstemStructuresShParameters,
    execution: Execution,
) -> QuantifyBrainstemStructuresShOutputs:
    """
    A script to gather results from FreeSurfer brainstem processing and write them
    to an output file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `QuantifyBrainstemStructuresShOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = quantify_brainstem_structures_sh_cargs(params, execution)
    ret = quantify_brainstem_structures_sh_outputs(params, execution)
    execution.run(cargs)
    return ret


def quantify_brainstem_structures_sh(
    output_file: str,
    subjects_directory: str | None = "/usr/local/freesurfer/subjects",
    runner: Runner | None = None,
) -> QuantifyBrainstemStructuresShOutputs:
    """
    A script to gather results from FreeSurfer brainstem processing and write them
    to an output file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        output_file: The path to the output file where results should be\
            written.
        subjects_directory: The directory containing subject data. Defaults to\
            '/usr/local/freesurfer/subjects' if not provided.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `QuantifyBrainstemStructuresShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(QUANTIFY_BRAINSTEM_STRUCTURES_SH_METADATA)
    params = quantify_brainstem_structures_sh_params(output_file=output_file, subjects_directory=subjects_directory)
    return quantify_brainstem_structures_sh_execute(params, execution)


__all__ = [
    "QUANTIFY_BRAINSTEM_STRUCTURES_SH_METADATA",
    "QuantifyBrainstemStructuresShOutputs",
    "QuantifyBrainstemStructuresShParameters",
    "quantify_brainstem_structures_sh",
    "quantify_brainstem_structures_sh_params",
]
