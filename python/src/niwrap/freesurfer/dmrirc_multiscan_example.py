# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DMRIRC_MULTISCAN_EXAMPLE_METADATA = Metadata(
    id="54430838d484aaa3828534d0b8611ae8345a17b7.boutiques",
    name="dmrirc.multiscan.example",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class DmrircMultiscanExampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dmrirc_multiscan_example(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """Result of the multi-scan DWI processing."""


def dmrirc_multiscan_example(
    subject_list: str,
    runner: Runner | None = None,
) -> DmrircMultiscanExampleOutputs:
    """
    Example script for DWI processing with multiple scans.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_list: List of subjects for processing (e.g., "huey huey dewey\
            dewey louie louie").
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DmrircMultiscanExampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DMRIRC_MULTISCAN_EXAMPLE_METADATA)
    cargs = []
    cargs.append("dmrirc.multiscan.example")
    cargs.append(subject_list)
    ret = DmrircMultiscanExampleOutputs(
        root=execution.output_file("."),
        output=execution.output_file("dmrirc_multiscan_output.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DMRIRC_MULTISCAN_EXAMPLE_METADATA",
    "DmrircMultiscanExampleOutputs",
    "dmrirc_multiscan_example",
]