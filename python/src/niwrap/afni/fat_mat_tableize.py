# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FAT_MAT_TABLEIZE_METADATA = Metadata(
    id="5ba44998c47e95e162b9d566a509d5fcbb197e51.boutiques",
    name="fat_mat_tableize",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
FatMatTableizeParameters = typing.TypedDict('FatMatTableizeParameters', {
    "__STYX_TYPE__": typing.Literal["fat_mat_tableize"],
    "input_matrices": list[str],
    "input_csv": typing.NotRequired[InputPathType | None],
    "input_list": typing.NotRequired[InputPathType | None],
    "output_prefix": str,
    "parameters": typing.NotRequired[list[str] | None],
    "version": bool,
    "date": bool,
    "help": bool,
    "help_short": bool,
    "help_view": bool,
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
        "fat_mat_tableize": fat_mat_tableize_cargs,
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
        "fat_mat_tableize": fat_mat_tableize_outputs,
    }
    return vt.get(t)


class FatMatTableizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fat_mat_tableize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_table: OutputPathType
    """Table file usable in AFNI group analysis programs."""
    output_log: OutputPathType
    """Log file reporting inputs, matching, and aspects of creating the table
    file."""


def fat_mat_tableize_params(
    input_matrices: list[str],
    output_prefix: str,
    input_csv: InputPathType | None = None,
    input_list: InputPathType | None = None,
    parameters: list[str] | None = None,
    version: bool = False,
    date: bool = False,
    help_: bool = False,
    help_short: bool = False,
    help_view: bool = False,
) -> FatMatTableizeParameters:
    """
    Build parameters.
    
    Args:
        input_matrices: Names of *.netcc or *.grid files with matrices to be\
            used to make table; can be provided using wildcard chars.
        output_prefix: Output basename for the table and log files. Suffix and\
            file extensions will be added for the outputs.
        input_csv: Name of a CSV file to include in the table. The first column\
            must have subject ID labels that match with the input matrix files.
        input_list: File containing paths to subject matrices and optionally\
            CSV IDs for matching.
        parameters: List of matrices to be included in the table, identified by\
            their parameter name.
        version: Display current version.
        date: Display release/editing date of current version.
        help_: Display help in terminal.
        help_short: Display help in terminal (short flag).
        help_view: Display help in a separate text editor.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fat_mat_tableize",
        "input_matrices": input_matrices,
        "output_prefix": output_prefix,
        "version": version,
        "date": date,
        "help": help_,
        "help_short": help_short,
        "help_view": help_view,
    }
    if input_csv is not None:
        params["input_csv"] = input_csv
    if input_list is not None:
        params["input_list"] = input_list
    if parameters is not None:
        params["parameters"] = parameters
    return params


def fat_mat_tableize_cargs(
    params: FatMatTableizeParameters,
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
    cargs.append("fat_mat_tableize.py")
    cargs.extend([
        "-in_mat",
        *params.get("input_matrices")
    ])
    if params.get("input_csv") is not None:
        cargs.extend([
            "-in_csv",
            execution.input_file(params.get("input_csv"))
        ])
    if params.get("input_list") is not None:
        cargs.extend([
            "-in_listfile",
            execution.input_file(params.get("input_list"))
        ])
    cargs.extend([
        "-prefix",
        params.get("output_prefix")
    ])
    if params.get("parameters") is not None:
        cargs.extend([
            "-pars",
            *params.get("parameters")
        ])
    if params.get("version"):
        cargs.append("-ver")
    if params.get("date"):
        cargs.append("-date")
    if params.get("help"):
        cargs.append("-help")
    if params.get("help_short"):
        cargs.append("-h")
    if params.get("help_view"):
        cargs.append("-hview")
    return cargs


def fat_mat_tableize_outputs(
    params: FatMatTableizeParameters,
    execution: Execution,
) -> FatMatTableizeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FatMatTableizeOutputs(
        root=execution.output_file("."),
        output_table=execution.output_file(params.get("output_prefix") + "_tbl.txt"),
        output_log=execution.output_file(params.get("output_prefix") + "_prep.log"),
    )
    return ret


def fat_mat_tableize_execute(
    params: FatMatTableizeParameters,
    execution: Execution,
) -> FatMatTableizeOutputs:
    """
    Make tables for AFNI group analysis programs from 3dNetCorr (*.netcc) and
    3dTrackID (*.grid) outputs, with optional additional subject information from
    CSV files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FatMatTableizeOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fat_mat_tableize_cargs(params, execution)
    ret = fat_mat_tableize_outputs(params, execution)
    execution.run(cargs)
    return ret


def fat_mat_tableize(
    input_matrices: list[str],
    output_prefix: str,
    input_csv: InputPathType | None = None,
    input_list: InputPathType | None = None,
    parameters: list[str] | None = None,
    version: bool = False,
    date: bool = False,
    help_: bool = False,
    help_short: bool = False,
    help_view: bool = False,
    runner: Runner | None = None,
) -> FatMatTableizeOutputs:
    """
    Make tables for AFNI group analysis programs from 3dNetCorr (*.netcc) and
    3dTrackID (*.grid) outputs, with optional additional subject information from
    CSV files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_matrices: Names of *.netcc or *.grid files with matrices to be\
            used to make table; can be provided using wildcard chars.
        output_prefix: Output basename for the table and log files. Suffix and\
            file extensions will be added for the outputs.
        input_csv: Name of a CSV file to include in the table. The first column\
            must have subject ID labels that match with the input matrix files.
        input_list: File containing paths to subject matrices and optionally\
            CSV IDs for matching.
        parameters: List of matrices to be included in the table, identified by\
            their parameter name.
        version: Display current version.
        date: Display release/editing date of current version.
        help_: Display help in terminal.
        help_short: Display help in terminal (short flag).
        help_view: Display help in a separate text editor.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FatMatTableizeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FAT_MAT_TABLEIZE_METADATA)
    params = fat_mat_tableize_params(input_matrices=input_matrices, input_csv=input_csv, input_list=input_list, output_prefix=output_prefix, parameters=parameters, version=version, date=date, help_=help_, help_short=help_short, help_view=help_view)
    return fat_mat_tableize_execute(params, execution)


__all__ = [
    "FAT_MAT_TABLEIZE_METADATA",
    "FatMatTableizeOutputs",
    "FatMatTableizeParameters",
    "fat_mat_tableize",
    "fat_mat_tableize_params",
]
