# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

QUOTIZE_METADATA = Metadata(
    id="d23de9ba9a8a0ec51eec10d409b73d3f766156d0.boutiques",
    name="quotize",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
QuotizeParameters = typing.TypedDict('QuotizeParameters', {
    "__STYX_TYPE__": typing.Literal["quotize"],
    "name": str,
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
        "quotize": quotize_cargs,
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
        "quotize": quotize_outputs,
    }.get(t)


class QuotizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `quotize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    array_output: OutputPathType
    """Generated C array of strings file"""


def quotize_params(
    name: str,
    input_file: InputPathType,
    output_file: str,
) -> QuotizeParameters:
    """
    Build parameters.
    
    Args:
        name: The name to be used for the array of strings.
        input_file: Input text file to be converted.
        output_file: Output file which will contain the C array of strings.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "quotize",
        "name": name,
        "input_file": input_file,
        "output_file": output_file,
    }
    return params


def quotize_cargs(
    params: QuotizeParameters,
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
    cargs.append("quotize")
    cargs.append(params.get("name"))
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(params.get("output_file"))
    return cargs


def quotize_outputs(
    params: QuotizeParameters,
    execution: Execution,
) -> QuotizeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = QuotizeOutputs(
        root=execution.output_file("."),
        array_output=execution.output_file(params.get("output_file")),
    )
    return ret


def quotize_execute(
    params: QuotizeParameters,
    execution: Execution,
) -> QuotizeOutputs:
    """
    Turns a text file into a C array of strings initialized into an array 'char
    *name[]'.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `QuotizeOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = quotize_cargs(params, execution)
    ret = quotize_outputs(params, execution)
    execution.run(cargs)
    return ret


def quotize(
    name: str,
    input_file: InputPathType,
    output_file: str,
    runner: Runner | None = None,
) -> QuotizeOutputs:
    """
    Turns a text file into a C array of strings initialized into an array 'char
    *name[]'.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        name: The name to be used for the array of strings.
        input_file: Input text file to be converted.
        output_file: Output file which will contain the C array of strings.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `QuotizeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(QUOTIZE_METADATA)
    params = quotize_params(name=name, input_file=input_file, output_file=output_file)
    return quotize_execute(params, execution)


__all__ = [
    "QUOTIZE_METADATA",
    "QuotizeOutputs",
    "QuotizeParameters",
    "quotize",
    "quotize_params",
]
