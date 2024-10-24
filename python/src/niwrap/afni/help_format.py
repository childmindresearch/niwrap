# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

HELP_FORMAT_METADATA = Metadata(
    id="2c2e44d1845d44d18c53666d3810111107853205.boutiques",
    name="help_format",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class HelpFormatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `help_format(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    formatted_output: OutputPathType
    """The formatted text with hyperlinks"""


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
    cargs = []
    cargs.append("help_format")
    cargs.append(stdin)
    ret = HelpFormatOutputs(
        root=execution.output_file("."),
        formatted_output=execution.output_file("formatted_output.html"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "HELP_FORMAT_METADATA",
    "HelpFormatOutputs",
    "help_format",
]
