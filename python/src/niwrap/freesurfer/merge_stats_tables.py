# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MERGE_STATS_TABLES_METADATA = Metadata(
    id="004967733986569ad699b7fcfc4e0e899cb02c90.boutiques",
    name="merge_stats_tables",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MergeStatsTablesParameters = typing.TypedDict('MergeStatsTablesParameters', {
    "__STYX_TYPE__": typing.Literal["merge_stats_tables"],
    "subject": typing.NotRequired[str | None],
    "input": typing.NotRequired[InputPathType | None],
    "outputfile": str,
    "meas": str,
    "subjectsfile": typing.NotRequired[InputPathType | None],
    "intable": typing.NotRequired[InputPathType | None],
    "subdir": typing.NotRequired[str | None],
    "delimiter": typing.NotRequired[str | None],
    "common_segs": bool,
    "all_segs": bool,
    "transpose": bool,
    "skip": bool,
    "debug": bool,
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
        "merge_stats_tables": merge_stats_tables_cargs,
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
    vt = {
        "merge_stats_tables": merge_stats_tables_outputs,
    }
    return vt.get(t)


class MergeStatsTablesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `merge_stats_tables(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    merged_stats_table: OutputPathType
    """The merged stats table"""


def merge_stats_tables_params(
    outputfile: str,
    meas: str,
    subject: str | None = None,
    input_: InputPathType | None = None,
    subjectsfile: InputPathType | None = None,
    intable: InputPathType | None = None,
    subdir: str | None = None,
    delimiter: str | None = None,
    common_segs: bool = False,
    all_segs: bool = False,
    transpose: bool = False,
    skip: bool = False,
    debug: bool = False,
) -> MergeStatsTablesParameters:
    """
    Build parameters.
    
    Args:
        outputfile: The output table file.
        meas: Measure to write in output table.
        subject: Specify a single subject name.
        input_: Specify a single input stat file.
        subjectsfile: Name of the file which has the list of subjects (one\
            subject per line).
        intable: Use `fname` as input (REQUIRED when passing subject ids).
        subdir: Use `subdir` instead of default "stats/" when passing subject\
            ids.
        delimiter: Delimiter between measures in the table. Options are 'tab',\
            'space', 'comma', and 'semicolon'. Default is 'space'.
        common_segs: Output only the common segmentations of all the statsfiles\
            given.
        all_segs: Output all the segmentations of the statsfiles given.
        transpose: Transpose the table (default is subjects in rows and\
            segmentations in cols).
        skip: If a subject does not have a stats file, skip it instead of\
            exiting.
        debug: Increase verbosity for debugging purposes.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "merge_stats_tables",
        "outputfile": outputfile,
        "meas": meas,
        "common_segs": common_segs,
        "all_segs": all_segs,
        "transpose": transpose,
        "skip": skip,
        "debug": debug,
    }
    if subject is not None:
        params["subject"] = subject
    if input_ is not None:
        params["input"] = input_
    if subjectsfile is not None:
        params["subjectsfile"] = subjectsfile
    if intable is not None:
        params["intable"] = intable
    if subdir is not None:
        params["subdir"] = subdir
    if delimiter is not None:
        params["delimiter"] = delimiter
    return params


def merge_stats_tables_cargs(
    params: MergeStatsTablesParameters,
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
    cargs.append("merge_stats_tables")
    if params.get("subject") is not None:
        cargs.extend([
            "-s",
            params.get("subject")
        ])
    if params.get("input") is not None:
        cargs.extend([
            "-i",
            execution.input_file(params.get("input"))
        ])
    cargs.extend([
        "-t",
        params.get("outputfile")
    ])
    cargs.extend([
        "-m",
        params.get("meas")
    ])
    if params.get("subjectsfile") is not None:
        cargs.extend([
            "--subjectsfile",
            execution.input_file(params.get("subjectsfile"))
        ])
    if params.get("intable") is not None:
        cargs.extend([
            "--intable",
            execution.input_file(params.get("intable"))
        ])
    if params.get("subdir") is not None:
        cargs.extend([
            "--subdir",
            params.get("subdir")
        ])
    if params.get("delimiter") is not None:
        cargs.extend([
            "-d",
            params.get("delimiter")
        ])
    if params.get("common_segs"):
        cargs.append("--common-segs")
    if params.get("all_segs"):
        cargs.append("--all-segs")
    cargs.append("[SEGIDS_FROM_FILE]")
    cargs.append("[SEGNO]")
    cargs.append("[NO_SEGNO_FLAG]")
    if params.get("transpose"):
        cargs.append("--transpose")
    if params.get("skip"):
        cargs.append("--skip")
    if params.get("debug"):
        cargs.append("-v")
    return cargs


def merge_stats_tables_outputs(
    params: MergeStatsTablesParameters,
    execution: Execution,
) -> MergeStatsTablesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MergeStatsTablesOutputs(
        root=execution.output_file("."),
        merged_stats_table=execution.output_file(params.get("outputfile")),
    )
    return ret


def merge_stats_tables_execute(
    params: MergeStatsTablesParameters,
    execution: Execution,
) -> MergeStatsTablesOutputs:
    """
    Merges a set of stats table files into a single stats table where each line is a
    subject and each column is a segmentation or parcellation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MergeStatsTablesOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = merge_stats_tables_cargs(params, execution)
    ret = merge_stats_tables_outputs(params, execution)
    execution.run(cargs)
    return ret


def merge_stats_tables(
    outputfile: str,
    meas: str,
    subject: str | None = None,
    input_: InputPathType | None = None,
    subjectsfile: InputPathType | None = None,
    intable: InputPathType | None = None,
    subdir: str | None = None,
    delimiter: str | None = None,
    common_segs: bool = False,
    all_segs: bool = False,
    transpose: bool = False,
    skip: bool = False,
    debug: bool = False,
    runner: Runner | None = None,
) -> MergeStatsTablesOutputs:
    """
    Merges a set of stats table files into a single stats table where each line is a
    subject and each column is a segmentation or parcellation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        outputfile: The output table file.
        meas: Measure to write in output table.
        subject: Specify a single subject name.
        input_: Specify a single input stat file.
        subjectsfile: Name of the file which has the list of subjects (one\
            subject per line).
        intable: Use `fname` as input (REQUIRED when passing subject ids).
        subdir: Use `subdir` instead of default "stats/" when passing subject\
            ids.
        delimiter: Delimiter between measures in the table. Options are 'tab',\
            'space', 'comma', and 'semicolon'. Default is 'space'.
        common_segs: Output only the common segmentations of all the statsfiles\
            given.
        all_segs: Output all the segmentations of the statsfiles given.
        transpose: Transpose the table (default is subjects in rows and\
            segmentations in cols).
        skip: If a subject does not have a stats file, skip it instead of\
            exiting.
        debug: Increase verbosity for debugging purposes.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MergeStatsTablesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MERGE_STATS_TABLES_METADATA)
    params = merge_stats_tables_params(subject=subject, input_=input_, outputfile=outputfile, meas=meas, subjectsfile=subjectsfile, intable=intable, subdir=subdir, delimiter=delimiter, common_segs=common_segs, all_segs=all_segs, transpose=transpose, skip=skip, debug=debug)
    return merge_stats_tables_execute(params, execution)


__all__ = [
    "MERGE_STATS_TABLES_METADATA",
    "MergeStatsTablesOutputs",
    "MergeStatsTablesParameters",
    "merge_stats_tables",
    "merge_stats_tables_params",
]
