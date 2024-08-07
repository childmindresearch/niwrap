# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

MAKE_RANDOM_TIMING_PY_METADATA = Metadata(
    id="167622fa6607e6dbad775bde91c2fa2f3b1324ef",
    name="make_random_timing.py",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
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
    num_runs: float | int,
    run_time: list[float | int],
    num_stim: float | int,
    num_reps: list[float | int],
    prefix: str,
    stim_dur: list[float | int] | None = None,
    across_runs: bool = False,
    max_consec: list[float | int] | None = None,
    max_rest: float | int | None = None,
    min_rest: float | int | None = None,
    not_first: list[str] | None = None,
    not_last: list[str] | None = None,
    offset: float | int | None = None,
    ordered_stimuli: list[str] | None = None,
    pre_stim_rest: float | int | None = None,
    post_stim_rest: float | int | None = None,
    save_3dd_cmd: str | None = None,
    seed: float | int | None = None,
    stim_labels: list[str] | None = None,
    t_digits: float | int | None = None,
    t_gran: float | int | None = None,
    tr: float | int | None = None,
    tr_locked: bool = False,
    verb: float | int | None = None,
    show_timing_stats: bool = False,
    runner: Runner | None = None,
) -> MakeRandomTimingPyOutputs:
    """
    make_random_timing.py by AFNI Team.
    
    Create random stimulus timing files for use with AFNI 3dDeconvolve.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/make_random_timing.py.html
    
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
    runner = runner or get_global_runner()
    if not (1 <= num_runs): 
        raise ValueError(f"'num_runs' must be greater than 1 <= x but was {num_runs}")
    if not (1 <= len(run_time)): 
        raise ValueError(f"Length of 'run_time' must be greater than 1 but was {len(run_time)}")
    if not (1 <= num_stim): 
        raise ValueError(f"'num_stim' must be greater than 1 <= x but was {num_stim}")
    if not (1 <= len(num_reps)): 
        raise ValueError(f"Length of 'num_reps' must be greater than 1 but was {len(num_reps)}")
    if stim_dur is not None and not (1 <= len(stim_dur)): 
        raise ValueError(f"Length of 'stim_dur' must be greater than 1 but was {len(stim_dur)}")
    if max_consec is not None and not (1 <= len(max_consec)): 
        raise ValueError(f"Length of 'max_consec' must be greater than 1 but was {len(max_consec)}")
    if not_first is not None and not (1 <= len(not_first)): 
        raise ValueError(f"Length of 'not_first' must be greater than 1 but was {len(not_first)}")
    if not_last is not None and not (1 <= len(not_last)): 
        raise ValueError(f"Length of 'not_last' must be greater than 1 but was {len(not_last)}")
    if ordered_stimuli is not None and not (1 <= len(ordered_stimuli)): 
        raise ValueError(f"Length of 'ordered_stimuli' must be greater than 1 but was {len(ordered_stimuli)}")
    if stim_labels is not None and not (1 <= len(stim_labels)): 
        raise ValueError(f"Length of 'stim_labels' must be greater than 1 but was {len(stim_labels)}")
    execution = runner.start_execution(MAKE_RANDOM_TIMING_PY_METADATA)
    cargs = []
    cargs.append("make_random_timing.py")
    cargs.append("[INPUT_PARAMS]")
    ret = MakeRandomTimingPyOutputs(
        root=execution.output_file("."),
        stim_output=execution.output_file(f"{prefix}_*.1D"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MAKE_RANDOM_TIMING_PY_METADATA",
    "MakeRandomTimingPyOutputs",
    "make_random_timing_py",
]
