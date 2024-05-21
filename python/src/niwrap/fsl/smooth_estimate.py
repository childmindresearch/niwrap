# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


SMOOTH_ESTIMATE_METADATA = Metadata(
    id="9c582d4acc84adc255ff88503899d7c04ce755ac",
    name="SmoothEstimate",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SmoothEstimateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `smooth_estimate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    res_volume: OutputPathType | None
    """Residual fit image"""
    zstat_volume: OutputPathType | None
    """Zstat image"""


def smooth_estimate(
    mask_file: InputPathType,
    dof: int | None = None,
    residual_fit_file: InputPathType | None = None,
    zstat_file: InputPathType | None = None,
    runner: Runner = None,
) -> SmoothEstimateOutputs:
    """
    SmoothEstimate by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Estimates the smoothness of an image.
    
    Args:
        mask_file: Brain mask volume.
        dof: Number of degrees of freedom.
        residual_fit_file: Residual-fit image file.
        zstat_file: Zstat image file.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `SmoothEstimateOutputs`).
    """
    runner = runner or get_global_runner()
    if (
        (zstat_file is not None) +
        (dof is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "zstat_file,\n"
            "dof"
        )
    if not (
        (zstat_file is not None) or
        (dof is not None)
    ):
        raise ValueError(
            "One of the following arguments must be specified:\n"
            "- zstat_file\n"
            "- dof"
        )
    if not (
        (dof is not None) ==
        (residual_fit_file is not None)
    ):
        raise ValueError(
            "All or none of the following arguments must be specified:\n"
            "dof,\n"
            "residual_fit_file"
        )
    execution = runner.start_execution(SMOOTH_ESTIMATE_METADATA)
    cargs = []
    cargs.append("smoothest")
    if dof is not None:
        cargs.append(("--dof=" + str(dof)))
    cargs.append(("--mask=" + execution.input_file(mask_file)))
    if residual_fit_file is not None:
        cargs.append(("--res=" + execution.input_file(residual_fit_file)))
    if zstat_file is not None:
        cargs.append(("--zstat=" + execution.input_file(zstat_file)))
    ret = SmoothEstimateOutputs(
        root=execution.output_file("."),
        res_volume=execution.output_file(f"{pathlib.Path(residual_fit_file).stem}", optional=True) if residual_fit_file is not None else None,
        zstat_volume=execution.output_file(f"{pathlib.Path(zstat_file).stem}", optional=True) if zstat_file is not None else None,
    )
    execution.run(cargs)
    return ret
