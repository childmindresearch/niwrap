# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_ROISTATS_METADATA = Metadata(
    id="80281254f3598a961619f69119f1d0eb9b58f421.boutiques",
    name="3dROIstats",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dRoistatsParameters = typing.TypedDict('V3dRoistatsParameters', {
    "__STYX_TYPE__": typing.Literal["3dROIstats"],
    "in_file": InputPathType,
    "mask": typing.NotRequired[InputPathType | None],
    "debug": bool,
    "format1D": bool,
    "format1DR": bool,
    "mask_f2short": bool,
    "mask_file": typing.NotRequired[InputPathType | None],
    "nobriklab": bool,
    "nomeanout": bool,
    "num_roi": typing.NotRequired[int | None],
    "quiet": bool,
    "roisel": typing.NotRequired[InputPathType | None],
    "stat": typing.NotRequired[list[InputPathType] | None],
    "zerofill": typing.NotRequired[str | None],
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
        "3dROIstats": v_3d_roistats_cargs,
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
        "3dROIstats": v_3d_roistats_outputs,
    }.get(t)


class V3dRoistatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_roistats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    stats: list[str]
    """There will be one line of output for every sub-brick of every input
    dataset. Across each line will be every statistic for every mask value. For
    instance, if there 3 mask values (1,2,3), then the columns Mean_1, Mean_2
    and Mean_3 will refer to the means across each mask value, respectively. If
    4 statistics are requested, then there will be 12 stats displayed on each
    line (4 for each mask region), besides the file and sub-brick number."""


def v_3d_roistats_params(
    in_file: InputPathType,
    mask: InputPathType | None = None,
    debug: bool = False,
    format1_d: bool = False,
    format1_dr: bool = False,
    mask_f2short: bool = False,
    mask_file: InputPathType | None = None,
    nobriklab: bool = False,
    nomeanout: bool = False,
    num_roi: int | None = None,
    quiet: bool = False,
    roisel: InputPathType | None = None,
    stat_: list[InputPathType] | None = None,
    zerofill: str | None = None,
) -> V3dRoistatsParameters:
    """
    Build parameters.
    
    Args:
        in_file: Input dataset.
        mask: Input mask.
        debug: Print debug information.
        format1_d: Output results in a 1d format that includes commented\
            labels.
        format1_dr: Output results in a 1d format that includes uncommented\
            labels. may not work optimally with typical 1d functions, but is useful\
            for r functions.
        mask_f2short: Tells the program to convert a float mask to short\
            integers, by simple rounding.
        mask_file: Input mask.
        nobriklab: Do not print the sub-brick label next to its index.
        nomeanout: Do not include the (zero-inclusive) mean among computed\
            stats.
        num_roi: Forces the assumption that the mask dataset's rois are denoted\
            by 1 to n inclusive. normally, the program figures out the rois on its\
            own. this option is useful if a) you are certain that the mask dataset\
            has no values outside the range [0 n], b) there may be some rois\
            missing between [1 n] in the mask data-set and c) you want those\
            columns in the output any-way so the output lines up with the output\
            from other invocations of 3droistats.
        quiet: Execute quietly.
        roisel: Only considers rois denoted by values found in the specified\
            file. note that the order of the rois as specified in the file is not\
            preserved. so an sel.1d of '2 8 20' produces the same output as '8 20\
            2'.
        stat_: A list of items which are 'mean' or 'sum' or 'voxels' or\
            'minmax' or 'sigma' or 'median' or 'mode' or 'summary' or 'zerominmax'\
            or 'zerosigma' or 'zeromedian' or 'zeromode'. Statistics to compute.\
            options include: * mean = compute the mean using only non_zero voxels.\
            implies the opposite for the mean computed by default. * median =\
            compute the median of nonzero voxels * mode = compute the mode of\
            nonzero voxels. (integral valued sets only) * minmax = compute the\
            min/max of nonzero voxels * sum = compute the sum using only nonzero\
            voxels. * voxels = compute the number of nonzero voxels * sigma =\
            compute the standard deviation of nonzero voxelsstatistics that include\
            zero-valued voxels: * zerominmax = compute the min/max of all voxels. *\
            zerosigma = compute the standard deviation of all voxels. * zeromedian\
            = compute the median of all voxels. * zeromode = compute the mode of\
            all voxels. * summary = only output a summary line with the grand mean\
            across all briks in the input dataset. this option cannot be used with\
            nomeanout.more that one option can be specified.
        zerofill: For roi labels not found, use the provided string instead of\
            a '0' in the output file. only active if `num_roi` is enabled.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dROIstats",
        "in_file": in_file,
        "debug": debug,
        "format1D": format1_d,
        "format1DR": format1_dr,
        "mask_f2short": mask_f2short,
        "nobriklab": nobriklab,
        "nomeanout": nomeanout,
        "quiet": quiet,
    }
    if mask is not None:
        params["mask"] = mask
    if mask_file is not None:
        params["mask_file"] = mask_file
    if num_roi is not None:
        params["num_roi"] = num_roi
    if roisel is not None:
        params["roisel"] = roisel
    if stat_ is not None:
        params["stat"] = stat_
    if zerofill is not None:
        params["zerofill"] = zerofill
    return params


def v_3d_roistats_cargs(
    params: V3dRoistatsParameters,
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
    cargs.append("3dROIstats")
    cargs.append(execution.input_file(params.get("in_file")))
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    cargs.append("[OUT_FILE]")
    if params.get("debug"):
        cargs.append("-debug")
    if params.get("format1D"):
        cargs.append("-1Dformat")
    if params.get("format1DR"):
        cargs.append("-1DRformat")
    if params.get("mask_f2short"):
        cargs.append("-mask_f2short")
    if params.get("mask_file") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask_file"))
        ])
    if params.get("nobriklab"):
        cargs.append("-nobriklab")
    if params.get("nomeanout"):
        cargs.append("-nomeanout")
    if params.get("num_roi") is not None:
        cargs.extend([
            "-numroi",
            str(params.get("num_roi"))
        ])
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("roisel") is not None:
        cargs.extend([
            "-roisel",
            execution.input_file(params.get("roisel"))
        ])
    if params.get("stat") is not None:
        cargs.extend([execution.input_file(f) for f in params.get("stat")])
    if params.get("zerofill") is not None:
        cargs.extend([
            "-zerofill",
            params.get("zerofill")
        ])
    return cargs


def v_3d_roistats_outputs(
    params: V3dRoistatsParameters,
    execution: Execution,
) -> V3dRoistatsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dRoistatsOutputs(
        root=execution.output_file("."),
        stats=[],
    )
    return ret


def v_3d_roistats_execute(
    params: V3dRoistatsParameters,
    execution: Execution,
) -> V3dRoistatsOutputs:
    """
    Display statistics over masked regions.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dRoistatsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_roistats_cargs(params, execution)
    ret = v_3d_roistats_outputs(params, execution)
    execution.run(cargs, handle_stdout=lambda s: ret.stats.append(s))
    return ret


def v_3d_roistats(
    in_file: InputPathType,
    mask: InputPathType | None = None,
    debug: bool = False,
    format1_d: bool = False,
    format1_dr: bool = False,
    mask_f2short: bool = False,
    mask_file: InputPathType | None = None,
    nobriklab: bool = False,
    nomeanout: bool = False,
    num_roi: int | None = None,
    quiet: bool = False,
    roisel: InputPathType | None = None,
    stat_: list[InputPathType] | None = None,
    zerofill: str | None = None,
    runner: Runner | None = None,
) -> V3dRoistatsOutputs:
    """
    Display statistics over masked regions.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        in_file: Input dataset.
        mask: Input mask.
        debug: Print debug information.
        format1_d: Output results in a 1d format that includes commented\
            labels.
        format1_dr: Output results in a 1d format that includes uncommented\
            labels. may not work optimally with typical 1d functions, but is useful\
            for r functions.
        mask_f2short: Tells the program to convert a float mask to short\
            integers, by simple rounding.
        mask_file: Input mask.
        nobriklab: Do not print the sub-brick label next to its index.
        nomeanout: Do not include the (zero-inclusive) mean among computed\
            stats.
        num_roi: Forces the assumption that the mask dataset's rois are denoted\
            by 1 to n inclusive. normally, the program figures out the rois on its\
            own. this option is useful if a) you are certain that the mask dataset\
            has no values outside the range [0 n], b) there may be some rois\
            missing between [1 n] in the mask data-set and c) you want those\
            columns in the output any-way so the output lines up with the output\
            from other invocations of 3droistats.
        quiet: Execute quietly.
        roisel: Only considers rois denoted by values found in the specified\
            file. note that the order of the rois as specified in the file is not\
            preserved. so an sel.1d of '2 8 20' produces the same output as '8 20\
            2'.
        stat_: A list of items which are 'mean' or 'sum' or 'voxels' or\
            'minmax' or 'sigma' or 'median' or 'mode' or 'summary' or 'zerominmax'\
            or 'zerosigma' or 'zeromedian' or 'zeromode'. Statistics to compute.\
            options include: * mean = compute the mean using only non_zero voxels.\
            implies the opposite for the mean computed by default. * median =\
            compute the median of nonzero voxels * mode = compute the mode of\
            nonzero voxels. (integral valued sets only) * minmax = compute the\
            min/max of nonzero voxels * sum = compute the sum using only nonzero\
            voxels. * voxels = compute the number of nonzero voxels * sigma =\
            compute the standard deviation of nonzero voxelsstatistics that include\
            zero-valued voxels: * zerominmax = compute the min/max of all voxels. *\
            zerosigma = compute the standard deviation of all voxels. * zeromedian\
            = compute the median of all voxels. * zeromode = compute the mode of\
            all voxels. * summary = only output a summary line with the grand mean\
            across all briks in the input dataset. this option cannot be used with\
            nomeanout.more that one option can be specified.
        zerofill: For roi labels not found, use the provided string instead of\
            a '0' in the output file. only active if `num_roi` is enabled.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dRoistatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ROISTATS_METADATA)
    params = v_3d_roistats_params(in_file=in_file, mask=mask, debug=debug, format1_d=format1_d, format1_dr=format1_dr, mask_f2short=mask_f2short, mask_file=mask_file, nobriklab=nobriklab, nomeanout=nomeanout, num_roi=num_roi, quiet=quiet, roisel=roisel, stat_=stat_, zerofill=zerofill)
    return v_3d_roistats_execute(params, execution)


__all__ = [
    "V3dRoistatsOutputs",
    "V3dRoistatsParameters",
    "V_3D_ROISTATS_METADATA",
    "v_3d_roistats",
    "v_3d_roistats_params",
]
