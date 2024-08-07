# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

AFNI_REFACER_MAKE_MASTER_ADDENDUM_METADATA = Metadata(
    id="101a8a288f4df4fc5c66dacf5a80168e79ddf3b7",
    name="afni_refacer_make_master_addendum",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
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
    afni_refacer_make_master_addendum by AFNI Team.
    
    Adjunct program for AFNI refacer, takes no command line arguments.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@afni_refacer_make_master_addendum.html
    
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
