# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSLVAL_METADATA = Metadata(
    id="1b97cfa9597071f4875c42a91132f64c38096ebd",
    name="fslval",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class FslvalOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslval(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    stdout: OutputPathType
    """Output printed to standard out"""


def fslval(
    input_file: InputPathType,
    keyword_: str,
    runner: Runner | None = None,
) -> FslvalOutputs:
    """
    fslval by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Tool for printing out header information from NIfTI image files.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Fslutils
    
    Args:
        input_file: Input NIfTI image file.
        keyword_: Keyword to query from the NIfTI header.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslvalOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLVAL_METADATA)
    cargs = []
    cargs.append("fslval")
    cargs.append(execution.input_file(input_file))
    cargs.append(keyword_)
    ret = FslvalOutputs(
        root=execution.output_file("."),
        stdout=execution.output_file(f"stdout"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLVAL_METADATA",
    "FslvalOutputs",
    "fslval",
]
