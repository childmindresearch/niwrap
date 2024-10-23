# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SMOOTHEST_METADATA = Metadata(
    id="8a52d129fe6572d8cbd3f308586aad4af9b0a620.boutiques",
    name="smoothest",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class SmoothestOutputs(typing.NamedTuple):
    """
    Output object returned when calling `smoothest(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def smoothest(
    mask: InputPathType,
    dof: float | None = None,
    residual_fit_image: InputPathType | None = None,
    zstat_image: InputPathType | None = None,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> SmoothestOutputs:
    """
    Tool to estimate smoothness of data from FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        mask: Brain mask volume.
        dof: Number of degrees of freedom.
        residual_fit_image: Filename of `residual-fit` image (use -d).
        zstat_image: Filename of zstat image (not with -d).
        verbose_flag: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SmoothestOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SMOOTHEST_METADATA)
    cargs = []
    cargs.append("smoothest")
    if dof is not None:
        cargs.extend([
            "-d",
            str(dof)
        ])
    if residual_fit_image is not None:
        cargs.extend([
            "-r",
            execution.input_file(residual_fit_image)
        ])
    if zstat_image is not None:
        cargs.extend([
            "-z",
            execution.input_file(zstat_image)
        ])
    cargs.extend([
        "-m",
        execution.input_file(mask)
    ])
    if verbose_flag:
        cargs.append("-V")
    ret = SmoothestOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SMOOTHEST_METADATA",
    "SmoothestOutputs",
    "smoothest",
]
