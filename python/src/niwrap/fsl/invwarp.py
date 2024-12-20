# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

INVWARP_METADATA = Metadata(
    id="e836370154f7a44a264fcff7fdc45d5150a0c0b2.boutiques",
    name="invwarp",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class InvwarpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `invwarp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    inverse_warp: OutputPathType
    """Name of output file, containing warps that are the "reverse" of those in
    --warp. this will be a field-file (rather than a file of spline
    coefficients), and it will have any affine component included as part of the
    displacements."""


def invwarp(
    warp: InputPathType,
    out_img: str,
    ref_img: InputPathType,
    absolute: bool = False,
    relative: bool = False,
    noconstraint: bool = False,
    jacobian_min: float | None = None,
    jacobian_max: float | None = None,
    debug: bool = False,
    runner: Runner | None = None,
) -> InvwarpOutputs:
    """
    
    Use FSL Invwarp to invert a FNIRT warp.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        warp: Filename for warp/shiftmap transform (volume).
        out_img: Filename for output (inverse warped) image.
        ref_img: Filename for new reference image.
        absolute: Use absolute warp convention (default): x' = w(x).
        relative: Use relative warp convention (default): x' = x + w(x).
        noconstraint: Do not apply jacobian constraint.
        jacobian_min: Minimum acceptable jacobian value for constraint (default\
            0.01).
        jacobian_max: Maximum acceptable jacobian value for constraint (default\
            100.0).
        debug: Turn on debugging output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `InvwarpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INVWARP_METADATA)
    cargs = []
    cargs.append("invwarp")
    cargs.append("--warp=" + execution.input_file(warp))
    cargs.append("--out=" + out_img)
    cargs.append("--ref=" + execution.input_file(ref_img))
    if absolute:
        cargs.append("--abs")
    if relative:
        cargs.append("--rel")
    if noconstraint:
        cargs.append("--noconstraint")
    if jacobian_min is not None:
        cargs.append("--jmin=" + str(jacobian_min))
    if jacobian_max is not None:
        cargs.append("--jmax=" + str(jacobian_max))
    if debug:
        cargs.append("--debug")
    ret = InvwarpOutputs(
        root=execution.output_file("."),
        inverse_warp=execution.output_file(out_img),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "INVWARP_METADATA",
    "InvwarpOutputs",
    "invwarp",
]
