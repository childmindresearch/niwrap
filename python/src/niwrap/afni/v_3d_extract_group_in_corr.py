# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_EXTRACT_GROUP_IN_CORR_METADATA = Metadata(
    id="589ed658ff74e91ed944c55e458a7888b478c333.boutiques",
    name="3dExtractGroupInCorr",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dExtractGroupInCorrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_extract_group_in_corr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType | None
    """Output dataset reconstructed from GroupInCorr data"""


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
    cargs = []
    cargs.append("3dExtractGroupInCorr")
    cargs.append(execution.input_file(group_in_corr_file))
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    ret = V3dExtractGroupInCorrOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file(prefix + "_[DATASET_LABEL].nii") if (prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dExtractGroupInCorrOutputs",
    "V_3D_EXTRACT_GROUP_IN_CORR_METADATA",
    "v_3d_extract_group_in_corr",
]
