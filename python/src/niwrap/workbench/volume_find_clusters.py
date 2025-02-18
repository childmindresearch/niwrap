# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

VOLUME_FIND_CLUSTERS_METADATA = Metadata(
    id="ec09ad8d9895aef68f1fee0d0addc56178d358ce.boutiques",
    name="volume-find-clusters",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
VolumeFindClustersParameters = typing.TypedDict('VolumeFindClustersParameters', {
    "__STYX_TYPE__": typing.Literal["volume-find-clusters"],
    "volume_in": InputPathType,
    "value_threshold": float,
    "minimum_volume": float,
    "volume_out": str,
    "opt_less_than": bool,
    "opt_roi_roi_volume": typing.NotRequired[InputPathType | None],
    "opt_subvolume_subvol": typing.NotRequired[str | None],
    "opt_size_ratio_ratio": typing.NotRequired[float | None],
    "opt_distance_distance": typing.NotRequired[float | None],
    "opt_start_startval": typing.NotRequired[int | None],
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
        "volume-find-clusters": volume_find_clusters_cargs,
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
        "volume-find-clusters": volume_find_clusters_outputs,
    }.get(t)


class VolumeFindClustersOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_find_clusters(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume"""


def volume_find_clusters_params(
    volume_in: InputPathType,
    value_threshold: float,
    minimum_volume: float,
    volume_out: str,
    opt_less_than: bool = False,
    opt_roi_roi_volume: InputPathType | None = None,
    opt_subvolume_subvol: str | None = None,
    opt_size_ratio_ratio: float | None = None,
    opt_distance_distance: float | None = None,
    opt_start_startval: int | None = None,
) -> VolumeFindClustersParameters:
    """
    Build parameters.
    
    Args:
        volume_in: the input volume.
        value_threshold: threshold for data values.
        minimum_volume: threshold for cluster volume, in mm^3.
        volume_out: the output volume.
        opt_less_than: find values less than <value-threshold>, rather than\
            greater.
        opt_roi_roi_volume: select a region of interest: the roi, as a volume\
            file.
        opt_subvolume_subvol: select a single subvolume: the subvolume number\
            or name.
        opt_size_ratio_ratio: ignore clusters smaller than a given fraction of\
            the largest cluster in map: fraction of the largest cluster's volume.
        opt_distance_distance: ignore clusters further than a given distance\
            from the largest cluster: how far from the largest cluster a cluster\
            can be, edge to edge, in mm.
        opt_start_startval: start labeling clusters from a value other than 1:\
            the value to give the first cluster found.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume-find-clusters",
        "volume_in": volume_in,
        "value_threshold": value_threshold,
        "minimum_volume": minimum_volume,
        "volume_out": volume_out,
        "opt_less_than": opt_less_than,
    }
    if opt_roi_roi_volume is not None:
        params["opt_roi_roi_volume"] = opt_roi_roi_volume
    if opt_subvolume_subvol is not None:
        params["opt_subvolume_subvol"] = opt_subvolume_subvol
    if opt_size_ratio_ratio is not None:
        params["opt_size_ratio_ratio"] = opt_size_ratio_ratio
    if opt_distance_distance is not None:
        params["opt_distance_distance"] = opt_distance_distance
    if opt_start_startval is not None:
        params["opt_start_startval"] = opt_start_startval
    return params


def volume_find_clusters_cargs(
    params: VolumeFindClustersParameters,
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
    cargs.append("-volume-find-clusters")
    cargs.append(execution.input_file(params.get("volume_in")))
    cargs.append(str(params.get("value_threshold")))
    cargs.append(str(params.get("minimum_volume")))
    cargs.append(params.get("volume_out"))
    if params.get("opt_less_than"):
        cargs.append("-less-than")
    if params.get("opt_roi_roi_volume") is not None:
        cargs.extend([
            "-roi",
            execution.input_file(params.get("opt_roi_roi_volume"))
        ])
    if params.get("opt_subvolume_subvol") is not None:
        cargs.extend([
            "-subvolume",
            params.get("opt_subvolume_subvol")
        ])
    if params.get("opt_size_ratio_ratio") is not None:
        cargs.extend([
            "-size-ratio",
            str(params.get("opt_size_ratio_ratio"))
        ])
    if params.get("opt_distance_distance") is not None:
        cargs.extend([
            "-distance",
            str(params.get("opt_distance_distance"))
        ])
    if params.get("opt_start_startval") is not None:
        cargs.extend([
            "-start",
            str(params.get("opt_start_startval"))
        ])
    return cargs


def volume_find_clusters_outputs(
    params: VolumeFindClustersParameters,
    execution: Execution,
) -> VolumeFindClustersOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VolumeFindClustersOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(params.get("volume_out")),
    )
    return ret


def volume_find_clusters_execute(
    params: VolumeFindClustersParameters,
    execution: Execution,
) -> VolumeFindClustersOutputs:
    """
    Filter clusters by volume.
    
    Outputs a volume with nonzero integers for all voxels within a large enough
    cluster, and zeros elsewhere. The integers denote cluster membership (by
    default, first cluster found will use value 1, second cluster 2, etc).
    Cluster values are not reused across frames of the output, but instead keep
    counting up. By default, values greater than <value-threshold> are
    considered to be in a cluster, use -less-than to test for values less than
    the threshold. To apply this as a mask to the data, or to do more
    complicated thresholding, see -volume-math.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VolumeFindClustersOutputs`).
    """
    params = execution.params(params)
    cargs = volume_find_clusters_cargs(params, execution)
    ret = volume_find_clusters_outputs(params, execution)
    execution.run(cargs)
    return ret


def volume_find_clusters(
    volume_in: InputPathType,
    value_threshold: float,
    minimum_volume: float,
    volume_out: str,
    opt_less_than: bool = False,
    opt_roi_roi_volume: InputPathType | None = None,
    opt_subvolume_subvol: str | None = None,
    opt_size_ratio_ratio: float | None = None,
    opt_distance_distance: float | None = None,
    opt_start_startval: int | None = None,
    runner: Runner | None = None,
) -> VolumeFindClustersOutputs:
    """
    Filter clusters by volume.
    
    Outputs a volume with nonzero integers for all voxels within a large enough
    cluster, and zeros elsewhere. The integers denote cluster membership (by
    default, first cluster found will use value 1, second cluster 2, etc).
    Cluster values are not reused across frames of the output, but instead keep
    counting up. By default, values greater than <value-threshold> are
    considered to be in a cluster, use -less-than to test for values less than
    the threshold. To apply this as a mask to the data, or to do more
    complicated thresholding, see -volume-math.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        volume_in: the input volume.
        value_threshold: threshold for data values.
        minimum_volume: threshold for cluster volume, in mm^3.
        volume_out: the output volume.
        opt_less_than: find values less than <value-threshold>, rather than\
            greater.
        opt_roi_roi_volume: select a region of interest: the roi, as a volume\
            file.
        opt_subvolume_subvol: select a single subvolume: the subvolume number\
            or name.
        opt_size_ratio_ratio: ignore clusters smaller than a given fraction of\
            the largest cluster in map: fraction of the largest cluster's volume.
        opt_distance_distance: ignore clusters further than a given distance\
            from the largest cluster: how far from the largest cluster a cluster\
            can be, edge to edge, in mm.
        opt_start_startval: start labeling clusters from a value other than 1:\
            the value to give the first cluster found.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeFindClustersOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_FIND_CLUSTERS_METADATA)
    params = volume_find_clusters_params(volume_in=volume_in, value_threshold=value_threshold, minimum_volume=minimum_volume, volume_out=volume_out, opt_less_than=opt_less_than, opt_roi_roi_volume=opt_roi_roi_volume, opt_subvolume_subvol=opt_subvolume_subvol, opt_size_ratio_ratio=opt_size_ratio_ratio, opt_distance_distance=opt_distance_distance, opt_start_startval=opt_start_startval)
    return volume_find_clusters_execute(params, execution)


__all__ = [
    "VOLUME_FIND_CLUSTERS_METADATA",
    "VolumeFindClustersOutputs",
    "VolumeFindClustersParameters",
    "volume_find_clusters",
    "volume_find_clusters_params",
]
