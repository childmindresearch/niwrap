# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

STATTABLEDIFF_METADATA = Metadata(
    id="da2be9a7f84a137a62df316b44d86990950378e4.boutiques",
    name="stattablediff",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class StattablediffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `stattablediff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_diff_table: OutputPathType
    """Generated table of differences"""


def stattablediff(
    t1: InputPathType,
    t2: InputPathType,
    output: str,
    percent_diff: bool = False,
    percent_diff_t1: bool = False,
    percent_diff_t2: bool = False,
    multiply: float | None = None,
    divide: float | None = None,
    common: bool = False,
    remove_exvivo: bool = False,
    diff_subjects: bool = False,
    noreplace53: bool = False,
    runner: Runner | None = None,
) -> StattablediffOutputs:
    """
    Creates a table of the differences between two stats tables.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        t1: Input table 1 (output of asegstats2table or aparcstats2table).
        t2: Input table 2 (output of asegstats2table or aparcstats2table).
        output: Output file for the table of differences.
        percent_diff: Compute percent difference with respect to mean of tables.
        percent_diff_t1: Compute percent difference with respect to table 1.
        percent_diff_t2: Compute percent difference with respect to table 2.
        multiply: Multiply by mulval.
        divide: Divide by divval.
        common: Compute difference on common segments (may reorder).
        remove_exvivo: Remove the string '_exvivo' from the column header.
        diff_subjects: Compare subjects with different names.
        noreplace53: Do not replace 5.3 structure names with later names.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `StattablediffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(STATTABLEDIFF_METADATA)
    cargs = []
    cargs.append("stattablediff")
    cargs.append(execution.input_file(t1))
    cargs.append(execution.input_file(t2))
    cargs.append(output)
    if percent_diff:
        cargs.append("--percent")
    if percent_diff_t1:
        cargs.append("--percent1")
    if percent_diff_t2:
        cargs.append("--percent2")
    if multiply is not None:
        cargs.extend([
            "--mul",
            str(multiply)
        ])
    if divide is not None:
        cargs.extend([
            "--div",
            str(divide)
        ])
    if common:
        cargs.append("--common")
    if remove_exvivo:
        cargs.append("--rm-exvivo")
    if diff_subjects:
        cargs.append("--diff-subjs")
    if noreplace53:
        cargs.append("--noreplace53")
    ret = StattablediffOutputs(
        root=execution.output_file("."),
        output_diff_table=execution.output_file(output),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "STATTABLEDIFF_METADATA",
    "StattablediffOutputs",
    "stattablediff",
]