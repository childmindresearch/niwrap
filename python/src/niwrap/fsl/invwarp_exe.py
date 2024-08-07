# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

INVWARP_METADATA = Metadata(
    id="74ccdf190a6e0120380345464cc87a1b581be482",
    name="invwarp",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class InvwarpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `invwarp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_inverse_warped_image: OutputPathType
    """Output inverse warped image"""


def invwarp(
    warp_file: InputPathType,
    out_file: str,
    ref_file: InputPathType,
    rel_flag: bool = False,
    abs_flag: bool = False,
    niter: float | int | None = None,
    regularise: float | int | None = 1.0,
    initwarp: InputPathType | None = None,
    noconstraint: bool = False,
    jmin: float | int | None = 0.01,
    jmax: float | int | None = 100.0,
    debug_flag: bool = False,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> InvwarpOutputs:
    """
    invwarp by University of Oxford (Mark Jenkinson).
    
    Inverse warp image volume using FSL's invwarp tool.
    
    More information:
    https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FNIRT/UsersGuide#A--invwarp
    
    Args:
        warp_file: Filename for warp/shiftmap transform (volume).
        out_file: Filename for output (inverse warped) image.
        ref_file: Filename for new reference image, i.e., what was originally\
            the input image (determines inverse warpvol's FOV and pixdims).
        rel_flag: Use relative warp convention: x' = x + w(x).
        abs_flag: Use absolute warp convention (default): x' = w(x).
        niter: Number of gradient-descent iterations (default=10).
        regularise: Regularisation strength (default=1.0).
        initwarp: Filename for initial warp transform (volume).
        noconstraint: Do not apply the Jacobian constraint.
        jmin: Minimum acceptable Jacobian value for constraint (default 0.01).
        jmax: Maximum acceptable Jacobian value for constraint (default 100.0).
        debug_flag: Turn on debugging output.
        verbose_flag: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `InvwarpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INVWARP_METADATA)
    cargs = []
    cargs.append("invwarp")
    cargs.append("-w")
    cargs.extend(["-w", execution.input_file(warp_file)])
    cargs.append("-o")
    cargs.extend(["-o", out_file])
    cargs.append("-r")
    cargs.extend(["-r", execution.input_file(ref_file)])
    if rel_flag:
        cargs.append("--rel")
    if abs_flag:
        cargs.append("--abs")
    if niter is not None:
        cargs.extend(["-n", str(niter)])
    if regularise is not None:
        cargs.extend(["--regularise", str(regularise)])
    if initwarp is not None:
        cargs.extend(["--initwarp", execution.input_file(initwarp)])
    if noconstraint:
        cargs.append("--noconstraint")
    if jmin is not None:
        cargs.extend(["--jmin", str(jmin)])
    if jmax is not None:
        cargs.extend(["--jmax", str(jmax)])
    if debug_flag:
        cargs.append("--debug")
    if verbose_flag:
        cargs.append("-v")
    ret = InvwarpOutputs(
        root=execution.output_file("."),
        output_inverse_warped_image=execution.output_file(f"{out_file}.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "INVWARP_METADATA",
    "InvwarpOutputs",
    "invwarp",
]
