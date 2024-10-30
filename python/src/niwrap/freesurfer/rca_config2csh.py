# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

RCA_CONFIG2CSH_METADATA = Metadata(
    id="a7dd967c3e4aa987eb6ee710bd94e91e4b6e3852.boutiques",
    name="rca-config2csh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class RcaConfig2cshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rca_config2csh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def rca_config2csh(
    configfile: InputPathType,
    runner: Runner | None = None,
) -> RcaConfig2cshOutputs:
    """
    rca-config2csh is a utility to convert configuration files into C-shell syntax.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        configfile: Configuration file to be converted.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RcaConfig2cshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RCA_CONFIG2CSH_METADATA)
    cargs = []
    cargs.append("rca-config2csh")
    cargs.append(execution.input_file(configfile))
    ret = RcaConfig2cshOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "RCA_CONFIG2CSH_METADATA",
    "RcaConfig2cshOutputs",
    "rca_config2csh",
]