# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

EXTRACTTXT_METADATA = Metadata(
    id="e05d836b193dfad17142ca596860e221c5181d48.boutiques",
    name="extracttxt",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class ExtracttxtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `extracttxt(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Extracted text output file"""


def extracttxt(
    search_word: str,
    file: InputPathType,
    num_trailing_lines: float | None = 0,
    relative_start: float | None = 0,
    runner: Runner | None = None,
) -> ExtracttxtOutputs:
    """
    Extracts text from a file based on a search word.
    
    Author: Oxford Centre for Functional MRI of the Brain (FMRIB)
    
    Args:
        search_word: The word to search for in the file.
        file: Path to the file where text is to be extracted.
        num_trailing_lines: Number of trailing lines to include after the\
            search word.
        relative_start: Relative start position to begin the search.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ExtracttxtOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(EXTRACTTXT_METADATA)
    cargs = []
    cargs.append("/usr/local/fsl/bin/extracttxt")
    cargs.append(search_word)
    cargs.append(execution.input_file(file))
    if num_trailing_lines is not None:
        cargs.append(str(num_trailing_lines))
    if relative_start is not None:
        cargs.append(str(relative_start))
    ret = ExtracttxtOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("output.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "EXTRACTTXT_METADATA",
    "ExtracttxtOutputs",
    "extracttxt",
]