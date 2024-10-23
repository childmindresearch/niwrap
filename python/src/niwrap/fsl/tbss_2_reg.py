# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TBSS_2_REG_METADATA = Metadata(
    id="0ce3315d3d359109a44d514c5fab4de2a02ac9a0.boutiques",
    name="tbss_2_reg",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class Tbss2RegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tbss_2_reg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def tbss_2_reg(
    use_fmrib58_fa_1mm: bool = False,
    target_image: InputPathType | None = None,
    find_best_target: bool = False,
    runner: Runner | None = None,
) -> Tbss2RegOutputs:
    """
    TBSS utility for target selection and registration for Tract-Based Spatial
    Statistics (TBSS) analysis.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        use_fmrib58_fa_1mm: Use FMRIB58_FA_1mm as the target for nonlinear\
            registrations (recommended).
        target_image: Use the specified image as the target for nonlinear\
            registrations.
        find_best_target: Find the best target from all images in the FA.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Tbss2RegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TBSS_2_REG_METADATA)
    cargs = []
    cargs.append("tbss_2_reg")
    if use_fmrib58_fa_1mm:
        cargs.append("-T")
    if target_image is not None:
        cargs.extend([
            "-t",
            execution.input_file(target_image)
        ])
    if find_best_target:
        cargs.append("-n")
    ret = Tbss2RegOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TBSS_2_REG_METADATA",
    "Tbss2RegOutputs",
    "tbss_2_reg",
]
