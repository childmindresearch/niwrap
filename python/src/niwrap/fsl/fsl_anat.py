# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSL_ANAT_METADATA = Metadata(
    id="27692d7019630686475148e4149b2dc6c57a40c6",
    name="fsl_anat",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class FslAnatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_anat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_anat_dir: OutputPathType | None
    """Output anatomical directory"""


def fsl_anat(
    structural_image: InputPathType | None = None,
    existing_anat_dir: str | None = None,
    output_dir: str | None = None,
    clobber_flag: bool = False,
    strongbias_flag: bool = False,
    weakbias_flag: bool = False,
    noreorient_flag: bool = False,
    nocrop_flag: bool = False,
    nobias_flag: bool = False,
    noreg_flag: bool = False,
    nononlinreg_flag: bool = False,
    noseg_flag: bool = False,
    nosubcortseg_flag: bool = False,
    bias_smoothing: float | int | None = None,
    image_type: str | None = None,
    nosearch_flag: bool = False,
    bet_f_param: float | int | None = None,
    nocleanup_flag: bool = False,
    runner: Runner | None = None,
) -> FslAnatOutputs:
    """
    fsl_anat by FMRIB Software Library (FSL) developers.
    
    A wrapper for FSL tools to process anatomical scans.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/fsl_anat
    
    Args:
        structural_image: Filename of input image (for one image only).
        existing_anat_dir: Directory name for existing .anat directory where\
            this script will be run in place.
        output_dir: Basename of directory for output (default is input image\
            basename followed by .anat).
        clobber_flag: If .anat directory exists (as specified by -o or default\
            from -i) then delete it and make a new one.
        strongbias_flag: Used for images with very strong bias fields.
        weakbias_flag: Used for images with smoother, more typical, bias fields\
            (default setting).
        noreorient_flag: Turn off step that does reorientation to standard\
            (fslreorient2std).
        nocrop_flag: Turn off step that does automated cropping (robustfov).
        nobias_flag: Turn off steps that do bias field correction (via FAST).
        noreg_flag: Turn off steps that do registration to standard (FLIRT and\
            FNIRT).
        nononlinreg_flag: Turn off step that does non-linear registration\
            (FNIRT).
        noseg_flag: Turn off step that does tissue-type segmentation (FAST).
        nosubcortseg_flag: Turn off step that does sub-cortical segmentation\
            (FIRST).
        bias_smoothing: Specify the value for bias field smoothing (the -l\
            option in FAST).
        image_type: Specify the type of image (choose one of T1 T2 PD - default\
            is T1).
        nosearch_flag: Specify that linear registration uses the -nosearch\
            option (FLIRT).
        bet_f_param: Specify f parameter for BET (only used if not running\
            non-linear reg and also wanting brain extraction done).
        nocleanup_flag: Do not remove intermediate files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslAnatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_ANAT_METADATA)
    cargs = []
    cargs.append("fsl_anat")
    cargs.append("[PARAMS]")
    cargs.append("-i")
    if structural_image is not None:
        cargs.extend(["-i", execution.input_file(structural_image)])
    cargs.append("-d")
    if existing_anat_dir is not None:
        cargs.extend(["-d", existing_anat_dir])
    ret = FslAnatOutputs(
        root=execution.output_file("."),
        output_anat_dir=execution.output_file(f"{output_dir}.anat", optional=True) if output_dir is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSL_ANAT_METADATA",
    "FslAnatOutputs",
    "fsl_anat",
]
