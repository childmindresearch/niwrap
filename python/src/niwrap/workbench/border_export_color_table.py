# This file was auto generated by Styx.
# Do not edit this file directly.

import pathlib
import typing

from styxdefs import *


BORDER_EXPORT_COLOR_TABLE_METADATA = Metadata(
    id="83f77bfaf4b9dff368b5d94b9fa01021dc6bda4c",
    name="border-export-color-table",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class BorderExportColorTableOutputs(typing.NamedTuple):
    """
    Output object returned when calling `border_export_color_table(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def border_export_color_table(
    border_file: InputPathType,
    table_out: str,
    opt_class_colors: bool = False,
    runner: Runner = None,
) -> BorderExportColorTableOutputs:
    """
    border-export-color-table by Washington University School of Medicin.
    
    Write border names and colors as text.
    
    Takes the names and colors of each border, and writes it to the same format
    as -metric-label-import expects. By default, the borders are colored by
    border name, specify -class-colors to color them by class instead. The key
    values start at 1 and follow the order of the borders in the file.
    
    Args:
        border_file: the input border file
        table_out: output - the output text file
        opt_class_colors: use class colors instead of the name colors
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `BorderExportColorTableOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BORDER_EXPORT_COLOR_TABLE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-border-export-color-table")
    cargs.append(execution.input_file(border_file))
    cargs.append(table_out)
    if opt_class_colors:
        cargs.append("-class-colors")
    ret = BorderExportColorTableOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BORDER_EXPORT_COLOR_TABLE_METADATA",
    "BorderExportColorTableOutputs",
    "border_export_color_table",
]
