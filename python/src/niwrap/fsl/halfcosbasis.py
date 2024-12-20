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


class HalfcosbasisOutputs(typing.NamedTuple):
    """
    Output object returned when calling `halfcosbasis(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


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
    cargs = []
    cargs.append("halfcosbasis")
    cargs.extend([
        "--hf",
        execution.input_file(hrf_param_file_hf)
    ])
    if verbose_flag:
        cargs.append("-V")
    if debug_level_debuglevel is not None:
        cargs.extend([
            "--debuglevel",
            str(debug_level_debuglevel)
        ])
    if timing_on_flag:
        cargs.append("--to")
    if log_dir_logdir is not None:
        cargs.extend([
            "--logdir",
            log_dir_logdir
        ])
    if num_hrf_samples is not None:
        cargs.extend([
            "--nhs",
            str(num_hrf_samples)
        ])
    if num_hrf_basis_funcs is not None:
        cargs.extend([
            "--nbfs",
            str(num_hrf_basis_funcs)
        ])
    if num_secs_nsecs is not None:
        cargs.extend([
            "--nsecs",
            str(num_secs_nsecs)
        ])
    if temp_res is not None:
        cargs.extend([
            "--res",
            str(temp_res)
        ])
    ret = HalfcosbasisOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "HALFCOSBASIS_METADATA",
    "HalfcosbasisOutputs",
    "halfcosbasis",
]
