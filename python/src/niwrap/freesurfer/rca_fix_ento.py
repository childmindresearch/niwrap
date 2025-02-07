# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RCA_FIX_ENTO_METADATA = Metadata(
    id="483fc4d892e00dbb3db293128c06ac20a3ba5034.boutiques",
    name="rca-fix-ento",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
RcaFixEntoParameters = typing.TypedDict('RcaFixEntoParameters', {
    "__STYX_TYPE__": typing.Literal["rca-fix-ento"],
    "subject": str,
    "threads": typing.NotRequired[float | None],
    "submit": bool,
    "account": typing.NotRequired[str | None],
    "brain_mask": bool,
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
        "rca-fix-ento": rca_fix_ento_cargs,
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
        "rca-fix-ento": rca_fix_ento_outputs,
    }.get(t)


class RcaFixEntoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rca_fix_ento(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    entowm_output: OutputPathType
    """Output segmentation of the WM around entorhinal cortex."""
    finalsurfs_output: OutputPathType
    """Edited brain.finalsurfs with manual edits."""
    backup_finalsufs_output: OutputPathType
    """Backup of the original brain.finalsurfs.manedit.mgz before edits."""


def rca_fix_ento_params(
    subject: str,
    threads: float | None = None,
    submit: bool = False,
    account: str | None = None,
    brain_mask: bool = False,
) -> RcaFixEntoParameters:
    """
    Build parameters.
    
    Args:
        subject: The subject identifier for processing.
        threads: Number of threads to use for processing.
        submit: Submit the task to sbatch with 1 thread and 14GB of memory.
        account: Specify the account to use when submitting to sbatch; default\
            is 'fhs'.
        brain_mask: Apply the ento fix to the brain.finalsurfs; this is turned\
            off due to a conflict with 255.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "rca-fix-ento",
        "subject": subject,
        "submit": submit,
        "brain_mask": brain_mask,
    }
    if threads is not None:
        params["threads"] = threads
    if account is not None:
        params["account"] = account
    return params


def rca_fix_ento_cargs(
    params: RcaFixEntoParameters,
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
    cargs.append("rca-fix-ento")
    cargs.extend([
        "-s",
        params.get("subject")
    ])
    if params.get("threads") is not None:
        cargs.extend([
            "--threads",
            str(params.get("threads"))
        ])
    if params.get("submit"):
        cargs.append("--submit")
    if params.get("account") is not None:
        cargs.extend([
            "--account",
            params.get("account")
        ])
    if params.get("brain_mask"):
        cargs.append("--brain-mask")
    return cargs


def rca_fix_ento_outputs(
    params: RcaFixEntoParameters,
    execution: Execution,
) -> RcaFixEntoOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RcaFixEntoOutputs(
        root=execution.output_file("."),
        entowm_output=execution.output_file(params.get("subject") + "/mri/entowm.mgz"),
        finalsurfs_output=execution.output_file(params.get("subject") + "/mri/brain.finalsurfs.manedit.mgz"),
        backup_finalsufs_output=execution.output_file(params.get("subject") + "/mri/backup.brain.finalsurfs.manedit.mgz"),
    )
    return ret


def rca_fix_ento_execute(
    params: RcaFixEntoParameters,
    execution: Execution,
) -> RcaFixEntoOutputs:
    """
    A tool to fix the entorhinal white matter in FreeSurfer using a deep learning
    network.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RcaFixEntoOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = rca_fix_ento_cargs(params, execution)
    ret = rca_fix_ento_outputs(params, execution)
    execution.run(cargs)
    return ret


def rca_fix_ento(
    subject: str,
    threads: float | None = None,
    submit: bool = False,
    account: str | None = None,
    brain_mask: bool = False,
    runner: Runner | None = None,
) -> RcaFixEntoOutputs:
    """
    A tool to fix the entorhinal white matter in FreeSurfer using a deep learning
    network.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: The subject identifier for processing.
        threads: Number of threads to use for processing.
        submit: Submit the task to sbatch with 1 thread and 14GB of memory.
        account: Specify the account to use when submitting to sbatch; default\
            is 'fhs'.
        brain_mask: Apply the ento fix to the brain.finalsurfs; this is turned\
            off due to a conflict with 255.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RcaFixEntoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RCA_FIX_ENTO_METADATA)
    params = rca_fix_ento_params(subject=subject, threads=threads, submit=submit, account=account, brain_mask=brain_mask)
    return rca_fix_ento_execute(params, execution)


__all__ = [
    "RCA_FIX_ENTO_METADATA",
    "RcaFixEntoOutputs",
    "RcaFixEntoParameters",
    "rca_fix_ento",
    "rca_fix_ento_params",
]
