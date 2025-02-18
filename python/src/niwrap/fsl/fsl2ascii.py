# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSL2ASCII_METADATA = Metadata(
    id="c9df873540f30253ed4ec8dbdb8a1829d92c7ee8.boutiques",
    name="fsl2ascii",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
Fsl2asciiParameters = typing.TypedDict('Fsl2asciiParameters', {
    "__STYX_TYPE__": typing.Literal["fsl2ascii"],
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
        "fsl2ascii": fsl2ascii_cargs,
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
        "fsl2ascii": fsl2ascii_outputs,
    }.get(t)


class Fsl2asciiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl2ascii(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_ascii_file: OutputPathType
    """Output ASCII text file"""


def fsl2ascii_params(
    input_file: InputPathType,
    output_file: str,
) -> Fsl2asciiParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input NIfTI (or analyze 7.5 format) image.
        output_file: Output ASCII text file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fsl2ascii",
        "input_file": input_file,
        "output_file": output_file,
    }
    return params


def fsl2ascii_cargs(
    params: Fsl2asciiParameters,
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
    cargs.append("fsl2ascii")
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(params.get("output_file"))
    return cargs


def fsl2ascii_outputs(
    params: Fsl2asciiParameters,
    execution: Execution,
) -> Fsl2asciiOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Fsl2asciiOutputs(
        root=execution.output_file("."),
        output_ascii_file=execution.output_file(params.get("output_file")),
    )
    return ret


def fsl2ascii_execute(
    params: Fsl2asciiParameters,
    execution: Execution,
) -> Fsl2asciiOutputs:
    """
    Convert NIfTI image or analyze 7.5 format file to ASCII text file.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Fsl2asciiOutputs`).
    """
    params = execution.params(params)
    cargs = fsl2ascii_cargs(params, execution)
    ret = fsl2ascii_outputs(params, execution)
    execution.run(cargs)
    return ret


def fsl2ascii(
    input_file: InputPathType,
    output_file: str,
    runner: Runner | None = None,
) -> Fsl2asciiOutputs:
    """
    Convert NIfTI image or analyze 7.5 format file to ASCII text file.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Input NIfTI (or analyze 7.5 format) image.
        output_file: Output ASCII text file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Fsl2asciiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL2ASCII_METADATA)
    params = fsl2ascii_params(input_file=input_file, output_file=output_file)
    return fsl2ascii_execute(params, execution)


__all__ = [
    "FSL2ASCII_METADATA",
    "Fsl2asciiOutputs",
    "Fsl2asciiParameters",
    "fsl2ascii",
    "fsl2ascii_params",
]
