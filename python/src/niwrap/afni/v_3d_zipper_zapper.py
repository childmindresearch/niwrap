# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_ZIPPER_ZAPPER_METADATA = Metadata(
    id="345c0ab457fab3fd59e06829b589145ef0e78581.boutiques",
    name="3dZipperZapper",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dZipperZapperParameters = typing.TypedDict('V3dZipperZapperParameters', {
    "__STYX_TYPE__": typing.Literal["3dZipperZapper"],
    "input_file": InputPathType,
    "output_prefix": str,
    "mask_file": typing.NotRequired[InputPathType | None],
    "min_slice_nvox": typing.NotRequired[float | None],
    "min_streak_len": typing.NotRequired[float | None],
    "do_out_slice_param": bool,
    "no_out_bad_mask": bool,
    "no_out_text_vals": bool,
    "dont_use_streak": bool,
    "dont_use_drop": bool,
    "dont_use_corr": bool,
    "min_streak_val": typing.NotRequired[float | None],
    "min_drop_frac": typing.NotRequired[float | None],
    "min_drop_diff": typing.NotRequired[float | None],
    "min_corr_len": typing.NotRequired[float | None],
    "min_corr_corr": typing.NotRequired[float | None],
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
        "3dZipperZapper": v_3d_zipper_zapper_cargs,
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
        "3dZipperZapper": v_3d_zipper_zapper_outputs,
    }.get(t)


class V3dZipperZapperOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_zipper_zapper(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    bad_slice_mask: OutputPathType
    """Mask of potentially bad slices across the input dataset."""
    bad_volumes_list: OutputPathType
    """1D file containing a list of the bad volumes."""
    per_volume_params: OutputPathType
    """1D file of the per-volume parameters used to detect badness."""
    calculated_slices: OutputPathType
    """1D file of the slices within which calculations were made."""
    good_volumes_selector: OutputPathType
    """Text file with the selector string of *good* volumes."""


def v_3d_zipper_zapper_params(
    input_file: InputPathType,
    output_prefix: str,
    mask_file: InputPathType | None = None,
    min_slice_nvox: float | None = None,
    min_streak_len: float | None = None,
    do_out_slice_param: bool = False,
    no_out_bad_mask: bool = False,
    no_out_text_vals: bool = False,
    dont_use_streak: bool = False,
    dont_use_drop: bool = False,
    dont_use_corr: bool = False,
    min_streak_val: float | None = None,
    min_drop_frac: float | None = None,
    min_drop_diff: float | None = None,
    min_corr_len: float | None = None,
    min_corr_corr: float | None = None,
) -> V3dZipperZapperParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input 3D+time file of DWIs or EPIs.
        output_prefix: Prefix for output file name.
        mask_file: Optional input of a single volume mask file, which gets\
            applied to each volume in the input file.
        min_slice_nvox: Set the minimum number of voxels to be in the mask for\
            a given slice to be included in the calculations.
        min_streak_len: Minimum number of slices in a row to look for\
            fluctuations within.
        do_out_slice_param: Output the map of slice parameters.
        no_out_bad_mask: Do not output the mask of 'bad' slices.
        no_out_text_vals: Do not output the 1D files of the slice parameter\
            values.
        dont_use_streak: Turn off the 'streak' criterion for identifying bad\
            slices.
        dont_use_drop: Turn off the 'drop' criterion for identifying bad\
            slices.
        dont_use_corr: Turn off the 'corr' criterion for identifying bad\
            slices.
        min_streak_val: Minimum magnitude of voxelwise relative differences to\
            perhaps be problematic.
        min_drop_frac: Minimum fraction for judging if the change in 'slice\
            parameter' differences between neighboring slices might be a sign of\
            badness.
        min_drop_diff: Minimum 'slice parameter' value within a single slice\
            that might be considered a bad sign.
        min_corr_len: Minimum number of slices in a row to look for consecutive\
            anticorrelations in brightness differences.
        min_corr_corr: Threshold for the magnitude of anticorrelations to be\
            considered potentially bad.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dZipperZapper",
        "input_file": input_file,
        "output_prefix": output_prefix,
        "do_out_slice_param": do_out_slice_param,
        "no_out_bad_mask": no_out_bad_mask,
        "no_out_text_vals": no_out_text_vals,
        "dont_use_streak": dont_use_streak,
        "dont_use_drop": dont_use_drop,
        "dont_use_corr": dont_use_corr,
    }
    if mask_file is not None:
        params["mask_file"] = mask_file
    if min_slice_nvox is not None:
        params["min_slice_nvox"] = min_slice_nvox
    if min_streak_len is not None:
        params["min_streak_len"] = min_streak_len
    if min_streak_val is not None:
        params["min_streak_val"] = min_streak_val
    if min_drop_frac is not None:
        params["min_drop_frac"] = min_drop_frac
    if min_drop_diff is not None:
        params["min_drop_diff"] = min_drop_diff
    if min_corr_len is not None:
        params["min_corr_len"] = min_corr_len
    if min_corr_corr is not None:
        params["min_corr_corr"] = min_corr_corr
    return params


def v_3d_zipper_zapper_cargs(
    params: V3dZipperZapperParameters,
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
    cargs.append("3dZipperZapper")
    cargs.extend([
        "-input",
        execution.input_file(params.get("input_file"))
    ])
    cargs.extend([
        "-prefix",
        params.get("output_prefix")
    ])
    if params.get("mask_file") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask_file"))
        ])
    if params.get("min_slice_nvox") is not None:
        cargs.extend([
            "-min_slice_nvox",
            str(params.get("min_slice_nvox"))
        ])
    if params.get("min_streak_len") is not None:
        cargs.extend([
            "-min_streak_len",
            str(params.get("min_streak_len"))
        ])
    if params.get("do_out_slice_param"):
        cargs.append("-do_out_slice_param")
    if params.get("no_out_bad_mask"):
        cargs.append("-no_out_bad_mask")
    if params.get("no_out_text_vals"):
        cargs.append("-no_out_text_vals")
    if params.get("dont_use_streak"):
        cargs.append("-dont_use_streak")
    if params.get("dont_use_drop"):
        cargs.append("-dont_use_drop")
    if params.get("dont_use_corr"):
        cargs.append("-dont_use_corr")
    if params.get("min_streak_val") is not None:
        cargs.extend([
            "-min_streak_val",
            str(params.get("min_streak_val"))
        ])
    if params.get("min_drop_frac") is not None:
        cargs.extend([
            "-min_drop_frac",
            str(params.get("min_drop_frac"))
        ])
    if params.get("min_drop_diff") is not None:
        cargs.extend([
            "-min_drop_diff",
            str(params.get("min_drop_diff"))
        ])
    if params.get("min_corr_len") is not None:
        cargs.extend([
            "-min_corr_len",
            str(params.get("min_corr_len"))
        ])
    if params.get("min_corr_corr") is not None:
        cargs.extend([
            "-min_corr_corr",
            str(params.get("min_corr_corr"))
        ])
    return cargs


