# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_EXTRACT_GROUP_IN_CORR_METADATA = Metadata(
    id="589ed658ff74e91ed944c55e458a7888b478c333.boutiques",
    name="3dExtractGroupInCorr",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dExtractGroupInCorrParameters = typing.TypedDict('V3dExtractGroupInCorrParameters', {
    "__STYX_TYPE__": typing.Literal["3dExtractGroupInCorr"],
    "group_in_corr_file": InputPathType,
    "prefix": typing.NotRequired[str | None],
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
        "3dExtractGroupInCorr": v_3d_extract_group_in_corr_cargs,
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
        "3dExtractGroupInCorr": v_3d_extract_group_in_corr_outputs,
    }.get(t)


class V3dExtractGroupInCorrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_extract_group_in_corr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType | None
    """Output dataset reconstructed from GroupInCorr data"""


def v_3d_extract_group_in_corr_params(
    group_in_corr_file: InputPathType,
    prefix: str | None = None,
) -> V3dExtractGroupInCorrParameters:
    """
    Build parameters.
    
    Args:
        group_in_corr_file: GroupInCorr file to extract datasets from (e.g.\
            AAA.grpincorr.niml).
        prefix: Prefix to prepend to dataset labels. Use 'NULL' to skip the use\
            of the prefix.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dExtractGroupInCorr",
        "group_in_corr_file": group_in_corr_file,
    }
    if prefix is not None:
        params["prefix"] = prefix
    return params


def v_3d_extract_group_in_corr_cargs(
    params: V3dExtractGroupInCorrParameters,
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
    cargs.append("3dExtractGroupInCorr")
    cargs.append(execution.input_file(params.get("group_in_corr_file")))
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    return cargs


def v_3d_extract_group_in_corr_outputs(
    params: V3dExtractGroupInCorrParameters,
    execution: Execution,
) -> V3dExtractGroupInCorrOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dExtractGroupInCorrOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file(params.get("prefix") + "_[DATASET_LABEL].nii") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_extract_group_in_corr_execute(
    params: V3dExtractGroupInCorrParameters,
    execution: Execution,
) -> V3dExtractGroupInCorrOutputs:
    """
    This program breaks the collection of images from a GroupInCorr file back into
    individual AFNI 3D+time datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dExtractGroupInCorrOutputs`).
    """
    cargs = v_3d_extract_group_in_corr_cargs(params, execution)
    ret = v_3d_extract_group_in_corr_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_extract_group_in_corr(
    group_in_corr_file: InputPathType,
    prefix: str | None = None,
    runner: Runner | None = None,
) -> V3dExtractGroupInCorrOutputs:
    """
    This program breaks the collection of images from a GroupInCorr file back into
    individual AFNI 3D+time datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        group_in_corr_file: GroupInCorr file to extract datasets from (e.g.\
            AAA.grpincorr.niml).
        prefix: Prefix to prepend to dataset labels. Use 'NULL' to skip the use\
            of the prefix.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dExtractGroupInCorrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_EXTRACT_GROUP_IN_CORR_METADATA)
    params = v_3d_extract_group_in_corr_params(group_in_corr_file=group_in_corr_file, prefix=prefix)
    return v_3d_extract_group_in_corr_execute(params, execution)


__all__ = [
    "V3dExtractGroupInCorrOutputs",
    "V3dExtractGroupInCorrParameters",
    "V_3D_EXTRACT_GROUP_IN_CORR_METADATA",
    "v_3d_extract_group_in_corr",
    "v_3d_extract_group_in_corr_params",
]
