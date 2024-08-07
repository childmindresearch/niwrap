# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

R_FUNCLIST_METADATA = Metadata(
    id="e94e9f123ee7b0140d15e573b504a0cff9b0b1b7",
    name="R_funclist",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class RFunclistOutputs(typing.NamedTuple):
    """
    Output object returned when calling `r_funclist(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def r_funclist(
    r_files: list[InputPathType] | None = None,
    runner: Runner | None = None,
) -> RFunclistOutputs:
    """
    R_funclist by AFNI Team.
    
    A quick list of functions defined in AFNI's .R files.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@R_funclist.html
    
    Args:
        r_files: R file(s) to be processed. If no files are specified, all .R\
            files in afni's bin directory are processed.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RFunclistOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(R_FUNCLIST_METADATA)
    cargs = []
    cargs.append("@R_funclist")
    if r_files is not None:
        cargs.extend([execution.input_file(f) for f in r_files])
    ret = RFunclistOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "RFunclistOutputs",
    "R_FUNCLIST_METADATA",
    "r_funclist",
]
