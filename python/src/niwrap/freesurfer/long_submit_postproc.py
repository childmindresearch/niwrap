# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

LONG_SUBMIT_POSTPROC_METADATA = Metadata(
    id="f5d6d8fc46443ea959ac2b4347964b2a0edf8163.boutiques",
    name="long_submit_postproc",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
LongSubmitPostprocParameters = typing.TypedDict('LongSubmitPostprocParameters', {
    "__STYX_TYPE__": typing.Literal["long_submit_postproc"],
    "qdec": InputPathType,
    "prog": str,
    "flags": typing.NotRequired[str | None],
    "dir": typing.NotRequired[str | None],
    "simulate": bool,
    "pause": typing.NotRequired[float | None],
    "max": typing.NotRequired[float | None],
    "queue": typing.NotRequired[str | None],
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
        "long_submit_postproc": long_submit_postproc_cargs,
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
        "long_submit_postproc": long_submit_postproc_outputs,
    }.get(t)


class LongSubmitPostprocOutputs(typing.NamedTuple):
    """
    Output object returned when calling `long_submit_postproc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def long_submit_postproc_params(
    qdec: InputPathType,
    prog: str,
    flags: str | None = None,
    dir_: str | None = None,
    simulate: bool = False,
    pause: float | None = 13,
    max_: float | None = 100,
    queue_: str | None = None,
) -> LongSubmitPostprocParameters:
    """
    Build parameters.
    
    Args:
        qdec: QDEC table file specifying the subjects and time points.
        prog: Longitudinal script to call.
        flags: Parameters (without --qdec) to pass to prog (using quotes ...).
        dir_: Directory to store sub-tables and command files.
        simulate: Do not submit anything, just print commands.
        pause: Pause in seconds between submissions.
        max_: Maximum number of jobs for this user.
        queue_: Special queue to submit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "long_submit_postproc",
        "qdec": qdec,
        "prog": prog,
        "simulate": simulate,
    }
    if flags is not None:
        params["flags"] = flags
    if dir_ is not None:
        params["dir"] = dir_
    if pause is not None:
        params["pause"] = pause
    if max_ is not None:
        params["max"] = max_
    if queue_ is not None:
        params["queue"] = queue_
    return params


def long_submit_postproc_cargs(
    params: LongSubmitPostprocParameters,
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
    cargs.append("long_submit_postproc")
    cargs.extend([
        "--qdec",
        execution.input_file(params.get("qdec"))
    ])
    cargs.extend([
        "--prog",
        params.get("prog")
    ])
    if params.get("flags") is not None:
        cargs.extend([
            "--flags",
            params.get("flags")
        ])
    if params.get("dir") is not None:
        cargs.extend([
            "--dir",
            params.get("dir")
        ])
    if params.get("simulate"):
        cargs.append("--simulate")
    if params.get("pause") is not None:
        cargs.extend([
            "--pause",
            str(params.get("pause"))
        ])
    if params.get("max") is not None:
        cargs.extend([
            "--max",
            str(params.get("max"))
        ])
    if params.get("queue") is not None:
        cargs.extend([
            "--queue",
            params.get("queue")
        ])
    return cargs


def long_submit_postproc_outputs(
    params: LongSubmitPostprocParameters,
    execution: Execution,
) -> LongSubmitPostprocOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = LongSubmitPostprocOutputs(
        root=execution.output_file("."),
    )
    return ret


def long_submit_postproc_execute(
    params: LongSubmitPostprocParameters,
    execution: Execution,
) -> LongSubmitPostprocOutputs:
    """
    Submits jobs to the cluster (either seychelles or launchpad at NMR) for
    longitudinal post-processing.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `LongSubmitPostprocOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = long_submit_postproc_cargs(params, execution)
    ret = long_submit_postproc_outputs(params, execution)
    execution.run(cargs)
    return ret


def long_submit_postproc(
    qdec: InputPathType,
    prog: str,
    flags: str | None = None,
    dir_: str | None = None,
    simulate: bool = False,
    pause: float | None = 13,
    max_: float | None = 100,
    queue_: str | None = None,
    runner: Runner | None = None,
) -> LongSubmitPostprocOutputs:
    """
    Submits jobs to the cluster (either seychelles or launchpad at NMR) for
    longitudinal post-processing.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        qdec: QDEC table file specifying the subjects and time points.
        prog: Longitudinal script to call.
        flags: Parameters (without --qdec) to pass to prog (using quotes ...).
        dir_: Directory to store sub-tables and command files.
        simulate: Do not submit anything, just print commands.
        pause: Pause in seconds between submissions.
        max_: Maximum number of jobs for this user.
        queue_: Special queue to submit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LongSubmitPostprocOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LONG_SUBMIT_POSTPROC_METADATA)
    params = long_submit_postproc_params(qdec=qdec, prog=prog, flags=flags, dir_=dir_, simulate=simulate, pause=pause, max_=max_, queue_=queue_)
    return long_submit_postproc_execute(params, execution)


__all__ = [
    "LONG_SUBMIT_POSTPROC_METADATA",
    "LongSubmitPostprocOutputs",
    "LongSubmitPostprocParameters",
    "long_submit_postproc",
    "long_submit_postproc_params",
]
