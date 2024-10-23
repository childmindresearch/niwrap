# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SUSAN_METADATA = Metadata(
    id="5c24a3e57820a39fa19fc83a47baad8cc56427a3.boutiques",
    name="susan",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class SusanOutputs(typing.NamedTuple):
    """
    Output object returned when calling `susan(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    filtered_output: OutputPathType
    """Filtered output image file"""


def susan(
    input_file: InputPathType,
    brightness_threshold: float,
    spatial_size: float,
    dimensionality: float,
    use_median_filter: float,
    n_usans: float,
    output_file: str,
    usan1: InputPathType | None = None,
    brightness_threshold1: float | None = None,
    usan2: InputPathType | None = None,
    brightness_threshold2: float | None = None,
    runner: Runner | None = None,
) -> SusanOutputs:
    """
    Non-linear noise reduction filtering tool.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Input image file.
        brightness_threshold: Brightness threshold; should be greater than\
            noise level and less than contrast of edges to be preserved.
        spatial_size: Spatial size (sigma, i.e., half-width) of smoothing, in\
            mm.
        dimensionality: Dimensionality (2 or 3), for within-plane (2) or fully\
            3D (3) smoothing.
        use_median_filter: Use median filter for cases where single-point noise\
            is detected (0 or 1).
        n_usans: Determine if the smoothing area is found from secondary images\
            (0, 1 or 2).
        output_file: Output image file.
        usan1: First USAN image file.
        brightness_threshold1: Brightness threshold for first USAN image.
        usan2: Second USAN image file.
        brightness_threshold2: Brightness threshold for second USAN image.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SusanOutputs`).
    """
    if not (2 <= dimensionality <= 3): 
        raise ValueError(f"'dimensionality' must be between 2 <= x <= 3 but was {dimensionality}")
    if not (0 <= use_median_filter <= 1): 
        raise ValueError(f"'use_median_filter' must be between 0 <= x <= 1 but was {use_median_filter}")
    if not (0 <= n_usans <= 2): 
        raise ValueError(f"'n_usans' must be between 0 <= x <= 2 but was {n_usans}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(SUSAN_METADATA)
    cargs = []
    cargs.append("susan")
    cargs.append(execution.input_file(input_file))
    cargs.append(str(brightness_threshold))
    cargs.append(str(spatial_size))
    cargs.append(str(dimensionality))
    cargs.append(str(use_median_filter))
    cargs.append(str(n_usans))
    if usan1 is not None:
        cargs.append(execution.input_file(usan1))
    if brightness_threshold1 is not None:
        cargs.append(str(brightness_threshold1))
    if usan2 is not None:
        cargs.append(execution.input_file(usan2))
    if brightness_threshold2 is not None:
        cargs.append(str(brightness_threshold2))
    cargs.append(output_file)
    ret = SusanOutputs(
        root=execution.output_file("."),
        filtered_output=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SUSAN_METADATA",
    "SusanOutputs",
    "susan",
]
