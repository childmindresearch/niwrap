# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FNIRTFILEUTILS_METADATA = Metadata(
    id="3602fcba77f3571ce6633e4b77bf43d5c917943e.boutiques",
    name="fnirtfileutils",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class FnirtfileutilsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fnirtfileutils(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_field_file: OutputPathType | None
    """Output field or coefficient volume"""
    jacobian_output_file: OutputPathType | None
    """Output jacobian determinant map volume"""
    jacobian_matrix_file: OutputPathType | None
    """Output full jacobian matrix 4D-map volume"""


def fnirtfileutils(
    input_coefs: InputPathType,
    ref_volume: InputPathType | None = None,
    out_field: str | None = None,
    output_format: str | None = "field",
    warp_res: float | None = None,
    knot_space: float | None = None,
    jacobian_output: str | None = None,
    jacobian_matrix_output: str | None = None,
    with_aff: bool = False,
    verbose_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> FnirtfileutilsOutputs:
    """
    FNIRT file utilities for FSL - Converts FNIRT warp field coefficients to other
    formats.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_coefs: Filename of input coefficient volume to be converted.
        ref_volume: Filename for reference volume.
        out_field: Filename for output field/coef volume - uses relative warp\
            convention.
        output_format: Output format [field, spline], default=field.
        warp_res: Warp resolution (mm), only relevant when --outformat=spline.
        knot_space: Knot-spacing (voxels), only relevant when\
            --outformat=spline.
        jacobian_output: Filename for output jacobian determinant map volume.
        jacobian_matrix_output: Filename for output full jacobian matrix 4D-map\
            volume.
        with_aff: If set, the affine transform is included in the\
            field/jacobian.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display this help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FnirtfileutilsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FNIRTFILEUTILS_METADATA)
    cargs = []
    cargs.append("fnirtfileutils")
    cargs.extend([
        "--in",
        execution.input_file(input_coefs)
    ])
    if ref_volume is not None:
        cargs.extend([
            "--ref",
            execution.input_file(ref_volume)
        ])
    if out_field is not None:
        cargs.extend([
            "--out",
            out_field
        ])
    if output_format is not None:
        cargs.extend([
            "--outformat",
            output_format
        ])
    if warp_res is not None:
        cargs.extend([
            "--warpres",
            str(warp_res)
        ])
    if knot_space is not None:
        cargs.extend([
            "--knotspace",
            str(knot_space)
        ])
    if jacobian_output is not None:
        cargs.extend([
            "--jac",
            jacobian_output
        ])
    if jacobian_matrix_output is not None:
        cargs.extend([
            "--matjac",
            jacobian_matrix_output
        ])
    if with_aff:
        cargs.append("--withaff")
    if verbose_flag:
        cargs.append("--verbose")
    if help_flag:
        cargs.append("--help")
    ret = FnirtfileutilsOutputs(
        root=execution.output_file("."),
        output_field_file=execution.output_file(out_field + ".nii.gz") if (out_field is not None) else None,
        jacobian_output_file=execution.output_file(jacobian_output + ".nii.gz") if (jacobian_output is not None) else None,
        jacobian_matrix_file=execution.output_file(jacobian_matrix_output + ".nii.gz") if (jacobian_matrix_output is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FNIRTFILEUTILS_METADATA",
    "FnirtfileutilsOutputs",
    "fnirtfileutils",
]
