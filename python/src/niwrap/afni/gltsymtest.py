# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

GLTSYMTEST_METADATA = Metadata(
    id="111559b879985876df56e5d64b9c55b4a89af6bb",
    name="GLTsymtest",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class GltsymtestOutputs(typing.NamedTuple):
    """
    Output object returned when calling `gltsymtest(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def gltsymtest(
    varlist: str,
    expr: list[str],
    badonly: bool = False,
    runner: Runner | None = None,
) -> GltsymtestOutputs:
    """
    GLTsymtest by AFNI Team.
    
    A tool to test the validity of '-gltsym' strings for use with 3dDeconvolve
    or 3dREMLfit.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/GLTsymtest.html
    
    Args:
        varlist: A list of allowed variable names in the expression, separated\
            by commas, semicolons, and/or spaces.
        expr: GLT symbolic expression(s), enclosed in quotes.
        badonly: A flag to only output BAD messages rather than all messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GltsymtestOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GLTSYMTEST_METADATA)
    cargs = []
    cargs.append("GLTsymtest")
    if badonly:
        cargs.append("-badonly")
    cargs.append(varlist)
    cargs.extend(expr)
    ret = GltsymtestOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "GLTSYMTEST_METADATA",
    "GltsymtestOutputs",
    "gltsymtest",
]
