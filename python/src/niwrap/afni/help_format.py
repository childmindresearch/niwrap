# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

HELP_FORMAT_METADATA = Metadata(
    id="2c2e44d1845d44d18c53666d3810111107853205.boutiques",
    name="help_format",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
HelpFormatParameters = typing.TypedDict('HelpFormatParameters', {
    "__STYX_TYPE__": typing.Literal["help_format"],
    "stdin": str,
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
        "help_format": help_format_cargs,
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
        "help_format": help_format_outputs,
    }.get(t)


class HelpFormatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `help_format(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    formatted_output: OutputPathType
    """The formatted text with hyperlinks"""


def help_format_params(
    stdin: str,
) -> HelpFormatParameters:
    """
    Build parameters.
    
    Args:
        stdin: Standard input text to be formatted.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "help_format",
        "stdin": stdin,
    }
    return params


def help_format_cargs(
    params: HelpFormatParameters,
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
    cargs.append("help_format")
    cargs.append(params.get("stdin"))
    return cargs


def help_format_outputs(
    params: HelpFormatParameters,
    execution: Execution,
) -> HelpFormatOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = HelpFormatOutputs(
        root=execution.output_file("."),
        formatted_output=execution.output_file("formatted_output.html"),
    )
    return ret


def help_format_execute(
    params: HelpFormatParameters,
    execution: Execution,
) -> HelpFormatOutputs:
    """
    Formats text by converting URLs into HTML hyperlinks.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `HelpFormatOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = help_format_cargs(params, execution)
    ret = help_format_outputs(params, execution)
    execution.run(cargs)
    return ret


def help_format(
    stdin: str,
    runner: Runner | None = None,
) -> HelpFormatOutputs:
    """
    Formats text by converting URLs into HTML hyperlinks.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        stdin: Standard input text to be formatted.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `HelpFormatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(HELP_FORMAT_METADATA)
    params = help_format_params(stdin=stdin)
    return help_format_execute(params, execution)


__all__ = [
    "HELP_FORMAT_METADATA",
    "HelpFormatOutputs",
    "HelpFormatParameters",
    "help_format",
    "help_format_params",
]
