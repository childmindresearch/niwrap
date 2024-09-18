# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ANTS_REGISTRATION_SYN_SH_METADATA = Metadata(
    id="2869670dcfe1ada190c1850a93d98fc5801188de.boutiques",
    name="ants_registration_syn_sh",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class AntsRegistrationSynShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_registration_syn_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    affine_transform: OutputPathType
    """Affine transformation matrix for registration"""
    inverse_warp: OutputPathType
    """Inverse warp field for registration"""
    forward_warp: OutputPathType
    """Forward warp field for registration"""


def ants_registration_syn_sh(
    image_dimension: typing.Literal[2, 3],
    fixed_image: InputPathType,
    moving_image: InputPathType,
    output_prefix: str,
    threads: int | None = None,
    initial_transform: list[str] | None = None,
    transform_type: typing.Literal["t", "r", "a", "s", "sr", "so", "b", "br", "bo"] | None = None,
    radius: int | None = None,
    spline_distance: int | None = None,
    gradient_step: float | None = None,
    masks: str | None = None,
    precision_type: typing.Literal["f", "d"] | None = None,
    use_histogram_matching: typing.Literal[0, 1] | None = None,
    use_repro_mode: typing.Literal[0, 1] | None = None,
    collapse_output_transforms: typing.Literal[0, 1] | None = None,
    random_seed: int | None = None,
    runner: Runner | None = None,
) -> AntsRegistrationSynShOutputs:
    """
    This script performs image registration using the SyN transform from the ANTs
    suite. The user can specify the dimensionality of the images, the fixed and
    moving images, and the output prefix. It supports various types of
    transformations and optional parameters such as initial transforms, gradient
    step size, mask usage, and more.
    
    Author: Brian B. Avants, Nick Tustison, and Gang Song
    
    URL: https://github.com/ANTsX/ANTs/
    
    Args:
        image_dimension: Image dimension: 2 or 3 (for 2 or 3-dimensional\
            registration of a single volume).
        fixed_image: Fixed image(s) or source image(s) or reference image(s).
        moving_image: Moving image(s) or target image(s).
        output_prefix: A prefix that is prepended to all output files.
        threads: Number of threads (default =\
            ITK_GLOBAL_DEFAULT_NUMBER_OF_THREADS if defined, otherwise 1).
        initial_transform: Initial transform(s) --- order specified on the\
            command line matters.
        transform_type: Transform type (default = 's'). Options:\
            - t: translation (1 stage)\
            - r: rigid (1 stage)\
            - a: rigid + affine (2 stages)\
            - s: rigid + affine + deformable syn (3 stages)\
            - sr: rigid + deformable syn (2 stages)\
            - so: deformable syn only (1 stage)\
            - b: rigid + affine + deformable b-spline syn (3 stages)\
            - br: rigid + deformable b-spline syn (2 stages)\
            - bo: deformable b-spline syn only (1 stage).
        radius: Radius for cross correlation metric used during SyN stage\
            (default = 4).
        spline_distance: Spline distance for deformable B-spline SyN transform\
            (default = 26).
        gradient_step: Gradient step size for SyN and B-spline SyN (default =\
            0.1).
        masks: Mask(s) for the fixed image space, or for the fixed and moving\
            image space in the format 'fixedMask,MovingMask'. Use -x once to\
            specify mask(s) to be used for all stages or use -x for each 'stage'\
            (cf -t option). If no mask is to be used for a particular stage, the\
            keyword 'NULL' should be used in place of file names.
        precision_type: Precision type (default = 'd'). Options:\
            - f: float\
            - d: double.
        use_histogram_matching: Use histogram matching (default = 0). Options:\
            - 0: false\
            - 1: true.
        use_repro_mode: Use 'repro' mode for exact reproducibility of output.\
            Uses GC metric for linear stages and a fixed random seed (default = 0).\
            Options:\
            - 0: false\
            - 1: true.
        collapse_output_transforms: Collapse output transforms (default = 1).\
            Options:\
            - 0: false\
            - 1: true.
        random_seed: Fix random seed to an int value.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsRegistrationSynShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_REGISTRATION_SYN_SH_METADATA)
    cargs = []
    cargs.append("antsRegistrationSyN.sh")
    cargs.extend([
        "-d",
        str(image_dimension)
    ])
    cargs.extend([
        "-f",
        execution.input_file(fixed_image)
    ])
    cargs.extend([
        "-m",
        execution.input_file(moving_image)
    ])
    cargs.extend([
        "-o",
        output_prefix
    ])
    if threads is not None:
        cargs.extend([
            "-n",
            str(threads)
        ])
    if initial_transform is not None:
        cargs.extend([
            "-i",
            *initial_transform
        ])
    if transform_type is not None:
        cargs.extend([
            "-t",
            transform_type
        ])
    if radius is not None:
        cargs.extend([
            "-r",
            str(radius)
        ])
    if spline_distance is not None:
        cargs.extend([
            "-s",
            str(spline_distance)
        ])
    if gradient_step is not None:
        cargs.extend([
            "-g",
            str(gradient_step)
        ])
    if masks is not None:
        cargs.extend([
            "-x",
            masks
        ])
    if precision_type is not None:
        cargs.extend([
            "-p",
            precision_type
        ])
    if use_histogram_matching is not None:
        cargs.extend([
            "-j",
            str(use_histogram_matching)
        ])
    if use_repro_mode is not None:
        cargs.extend([
            "-y",
            str(use_repro_mode)
        ])
    if collapse_output_transforms is not None:
        cargs.extend([
            "-z",
            str(collapse_output_transforms)
        ])
    if random_seed is not None:
        cargs.extend([
            "-e",
            str(random_seed)
        ])
    ret = AntsRegistrationSynShOutputs(
        root=execution.output_file("."),
        affine_transform=execution.output_file(output_prefix + "0GenericAffine.mat"),
        inverse_warp=execution.output_file(output_prefix + "1InverseWarp.nii.gz"),
        forward_warp=execution.output_file(output_prefix + "1Warp.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ANTS_REGISTRATION_SYN_SH_METADATA",
    "AntsRegistrationSynShOutputs",
    "ants_registration_syn_sh",
]
