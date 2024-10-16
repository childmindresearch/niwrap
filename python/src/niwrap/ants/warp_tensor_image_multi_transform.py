# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

WARP_TENSOR_IMAGE_MULTI_TRANSFORM_METADATA = Metadata(
    id="ddb6d9ec5d1dad31783e356ecb28a5db5ab8874d.boutiques",
    name="WarpTensorImageMultiTransform",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class WarpTensorImageMultiTransformOutputs(typing.NamedTuple):
    """
    Output object returned when calling `warp_tensor_image_multi_transform(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_file: OutputPathType
    """The resultant transformed output image."""


def warp_tensor_image_multi_transform(
    image_dimension: int,
    moving_image: InputPathType,
    output_image: str,
    transforms: list[str],
    reference_image: InputPathType | None = None,
    tightest_bounding_box: bool = False,
    reslice_by_header: bool = False,
    use_nearest_neighbor: bool = False,
    runner: Runner | None = None,
) -> WarpTensorImageMultiTransformOutputs:
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
        image_dimension: Dimensionality of the image (e.g., 2D or 3D).
        moving_image: The moving image that will be transformed.
        output_image: Path for saving the transformed output image.
        transforms: List of transformations to apply, which can include\
            deformation fields or affine transforms.
        reference_image: Reference image for reslicing or defining the\
            transformation domain.
        tightest_bounding_box: Compute the tightest bounding box using all\
            affine transformations.
        reslice_by_header: Use the orientation matrix and origin encoded in the\
            image file header for reslicing.
        use_nearest_neighbor: Use Nearest Neighbor Interpolator for the\
            transformation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `WarpTensorImageMultiTransformOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(WARP_TENSOR_IMAGE_MULTI_TRANSFORM_METADATA)
    cargs = []
    cargs.append("WarpImageMultiTransform")
    cargs.append(str(image_dimension))
    cargs.append(execution.input_file(moving_image))
    cargs.append(output_image)
    if reference_image is not None:
        cargs.extend([
            "-R",
            execution.input_file(reference_image)
        ])
    if tightest_bounding_box:
        cargs.append("--tightest-bounding-box")
    if reslice_by_header:
        cargs.append("--reslice-by-header")
    if use_nearest_neighbor:
        cargs.append("--use-NN")
    cargs.extend(transforms)
    ret = WarpTensorImageMultiTransformOutputs(
        root=execution.output_file("."),
        output_image_file=execution.output_file(output_image),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "WARP_TENSOR_IMAGE_MULTI_TRANSFORM_METADATA",
    "WarpTensorImageMultiTransformOutputs",
    "warp_tensor_image_multi_transform",
]
