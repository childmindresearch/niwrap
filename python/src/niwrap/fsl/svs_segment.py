# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SVS_SEGMENT_METADATA = Metadata(
    id="e590cc39f615b59773ffb785497633baec0cde4c.boutiques",
    name="svs_segment",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class SvsSegmentOutputs(typing.NamedTuple):
    """
    Output object returned when calling `svs_segment(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    mask_file: OutputPathType | None
    """Generated mask file in T1 space"""
    segmentation_file: OutputPathType | None
    """Generated tissue segmentation file"""


def svs_segment(
    svs_file: InputPathType,
    t1_file: InputPathType | None = None,
    anat_dir: str | None = None,
    output_dir: str | None = None,
    filename_stem: str | None = None,
    mask_only_flag: bool = False,
    no_clean_flag: bool = False,
    runner: Runner | None = None,
) -> SvsSegmentOutputs:
    """
    FSL Magnetic Resonance Spectroscopy tool to construct mask in T1 space of an SVS
    voxel and generate a tissue segmentation file.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        svs_file: SVS nifti file.
        t1_file: T1 nifti file.
        anat_dir: fsl_anat output directory.
        output_dir: Output directory.
        filename_stem: File name stem. _mask.nii.gz or _segmentation.json will\
            be added.
        mask_only_flag: Only perform masking stage, do not run fsl_anat if only\
            T1 passed.
        no_clean_flag: Don't clean intermediate output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SvsSegmentOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SVS_SEGMENT_METADATA)
    cargs = []
    cargs.append("svs_segment")
    cargs.append(execution.input_file(svs_file))
    if t1_file is not None:
        cargs.extend([
            "-t",
            execution.input_file(t1_file)
        ])
    if anat_dir is not None:
        cargs.extend([
            "-a",
            anat_dir
        ])
    if output_dir is not None:
        cargs.extend([
            "-o",
            output_dir
        ])
    if filename_stem is not None:
        cargs.extend([
            "-f",
            filename_stem
        ])
    if mask_only_flag:
        cargs.append("-m")
    if no_clean_flag:
        cargs.append("--no_clean")
    ret = SvsSegmentOutputs(
        root=execution.output_file("."),
        mask_file=execution.output_file(output_dir + "/" + filename_stem + "_mask.nii.gz") if (output_dir is not None and filename_stem is not None) else None,
        segmentation_file=execution.output_file(output_dir + "/" + filename_stem + "_segmentation.json") if (output_dir is not None and filename_stem is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SVS_SEGMENT_METADATA",
    "SvsSegmentOutputs",
    "svs_segment",
]
