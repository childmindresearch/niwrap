# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SVS_SEGMENT_METADATA = Metadata(
    id="1bfa7d5c70dcad5ba10e9a79957ecc2f9dcdea6c",
    name="svs_segment",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
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
    svs_segment by FSL Development Team.
    
    FSL Magnetic Resonance Spectroscopy tool to construct mask in T1 space of an
    SVS voxel and generate a tissue segmentation file.
    
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
    if (
        (t1_file is not None) +
        (anat_dir is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "t1_file,\n"
            "anat_dir"
        )
    execution = runner.start_execution(SVS_SEGMENT_METADATA)
    cargs = []
    cargs.append("svs_segment")
    cargs.append(execution.input_file(svs_file))
    if t1_file is not None:
        cargs.extend(["-t", execution.input_file(t1_file)])
    if anat_dir is not None:
        cargs.extend(["-a", anat_dir])
    if output_dir is not None:
        cargs.extend(["-o", output_dir])
    if filename_stem is not None:
        cargs.extend(["-f", filename_stem])
    if mask_only_flag:
        cargs.append("-m")
    if no_clean_flag:
        cargs.append("--no_clean")
    ret = SvsSegmentOutputs(
        root=execution.output_file("."),
        mask_file=execution.output_file(f"{output_dir}/{filename_stem}_mask.nii.gz", optional=True) if output_dir is not None and filename_stem is not None else None,
        segmentation_file=execution.output_file(f"{output_dir}/{filename_stem}_segmentation.json", optional=True) if output_dir is not None and filename_stem is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SVS_SEGMENT_METADATA",
    "SvsSegmentOutputs",
    "svs_segment",
]
