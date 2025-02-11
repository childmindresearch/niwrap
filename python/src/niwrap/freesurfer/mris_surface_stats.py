# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_SURFACE_STATS_METADATA = Metadata(
    id="a615c38b1e647ea0789fa48d75a57ab954bd3b51.boutiques",
    name="mris_surface_stats",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisSurfaceStatsParameters = typing.TypedDict('MrisSurfaceStatsParameters', {
    "__STYX_TYPE__": typing.Literal["mris_surface_stats"],
    "nsmooth": typing.NotRequired[float | None],
    "surf_name": InputPathType,
    "mask_name": typing.NotRequired[InputPathType | None],
    "out_name": str,
    "mean": typing.NotRequired[str | None],
    "absmean": typing.NotRequired[str | None],
    "absstd": typing.NotRequired[str | None],
    "zscore": typing.NotRequired[str | None],
    "first_group_size": typing.NotRequired[float | None],
    "src_type": typing.NotRequired[str | None],
    "trg_type": typing.NotRequired[str | None],
    "debug": typing.NotRequired[float | None],
    "data_files": list[InputPathType],
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
        "mris_surface_stats": mris_surface_stats_cargs,
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
        "mris_surface_stats": mris_surface_stats_outputs,
    }.get(t)


class MrisSurfaceStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_surface_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    std_output: OutputPathType
    """Standard deviation map of the input thickness difference maps"""
    mean_output: OutputPathType | None
    """Mean map of the input thickness difference maps"""
    absmean_output: OutputPathType | None
    """Absolute mean map of the input thickness difference maps"""
    absstd_output: OutputPathType | None
    """Standard deviation map of the absolute differences"""
    zscore_output: OutputPathType | None
    """Z-score map of the input thickness difference maps"""


def mris_surface_stats_params(
    surf_name: InputPathType,
    out_name: str,
    data_files: list[InputPathType],
    nsmooth: float | None = None,
    mask_name: InputPathType | None = None,
    mean: str | None = None,
    absmean: str | None = None,
    absstd: str | None = None,
    zscore: str | None = None,
    first_group_size: float | None = None,
    src_type: str | None = None,
    trg_type: str | None = None,
    debug: float | None = None,
) -> MrisSurfaceStatsParameters:
    """
    Build parameters.
    
    Args:
        surf_name: Set the surface filename.
        out_name: Set the output filename (standard deviation of data).
        data_files: List of input data files for computation.
        nsmooth: Specify number of smoothing steps.
        mask_name: Set the filename for surface mask.
        mean: Set the output filename for mean.
        absmean: Set the output filename for absolute mean.
        absstd: Set the output filename for standard deviation of absolute mean.
        zscore: Set the output filename for z-score (only if first_group_size >\
            0).
        first_group_size: Specify how many subjects at the beginning belong to\
            first group.
        src_type: Input surface data format (default = paint).
        trg_type: Output format (default = paint).
        debug: Specify which surface vertex number to debug.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_surface_stats",
        "surf_name": surf_name,
        "out_name": out_name,
        "data_files": data_files,
    }
    if nsmooth is not None:
        params["nsmooth"] = nsmooth
    if mask_name is not None:
        params["mask_name"] = mask_name
    if mean is not None:
        params["mean"] = mean
    if absmean is not None:
        params["absmean"] = absmean
    if absstd is not None:
        params["absstd"] = absstd
    if zscore is not None:
        params["zscore"] = zscore
    if first_group_size is not None:
        params["first_group_size"] = first_group_size
    if src_type is not None:
        params["src_type"] = src_type
    if trg_type is not None:
        params["trg_type"] = trg_type
    if debug is not None:
        params["debug"] = debug
    return params


def mris_surface_stats_cargs(
    params: MrisSurfaceStatsParameters,
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
    cargs.append("mris_surface_stats")
    if params.get("nsmooth") is not None:
        cargs.extend([
            "-nsmooth",
            str(params.get("nsmooth"))
        ])
    cargs.extend([
        "-surf_name",
        execution.input_file(params.get("surf_name"))
    ])
    if params.get("mask_name") is not None:
        cargs.extend([
            "-mask_name",
            execution.input_file(params.get("mask_name"))
        ])
    cargs.extend([
        "-out_name",
        params.get("out_name")
    ])
    if params.get("mean") is not None:
        cargs.extend([
            "-mean",
            params.get("mean")
        ])
    if params.get("absmean") is not None:
        cargs.extend([
            "-absmean",
            params.get("absmean")
        ])
    if params.get("absstd") is not None:
        cargs.extend([
            "-absstd",
            params.get("absstd")
        ])
    if params.get("zscore") is not None:
        cargs.extend([
            "-zscore",
            params.get("zscore")
        ])
    if params.get("first_group_size") is not None:
        cargs.extend([
            "-first_group_size",
            str(params.get("first_group_size"))
        ])
    if params.get("src_type") is not None:
        cargs.extend([
            "-src_type",
            params.get("src_type")
        ])
    if params.get("trg_type") is not None:
        cargs.extend([
            "-trg_type",
            params.get("trg_type")
        ])
    if params.get("debug") is not None:
        cargs.extend([
            "-debug",
            str(params.get("debug"))
        ])
    cargs.extend([execution.input_file(f) for f in params.get("data_files")])
    return cargs


def mris_surface_stats_outputs(
    params: MrisSurfaceStatsParameters,
    execution: Execution,
) -> MrisSurfaceStatsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisSurfaceStatsOutputs(
        root=execution.output_file("."),
        std_output=execution.output_file(params.get("out_name")),
        mean_output=execution.output_file(params.get("mean")) if (params.get("mean") is not None) else None,
        absmean_output=execution.output_file(params.get("absmean")) if (params.get("absmean") is not None) else None,
        absstd_output=execution.output_file(params.get("absstd")) if (params.get("absstd") is not None) else None,
        zscore_output=execution.output_file(params.get("zscore")) if (params.get("zscore") is not None) else None,
    )
    return ret


def mris_surface_stats_execute(
    params: MrisSurfaceStatsParameters,
    execution: Execution,
) -> MrisSurfaceStatsOutputs:
    """
    Computes the group-wise mean and standard deviation of thickness differences at
    every vertex of the template surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisSurfaceStatsOutputs`).
    """
    cargs = mris_surface_stats_cargs(params, execution)
    ret = mris_surface_stats_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_surface_stats(
    surf_name: InputPathType,
    out_name: str,
    data_files: list[InputPathType],
    nsmooth: float | None = None,
    mask_name: InputPathType | None = None,
    mean: str | None = None,
    absmean: str | None = None,
    absstd: str | None = None,
    zscore: str | None = None,
    first_group_size: float | None = None,
    src_type: str | None = None,
    trg_type: str | None = None,
    debug: float | None = None,
    runner: Runner | None = None,
) -> MrisSurfaceStatsOutputs:
    """
    Computes the group-wise mean and standard deviation of thickness differences at
    every vertex of the template surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surf_name: Set the surface filename.
        out_name: Set the output filename (standard deviation of data).
        data_files: List of input data files for computation.
        nsmooth: Specify number of smoothing steps.
        mask_name: Set the filename for surface mask.
        mean: Set the output filename for mean.
        absmean: Set the output filename for absolute mean.
        absstd: Set the output filename for standard deviation of absolute mean.
        zscore: Set the output filename for z-score (only if first_group_size >\
            0).
        first_group_size: Specify how many subjects at the beginning belong to\
            first group.
        src_type: Input surface data format (default = paint).
        trg_type: Output format (default = paint).
        debug: Specify which surface vertex number to debug.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisSurfaceStatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_SURFACE_STATS_METADATA)
    params = mris_surface_stats_params(nsmooth=nsmooth, surf_name=surf_name, mask_name=mask_name, out_name=out_name, mean=mean, absmean=absmean, absstd=absstd, zscore=zscore, first_group_size=first_group_size, src_type=src_type, trg_type=trg_type, debug=debug, data_files=data_files)
    return mris_surface_stats_execute(params, execution)


__all__ = [
    "MRIS_SURFACE_STATS_METADATA",
    "MrisSurfaceStatsOutputs",
    "MrisSurfaceStatsParameters",
    "mris_surface_stats",
    "mris_surface_stats_params",
]
