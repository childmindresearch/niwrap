# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CIFTI_ROI_AVERAGE_METADATA = Metadata(
    id="1b13bf5892e798c2e102f4545e49286ec743589d.boutiques",
    name="cifti-roi-average",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
CiftiRoiAverageParameters = typing.TypedDict('CiftiRoiAverageParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-roi-average"],
    "cifti_in": InputPathType,
    "text_out": str,
    "opt_cifti_roi_roi_cifti": typing.NotRequired[InputPathType | None],
    "opt_left_roi_roi_metric": typing.NotRequired[InputPathType | None],
    "opt_right_roi_roi_metric": typing.NotRequired[InputPathType | None],
    "opt_cerebellum_roi_roi_metric": typing.NotRequired[InputPathType | None],
    "opt_vol_roi_roi_vol": typing.NotRequired[InputPathType | None],
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
        "cifti-roi-average": cifti_roi_average_cargs,
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
    vt = {}
    return vt.get(t)


class CiftiRoiAverageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_roi_average(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def cifti_roi_average_params(
    cifti_in: InputPathType,
    text_out: str,
    opt_cifti_roi_roi_cifti: InputPathType | None = None,
    opt_left_roi_roi_metric: InputPathType | None = None,
    opt_right_roi_roi_metric: InputPathType | None = None,
    opt_cerebellum_roi_roi_metric: InputPathType | None = None,
    opt_vol_roi_roi_vol: InputPathType | None = None,
) -> CiftiRoiAverageParameters:
    """
    Build parameters.
    
    Args:
        cifti_in: the cifti file to average rows from.
        text_out: output text file of the average values.
        opt_cifti_roi_roi_cifti: cifti file containing combined rois: the rois\
            as a cifti file.
        opt_left_roi_roi_metric: vertices to use from left hemisphere: the left\
            roi as a metric file.
        opt_right_roi_roi_metric: vertices to use from right hemisphere: the\
            right roi as a metric file.
        opt_cerebellum_roi_roi_metric: vertices to use from cerebellum: the\
            cerebellum roi as a metric file.
        opt_vol_roi_roi_vol: voxels to use: the roi volume file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-roi-average",
        "cifti_in": cifti_in,
        "text_out": text_out,
    }
    if opt_cifti_roi_roi_cifti is not None:
        params["opt_cifti_roi_roi_cifti"] = opt_cifti_roi_roi_cifti
    if opt_left_roi_roi_metric is not None:
        params["opt_left_roi_roi_metric"] = opt_left_roi_roi_metric
    if opt_right_roi_roi_metric is not None:
        params["opt_right_roi_roi_metric"] = opt_right_roi_roi_metric
    if opt_cerebellum_roi_roi_metric is not None:
        params["opt_cerebellum_roi_roi_metric"] = opt_cerebellum_roi_roi_metric
    if opt_vol_roi_roi_vol is not None:
        params["opt_vol_roi_roi_vol"] = opt_vol_roi_roi_vol
    return params


def cifti_roi_average_cargs(
    params: CiftiRoiAverageParameters,
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
    cargs.append("-cifti-roi-average")
    cargs.append(execution.input_file(params.get("cifti_in")))
    cargs.append(params.get("text_out"))
    if params.get("opt_cifti_roi_roi_cifti") is not None:
        cargs.extend([
            "-cifti-roi",
            execution.input_file(params.get("opt_cifti_roi_roi_cifti"))
        ])
    if params.get("opt_left_roi_roi_metric") is not None:
        cargs.extend([
            "-left-roi",
            execution.input_file(params.get("opt_left_roi_roi_metric"))
        ])
    if params.get("opt_right_roi_roi_metric") is not None:
        cargs.extend([
            "-right-roi",
            execution.input_file(params.get("opt_right_roi_roi_metric"))
        ])
    if params.get("opt_cerebellum_roi_roi_metric") is not None:
        cargs.extend([
            "-cerebellum-roi",
            execution.input_file(params.get("opt_cerebellum_roi_roi_metric"))
        ])
    if params.get("opt_vol_roi_roi_vol") is not None:
        cargs.extend([
            "-vol-roi",
            execution.input_file(params.get("opt_vol_roi_roi_vol"))
        ])
    return cargs


def cifti_roi_average_outputs(
    params: CiftiRoiAverageParameters,
    execution: Execution,
) -> CiftiRoiAverageOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiRoiAverageOutputs(
        root=execution.output_file("."),
    )
    return ret


def cifti_roi_average_execute(
    params: CiftiRoiAverageParameters,
    execution: Execution,
) -> CiftiRoiAverageOutputs:
    """
    Average rows in a single cifti file.
    
    Average the rows that are within the specified ROIs, and write the resulting
    average row to a text file, separated by newlines. If -cifti-roi is
    specified, -left-roi, -right-roi, -cerebellum-roi, and -vol-roi must not be
    specified.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiRoiAverageOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = cifti_roi_average_cargs(params, execution)
    ret = cifti_roi_average_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_roi_average(
    cifti_in: InputPathType,
    text_out: str,
    opt_cifti_roi_roi_cifti: InputPathType | None = None,
    opt_left_roi_roi_metric: InputPathType | None = None,
    opt_right_roi_roi_metric: InputPathType | None = None,
    opt_cerebellum_roi_roi_metric: InputPathType | None = None,
    opt_vol_roi_roi_vol: InputPathType | None = None,
    runner: Runner | None = None,
) -> CiftiRoiAverageOutputs:
    """
    Average rows in a single cifti file.
    
    Average the rows that are within the specified ROIs, and write the resulting
    average row to a text file, separated by newlines. If -cifti-roi is
    specified, -left-roi, -right-roi, -cerebellum-roi, and -vol-roi must not be
    specified.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        cifti_in: the cifti file to average rows from.
        text_out: output text file of the average values.
        opt_cifti_roi_roi_cifti: cifti file containing combined rois: the rois\
            as a cifti file.
        opt_left_roi_roi_metric: vertices to use from left hemisphere: the left\
            roi as a metric file.
        opt_right_roi_roi_metric: vertices to use from right hemisphere: the\
            right roi as a metric file.
        opt_cerebellum_roi_roi_metric: vertices to use from cerebellum: the\
            cerebellum roi as a metric file.
        opt_vol_roi_roi_vol: voxels to use: the roi volume file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiRoiAverageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_ROI_AVERAGE_METADATA)
    params = cifti_roi_average_params(cifti_in=cifti_in, text_out=text_out, opt_cifti_roi_roi_cifti=opt_cifti_roi_roi_cifti, opt_left_roi_roi_metric=opt_left_roi_roi_metric, opt_right_roi_roi_metric=opt_right_roi_roi_metric, opt_cerebellum_roi_roi_metric=opt_cerebellum_roi_roi_metric, opt_vol_roi_roi_vol=opt_vol_roi_roi_vol)
    return cifti_roi_average_execute(params, execution)


__all__ = [
    "CIFTI_ROI_AVERAGE_METADATA",
    "CiftiRoiAverageOutputs",
    "CiftiRoiAverageParameters",
    "cifti_roi_average",
    "cifti_roi_average_params",
]
