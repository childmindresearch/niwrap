# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SIENA_METADATA = Metadata(
    id="fc70ce3730645b644f496627fd9f049857af6f8e",
    name="siena",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class SienaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `siena(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_report: OutputPathType | None
    """Siena analysis report"""
    ventricle_analysis_report: OutputPathType | None
    """Siena ventricle analysis report"""


def siena(
    input1: InputPathType,
    input2: InputPathType,
    output_dir: str | None = None,
    debug_flag: bool = False,
    bet_options: str | None = None,
    two_class_seg_flag: bool = False,
    t2_weighted_flag: bool = False,
    standard_space_mask_flag: bool = False,
    upper_ignore: float | int | None = None,
    lower_ignore: float | int | None = None,
    sienadiff_options: str | None = None,
    ventricle_analysis_flag: bool = False,
    ventricle_mask: InputPathType | None = None,
    runner: Runner | None = None,
) -> SienaOutputs:
    """
    siena by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Structural Image Evaluation, using Normalization, of Atrophy tool for
    evaluating brain atrophy between two timepoints.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/SIENA
    
    Args:
        input1: First input image (e.g. timepoint 1 image, img1.nii.gz).
        input2: Second input image (e.g. timepoint 2 image, img2.nii.gz).
        output_dir: Set output directory (default output is\
            <input1>_to_<input2>_siena).
        debug_flag: Debug (don't delete intermediate files).
        bet_options: Options to pass to BET brain extraction (inside\
            double-quotes), e.g. -B "-f 0.3".
        two_class_seg_flag: Two-class segmentation (don't segment grey and\
            white matter separately).
        t2_weighted_flag: T2-weighted input image (default T1-weighted).
        standard_space_mask_flag: Use standard-space masking as well as BET.
        upper_ignore: Ignore from t (mm) upwards in MNI152/Talairach space.
        lower_ignore: Ignore from b (mm) downwards in MNI152/Talairach space (b\
            should probably be negative).
        sienadiff_options: Options to pass to siena_diff timepoint differencing\
            (inside double-quotes), e.g. -S "-s -i 20".
        ventricle_analysis_flag: Run ventricle analysis (VIENA).
        ventricle_mask: Optional user-supplied ventricle mask (default is\
            /usr/local/fsl/data/standard/MNI152_T1_2mm_VentricleMask).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SienaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SIENA_METADATA)
    cargs = []
    cargs.append("siena")
    cargs.append(execution.input_file(input1))
    cargs.append(execution.input_file(input2))
    if output_dir is not None:
        cargs.extend(["-o", output_dir])
    if debug_flag:
        cargs.append("-d")
    if bet_options is not None:
        cargs.extend(["-B", bet_options])
    if two_class_seg_flag:
        cargs.append("-2")
    if t2_weighted_flag:
        cargs.append("-t2")
    if standard_space_mask_flag:
        cargs.append("-m")
    if upper_ignore is not None:
        cargs.extend(["-t", str(upper_ignore)])
    if lower_ignore is not None:
        cargs.extend(["-b", str(lower_ignore)])
    if sienadiff_options is not None:
        cargs.extend(["-S", sienadiff_options])
    if ventricle_analysis_flag:
        cargs.append("-V")
    if ventricle_mask is not None:
        cargs.extend(["-v", execution.input_file(ventricle_mask)])
    ret = SienaOutputs(
        root=execution.output_file("."),
        output_report=execution.output_file(f"{output_dir}/report.html") if output_dir is not None else None,
        ventricle_analysis_report=execution.output_file(f"{output_dir}/report_vent.html", optional=True) if output_dir is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SIENA_METADATA",
    "SienaOutputs",
    "siena",
]