def v_3d_zipper_zapper_outputs(
    params: V3dZipperZapperParameters,
    execution: Execution,
) -> V3dZipperZapperOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dZipperZapperOutputs(
        root=execution.output_file("."),
        bad_slice_mask=execution.output_file(params.get("output_prefix") + "_badmask.nii.gz"),
        bad_volumes_list=execution.output_file(params.get("output_prefix") + "_badvols.1D"),
        per_volume_params=execution.output_file(params.get("output_prefix") + "_param.1D"),
        calculated_slices=execution.output_file(params.get("output_prefix") + "_sli.1D"),
        good_volumes_selector=execution.output_file(params.get("output_prefix") + "_goodvols.txt"),
    )
    return ret


def v_3d_zipper_zapper_execute(
    params: V3dZipperZapperParameters,
    execution: Execution,
) -> V3dZipperZapperOutputs:
    """
    A basic program to highlight problematic volumes in data sets, especially
    EPI/DWI data sets with interleaved acquisition.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dZipperZapperOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_zipper_zapper_cargs(params, execution)
    ret = v_3d_zipper_zapper_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_zipper_zapper(
    input_file: InputPathType,
    output_prefix: str,
    mask_file: InputPathType | None = None,
    min_slice_nvox: float | None = None,
    min_streak_len: float | None = None,
    do_out_slice_param: bool = False,
    no_out_bad_mask: bool = False,
    no_out_text_vals: bool = False,
    dont_use_streak: bool = False,
    dont_use_drop: bool = False,
    dont_use_corr: bool = False,
    min_streak_val: float | None = None,
    min_drop_frac: float | None = None,
    min_drop_diff: float | None = None,
    min_corr_len: float | None = None,
    min_corr_corr: float | None = None,
    runner: Runner | None = None,
) -> V3dZipperZapperOutputs:
    """
    A basic program to highlight problematic volumes in data sets, especially
    EPI/DWI data sets with interleaved acquisition.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Input 3D+time file of DWIs or EPIs.
        output_prefix: Prefix for output file name.
        mask_file: Optional input of a single volume mask file, which gets\
            applied to each volume in the input file.
        min_slice_nvox: Set the minimum number of voxels to be in the mask for\
            a given slice to be included in the calculations.
        min_streak_len: Minimum number of slices in a row to look for\
            fluctuations within.
        do_out_slice_param: Output the map of slice parameters.
        no_out_bad_mask: Do not output the mask of 'bad' slices.
        no_out_text_vals: Do not output the 1D files of the slice parameter\
            values.
        dont_use_streak: Turn off the 'streak' criterion for identifying bad\
            slices.
        dont_use_drop: Turn off the 'drop' criterion for identifying bad\
            slices.
        dont_use_corr: Turn off the 'corr' criterion for identifying bad\
            slices.
        min_streak_val: Minimum magnitude of voxelwise relative differences to\
            perhaps be problematic.
        min_drop_frac: Minimum fraction for judging if the change in 'slice\
            parameter' differences between neighboring slices might be a sign of\
            badness.
        min_drop_diff: Minimum 'slice parameter' value within a single slice\
            that might be considered a bad sign.
        min_corr_len: Minimum number of slices in a row to look for consecutive\
            anticorrelations in brightness differences.
        min_corr_corr: Threshold for the magnitude of anticorrelations to be\
            considered potentially bad.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dZipperZapperOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ZIPPER_ZAPPER_METADATA)
    params = v_3d_zipper_zapper_params(input_file=input_file, output_prefix=output_prefix, mask_file=mask_file, min_slice_nvox=min_slice_nvox, min_streak_len=min_streak_len, do_out_slice_param=do_out_slice_param, no_out_bad_mask=no_out_bad_mask, no_out_text_vals=no_out_text_vals, dont_use_streak=dont_use_streak, dont_use_drop=dont_use_drop, dont_use_corr=dont_use_corr, min_streak_val=min_streak_val, min_drop_frac=min_drop_frac, min_drop_diff=min_drop_diff, min_corr_len=min_corr_len, min_corr_corr=min_corr_corr)
    return v_3d_zipper_zapper_execute(params, execution)


__all__ = [
    "V3dZipperZapperOutputs",
    "V3dZipperZapperParameters",
    "V_3D_ZIPPER_ZAPPER_METADATA",
    "v_3d_zipper_zapper",
    "v_3d_zipper_zapper_params",
]
