# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:58:55.964952

import typing

from ..styxdefs import *


LABEL_EXPORT_TABLE_METADATA = Metadata(
    id="50b60f52988dae7ee8c9ffae8b24abd6170fb709",
    name="label-export-table",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class LabelExportTableOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_export_table(...)`.
    """


def label_export_table(
    runner: Runner,
    label_in: InputPathType,
    table_out: str,
) -> LabelExportTableOutputs:
    """
    EXPORT LABEL TABLE FROM GIFTI AS TEXT.
    
    Takes the label table from the gifti label file, and writes it to a text
    format matching what is expected by -metric-label-import.
    
    Args:
        runner: Command runner
        label_in: the input label file
        table_out: output - the output text file
    Returns:
        NamedTuple of outputs (described in `LabelExportTableOutputs`).
    """
    execution = runner.start_execution(LABEL_EXPORT_TABLE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-label-export-table")
    cargs.append(execution.input_file(label_in))
    cargs.append(table_out)
    ret = LabelExportTableOutputs(
    )
    execution.run(cargs)
    return ret
