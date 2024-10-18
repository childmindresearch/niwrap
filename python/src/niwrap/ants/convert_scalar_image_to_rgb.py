# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CONVERT_SCALAR_IMAGE_TO_RGB_METADATA = Metadata(
    id="8e941d90a298bf84b0c2980db9795b8ba8a4a1a6.boutiques",
    name="ConvertScalarImageToRGB",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class ConvertScalarImageToRgbOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_scalar_image_to_rgb(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_rgb_image: OutputPathType
    """The resulting RGB image after conversion."""


def convert_scalar_image_to_rgb(
    image_dimension: int,
    input_image: InputPathType,
    output_image: InputPathType,
    mask: InputPathType,
    colormap: typing.Literal["grey", "red", "green", "blue", "copper", "jet", "hsv", "spring", "summer", "autumn", "winter", "hot", "cool", "overunder", "custom"],
    custom_colormap_file: InputPathType | None = None,
    minimum_input: float | None = None,
    maximum_input: float | None = None,
    minimum_rgb_output: int | None = 0,
    maximum_rgb_output: int | None = 255,
    vtk_lookup_table: str | None = None,
    runner: Runner | None = None,
) -> ConvertScalarImageToRgbOutputs:
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
        image_dimension: The dimensionality of the image (e.g., 2D or 3D).
        input_image: The input scalar image to be converted to RGB.
        output_image: The output RGB image file.
        mask: The mask image to apply during conversion.
        colormap: The colormap to use for RGB conversion.
        custom_colormap_file: The file specifying the custom colormap (only\
            used if colormap is 'custom').
        minimum_input: The minimum input value for scaling.
        maximum_input: The maximum input value for scaling.
        minimum_rgb_output: The minimum output value for the RGB image.\
            Defaults to 0.
        maximum_rgb_output: The maximum output value for the RGB image.\
            Defaults to 255.
        vtk_lookup_table: The VTK lookup table to apply for additional\
            customization.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvertScalarImageToRgbOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERT_SCALAR_IMAGE_TO_RGB_METADATA)
    cargs = []
    cargs.append("ConvertScalarImageToRGB")
    cargs.append(str(image_dimension))
    cargs.append(execution.input_file(input_image))
    cargs.append(execution.input_file(output_image))
    cargs.append(execution.input_file(mask))
    cargs.append(colormap)
    if custom_colormap_file is not None:
        cargs.append(execution.input_file(custom_colormap_file))
    if minimum_input is not None:
        cargs.append(str(minimum_input))
    if maximum_input is not None:
        cargs.append(str(maximum_input))
    if minimum_rgb_output is not None:
        cargs.append(str(minimum_rgb_output))
    if maximum_rgb_output is not None:
        cargs.append(str(maximum_rgb_output))
    if vtk_lookup_table is not None:
        cargs.append(vtk_lookup_table)
    ret = ConvertScalarImageToRgbOutputs(
        root=execution.output_file("."),
        output_rgb_image=execution.output_file(pathlib.Path(output_image).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CONVERT_SCALAR_IMAGE_TO_RGB_METADATA",
    "ConvertScalarImageToRgbOutputs",
    "convert_scalar_image_to_rgb",
]
