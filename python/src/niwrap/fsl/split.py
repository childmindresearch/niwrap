# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SPLIT_METADATA = Metadata(
    id="cf36dea6bdf65684cffa0415751f7699357f5aea",
    name="Split",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SplitOutputs(typing.NamedTuple):
    """
    Output object returned when calling `split(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_folder: OutputPathType
    """Output folder with multiple files."""


def split(
    in_file: InputPathType,
    out_base_name: str | None = None,
    dimension: typing.Literal["t", "x", "y", "z"] = "t",
    runner: Runner | None = None,
) -> SplitOutputs:
    """
    Split by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    split a 4D file into lots of 3D files (eg for inputting to SPM).
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Fslutils
    
    Args:
        in_file: Input image to split along dimension (default: time).
        out_base_name: Output prefix.
        dimension: 't' or 'x' or 'y' or 'z'. Dimension to mean across.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SplitOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SPLIT_METADATA)
    cargs = []
    cargs.append("fslsplit")
    cargs.append(execution.input_file(in_file))
    if out_base_name is not None:
        cargs.append(
            "out/" +
            out_base_name +
            ""
        )
    cargs.append(("-" + dimension))
    ret = SplitOutputs(
        root=execution.output_file("."),
        out_folder=execution.output_file(f"out/"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SPLIT_METADATA",
    "SplitOutputs",
    "split",
]
