# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SLICES_SUMMARY_METADATA = Metadata(
    id="c5a3bab21de16027f47ca41d594a765937d99825.boutiques",
    name="slices_summary",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class SlicesSummaryOutputs(typing.NamedTuple):
    """
    Output object returned when calling `slices_summary(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    summary_images_directory: OutputPathType
    """Directory containing summary images"""
    combined_summary_image: OutputPathType
    """Combined summary PNG image"""


def slices_summary(
    v_4d_input_file: InputPathType,
    threshold: float,
    background_image: InputPathType,
    pictures_sum_second: str,
    pictures_sum_second_: str,
    output_png: str,
    timepoints: str,
    single_slice_flag: bool = False,
    darker_background_flag: bool = False,
    dumb_rule_flag: bool = False,
    runner: Runner | None = None,
) -> SlicesSummaryOutputs:
    """
    Generate summary PNG images for 4D neuroimaging data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        v_4d_input_file: 4D input image (e.g., melodic_IC).
        threshold: Threshold value for the slices.
        background_image: Background image file (e.g., standard/MNI152_T1_2mm).
        pictures_sum_second: Path to summary images directory.
        pictures_sum_second_: Path to summary images directory.
        output_png: Output PNG file.
        timepoints: Space-separated list of timepoints to use; first timepoint\
            is 0.
        single_slice_flag: Generate single-slice summary images instead of\
            3-slice.
        darker_background_flag: Make background darker and colour brighter, for\
            greater colour visibility.
        dumb_rule_flag: Use dumber rule for choosing optimal slice.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SlicesSummaryOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SLICES_SUMMARY_METADATA)
    cargs = []
    cargs.append("slices_summary")
    cargs.append(execution.input_file(v_4d_input_file))
    cargs.append(str(threshold))
    cargs.append(execution.input_file(background_image))
    cargs.append(pictures_sum_second)
    if single_slice_flag:
        cargs.append("-1")
    if darker_background_flag:
        cargs.append("-d")
    if dumb_rule_flag:
        cargs.append("-c")
    cargs.append("|")
    cargs.append("slices_summary")
    cargs.append(pictures_sum_second_)
    cargs.append(output_png)
    cargs.append(timepoints)
    ret = SlicesSummaryOutputs(
        root=execution.output_file("."),
        summary_images_directory=execution.output_file(pictures_sum_second_),
        combined_summary_image=execution.output_file(output_png),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SLICES_SUMMARY_METADATA",
    "SlicesSummaryOutputs",
    "slices_summary",
]
