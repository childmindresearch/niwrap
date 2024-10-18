# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SMOOTH_IMAGE_METADATA = Metadata(
    id="ffbdb8454b819d5fc88d02867a000664d9cdaf13.boutiques",
    name="SmoothImage",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class SmoothImageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `smooth_image(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    smoothed_image: OutputPathType
    """The output smoothed image file."""


def smooth_image(
    image_dimension: int,
    image_ext: InputPathType,
    smoothing_sigma: str,
    out_image_ext: str,
    sigma_units: typing.Literal[0, 1] | None = None,
    median_filter: typing.Literal[0, 1] | None = None,
    runner: Runner | None = None,
) -> SmoothImageOutputs:
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
        image_dimension: Specifies the dimensionality of the image.
        image_ext: The input image file to be smoothed.
        smoothing_sigma: The sigma value for smoothing. A separate sigma may be\
            specified for each dimension, e.g., '1.5x1x2'.
        out_image_ext: The output smoothed image file.
        sigma_units: Determines if sigma is in spacing units (1) or not (0).\
            Default is 0.
        median_filter: Whether to use median filter. Default is 0. If using\
            median filter, sigma represents the radius in voxels.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SmoothImageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SMOOTH_IMAGE_METADATA)
    cargs = []
    cargs.append("SmoothImage")
    cargs.append(str(image_dimension))
    cargs.append(execution.input_file(image_ext))
    cargs.append(smoothing_sigma)
    cargs.append(out_image_ext)
    if sigma_units is not None:
        cargs.append(str(sigma_units))
    if median_filter is not None:
        cargs.append(str(median_filter))
    ret = SmoothImageOutputs(
        root=execution.output_file("."),
        smoothed_image=execution.output_file(out_image_ext),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SMOOTH_IMAGE_METADATA",
    "SmoothImageOutputs",
    "smooth_image",
]
