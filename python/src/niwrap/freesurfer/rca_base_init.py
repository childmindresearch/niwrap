# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

RCA_BASE_INIT_METADATA = Metadata(
    id="2b694b2566d2da6e924a830a4008847ba76324ae.boutiques",
    name="rca-base-init",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class RcaBaseInitOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rca_base_init(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def rca_base_init(
    log_file: str | None = None,
    status_file: str | None = None,
    cmd_file: str | None = None,
    runner: Runner | None = None,
) -> RcaBaseInitOutputs:
    """
    Initialize base subject for recon-all processing.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        log_file: Path to the local log file for output.
        status_file: Path to the status file to append logs.
        cmd_file: Path to the command file to append execution commands.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RcaBaseInitOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RCA_BASE_INIT_METADATA)
    cargs = []
    cargs.append("rca-base-init")
    if log_file is not None:
        cargs.append(log_file)
    if status_file is not None:
        cargs.append(status_file)
    if cmd_file is not None:
        cargs.append(cmd_file)
    ret = RcaBaseInitOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "RCA_BASE_INIT_METADATA",
    "RcaBaseInitOutputs",
    "rca_base_init",
]