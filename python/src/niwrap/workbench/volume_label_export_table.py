# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

VOLUME_LABEL_EXPORT_TABLE_METADATA = Metadata(
    id="86c9c9cf58b47541d1d528902747ffa6459b6bac.boutiques",
    name="volume-label-export-table",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
VolumeLabelExportTableParameters = typing.TypedDict('VolumeLabelExportTableParameters', {
    "__STYX_TYPE__": typing.Literal["volume-label-export-table"],
    "label_in": InputPathType,
    "map": str,
    "table_out": str,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "volume-label-export-table": volume_label_export_table_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
    }.get(t)


class VolumeLabelExportTableOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_label_export_table(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def volume_label_export_table_params(
    label_in: InputPathType,
    map_: str,
    table_out: str,
) -> VolumeLabelExportTableParameters:
    """
    Build parameters.
    
    Args:
        label_in: the input volume label file.
        map_: the number or name of the label map to use.
        table_out: output - the output text file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume-label-export-table",
        "label_in": label_in,
        "map": map_,
        "table_out": table_out,
    }
    return params


def volume_label_export_table_cargs(
    params: VolumeLabelExportTableParameters,
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
    cargs.append("wb_command")
    cargs.append("-volume-label-export-table")
    cargs.append(execution.input_file(params.get("label_in")))
    cargs.append(params.get("map"))
    cargs.append(params.get("table_out"))
    return cargs


def volume_label_export_table_outputs(
    params: VolumeLabelExportTableParameters,
    execution: Execution,
) -> VolumeLabelExportTableOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VolumeLabelExportTableOutputs(
        root=execution.output_file("."),
    )
    return ret


def volume_label_export_table_execute(
    params: VolumeLabelExportTableParameters,
    execution: Execution,
) -> VolumeLabelExportTableOutputs:
    """
    Export label table from volume as text.
    
    Takes the label table from the volume label map, and writes it to a text
    format matching what is expected by -volume-label-import.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VolumeLabelExportTableOutputs`).
    """
    params = execution.params(params)
    cargs = volume_label_export_table_cargs(params, execution)
    ret = volume_label_export_table_outputs(params, execution)
    execution.run(cargs)
    return ret


def volume_label_export_table(
    label_in: InputPathType,
    map_: str,
    table_out: str,
    runner: Runner | None = None,
) -> VolumeLabelExportTableOutputs:
    """
    Export label table from volume as text.
    
    Takes the label table from the volume label map, and writes it to a text
    format matching what is expected by -volume-label-import.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        label_in: the input volume label file.
        map_: the number or name of the label map to use.
        table_out: output - the output text file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeLabelExportTableOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_LABEL_EXPORT_TABLE_METADATA)
    params = volume_label_export_table_params(label_in=label_in, map_=map_, table_out=table_out)
    return volume_label_export_table_execute(params, execution)


__all__ = [
    "VOLUME_LABEL_EXPORT_TABLE_METADATA",
    "VolumeLabelExportTableOutputs",
    "VolumeLabelExportTableParameters",
    "volume_label_export_table",
    "volume_label_export_table_params",
]
