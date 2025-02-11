# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ANTS_MOTION_CORR_STATS_METADATA = Metadata(
    id="ae93cc3983b8309bee22c105a3b82c9e97354cf5.boutiques",
    name="antsMotionCorrStats",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
AntsMotionCorrStatsParameters = typing.TypedDict('AntsMotionCorrStatsParameters', {
    "__STYX_TYPE__": typing.Literal["antsMotionCorrStats"],
    "mask": InputPathType,
    "moco_params": InputPathType,
    "output": str,
    "transform_index": typing.NotRequired[int | None],
    "framewise": typing.NotRequired[typing.Literal[0, 1] | None],
    "spatial_map": bool,
    "timeseries_displacement": bool,
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
        "antsMotionCorrStats": ants_motion_corr_stats_cargs,
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
        "antsMotionCorrStats": ants_motion_corr_stats_outputs,
    }.get(t)


class AntsMotionCorrStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_motion_corr_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    corrected_csv: OutputPathType
    """The corrected motion parameters.csv file."""


def ants_motion_corr_stats_params(
    mask: InputPathType,
    moco_params: InputPathType,
    output: str,
    transform_index: int | None = None,
    framewise: typing.Literal[0, 1] | None = None,
    spatial_map: bool = False,
    timeseries_displacement: bool = False,
) -> AntsMotionCorrStatsParameters:
    """
    Build parameters.
    
    Args:
        mask: Mask image - compute displacements within mask.
        moco_params: Motion correction parameters from antsMotionCorr.
        output: Specify the output file.
        transform_index: Specify the index for a 3D transform to output.
        framewise: Do framewise summary stats.
        spatial_map: Output image of displacement magnitude.
        timeseries_displacement: Output 4d time-series image of displacement\
            magnitude.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "antsMotionCorrStats",
        "mask": mask,
        "moco_params": moco_params,
        "output": output,
        "spatial_map": spatial_map,
        "timeseries_displacement": timeseries_displacement,
    }
    if transform_index is not None:
        params["transform_index"] = transform_index
    if framewise is not None:
        params["framewise"] = framewise
    return params


def ants_motion_corr_stats_cargs(
    params: AntsMotionCorrStatsParameters,
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
    cargs.append("antsMotionCorrStats")
    cargs.extend([
        "-x",
        execution.input_file(params.get("mask"))
    ])
    cargs.extend([
        "-m",
        execution.input_file(params.get("moco_params"))
    ])
    cargs.extend([
        "-o",
        params.get("output")
    ])
    if params.get("transform_index") is not None:
        cargs.extend([
            "-t",
            str(params.get("transform_index"))
        ])
    if params.get("framewise") is not None:
        cargs.extend([
            "-f",
            str(params.get("framewise"))
        ])
    if params.get("spatial_map"):
        cargs.append("-s")
    if params.get("timeseries_displacement"):
        cargs.append("-d")
    return cargs


def ants_motion_corr_stats_outputs(
    params: AntsMotionCorrStatsParameters,
    execution: Execution,
) -> AntsMotionCorrStatsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AntsMotionCorrStatsOutputs(
        root=execution.output_file("."),
        corrected_csv=execution.output_file(params.get("output")),
    )
    return ret


def ants_motion_corr_stats_execute(
    params: AntsMotionCorrStatsParameters,
    execution: Execution,
) -> AntsMotionCorrStatsOutputs:
    """
    Create summary measures of the parameters that are output by antsMotionCorr.
    Currently only works for linear transforms. Outputs the mean and max
    displacements for the voxels within a provided mask, at each time point. By
    default the displacements are relative to the reference space, but the framewise
    option may be used to provide displacements between consecutive time points.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AntsMotionCorrStatsOutputs`).
    """
    cargs = ants_motion_corr_stats_cargs(params, execution)
    ret = ants_motion_corr_stats_outputs(params, execution)
    execution.run(cargs)
    return ret


def ants_motion_corr_stats(
    mask: InputPathType,
    moco_params: InputPathType,
    output: str,
    transform_index: int | None = None,
    framewise: typing.Literal[0, 1] | None = None,
    spatial_map: bool = False,
    timeseries_displacement: bool = False,
    runner: Runner | None = None,
) -> AntsMotionCorrStatsOutputs:
    """
    Create summary measures of the parameters that are output by antsMotionCorr.
    Currently only works for linear transforms. Outputs the mean and max
    displacements for the voxels within a provided mask, at each time point. By
    default the displacements are relative to the reference space, but the framewise
    option may be used to provide displacements between consecutive time points.
    
    Author: ANTs Developers
    
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
    params = ants_motion_corr_stats_params(mask=mask, moco_params=moco_params, output=output, transform_index=transform_index, framewise=framewise, spatial_map=spatial_map, timeseries_displacement=timeseries_displacement)
    return ants_motion_corr_stats_execute(params, execution)


__all__ = [
    "ANTS_MOTION_CORR_STATS_METADATA",
    "AntsMotionCorrStatsOutputs",
    "AntsMotionCorrStatsParameters",
    "ants_motion_corr_stats",
    "ants_motion_corr_stats_params",
]
