# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__R_FUNCLIST_METADATA = Metadata(
    id="9490879edb062904e83247c8917c8d58d72e0fd5.boutiques",
    name="@R_funclist",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VRFunclistOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__r_funclist(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__r_funclist(
    r_files: list[InputPathType] | None = None,
    runner: Runner | None = None,
) -> VRFunclistOutputs:
    """
    A quick list of functions defined in AFNI's .R files.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/@R_funclist.html
    
    Args:
        r_files: R file(s) to be processed. If no files are specified, all .R\
            files in afni's bin directory are processed.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VRFunclistOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__R_FUNCLIST_METADATA)
    cargs = []
    cargs.append("@R_funclist")
    if r_files is not None:
        cargs.extend([execution.input_file(f) for f in r_files])
    ret = VRFunclistOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VRFunclistOutputs",
    "V__R_FUNCLIST_METADATA",
    "v__r_funclist",
]
