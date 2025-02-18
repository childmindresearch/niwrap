# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

AFNI_BATCH_R_METADATA = Metadata(
    id="78789aab686dc723a7f6543875033396e8a4b97c.boutiques",
    name="AFNI_Batch_R",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
AfniBatchRParameters = typing.TypedDict('AfniBatchRParameters', {
    "__STYX_TYPE__": typing.Literal["AFNI_Batch_R"],
    "no_restore": bool,
    "save_workspace": bool,
    "no_readline": bool,
    "vanilla_mode": bool,
    "help": bool,
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
        "AFNI_Batch_R": afni_batch_r_cargs,
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


class AfniBatchROutputs(typing.NamedTuple):
    """
    Output object returned when calling `afni_batch_r(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def afni_batch_r_params(
    no_restore: bool = False,
    save_workspace: bool = False,
    no_readline: bool = False,
    vanilla_mode: bool = False,
    help_: bool = False,
) -> AfniBatchRParameters:
    """
    Build parameters.
    
    Args:
        no_restore: Do not restore anything in the R workspace at startup.
        save_workspace: Save the workspace at the end of the script execution.
        no_readline: Disable reading input from the command line.
        vanilla_mode: Run R without saving the workspace at the end, restoring\
            anything, reading the site file, or acting on startup files.
        help_: Display this help message and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "AFNI_Batch_R",
        "no_restore": no_restore,
        "save_workspace": save_workspace,
        "no_readline": no_readline,
        "vanilla_mode": vanilla_mode,
        "help": help_,
    }
    return params


def afni_batch_r_cargs(
    params: AfniBatchRParameters,
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
    cargs.append("AFNI_Batch_R")
    cargs.append("R")
    cargs.append("CMD")
    cargs.append("BATCH")
    if params.get("no_restore"):
        cargs.append("--no-restore")
    if params.get("save_workspace"):
        cargs.append("--save")
    if params.get("no_readline"):
        cargs.append("--no-readline")
    if params.get("vanilla_mode"):
        cargs.append("--vanilla")
    cargs.append("--args")
    if params.get("help"):
        cargs.append("-help")
    return cargs


def afni_batch_r_outputs(
    params: AfniBatchRParameters,
    execution: Execution,
) -> AfniBatchROutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AfniBatchROutputs(
        root=execution.output_file("."),
    )
    return ret


def afni_batch_r_execute(
    params: AfniBatchRParameters,
    execution: Execution,
) -> AfniBatchROutputs:
    """
    Batch mode for executing R scripts in the AFNI environment.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AfniBatchROutputs`).
    """
    params = execution.params(params)
    cargs = afni_batch_r_cargs(params, execution)
    ret = afni_batch_r_outputs(params, execution)
    execution.run(cargs)
    return ret


def afni_batch_r(
    no_restore: bool = False,
    save_workspace: bool = False,
    no_readline: bool = False,
    vanilla_mode: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> AfniBatchROutputs:
    """
    Batch mode for executing R scripts in the AFNI environment.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        no_restore: Do not restore anything in the R workspace at startup.
        save_workspace: Save the workspace at the end of the script execution.
        no_readline: Disable reading input from the command line.
        vanilla_mode: Run R without saving the workspace at the end, restoring\
            anything, reading the site file, or acting on startup files.
        help_: Display this help message and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AfniBatchROutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AFNI_BATCH_R_METADATA)
    params = afni_batch_r_params(no_restore=no_restore, save_workspace=save_workspace, no_readline=no_readline, vanilla_mode=vanilla_mode, help_=help_)
    return afni_batch_r_execute(params, execution)


__all__ = [
    "AFNI_BATCH_R_METADATA",
    "AfniBatchROutputs",
    "AfniBatchRParameters",
    "afni_batch_r",
    "afni_batch_r_params",
]
