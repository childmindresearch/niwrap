# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_TOUTCOUNT_METADATA = Metadata(
    id="b726a8742694b4a0acfdfd929608a00118e5b42b.boutiques",
    name="3dToutcount",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dToutcountParameters = typing.TypedDict('V3dToutcountParameters', {
    "__STYX_TYPE__": typing.Literal["3dToutcount"],
    "input_dataset": str,
    "output_prefix": typing.NotRequired[str | None],
    "mask_dataset": typing.NotRequired[str | None],
    "q_threshold": typing.NotRequired[float | None],
    "autoclip": bool,
    "automask": bool,
    "fraction": bool,
    "range": bool,
    "polort_order": typing.NotRequired[float | None],
    "legendre": bool,
})


def dyn_cargs(
    t: str,
) -> None:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    vt = {
        "3dToutcount": v_3d_toutcount_cargs,
    }
    return vt.get(t)


def dyn_outputs(
    t: str,
) -> None:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    vt = {
        "3dToutcount": v_3d_toutcount_outputs,
    }
    return vt.get(t)


class V3dToutcountOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_toutcount(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_afni_head: OutputPathType | None
    """Output dataset in AFNI format (HEAD file)."""
    output_afni_brik: OutputPathType | None
    """Output dataset in AFNI format (BRIK file)."""


def v_3d_toutcount_params(
    input_dataset: str,
    output_prefix: str | None = None,
    mask_dataset: str | None = None,
    q_threshold: float | None = None,
    autoclip: bool = False,
    automask: bool = False,
    fraction: bool = False,
    range_: bool = False,
    polort_order: float | None = None,
    legendre: bool = False,
) -> V3dToutcountParameters:
    """
    Build parameters.
    
    Args:
        input_dataset: Input 3D+time dataset (e.g. dataset+orig).
        output_prefix: Prefix of the new dataset saved with the outlier Q\
            values, applicable with the -save option.
        mask_dataset: Only count voxels in the provided mask dataset.
        q_threshold: Use 'q' instead of 0.001 in the calculation of alpha. Must\
            be within range 0 < q < 1.
        autoclip: Clip off 'small' voxels (as in 3dClipLevel). Cannot use with\
            -mask.
        automask: Automatically mask the dataset. Cannot use with -mask.
        fraction: Output the fraction of (masked) voxels which are outliers at\
            each time point, instead of the count.
        range_: Print out median+3.5*MAD of outlier count with each time point.
        polort_order: Detrend each voxel time series with polynomials of order\
            'nn'. Default value is 0, which removes the median.
        legendre: Use Legendre polynomials for detrending (also allows -polort\
            > 3).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dToutcount",
        "input_dataset": input_dataset,
        "autoclip": autoclip,
        "automask": automask,
        "fraction": fraction,
        "range": range_,
        "legendre": legendre,
    }
    if output_prefix is not None:
        params["output_prefix"] = output_prefix
    if mask_dataset is not None:
        params["mask_dataset"] = mask_dataset
    if q_threshold is not None:
        params["q_threshold"] = q_threshold
    if polort_order is not None:
        params["polort_order"] = polort_order
    return params


def v_3d_toutcount_cargs(
    params: V3dToutcountParameters,
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
    cargs.append("3dToutcount")
    cargs.append(params.get("input_dataset"))
    if params.get("output_prefix") is not None:
        cargs.append(params.get("output_prefix"))
    if params.get("mask_dataset") is not None:
        cargs.extend([
            "-mask",
            params.get("mask_dataset")
        ])
    if params.get("q_threshold") is not None:
        cargs.extend([
            "-qthr",
            str(params.get("q_threshold"))
        ])
    if params.get("autoclip"):
        cargs.append("-autoclip")
    if params.get("automask"):
        cargs.append("-automask")
    if params.get("fraction"):
        cargs.append("-fraction")
    if params.get("range"):
        cargs.append("-range")
    if params.get("polort_order") is not None:
        cargs.extend([
            "-polort",
            str(params.get("polort_order"))
        ])
    if params.get("legendre"):
        cargs.append("-legendre")
    return cargs


def v_3d_toutcount_outputs(
    params: V3dToutcountParameters,
    execution: Execution,
) -> V3dToutcountOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dToutcountOutputs(
        root=execution.output_file("."),
        output_afni_head=execution.output_file(params.get("output_prefix") + ".HEAD") if (params.get("output_prefix") is not None) else None,
        output_afni_brik=execution.output_file(params.get("output_prefix") + ".BRIK") if (params.get("output_prefix") is not None) else None,
    )
    return ret


def v_3d_toutcount_execute(
    params: V3dToutcountParameters,
    execution: Execution,
) -> V3dToutcountOutputs:
    """
    Calculates the number of 'outliers' in a 3D+time dataset at each time point.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dToutcountOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_toutcount_cargs(params, execution)
    ret = v_3d_toutcount_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_toutcount(
    input_dataset: str,
    output_prefix: str | None = None,
    mask_dataset: str | None = None,
    q_threshold: float | None = None,
    autoclip: bool = False,
    automask: bool = False,
    fraction: bool = False,
    range_: bool = False,
    polort_order: float | None = None,
    legendre: bool = False,
    runner: Runner | None = None,
) -> V3dToutcountOutputs:
    """
    Calculates the number of 'outliers' in a 3D+time dataset at each time point.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Input 3D+time dataset (e.g. dataset+orig).
        output_prefix: Prefix of the new dataset saved with the outlier Q\
            values, applicable with the -save option.
        mask_dataset: Only count voxels in the provided mask dataset.
        q_threshold: Use 'q' instead of 0.001 in the calculation of alpha. Must\
            be within range 0 < q < 1.
        autoclip: Clip off 'small' voxels (as in 3dClipLevel). Cannot use with\
            -mask.
        automask: Automatically mask the dataset. Cannot use with -mask.
        fraction: Output the fraction of (masked) voxels which are outliers at\
            each time point, instead of the count.
        range_: Print out median+3.5*MAD of outlier count with each time point.
        polort_order: Detrend each voxel time series with polynomials of order\
            'nn'. Default value is 0, which removes the median.
        legendre: Use Legendre polynomials for detrending (also allows -polort\
            > 3).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dToutcountOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TOUTCOUNT_METADATA)
    params = v_3d_toutcount_params(input_dataset=input_dataset, output_prefix=output_prefix, mask_dataset=mask_dataset, q_threshold=q_threshold, autoclip=autoclip, automask=automask, fraction=fraction, range_=range_, polort_order=polort_order, legendre=legendre)
    return v_3d_toutcount_execute(params, execution)


__all__ = [
    "V3dToutcountOutputs",
    "V3dToutcountParameters",
    "V_3D_TOUTCOUNT_METADATA",
    "v_3d_toutcount",
    "v_3d_toutcount_params",
]
