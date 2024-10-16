# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ANTS_MOTION_CORR_STATS_METADATA = Metadata(
    id="8e0a32cbffc273335495a2514dc805b34872be58.boutiques",
    name="antsMotionCorrStats",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class AntsMotionCorrStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_motion_corr_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    corrected_csv: OutputPathType
    """The corrected motion parameters.csv file."""


def ants_motion_corr_stats(
    mask: InputPathType,
    moco_params: InputPathType,
    output: InputPathType,
    transform_index: int | None = None,
    framewise: typing.Literal[0, 1] | None = None,
    spatial_map: bool = False,
    timeseries_displacement: bool = False,
    runner: Runner | None = None,
) -> AntsMotionCorrStatsOutputs:
    """
    Advanced Normalization Tools (ANTs) is a C++ library available through the
    command line that computes high-dimensional mappings to capture the statistics
    of brain structure and function. It allows one to organize, visualize and
    statistically explore large biomedical image sets. Additionally, it integrates
    imaging modalities in space + time and works across species or organ systems
    with minimal customization.
    
    The ANTs library is considered a state-of-the-art medical image registration
    and segmentation toolkit which depends on the Insight ToolKit, a widely used
    medical image processing library to which ANTs developers contribute.
    ANTs-related tools have also won several international, unbiased
    competitions such as MICCAI, BRATS, and STACOM.
    
    Author: ANTs developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        mask: Mask image - compute displacements within mask.
        moco_params: Motion correction parameters from antsMotionCorr.
        output: Specify the output file.
        transform_index: Specify the index for a 3D transform to output.
        framewise: Do framewise summary stats.
        spatial_map: Output image of displacement magnitude.
        timeseries_displacement: Output 4d time-series image of displacement\
            magnitude.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsMotionCorrStatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_MOTION_CORR_STATS_METADATA)
    cargs = []
    cargs.append("antsMotionCorrStats")
    cargs.extend([
        "-x",
        execution.input_file(mask)
    ])
    cargs.extend([
        "-m",
        execution.input_file(moco_params)
    ])
    cargs.extend([
        "-o",
        execution.input_file(output)
    ])
    if transform_index is not None:
        cargs.extend([
            "-t",
            str(transform_index)
        ])
    if framewise is not None:
        cargs.extend([
            "-f",
            str(framewise)
        ])
    if spatial_map:
        cargs.append("-s")
    if timeseries_displacement:
        cargs.append("-d")
    ret = AntsMotionCorrStatsOutputs(
        root=execution.output_file("."),
        corrected_csv=execution.output_file(pathlib.Path(output).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ANTS_MOTION_CORR_STATS_METADATA",
    "AntsMotionCorrStatsOutputs",
    "ants_motion_corr_stats",
]
