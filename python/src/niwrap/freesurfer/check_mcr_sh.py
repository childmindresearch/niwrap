# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CHECK_MCR_SH_METADATA = Metadata(
    id="791978a63c49f038efea95973ac807e32f4fd537.boutiques",
    name="checkMCR.sh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
CheckMcrShParameters = typing.TypedDict('CheckMcrShParameters', {
    "__STYX_TYPE__": typing.Literal["checkMCR.sh"],
    "help": bool,
})


def dyn_cargs(
    t: str,
) -> None:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    vt = {
        "checkMCR.sh": check_mcr_sh_cargs,
    }
    return vt.get(t)


def dyn_outputs(
    t: str,
) -> None:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    vt = {}
    return vt.get(t)


class CheckMcrShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `check_mcr_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def check_mcr_sh_params(
    help_: bool = False,
) -> CheckMcrShParameters:
    """
    Build parameters.
    
    Args:
        help_: Display help information about checkMCR.sh.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "checkMCR.sh",
        "help": help_,
    }
    return params


def check_mcr_sh_cargs(
    params: CheckMcrShParameters,
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
    cargs.append("checkMCR.sh")
    if params.get("help"):
        cargs.append("--help")
    return cargs


def check_mcr_sh_outputs(
    params: CheckMcrShParameters,
    execution: Execution,
) -> CheckMcrShOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CheckMcrShOutputs(
        root=execution.output_file("."),
    )
    return ret


def check_mcr_sh_execute(
    params: CheckMcrShParameters,
    execution: Execution,
) -> CheckMcrShOutputs:
    """
    Script to check for the presence of Matlab Compiler Runtime (MCR) for Matlab
    2019b, used for the hippocampal/amygdala and brainstem modules.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CheckMcrShOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = check_mcr_sh_cargs(params, execution)
    ret = check_mcr_sh_outputs(params, execution)
    execution.run(cargs)
    return ret


def check_mcr_sh(
    help_: bool = False,
    runner: Runner | None = None,
) -> CheckMcrShOutputs:
    """
    Script to check for the presence of Matlab Compiler Runtime (MCR) for Matlab
    2019b, used for the hippocampal/amygdala and brainstem modules.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        help_: Display help information about checkMCR.sh.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CheckMcrShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CHECK_MCR_SH_METADATA)
    params = check_mcr_sh_params(help_=help_)
    return check_mcr_sh_execute(params, execution)


__all__ = [
    "CHECK_MCR_SH_METADATA",
    "CheckMcrShOutputs",
    "check_mcr_sh",
    "check_mcr_sh_params",
]
