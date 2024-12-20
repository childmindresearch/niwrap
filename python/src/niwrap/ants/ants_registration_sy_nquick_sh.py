# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ANTS_REGISTRATION_SY_NQUICK_SH_METADATA = Metadata(
    id="95f42ebdf9e80a10a0b738811253de777466a830.boutiques",
    name="antsRegistrationSyNQuick.sh",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class AntsRegistrationSyNquickShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_registration_sy_nquick_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_transform: OutputPathType
    """Affine transformation matrix resulting from registration."""
    output_warp: OutputPathType
    """Warp field resulting from the registration."""
    output_inverse_warp: OutputPathType
    """Inverse warp field resulting from the registration."""
    output_warped_image: OutputPathType
    """Warped moving image."""


def ants_registration_sy_nquick_sh(
    dimensionality: typing.Literal[2, 3],
    fixed_image: InputPathType,
    moving_image: InputPathType,
    output_prefix: str,
    transform_type: typing.Literal["s", "b"] | None = None,
    runner: Runner | None = None,
) -> AntsRegistrationSyNquickShOutputs:
    """
    A script to quickly compute a SyN-based registration between two images using
    ANTS.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        dimensionality: Dimensionality of the images (2 or 3).
        fixed_image: Fixed image to which the moving image is registered.
        moving_image: Moving image that is registered to the fixed image.
        output_prefix: Prefix for the output files.
        transform_type: Type of transform: 's' for SyN, 'b' for B-spline SyN.\
            Default is 's'.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsRegistrationSyNquickShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_REGISTRATION_SY_NQUICK_SH_METADATA)
    cargs = []
    cargs.append("antsRegistrationSyNQuick.sh")
    cargs.extend([
        "-d",
        str(dimensionality)
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
    if transform_type is not None:
        cargs.append(transform_type)
    ret = AntsRegistrationSyNquickShOutputs(
        root=execution.output_file("."),
        output_transform=execution.output_file(output_prefix + "0GenericAffine.mat"),
        output_warp=execution.output_file(output_prefix + "1Warp.nii.gz"),
        output_inverse_warp=execution.output_file(output_prefix + "1InverseWarp.nii.gz"),
        output_warped_image=execution.output_file(output_prefix + "Warped.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ANTS_REGISTRATION_SY_NQUICK_SH_METADATA",
    "AntsRegistrationSyNquickShOutputs",
    "ants_registration_sy_nquick_sh",
]
