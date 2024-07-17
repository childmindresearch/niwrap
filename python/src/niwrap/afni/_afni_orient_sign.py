# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

AFNI_ORIENT_SIGN_METADATA = Metadata(
    id="c20bfe8a6225bde4b3a62cc7c1779ae18cceeba2",
    name="AfniOrientSign",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class AfniOrientSignOutputs(typing.NamedTuple):
    """
    Output object returned when calling `afni_orient_sign(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output file containing the orientation signs of the dataset"""


def afni_orient_sign(
    infile: InputPathType,
    runner: Runner | None = None,
) -> AfniOrientSignOutputs:
    """
    AfniOrientSign by AFNI Team.
    
    A tool within the AFNI suite to determine the orientation signs of datasets.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@AfniOrientSign.html
    
    Args:
        infile: Input image file to determine orientation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AfniOrientSignOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AFNI_ORIENT_SIGN_METADATA)
    cargs = []
    cargs.append("3dinfo")
    cargs.append("-orient")
    cargs.append(execution.input_file(infile))
    ret = AfniOrientSignOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(f"{pathlib.Path(infile).name}_orient.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AFNI_ORIENT_SIGN_METADATA",
    "AfniOrientSignOutputs",
    "afni_orient_sign",
]
