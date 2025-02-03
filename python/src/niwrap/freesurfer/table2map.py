# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TABLE2MAP_METADATA = Metadata(
    id="a1a6b6fb84c32df9b568c86f461d163ba6cbfca6.boutiques",
    name="table2map",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
Table2mapParameters = typing.TypedDict('Table2mapParameters', {
    "__STYX_TYPE__": typing.Literal["table2map"],
    "input_table": InputPathType,
    "output_map": str,
    "segmentation": typing.NotRequired[InputPathType | None],
    "parcellation": typing.NotRequired[InputPathType | None],
    "columns": typing.NotRequired[list[str] | None],
    "lookup_table": typing.NotRequired[InputPathType | None],
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
        "table2map": table2map_cargs,
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


class Table2mapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `table2map(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def table2map_params(
    input_table: InputPathType,
    output_map: str,
    segmentation: InputPathType | None = None,
    parcellation: InputPathType | None = None,
    columns: list[str] | None = None,
    lookup_table: InputPathType | None = None,
) -> Table2mapParameters:
    """
    Build parameters.
    
    Args:
        input_table: Input table.
        output_map: Output map.
        segmentation: Segmentation to map to.
        parcellation: Parcellation to map to.
        columns: Table columns to map. All are included by default.
        lookup_table: Alternative lookup table.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "table2map",
        "input_table": input_table,
        "output_map": output_map,
    }
    if segmentation is not None:
        params["segmentation"] = segmentation
    if parcellation is not None:
        params["parcellation"] = parcellation
    if columns is not None:
        params["columns"] = columns
    if lookup_table is not None:
        params["lookup_table"] = lookup_table
    return params


def table2map_cargs(
    params: Table2mapParameters,
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
    cargs.append("table2map")
    cargs.extend([
        "-t",
        execution.input_file(params.get("input_table"))
    ])
    cargs.extend([
        "-o",
        params.get("output_map")
    ])
    if params.get("segmentation") is not None:
        cargs.extend([
            "-s",
            execution.input_file(params.get("segmentation"))
        ])
    if params.get("parcellation") is not None:
        cargs.extend([
            "-p",
            execution.input_file(params.get("parcellation"))
        ])
    if params.get("columns") is not None:
        cargs.extend([
            "-c",
            *params.get("columns")
        ])
    if params.get("lookup_table") is not None:
        cargs.extend([
            "-l",
            execution.input_file(params.get("lookup_table"))
        ])
    return cargs


def table2map_outputs(
    params: Table2mapParameters,
    execution: Execution,
) -> Table2mapOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Table2mapOutputs(
        root=execution.output_file("."),
    )
    return ret


def table2map_execute(
    params: Table2mapParameters,
    execution: Execution,
) -> Table2mapOutputs:
    """
    A tool to map data from a table onto an output map, optionally using
    segmentation or parcellation files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Table2mapOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = table2map_cargs(params, execution)
    ret = table2map_outputs(params, execution)
    execution.run(cargs)
    return ret


def table2map(
    input_table: InputPathType,
    output_map: str,
    segmentation: InputPathType | None = None,
    parcellation: InputPathType | None = None,
    columns: list[str] | None = None,
    lookup_table: InputPathType | None = None,
    runner: Runner | None = None,
) -> Table2mapOutputs:
    """
    A tool to map data from a table onto an output map, optionally using
    segmentation or parcellation files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_table: Input table.
        output_map: Output map.
        segmentation: Segmentation to map to.
        parcellation: Parcellation to map to.
        columns: Table columns to map. All are included by default.
        lookup_table: Alternative lookup table.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Table2mapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TABLE2MAP_METADATA)
    params = table2map_params(input_table=input_table, output_map=output_map, segmentation=segmentation, parcellation=parcellation, columns=columns, lookup_table=lookup_table)
    return table2map_execute(params, execution)


__all__ = [
    "TABLE2MAP_METADATA",
    "Table2mapOutputs",
    "table2map",
    "table2map_params",
]
