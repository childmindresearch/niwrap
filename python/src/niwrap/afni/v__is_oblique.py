# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V__IS_OBLIQUE_METADATA = Metadata(
    id="b4c4efc1dde8a1f7284f71e50f9c7006dd457c42",
    name="@isOblique",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VIsObliqueOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__is_oblique(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    result: OutputPathType
    """Output result indicating if the file is oblique or plumb"""


def v__is_oblique(
    infile: InputPathType,
    runner: Runner | None = None,
) -> VIsObliqueOutputs:
    """
    @isOblique by AFNI Team.
    
    Determine if a file is oblique or plumb.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@isOblique.html
    
    Args:
        infile: Input file (e.g., Hello+orig.HEAD).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VIsObliqueOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__IS_OBLIQUE_METADATA)
    cargs = []
    cargs.append("@isOblique")
    cargs.append(execution.input_file(infile))
    ret = VIsObliqueOutputs(
        root=execution.output_file("."),
        result=execution.output_file(f"oblique_check_result.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VIsObliqueOutputs",
    "V__IS_OBLIQUE_METADATA",
    "v__is_oblique",
]