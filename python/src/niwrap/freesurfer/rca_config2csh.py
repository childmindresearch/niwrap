# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RCA_CONFIG2CSH_METADATA = Metadata(
    id="a6974f7a84f9b447ffa3652155f3daff457ba308.boutiques",
    name="rca-config2csh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
RcaConfig2cshParameters = typing.TypedDict('RcaConfig2cshParameters', {
    "__STYX_TYPE__": typing.Literal["rca-config2csh"],
    "configfile": InputPathType,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "rca-config2csh": rca_config2csh_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
    }.get(t)


class RcaConfig2cshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rca_config2csh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def rca_config2csh_params(
    configfile: InputPathType,
) -> RcaConfig2cshParameters:
    """
    Build parameters.
    
    Args:
        configfile: Configuration file to be converted.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "rca-config2csh",
        "configfile": configfile,
    }
    return params


def rca_config2csh_cargs(
    params: RcaConfig2cshParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.extend([
        "-config2csh",
        "rca" + execution.input_file(params.get("configfile"))
    ])
    return cargs


def rca_config2csh_outputs(
    params: RcaConfig2cshParameters,
    execution: Execution,
) -> RcaConfig2cshOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RcaConfig2cshOutputs(
        root=execution.output_file("."),
    )
    return ret


def rca_config2csh_execute(
    params: RcaConfig2cshParameters,
    execution: Execution,
) -> RcaConfig2cshOutputs:
    """
    rca-config2csh is a utility to convert configuration files into C-shell syntax.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RcaConfig2cshOutputs`).
    """
    params = execution.params(params)
    cargs = rca_config2csh_cargs(params, execution)
    ret = rca_config2csh_outputs(params, execution)
    execution.run(cargs)
    return ret


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
    params = rca_config2csh_params(configfile=configfile)
    return rca_config2csh_execute(params, execution)


__all__ = [
    "RCA_CONFIG2CSH_METADATA",
    "RcaConfig2cshOutputs",
    "RcaConfig2cshParameters",
    "rca_config2csh",
    "rca_config2csh_params",
]
