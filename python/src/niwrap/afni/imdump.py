# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

IMDUMP_METADATA = Metadata(
    id="4e73bdbaee3494f5caf94b9758fe364072faee80",
    name="imdump",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class ImdumpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `imdump(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    stdout: OutputPathType
    """Nonzero pixels in the format: x-index y-index value, one pixel per line."""


def imdump(
    input_image: InputPathType,
    runner: Runner | None = None,
) -> ImdumpOutputs:
    """
    imdump by AFNI Team.
    
    Prints out nonzero pixels in an image.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/imdump.html
    
    Args:
        input_image: Input image file to be processed.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImdumpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMDUMP_METADATA)
    cargs = []
    cargs.append("imdump")
    cargs.append(execution.input_file(input_image))
    ret = ImdumpOutputs(
        root=execution.output_file("."),
        stdout=execution.output_file(f"stdout.txt", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "IMDUMP_METADATA",
    "ImdumpOutputs",
    "imdump",
]
