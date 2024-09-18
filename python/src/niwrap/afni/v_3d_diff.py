# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_DIFF_METADATA = Metadata(
    id="a194a2e3904bf89fe5eee2f867c6c095e389a795.boutiques",
    name="3dDiff",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dDiffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_diff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_log: OutputPathType
    """Log file containing the element-wise differences."""


def v_3d_diff(
    dataset_a: InputPathType,
    dataset_b: InputPathType,
    tolerance: float | None = None,
    mask: InputPathType | None = None,
    quiet_mode: bool = False,
    tabular_mode: bool = False,
    brutalist_mode: bool = False,
    long_report_mode: bool = False,
    runner: Runner | None = None,
) -> V3dDiffOutputs:
    """
    A program to examine element-wise differences between two images.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dDiff.html
    
    Args:
        dataset_a: First input dataset for comparison.
        dataset_b: Second input dataset for comparison.
        tolerance: Floating-point tolerance/epsilon for the comparison.
        mask: Mask to use when comparing the datasets.
        quiet_mode: Quiet mode: 0 for no differences, 1 for differences, -1 for\
            error.
        tabular_mode: Display a table of differences, mainly for 4D data.
        brutalist_mode: Display one-liner with summary of differences.
        long_report_mode: Print a detailed report with more information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dDiffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_DIFF_METADATA)
    cargs = []
    cargs.append("3dDiff")
    cargs.extend([
        "-a",
        execution.input_file(dataset_a)
    ])
    cargs.extend([
        "-b",
        execution.input_file(dataset_b)
    ])
    if tolerance is not None:
        cargs.extend([
            "-tol",
            str(tolerance)
        ])
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if quiet_mode:
        cargs.append("-q")
    if tabular_mode:
        cargs.append("-tabular")
    if brutalist_mode:
        cargs.append("-brutalist")
    if long_report_mode:
        cargs.append("-long_report")
    ret = V3dDiffOutputs(
        root=execution.output_file("."),
        output_log=execution.output_file(pathlib.Path(dataset_a).name + "_vs_" + pathlib.Path(dataset_b).name + ".log"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dDiffOutputs",
    "V_3D_DIFF_METADATA",
    "v_3d_diff",
]