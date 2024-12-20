# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

GEN_SS_REVIEW_TABLE_PY_METADATA = Metadata(
    id="14139376af49e78f5d6fa5b8178a8e41bcf15797.boutiques",
    name="gen_ss_review_table.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class GenSsReviewTablePyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `gen_ss_review_table_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_table: OutputPathType | None
    """Final table output file"""
    output_outliers: OutputPathType | None
    """Outliers table output file"""


def gen_ss_review_table_py(
    infiles: list[InputPathType],
    write_table: InputPathType | None = None,
    write_outliers: InputPathType | None = None,
    overwrite: bool = False,
    empty_is_outlier: bool = False,
    outlier_sep: str | None = None,
    separator: str | None = None,
    showlabs: bool = False,
    show_infiles: bool = False,
    show_keepers: bool = False,
    report_outliers: list[str] | None = None,
    report_outliers_fill_style: str | None = None,
    show_missing: bool = False,
    verbosity: int | None = None,
    runner: Runner | None = None,
) -> GenSsReviewTablePyOutputs:
    """
    Generate a table from ss_review_basic output files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        infiles: Input ss_review_basic output text files to process.
        write_table: Write final table to the given file.
        write_outliers: Write outlier table to the given file.
        overwrite: Overwrite the output -write_table, if it exists.
        empty_is_outlier: Treat empty tests as outliers.
        outlier_sep: Use SEP for the outlier table separator.
        separator: Use SEP for the label/vals separator (default = ':').
        showlabs: Display counts of all labels found, with parents.
        show_infiles: Include input files in reviewtable result.
        show_keepers: Show a table of subjects kept rather than dropped.
        report_outliers: Report outliers where the comparison holds.
        report_outliers_fill_style: How to fill non-outliers in the table.
        show_missing: Display all missing keys.
        verbosity: Verbosity level.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GenSsReviewTablePyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GEN_SS_REVIEW_TABLE_PY_METADATA)
    cargs = []
    cargs.append("gen_ss_review_table.py")
    cargs.extend([execution.input_file(f) for f in infiles])
    if write_table is not None:
        cargs.extend([
            "-write_table",
            execution.input_file(write_table)
        ])
    if write_outliers is not None:
        cargs.extend([
            "-write_outliers",
            execution.input_file(write_outliers)
        ])
    if overwrite:
        cargs.append("-overwrite")
    if empty_is_outlier:
        cargs.append("-empty_is_outlier")
    if outlier_sep is not None:
        cargs.extend([
            "-outlier_sep",
            outlier_sep
        ])
    if separator is not None:
        cargs.extend([
            "-separator",
            separator
        ])
    if showlabs:
        cargs.append("-showlabs")
    if show_infiles:
        cargs.append("-show_infiles")
    if show_keepers:
        cargs.append("-show_keepers")
    if report_outliers is not None:
        cargs.extend([
            "-report_outliers",
            *report_outliers
        ])
    if report_outliers_fill_style is not None:
        cargs.extend([
            "-report_outliers_fill_style",
            report_outliers_fill_style
        ])
    if show_missing:
        cargs.append("-show_missing")
    if verbosity is not None:
        cargs.extend([
            "-verb",
            str(verbosity)
        ])
    ret = GenSsReviewTablePyOutputs(
        root=execution.output_file("."),
        output_table=execution.output_file(pathlib.Path(write_table).name) if (write_table is not None) else None,
        output_outliers=execution.output_file(pathlib.Path(write_outliers).name) if (write_outliers is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "GEN_SS_REVIEW_TABLE_PY_METADATA",
    "GenSsReviewTablePyOutputs",
    "gen_ss_review_table_py",
]
