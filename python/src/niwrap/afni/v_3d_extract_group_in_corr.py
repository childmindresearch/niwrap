# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_EXTRACT_GROUP_IN_CORR_METADATA = Metadata(
    id="b8b23d33ef8a1a71fb2a203bde388bdc12a7bbe9.boutiques",
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
    output_dataset: OutputPathType
    """Output dataset reconstructed from GroupInCorr data"""


def v_3d_extract_group_in_corr(
    group_in_corr_file: InputPathType,
    runner: Runner | None = None,
) -> V3dExtractGroupInCorrOutputs:
    """
    This program breaks the collection of images from a GroupInCorr file back into
    individual AFNI 3D+time datasets.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dExtractGroupInCorr.html
    
    Args:
        group_in_corr_file: GroupInCorr file to extract datasets from (e.g.\
            AAA.grpincorr.niml).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dExtractGroupInCorrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_EXTRACT_GROUP_IN_CORR_METADATA)
    cargs = []
    cargs.append("3dExtractGroupInCorr")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(group_in_corr_file))
    ret = V3dExtractGroupInCorrOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file("[PREFIX]_[DATASET_LABEL].nii"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dExtractGroupInCorrOutputs",
    "V_3D_EXTRACT_GROUP_IN_CORR_METADATA",
    "v_3d_extract_group_in_corr",
]