# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_2DCAT_METADATA = Metadata(
    id="45473291ac5d44dcdcc4d0c691b40e4d4c4d28b3",
    name="2dcat",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V2dcatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_2dcat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image: OutputPathType | None
    """The main output image matrix file."""
    output_1_d: OutputPathType | None
    """A 1D file containing the average of RGB values, if the prefix ends with .1D."""


def v_2dcat(
    filenames: list[InputPathType],
    scale_image: InputPathType | None = None,
    scale_pixels: InputPathType | None = None,
    scale_intensity: bool = False,
    gscale: float | int | None = None,
    rgb_out: bool = False,
    res_in: list[float | int] | None = None,
    respad_in: list[float | int] | None = None,
    pad_val: float | int | None = None,
    crop: list[float | int] | None = None,
    autocrop_ctol: float | int | None = None,
    autocrop_atol: float | int | None = None,
    autocrop: bool = False,
    zero_wrap: bool = False,
    white_wrap: bool = False,
    gray_wrap: float | int | None = None,
    image_wrap: bool = False,
    rand_wrap: bool = False,
    prefix: str | None = None,
    matrix: list[float | int] | None = None,
    nx: float | int | None = None,
    ny: float | int | None = None,
    matrix_from_scale: bool = False,
    gap: float | int | None = None,
    gap_col: list[float | int] | None = None,
    runner: Runner | None = None,
) -> V2dcatOutputs:
    """
    2dcat by AFNI Team.
    
    Puts a set of images into an image matrix montage of NX by NY images.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/2dcat.html
    
    Args:
        filenames: List of input image files.
        scale_image: Multiply each image in the output image matrix by the\
            color or intensity of the pixel in the scale image.
        scale_pixels: Multiply each pixel in the output image by the color or\
            intensity of the pixel in the scale image. The scale image is resized\
            to the output image's resolution.
        scale_intensity: Use the intensity (average color) of the pixel instead\
            of its color.
        gscale: Apply additional scaling factor.
        rgb_out: Force output to be in RGB, even if input is bytes.
        res_in: Set resolution of all input images.
        respad_in: Resample to max while respecting the aspect ratio, then pad\
            to desired pixel count.
        pad_val: Set the padding value when using -respad_in. Should be in the\
            range [0, 255], default is 0.
        crop: Crop images by specified number of pixels from the left, right,\
            top, and bottom.
        autocrop_ctol: Automatically crop lines where RGB values differ by less\
            than the specified percentage from the corner pixel values.
        autocrop_atol: Automatically crop lines where RGB values differ by less\
            than the specified percentage from the line average.
        autocrop: Automatically crop lines with default tolerances using both\
            autocrop_atol and autocrop_ctol set to 20.
        zero_wrap: Use solid black images if not enough images are provided to\
            fill the matrix.
        white_wrap: Use solid white images if not enough images are provided to\
            fill the matrix.
        gray_wrap: Use solid gray images if not enough images are provided to\
            fill the matrix. The gray value must be between 0 and 1.0.
        image_wrap: Reuse images to fill the matrix. This is the default\
            behavior.
        rand_wrap: Randomize the order of images when reusing to fill the\
            matrix.
        prefix: Prefix the output file names with the specified string.
        matrix: Specify the number of images in each row (NX) and column (NY)\
            of the image matrix.
        nx: Specify the number of images in each row.
        ny: Specify the number of images in each column.
        matrix_from_scale: Set matrix dimensions NX and NY to be the same as\
            the SCALE_IMG's dimensions. Requires the -scale_image option.
        gap: Put a gap of specified pixels between images.
        gap_col: Set color of the gap line to specified R, G, B values. Values\
            range from 0 to 255.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V2dcatOutputs`).
    """
    runner = runner or get_global_runner()
    if res_in is not None and (len(res_in) != 2): 
        raise ValueError(f"Length of 'res_in' must be 2 but was {len(res_in)}")
    if respad_in is not None and (len(respad_in) != 2): 
        raise ValueError(f"Length of 'respad_in' must be 2 but was {len(respad_in)}")
    if pad_val is not None and not (0 <= pad_val <= 255): 
        raise ValueError(f"'pad_val' must be between 0 <= x <= 255 but was {pad_val}")
    if crop is not None and (len(crop) != 4): 
        raise ValueError(f"Length of 'crop' must be 4 but was {len(crop)}")
    if gray_wrap is not None and not (0 <= gray_wrap <= 1): 
        raise ValueError(f"'gray_wrap' must be between 0 <= x <= 1 but was {gray_wrap}")
    if matrix is not None and (len(matrix) != 2): 
        raise ValueError(f"Length of 'matrix' must be 2 but was {len(matrix)}")
    if gap_col is not None and (len(gap_col) != 3): 
        raise ValueError(f"Length of 'gap_col' must be 3 but was {len(gap_col)}")
    execution = runner.start_execution(V_2DCAT_METADATA)
    cargs = []
    cargs.append("2dcat")
    cargs.append("[OPTIONS]")
    cargs.extend([execution.input_file(f) for f in filenames])
    ret = V2dcatOutputs(
        root=execution.output_file("."),
        output_image=execution.output_file(f"{prefix}.ppm") if prefix is not None else None,
        output_1_d=execution.output_file(f"{prefix}.1D", optional=True) if prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V2dcatOutputs",
    "V_2DCAT_METADATA",
    "v_2dcat",
]
