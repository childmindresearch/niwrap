# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MAKE_RANDOM_TIMING_PY_METADATA = Metadata(
    id="015b2b1c66a3f929dc8b7bc80bb3691f68a641ef.boutiques",
    name="make_random_timing.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class MakeRandomTimingPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `make_random_timing_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    stim_output: OutputPathType
    """Stimulus timing output file"""


def make_random_timing_py(
    num_runs: float,
    run_time: list[float],
    num_stim: float,
    num_reps: list[float],
    prefix: str,
    stim_dur: list[float] | None = None,
    across_runs: bool = False,
    max_consec: list[float] | None = None,
    max_rest: float | None = None,
    min_rest: float | None = None,
    not_first: list[str] | None = None,
    not_last: list[str] | None = None,
    offset: float | None = None,
    ordered_stimuli: list[str] | None = None,
    pre_stim_rest: float | None = None,
    post_stim_rest: float | None = None,
    save_3dd_cmd: str | None = None,
    seed: float | None = None,
    stim_labels: list[str] | None = None,
    t_digits: float | None = None,
    t_gran: float | None = None,
    tr: float | None = None,
    tr_locked: bool = False,
    verb: float | None = None,
    show_timing_stats: bool = False,
    runner: Runner | None = None,
) -> MakeRandomTimingPyOutputs:
    """
    Create random stimulus timing files for use with AFNI 3dDeconvolve.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        num_runs: Set the number of runs.
        run_time: Set the total time per run (in seconds).
        num_stim: Set the number of stimulus classes.
        num_reps: Set the number of repetitions per class (or across runs).
        prefix: Set the prefix for output filenames.
        stim_dur: Set the duration for a single stimulus (in seconds).
        across_runs: Distribute stimuli across all runs at once.
        max_consec: Specify maximum consecutive stimuli per class.
        max_rest: Specify maximum rest between stimuli.
        min_rest: Specify extra rest after each stimulus.
        not_first: Specify classes that should not start a run.
        not_last: Specify classes that should not end a run.
        offset: Specify an offset to add to every stim time.
        ordered_stimuli: Specify a partial ordering of stimuli.
        pre_stim_rest: Specify minimum rest period to start each run.
        post_stim_rest: Specify minimum rest period to end each run.
        save_3dd_cmd: Save a 3dDeconvolve -nodata example.
        seed: Specify a seed for random number generation.
        stim_labels: Specify labels for the stimulus classes.
        t_digits: Set the number of decimal places for times.
        t_gran: Set the time granularity.
        tr: Set the scanner TR.
        tr_locked: Make stimuli timing locked to the accompanying TR.
        verb: Set the verbose level.
        show_timing_stats: Show statistics from the timing.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MakeRandomTimingPyOutputs`).
    """
    if not (1 <= num_runs): 
        raise ValueError(f"'num_runs' must be greater than 1 <= x but was {num_runs}")
    if not (1 <= num_stim): 
        raise ValueError(f"'num_stim' must be greater than 1 <= x but was {num_stim}")
    if not_first is not None and not (1 <= len(not_first)): 
        raise ValueError(f"Length of 'not_first' must be greater than 1 but was {len(not_first)}")
    if not_last is not None and not (1 <= len(not_last)): 
        raise ValueError(f"Length of 'not_last' must be greater than 1 but was {len(not_last)}")
    if ordered_stimuli is not None and not (1 <= len(ordered_stimuli)): 
        raise ValueError(f"Length of 'ordered_stimuli' must be greater than 1 but was {len(ordered_stimuli)}")
    if stim_labels is not None and not (1 <= len(stim_labels)): 
        raise ValueError(f"Length of 'stim_labels' must be greater than 1 but was {len(stim_labels)}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAKE_RANDOM_TIMING_PY_METADATA)
    cargs = []
    cargs.append("make_random_timing.py")
    cargs.extend([
        "-num_runs",
        str(num_runs)
    ])
    cargs.extend([
        "-run_time",
        *map(str, run_time)
    ])
    cargs.extend([
        "-num_stim",
        str(num_stim)
    ])
    cargs.extend([
        "-num_reps",
        *map(str, num_reps)
    ])
    cargs.extend([
        "-prefix",
        prefix
    ])
    if stim_dur is not None:
        cargs.extend([
            "-stim_dur",
            *map(str, stim_dur)
        ])
    if across_runs:
        cargs.append("-across_runs")
    if max_consec is not None:
        cargs.extend([
            "-max_consec",
            *map(str, max_consec)
        ])
    if max_rest is not None:
        cargs.extend([
            "-max_rest",
            str(max_rest)
        ])
    if min_rest is not None:
        cargs.extend([
            "-min_rest",
            str(min_rest)
        ])
    if not_first is not None:
        cargs.extend([
            "-not_first",
            *not_first
        ])
    if not_last is not None:
        cargs.extend([
            "-not_last",
            *not_last
        ])
    if offset is not None:
        cargs.extend([
            "-offset",
            str(offset)
        ])
    if ordered_stimuli is not None:
        cargs.extend([
            "-ordered_stimuli",
            *ordered_stimuli
        ])
    if pre_stim_rest is not None:
        cargs.extend([
            "-pre_stim_rest",
            str(pre_stim_rest)
        ])
    if post_stim_rest is not None:
        cargs.extend([
            "-post_stim_rest",
            str(post_stim_rest)
        ])
    if save_3dd_cmd is not None:
        cargs.extend([
            "-save_3dd_cmd",
            save_3dd_cmd
        ])
    if seed is not None:
        cargs.extend([
            "-seed",
            str(seed)
        ])
    if stim_labels is not None:
        cargs.extend([
            "-stim_labels",
            *stim_labels
        ])
    if t_digits is not None:
        cargs.extend([
            "-t_digits",
            str(t_digits)
        ])
    if t_gran is not None:
        cargs.extend([
            "-t_gran",
            str(t_gran)
        ])
    if tr is not None:
        cargs.extend([
            "-tr",
            str(tr)
        ])
    if tr_locked:
        cargs.append("-tr_locked")
    if verb is not None:
        cargs.extend([
            "-verb",
            str(verb)
        ])
    if show_timing_stats:
        cargs.append("-show_timing_stats")
    ret = MakeRandomTimingPyOutputs(
        root=execution.output_file("."),
        stim_output=execution.output_file(prefix + "_*.1D"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MAKE_RANDOM_TIMING_PY_METADATA",
    "MakeRandomTimingPyOutputs",
    "make_random_timing_py",
]
