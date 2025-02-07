# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSLSIZE_METADATA = Metadata(
    id="0e62170c91253f2d2dac79736f7cbce706903786.boutiques",
    name="fslsize",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FslsizeParameters = typing.TypedDict('FslsizeParameters', {
    "__STYX_TYPE__": typing.Literal["fslsize"],
    "input_file": InputPathType,
    "short_format_flag": bool,
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
        "fslsize": fslsize_cargs,
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
        "fslsize": fslsize_outputs,
    }.get(t)


class FslsizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslsize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fslsize_params(
    input_file: InputPathType,
    short_format_flag: bool = False,
) -> FslsizeParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input image file.
        short_format_flag: Output using short format (one line).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslsize",
        "input_file": input_file,
        "short_format_flag": short_format_flag,
    }
    return params


def fslsize_cargs(
    params: FslsizeParameters,
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
    cargs.append("fslsize")
    cargs.append(execution.input_file(params.get("input_file")))
    if params.get("short_format_flag"):
        cargs.append("-s")
    return cargs


def fslsize_outputs(
    params: FslsizeParameters,
    execution: Execution,
) -> FslsizeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslsizeOutputs(
        root=execution.output_file("."),
    )
    return ret


def fslsize_execute(
    params: FslsizeParameters,
    execution: Execution,
) -> FslsizeOutputs:
    """
    Tool to output the size of an image file in FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslsizeOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fslsize_cargs(params, execution)
    ret = fslsize_outputs(params, execution)
    execution.run(cargs)
    return ret


def fslsize(
    input_file: InputPathType,
    short_format_flag: bool = False,
    runner: Runner | None = None,
) -> FslsizeOutputs:
    """
    Tool to output the size of an image file in FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Input image file.
        short_format_flag: Output using short format (one line).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslsizeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLSIZE_METADATA)
    params = fslsize_params(input_file=input_file, short_format_flag=short_format_flag)
    return fslsize_execute(params, execution)


__all__ = [
    "FSLSIZE_METADATA",
    "FslsizeOutputs",
    "FslsizeParameters",
    "fslsize",
    "fslsize_params",
]
