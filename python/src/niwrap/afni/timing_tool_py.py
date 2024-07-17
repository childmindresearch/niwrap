# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

TIMING_TOOL_PY_METADATA = Metadata(
    id="d78a4318e06ce3bcf2c99989375e9e9feeb5c89a",
    name="timing_tool.py",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class TimingToolPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `timing_tool_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_timing_file: OutputPathType | None
    """Output timing file as specified"""
    timing_to_1_d_output: OutputPathType | None
    """Output 1D formatted stimulus data"""


def timing_tool_py(
    timing_file: InputPathType | None = None,
    output_file: str | None = None,
    run_length: list[float | int] | None = None,
    tr: float | int | None = None,
    offset: float | int | None = None,
    extend_file: InputPathType | None = None,
    sort: bool = False,
    scale_data: float | int | None = None,
    shift_to_run_offset: float | int | None = None,
    timing_to_1_d_file: str | None = None,
    stim_duration: float | int | None = None,
    multi_timing_files: list[InputPathType] | None = None,
    multi_show_isi_stats: bool = False,
    multi_show_timing: bool = False,
    show_timing: bool = False,
    multi_stim_duration: list[float | int] | None = None,
    round_times_frac: float | int | None = None,
    truncate_times: bool = False,
    multi_timing_event_list: str | None = None,
    runner: Runner | None = None,
) -> TimingToolPyOutputs:
    """
    timing_tool.py by AFNI Team.
    
    Tool for manipulating and evaluating stimulus timing files.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/timing_tool.py.html
    
    Args:
        timing_file: Specify a stimulus timing file to load.
        output_file: Specify the output timing file.
        run_length: Specify the run duration(s), in seconds.
        tr: Specify the time resolution in 1D output (in seconds).
        offset: Add OFFSET to every time in the main element.
        extend_file: Extend timing rows with those in NEW_FILE.
        sort: Sort the times, per row (run).
        scale_data: Multiply every stim time by SCALAR.
        shift_to_run_offset: Shift times so first event is at start of run.
        timing_to_1_d_file: Convert stim_times format to stim_file.
        stim_duration: Specify the stimulus duration, in seconds.
        multi_timing_files: Specify multiple timing files to load.
        multi_show_isi_stats: Display timing and ISI statistics for the\
            multiple timing files.
        multi_show_timing: Display info on multiple timing elements.
        show_timing: Display info on the main timing element.
        multi_stim_duration: Specify stimulus duration(s), in seconds, for\
            multiple timing elements.
        round_times_frac: Round times to multiples of the TR (0.0 <= FRAC <=\
            1.0).
        truncate_times: Truncate times to multiples of the TR.
        multi_timing_event_list: Create an event list file from multiple timing\
            files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TimingToolPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TIMING_TOOL_PY_METADATA)
    cargs = []
    cargs.append("timing_tool.py")
    cargs.append("[COMMANDS]")
    ret = TimingToolPyOutputs(
        root=execution.output_file("."),
        output_timing_file=execution.output_file(f"{output_file}", optional=True) if output_file is not None else None,
        timing_to_1_d_output=execution.output_file(f"{timing_to_1_d_file}", optional=True) if timing_to_1_d_file is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TIMING_TOOL_PY_METADATA",
    "TimingToolPyOutputs",
    "timing_tool_py",
]
