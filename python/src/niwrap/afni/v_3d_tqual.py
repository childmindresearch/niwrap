# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_TQUAL_METADATA = Metadata(
    id="a5953b420d22f8f6c2b20824e280582d44af991c.boutiques",
    name="3dTqual",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dTqualParameters = typing.TypedDict('V3dTqualParameters', {
    "__STYX_TYPE__": typing.Literal["3dTqual"],
    "dataset": InputPathType,
    "spearman": bool,
    "quadrant": bool,
    "autoclip": bool,
    "automask": bool,
    "clip": typing.NotRequired[float | None],
    "mask": typing.NotRequired[InputPathType | None],
    "range": bool,
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
        "3dTqual": v_3d_tqual_cargs,
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
        "3dTqual": v_3d_tqual_outputs,
    }.get(t)


class V3dTqualOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_tqual(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    time_series: OutputPathType
    """The 1D time series with the quality index for each sub-brick"""


def v_3d_tqual_params(
    dataset: InputPathType,
    spearman: bool = False,
    quadrant: bool = False,
    autoclip: bool = False,
    automask: bool = False,
    clip: float | None = None,
    mask: InputPathType | None = None,
    range_: bool = False,
) -> V3dTqualParameters:
    """
    Build parameters.
    
    Args:
        dataset: Input 3D+time dataset.
        spearman: Quality index is 1 minus the Spearman (rank) correlation\
            coefficient of each sub-brick with the median sub-brick (default\
            method).
        quadrant: Quality index is 1 minus the quadrant correlation coefficient\
            as the quality index.
        autoclip: Clip off low-intensity regions in the median sub-brick, only\
            compute correlation between high-intensity voxels.
        automask: Automatically mask and compute correlation only across\
            high-intensity (presumably brain) voxels.
        clip: Clip off values below given threshold in the median sub-brick.
        mask: Compute correlation only across masked voxels from the given\
            dataset.
        range_: Print the median-3.5*MAD and median+3.5*MAD values with each\
            quality index for plotting.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dTqual",
        "dataset": dataset,
        "spearman": spearman,
        "quadrant": quadrant,
        "autoclip": autoclip,
        "automask": automask,
        "range": range_,
    }
    if clip is not None:
        params["clip"] = clip
    if mask is not None:
        params["mask"] = mask
    return params


def v_3d_tqual_cargs(
    params: V3dTqualParameters,
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
    cargs.append("3dTqual")
    cargs.append(execution.input_file(params.get("dataset")))
    if params.get("spearman"):
        cargs.append("-spearman")
    if params.get("quadrant"):
        cargs.append("-quadrant")
    if params.get("autoclip"):
        cargs.append("-autoclip")
    if params.get("automask"):
        cargs.append("-automask")
    if params.get("clip") is not None:
        cargs.extend([
            "-clip",
            str(params.get("clip"))
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("range"):
        cargs.append("-range")
    return cargs


def v_3d_tqual_outputs(
    params: V3dTqualParameters,
    execution: Execution,
) -> V3dTqualOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dTqualOutputs(
        root=execution.output_file("."),
        time_series=execution.output_file("stdout"),
    )
    return ret


def v_3d_tqual_execute(
    params: V3dTqualParameters,
    execution: Execution,
) -> V3dTqualOutputs:
    """
    Computes a quality index for each sub-brick in a 3D+time dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dTqualOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_tqual_cargs(params, execution)
    ret = v_3d_tqual_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_tqual(
    dataset: InputPathType,
    spearman: bool = False,
    quadrant: bool = False,
    autoclip: bool = False,
    automask: bool = False,
    clip: float | None = None,
    mask: InputPathType | None = None,
    range_: bool = False,
    runner: Runner | None = None,
) -> V3dTqualOutputs:
    """
    Computes a quality index for each sub-brick in a 3D+time dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset: Input 3D+time dataset.
        spearman: Quality index is 1 minus the Spearman (rank) correlation\
            coefficient of each sub-brick with the median sub-brick (default\
            method).
        quadrant: Quality index is 1 minus the quadrant correlation coefficient\
            as the quality index.
        autoclip: Clip off low-intensity regions in the median sub-brick, only\
            compute correlation between high-intensity voxels.
        automask: Automatically mask and compute correlation only across\
            high-intensity (presumably brain) voxels.
        clip: Clip off values below given threshold in the median sub-brick.
        mask: Compute correlation only across masked voxels from the given\
            dataset.
        range_: Print the median-3.5*MAD and median+3.5*MAD values with each\
            quality index for plotting.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTqualOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TQUAL_METADATA)
    params = v_3d_tqual_params(dataset=dataset, spearman=spearman, quadrant=quadrant, autoclip=autoclip, automask=automask, clip=clip, mask=mask, range_=range_)
    return v_3d_tqual_execute(params, execution)


__all__ = [
    "V3dTqualOutputs",
    "V3dTqualParameters",
    "V_3D_TQUAL_METADATA",
    "v_3d_tqual",
    "v_3d_tqual_params",
]
