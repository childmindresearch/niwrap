# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

LONG_SUBMIT_JOBS_METADATA = Metadata(
    id="d9fdcdcc044b4b6a583cb8d7681940ebbb389e10.boutiques",
    name="long_submit_jobs",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
LongSubmitJobsParameters = typing.TypedDict('LongSubmitJobsParameters', {
    "__STYX_TYPE__": typing.Literal["long_submit_jobs"],
    "qdec": InputPathType,
    "cdir": str,
    "bdir": typing.NotRequired[str | None],
    "ldir": typing.NotRequired[str | None],
    "scriptsdir": typing.NotRequired[str | None],
    "cross": bool,
    "base": bool,
    "long": bool,
    "cflags": typing.NotRequired[str | None],
    "bflags": typing.NotRequired[str | None],
    "lflags": typing.NotRequired[str | None],
    "affine": bool,
    "force": bool,
    "simulate": bool,
    "simfiles": bool,
    "check": bool,
    "pause": typing.NotRequired[float | None],
    "max": typing.NotRequired[float | None],
    "queue": typing.NotRequired[str | None],
    "cmem": typing.NotRequired[float | None],
    "bmem": typing.NotRequired[float | None],
    "lmem": typing.NotRequired[float | None],
    "cnodes": typing.NotRequired[float | None],
    "bnodes": typing.NotRequired[float | None],
    "lnodes": typing.NotRequired[float | None],
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
        "long_submit_jobs": long_submit_jobs_cargs,
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


class LongSubmitJobsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `long_submit_jobs(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def long_submit_jobs_params(
    qdec: InputPathType,
    cdir: str,
    bdir: str | None = None,
    ldir: str | None = None,
    scriptsdir: str | None = None,
    cross: bool = False,
    base: bool = False,
    long: bool = False,
    cflags: str | None = None,
    bflags: str | None = None,
    lflags: str | None = None,
    affine: bool = False,
    force: bool = False,
    simulate: bool = False,
    simfiles: bool = False,
    check: bool = False,
    pause: float | None = None,
    max_: float | None = None,
    queue_: str | None = None,
    cmem: float | None = None,
    bmem: float | None = None,
    lmem: float | None = None,
    cnodes: float | None = None,
    bnodes: float | None = None,
    lnodes: float | None = None,
) -> LongSubmitJobsParameters:
    """
    Build parameters.
    
    Args:
        qdec: QDEC table file specifying the subjects and time points.
        cdir: Directory for cross-sectional subjects (inherited by base and\
            long).
        bdir: Directory for base runs (default: inherit from cross).
        ldir: Directory for longitudinal runs (default: inherit from base).
        scriptsdir: Location to save submitted scripts (default:\
            <cdir,bdir,ldir>/scripts_submitted).
        cross: Process cross-sectional streams.
        base: Process base streams.
        long: Process longitudinal streams.
        cflags: Manual flags for cross processing (e.g., '-all -cw256').
        bflags: Manual flags for base processing (default: '-all').
        lflags: Manual flags for long processing (default: '-all').
        affine: Use affine registration for base.
        force: Force reprocessing of jobs even if marked as done.
        simulate: Simulate submission only, without executing.
        simfiles: Simulate command file creation only, without executing.
        check: Check if all longitudinal processing is complete.
        pause: Pause duration (in seconds) between submissions (default: 13).
        max_: Maximum number of jobs per user (default: 100).
        queue_: Queue to submit jobs.
        cmem: RAM (in GB) requested for cross (default: 7).
        bmem: RAM (in GB) requested for base (default: 7).
        lmem: RAM (in GB) requested for long (default: 7).
        cnodes: Number of nodes for cross runs (default: 1).
        bnodes: Number of nodes for base runs (default: 1).
        lnodes: Number of nodes for long runs (default: 1).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "long_submit_jobs",
        "qdec": qdec,
        "cdir": cdir,
        "cross": cross,
        "base": base,
        "long": long,
        "affine": affine,
        "force": force,
        "simulate": simulate,
        "simfiles": simfiles,
        "check": check,
    }
    if bdir is not None:
        params["bdir"] = bdir
    if ldir is not None:
        params["ldir"] = ldir
    if scriptsdir is not None:
        params["scriptsdir"] = scriptsdir
    if cflags is not None:
        params["cflags"] = cflags
    if bflags is not None:
        params["bflags"] = bflags
    if lflags is not None:
        params["lflags"] = lflags
    if pause is not None:
        params["pause"] = pause
    if max_ is not None:
        params["max"] = max_
    if queue_ is not None:
        params["queue"] = queue_
    if cmem is not None:
        params["cmem"] = cmem
    if bmem is not None:
        params["bmem"] = bmem
    if lmem is not None:
        params["lmem"] = lmem
    if cnodes is not None:
        params["cnodes"] = cnodes
    if bnodes is not None:
        params["bnodes"] = bnodes
    if lnodes is not None:
        params["lnodes"] = lnodes
    return params


def long_submit_jobs_cargs(
    params: LongSubmitJobsParameters,
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
    cargs.append("long_submit_jobs")
    cargs.extend([
        "--qdec",
        execution.input_file(params.get("qdec"))
    ])
    cargs.extend([
        "--cdir",
        params.get("cdir")
    ])
    if params.get("bdir") is not None:
        cargs.extend([
            "--bdir",
            params.get("bdir")
        ])
    if params.get("ldir") is not None:
        cargs.extend([
            "--ldir",
            params.get("ldir")
        ])
    if params.get("scriptsdir") is not None:
        cargs.extend([
            "--scriptsdir",
            params.get("scriptsdir")
        ])
    if params.get("cross"):
        cargs.append("--cross")
    if params.get("base"):
        cargs.append("--base")
    if params.get("long"):
        cargs.append("--long")
    if params.get("cflags") is not None:
        cargs.extend([
            "--cflags",
            params.get("cflags")
        ])
    if params.get("bflags") is not None:
        cargs.extend([
            "--bflags",
            params.get("bflags")
        ])
    if params.get("lflags") is not None:
        cargs.extend([
            "--lflags",
            params.get("lflags")
        ])
    if params.get("affine"):
        cargs.append("--affine")
    if params.get("force"):
        cargs.append("--force")
    if params.get("simulate"):
        cargs.append("--simulate")
    if params.get("simfiles"):
        cargs.append("--simfiles")
    cargs.append("[--skip]")
    cargs.append("[--skiperror]")
    if params.get("check"):
        cargs.append("--check")
    cargs.append("[--update-recon-all]")
    cargs.append("[--use-recon-all]")
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
    if params.get("cmem") is not None:
        cargs.extend([
            "--cmem",
            str(params.get("cmem"))
        ])
    if params.get("bmem") is not None:
        cargs.extend([
            "--bmem",
            str(params.get("bmem"))
        ])
    if params.get("lmem") is not None:
        cargs.extend([
            "--lmem",
            str(params.get("lmem"))
        ])
    if params.get("cnodes") is not None:
        cargs.extend([
            "--cnodes",
            str(params.get("cnodes"))
        ])
    if params.get("bnodes") is not None:
        cargs.extend([
            "--bnodes",
            str(params.get("bnodes"))
        ])
    if params.get("lnodes") is not None:
        cargs.extend([
            "--lnodes",
            str(params.get("lnodes"))
        ])
    return cargs


def long_submit_jobs_outputs(
    params: LongSubmitJobsParameters,
    execution: Execution,
) -> LongSubmitJobsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = LongSubmitJobsOutputs(
        root=execution.output_file("."),
    )
    return ret


def long_submit_jobs_execute(
    params: LongSubmitJobsParameters,
    execution: Execution,
) -> LongSubmitJobsOutputs:
    """
    Submits longitudinal processing jobs to the NMR cluster (seychelles or
    launchpad).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `LongSubmitJobsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = long_submit_jobs_cargs(params, execution)
    ret = long_submit_jobs_outputs(params, execution)
    execution.run(cargs)
    return ret


def long_submit_jobs(
    qdec: InputPathType,
    cdir: str,
    bdir: str | None = None,
    ldir: str | None = None,
    scriptsdir: str | None = None,
    cross: bool = False,
    base: bool = False,
    long: bool = False,
    cflags: str | None = None,
    bflags: str | None = None,
    lflags: str | None = None,
    affine: bool = False,
    force: bool = False,
    simulate: bool = False,
    simfiles: bool = False,
    check: bool = False,
    pause: float | None = None,
    max_: float | None = None,
    queue_: str | None = None,
    cmem: float | None = None,
    bmem: float | None = None,
    lmem: float | None = None,
    cnodes: float | None = None,
    bnodes: float | None = None,
    lnodes: float | None = None,
    runner: Runner | None = None,
) -> LongSubmitJobsOutputs:
    """
    Submits longitudinal processing jobs to the NMR cluster (seychelles or
    launchpad).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        qdec: QDEC table file specifying the subjects and time points.
        cdir: Directory for cross-sectional subjects (inherited by base and\
            long).
        bdir: Directory for base runs (default: inherit from cross).
        ldir: Directory for longitudinal runs (default: inherit from base).
        scriptsdir: Location to save submitted scripts (default:\
            <cdir,bdir,ldir>/scripts_submitted).
        cross: Process cross-sectional streams.
        base: Process base streams.
        long: Process longitudinal streams.
        cflags: Manual flags for cross processing (e.g., '-all -cw256').
        bflags: Manual flags for base processing (default: '-all').
        lflags: Manual flags for long processing (default: '-all').
        affine: Use affine registration for base.
        force: Force reprocessing of jobs even if marked as done.
        simulate: Simulate submission only, without executing.
        simfiles: Simulate command file creation only, without executing.
        check: Check if all longitudinal processing is complete.
        pause: Pause duration (in seconds) between submissions (default: 13).
        max_: Maximum number of jobs per user (default: 100).
        queue_: Queue to submit jobs.
        cmem: RAM (in GB) requested for cross (default: 7).
        bmem: RAM (in GB) requested for base (default: 7).
        lmem: RAM (in GB) requested for long (default: 7).
        cnodes: Number of nodes for cross runs (default: 1).
        bnodes: Number of nodes for base runs (default: 1).
        lnodes: Number of nodes for long runs (default: 1).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LongSubmitJobsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LONG_SUBMIT_JOBS_METADATA)
    params = long_submit_jobs_params(qdec=qdec, cdir=cdir, bdir=bdir, ldir=ldir, scriptsdir=scriptsdir, cross=cross, base=base, long=long, cflags=cflags, bflags=bflags, lflags=lflags, affine=affine, force=force, simulate=simulate, simfiles=simfiles, check=check, pause=pause, max_=max_, queue_=queue_, cmem=cmem, bmem=bmem, lmem=lmem, cnodes=cnodes, bnodes=bnodes, lnodes=lnodes)
    return long_submit_jobs_execute(params, execution)


__all__ = [
    "LONG_SUBMIT_JOBS_METADATA",
    "LongSubmitJobsOutputs",
    "LongSubmitJobsParameters",
    "long_submit_jobs",
    "long_submit_jobs_params",
]
