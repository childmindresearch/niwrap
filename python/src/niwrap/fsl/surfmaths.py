# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SURFMATHS_METADATA = Metadata(
    id="475c9dce376d5d1c7770296cb98d52d4ee724d36",
    name="surfmaths",
)


class SurfmathsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surfmaths(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output surface file generated by the tool."""


def surfmaths(
    first_input: InputPathType,
    output: InputPathType,
    operations_inputs: list[str] | None = None,
    runner: Runner | None = None,
) -> SurfmathsOutputs:
    """
    surfmaths.
    
    A command-line tool for performing various mathematical operations on
    surface files.
    
    Args:
        first_input: First input surface file.
        output: Output surface file.
        operations_inputs: Mathematical operations and additional inputs.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfmathsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFMATHS_METADATA)
    cargs = []
    cargs.append("surfmaths")
    cargs.append(execution.input_file(first_input))
    if operations_inputs is not None:
        cargs.extend(operations_inputs)
    cargs.append(execution.input_file(output))
    ret = SurfmathsOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"{pathlib.Path(output).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFMATHS_METADATA",
    "SurfmathsOutputs",
    "surfmaths",
]
