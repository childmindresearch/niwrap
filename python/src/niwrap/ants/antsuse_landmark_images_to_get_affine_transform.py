# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ANTSUSE_LANDMARK_IMAGES_TO_GET_AFFINE_TRANSFORM_METADATA = Metadata(
    id="de0a97ee512e7d859ed0be055747315b257fed2c.boutiques",
    name="ANTSUseLandmarkImagesToGetAffineTransform",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class AntsuseLandmarkImagesToGetAffineTransformOutputs(typing.NamedTuple):
    """
    Output object returned when calling `antsuse_landmark_images_to_get_affine_transform(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    affine_transform_matrix: OutputPathType
    """The output is the affine transformation matrix file."""


def antsuse_landmark_images_to_get_affine_transform(
    fixed_image: InputPathType,
    moving_image: InputPathType,
    transform_type: typing.Literal["rigid", "affine"],
    output_affine: str,
    runner: Runner | None = None,
) -> AntsuseLandmarkImagesToGetAffineTransformOutputs:
    """
    Advanced Normalization Tools (ANTs) is a C++ library available through the
    command line that computes high-dimensional mappings to capture the statistics
    of brain structure and function. It allows one to organize, visualize and
    statistically explore large biomedical image sets. Additionally, it integrates
    imaging modalities in space + time and works across species or organ systems
    with minimal customization.
    
    The ANTs library is considered a state-of-the-art medical image registration
    and segmentation toolkit which depends on the Insight ToolKit, a widely used
    medical image processing library to which ANTs developers contribute.
    ANTs-related tools have also won several international, unbiased
    competitions such as MICCAI, BRATS, and STACOM.
    
    Author: ANTs developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        fixed_image: The fixed image containing labeled landmarks (N-ary\
            image).
        moving_image: The moving image containing labeled landmarks (N-ary\
            image).
        transform_type: Type of transform to compute: 'rigid' or 'affine'.
        output_affine: The output file for the affine transform matrix (e.g.,\
            OutAffine.txt).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsuseLandmarkImagesToGetAffineTransformOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTSUSE_LANDMARK_IMAGES_TO_GET_AFFINE_TRANSFORM_METADATA)
    cargs = []
    cargs.append("ANTSUseLandmarkImagesToGetAffineTransform")
    cargs.append(execution.input_file(fixed_image))
    cargs.append(execution.input_file(moving_image))
    cargs.append(transform_type)
    cargs.append(output_affine)
    ret = AntsuseLandmarkImagesToGetAffineTransformOutputs(
        root=execution.output_file("."),
        affine_transform_matrix=execution.output_file(output_affine),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ANTSUSE_LANDMARK_IMAGES_TO_GET_AFFINE_TRANSFORM_METADATA",
    "AntsuseLandmarkImagesToGetAffineTransformOutputs",
    "antsuse_landmark_images_to_get_affine_transform",
]
