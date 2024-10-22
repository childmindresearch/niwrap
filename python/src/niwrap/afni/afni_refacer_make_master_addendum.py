# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

AFNI_REFACER_MAKE_MASTER_ADDENDUM_METADATA = Metadata(
    id="e30e20c7bc7d0ea07a74a8e54ffb3a406c826955.boutiques",
    name="afni_refacer_make_master_addendum",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class AfniRefacerMakeMasterAddendumOutputs(typing.NamedTuple):
    """
    Output object returned when calling `afni_refacer_make_master_addendum(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def afni_refacer_make_master_addendum(
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> AfniRefacerMakeMasterAddendumOutputs:
    """
    Adjunct program for AFNI refacer, takes no command line arguments.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        help_: Display the help message.
        version: Display the version info.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AfniRefacerMakeMasterAddendumOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AFNI_REFACER_MAKE_MASTER_ADDENDUM_METADATA)
    cargs = []
    cargs.append("afni_refacer_make_master_addendum")
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-ver")
    ret = AfniRefacerMakeMasterAddendumOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AFNI_REFACER_MAKE_MASTER_ADDENDUM_METADATA",
    "AfniRefacerMakeMasterAddendumOutputs",
    "afni_refacer_make_master_addendum",
]