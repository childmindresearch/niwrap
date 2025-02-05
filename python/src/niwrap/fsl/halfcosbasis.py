# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

HALFCOSBASIS_METADATA = Metadata(
    id="752770982c70721206de454aa792dfd7ea8b330b.boutiques",
    name="halfcosbasis",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
HalfcosbasisParameters = typing.TypedDict('HalfcosbasisParameters', {
    "__STYX_TYPE__": typing.Literal["halfcosbasis"],
    "hrf_param_file_hf": InputPathType,
    "verbose_flag": bool,
    "debug_level_debuglevel": typing.NotRequired[float | None],
    "timing_on_flag": bool,
    "log_dir_logdir": typing.NotRequired[str | None],
    "num_hrf_samples": typing.NotRequired[float | None],
    "num_hrf_basis_funcs": typing.NotRequired[float | None],
    "num_secs_nsecs": typing.NotRequired[float | None],
    "temp_res": typing.NotRequired[float | None],
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
        "halfcosbasis": halfcosbasis_cargs,
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


class HalfcosbasisOutputs(typing.NamedTuple):
    """
    Output object returned when calling `halfcosbasis(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def halfcosbasis_params(
    hrf_param_file_hf: InputPathType,
    verbose_flag: bool = False,
    debug_level_debuglevel: float | None = None,
    timing_on_flag: bool = False,
    log_dir_logdir: str | None = None,
    num_hrf_samples: float | None = 1000,
    num_hrf_basis_funcs: float | None = 3,
    num_secs_nsecs: float | None = 40,
    temp_res: float | None = 0.05,
) -> HalfcosbasisParameters:
    """
    Build parameters.
    
    Args:
        hrf_param_file_hf: Half cosine HRF parameter ranges file.
        verbose_flag: Switch on diagnostic messages.
        debug_level_debuglevel: Set debug level.
        timing_on_flag: Turn timing on.
        log_dir_logdir: Log directory.
        num_hrf_samples: Number of HRF samples to use (default is 1000).
        num_hrf_basis_funcs: Number of HRF basis functions to use (default is\
            3).
        num_secs_nsecs: Number of seconds (default is 40).
        temp_res: Temporal resolution (default is 0.05).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "halfcosbasis",
        "hrf_param_file_hf": hrf_param_file_hf,
        "verbose_flag": verbose_flag,
        "timing_on_flag": timing_on_flag,
    }
    if debug_level_debuglevel is not None:
        params["debug_level_debuglevel"] = debug_level_debuglevel
    if log_dir_logdir is not None:
        params["log_dir_logdir"] = log_dir_logdir
    if num_hrf_samples is not None:
        params["num_hrf_samples"] = num_hrf_samples
    if num_hrf_basis_funcs is not None:
        params["num_hrf_basis_funcs"] = num_hrf_basis_funcs
    if num_secs_nsecs is not None:
        params["num_secs_nsecs"] = num_secs_nsecs
    if temp_res is not None:
        params["temp_res"] = temp_res
    return params


def halfcosbasis_cargs(
    params: HalfcosbasisParameters,
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
    cargs.append("halfcosbasis")
    cargs.extend([
        "--hf",
        execution.input_file(params.get("hrf_param_file_hf"))
    ])
    if params.get("verbose_flag"):
        cargs.append("-V")
    if params.get("debug_level_debuglevel") is not None:
        cargs.extend([
            "--debuglevel",
            str(params.get("debug_level_debuglevel"))
        ])
    if params.get("timing_on_flag"):
        cargs.append("--to")
    if params.get("log_dir_logdir") is not None:
        cargs.extend([
            "--logdir",
            params.get("log_dir_logdir")
        ])
    if params.get("num_hrf_samples") is not None:
        cargs.extend([
            "--nhs",
            str(params.get("num_hrf_samples"))
        ])
    if params.get("num_hrf_basis_funcs") is not None:
        cargs.extend([
            "--nbfs",
            str(params.get("num_hrf_basis_funcs"))
        ])
    if params.get("num_secs_nsecs") is not None:
        cargs.extend([
            "--nsecs",
            str(params.get("num_secs_nsecs"))
        ])
    if params.get("temp_res") is not None:
        cargs.extend([
            "--res",
            str(params.get("temp_res"))
        ])
    return cargs


def halfcosbasis_outputs(
    params: HalfcosbasisParameters,
    execution: Execution,
) -> HalfcosbasisOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = HalfcosbasisOutputs(
        root=execution.output_file("."),
    )
    return ret


def halfcosbasis_execute(
    params: HalfcosbasisParameters,
    execution: Execution,
) -> HalfcosbasisOutputs:
    """
    Tool for handling half-cosine basis functions in FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `HalfcosbasisOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = halfcosbasis_cargs(params, execution)
    ret = halfcosbasis_outputs(params, execution)
    execution.run(cargs)
    return ret


def halfcosbasis(
    hrf_param_file_hf: InputPathType,
    verbose_flag: bool = False,
    debug_level_debuglevel: float | None = None,
    timing_on_flag: bool = False,
    log_dir_logdir: str | None = None,
    num_hrf_samples: float | None = 1000,
    num_hrf_basis_funcs: float | None = 3,
    num_secs_nsecs: float | None = 40,
    temp_res: float | None = 0.05,
    runner: Runner | None = None,
) -> HalfcosbasisOutputs:
    """
    Tool for handling half-cosine basis functions in FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        hrf_param_file_hf: Half cosine HRF parameter ranges file.
        verbose_flag: Switch on diagnostic messages.
        debug_level_debuglevel: Set debug level.
        timing_on_flag: Turn timing on.
        log_dir_logdir: Log directory.
        num_hrf_samples: Number of HRF samples to use (default is 1000).
        num_hrf_basis_funcs: Number of HRF basis functions to use (default is\
            3).
        num_secs_nsecs: Number of seconds (default is 40).
        temp_res: Temporal resolution (default is 0.05).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `HalfcosbasisOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(HALFCOSBASIS_METADATA)
    params = halfcosbasis_params(hrf_param_file_hf=hrf_param_file_hf, verbose_flag=verbose_flag, debug_level_debuglevel=debug_level_debuglevel, timing_on_flag=timing_on_flag, log_dir_logdir=log_dir_logdir, num_hrf_samples=num_hrf_samples, num_hrf_basis_funcs=num_hrf_basis_funcs, num_secs_nsecs=num_secs_nsecs, temp_res=temp_res)
    return halfcosbasis_execute(params, execution)


__all__ = [
    "HALFCOSBASIS_METADATA",
    "HalfcosbasisOutputs",
    "HalfcosbasisParameters",
    "halfcosbasis",
    "halfcosbasis_params",
]
