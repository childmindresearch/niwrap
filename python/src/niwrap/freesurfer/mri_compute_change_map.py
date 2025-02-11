# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_COMPUTE_CHANGE_MAP_METADATA = Metadata(
    id="4cf0713520dd67c2b0f360d78cb6a13011d05e50.boutiques",
    name="mri_compute_change_map",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriComputeChangeMapParameters = typing.TypedDict('MriComputeChangeMapParameters', {
    "__STYX_TYPE__": typing.Literal["mri_compute_change_map"],
    "mean_filter": bool,
    "gaussian_sigma": typing.NotRequired[float | None],
    "volume1": InputPathType,
    "volume2": InputPathType,
    "transform": InputPathType,
    "outvolume": str,
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
        "mri_compute_change_map": mri_compute_change_map_cargs,
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
        "mri_compute_change_map": mri_compute_change_map_outputs,
    }.get(t)


class MriComputeChangeMapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_compute_change_map(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_change_map: OutputPathType
    """Output change map registered with Volume 1"""


def mri_compute_change_map_params(
    volume1: InputPathType,
    volume2: InputPathType,
    transform: InputPathType,
    outvolume: str,
    mean_filter: bool = False,
    gaussian_sigma: float | None = None,
) -> MriComputeChangeMapParameters:
    """
    Build parameters.
    
    Args:
        volume1: First volume (e.g. volume1.mgz).
        volume2: Second volume, transformed into the space of Volume 1 (e.g.\
            volume2.mgz).
        transform: Transform that takes Volume 2 coordinates into Volume 1\
            space.
        outvolume: Output change map volume (e.g. change_map.mgz).
        mean_filter: Apply mean filter to the output before writing.
        gaussian_sigma: Smooth with Gaussian filter of specified sigma before\
            writing.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_compute_change_map",
        "mean_filter": mean_filter,
        "volume1": volume1,
        "volume2": volume2,
        "transform": transform,
        "outvolume": outvolume,
    }
    if gaussian_sigma is not None:
        params["gaussian_sigma"] = gaussian_sigma
    return params


def mri_compute_change_map_cargs(
    params: MriComputeChangeMapParameters,
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
    cargs.append("mri_compute_change_map")
    if params.get("mean_filter"):
        cargs.append("-m")
    if params.get("gaussian_sigma") is not None:
        cargs.extend([
            "-s",
            str(params.get("gaussian_sigma"))
        ])
    cargs.append(execution.input_file(params.get("volume1")))
    cargs.append(execution.input_file(params.get("volume2")))
    cargs.append(execution.input_file(params.get("transform")))
    cargs.append(params.get("outvolume"))
    return cargs


def mri_compute_change_map_outputs(
    params: MriComputeChangeMapParameters,
    execution: Execution,
) -> MriComputeChangeMapOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriComputeChangeMapOutputs(
        root=execution.output_file("."),
        out_change_map=execution.output_file(params.get("outvolume")),
    )
    return ret


def mri_compute_change_map_execute(
    params: MriComputeChangeMapParameters,
    execution: Execution,
) -> MriComputeChangeMapOutputs:
    """
    Compute the change map between two MRI volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriComputeChangeMapOutputs`).
    """
    cargs = mri_compute_change_map_cargs(params, execution)
    ret = mri_compute_change_map_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_compute_change_map(
    volume1: InputPathType,
    volume2: InputPathType,
    transform: InputPathType,
    outvolume: str,
    mean_filter: bool = False,
    gaussian_sigma: float | None = None,
    runner: Runner | None = None,
) -> MriComputeChangeMapOutputs:
    """
    Compute the change map between two MRI volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        volume1: First volume (e.g. volume1.mgz).
        volume2: Second volume, transformed into the space of Volume 1 (e.g.\
            volume2.mgz).
        transform: Transform that takes Volume 2 coordinates into Volume 1\
            space.
        outvolume: Output change map volume (e.g. change_map.mgz).
        mean_filter: Apply mean filter to the output before writing.
        gaussian_sigma: Smooth with Gaussian filter of specified sigma before\
            writing.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriComputeChangeMapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_COMPUTE_CHANGE_MAP_METADATA)
    params = mri_compute_change_map_params(mean_filter=mean_filter, gaussian_sigma=gaussian_sigma, volume1=volume1, volume2=volume2, transform=transform, outvolume=outvolume)
    return mri_compute_change_map_execute(params, execution)


__all__ = [
    "MRI_COMPUTE_CHANGE_MAP_METADATA",
    "MriComputeChangeMapOutputs",
    "MriComputeChangeMapParameters",
    "mri_compute_change_map",
    "mri_compute_change_map_params",
]
