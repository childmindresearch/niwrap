# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__DO_EXAMPLES_METADATA = Metadata(
    id="a5f5babbb2f0bb51da55277761894b52baf0592c.boutiques",
    name="@DO.examples",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VDoExamplesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__do_examples(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_log: OutputPathType
    """Output log file when running in auto test mode"""


def v__do_examples(
    auto_test: bool = False,
    runner: Runner | None = None,
) -> VDoExamplesOutputs:
    """
    A script to illustrate the use of Displayable Objects in SUMA.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/@DO.examples.html
    
    Args:
        auto_test: Run this script in test mode where user prompts are timed\
            out at 2 seconds, and the command output log is preserved in a file\
            called __testlog.txt.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VDoExamplesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__DO_EXAMPLES_METADATA)
    cargs = []
    cargs.append("@DO.examples")
    if auto_test:
        cargs.append("-auto_test")
    ret = VDoExamplesOutputs(
        root=execution.output_file("."),
        output_log=execution.output_file("__testlog.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VDoExamplesOutputs",
    "V__DO_EXAMPLES_METADATA",
    "v__do_examples",
]
