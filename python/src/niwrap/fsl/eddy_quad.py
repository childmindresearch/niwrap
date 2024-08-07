# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

EDDY_QUAD_METADATA = Metadata(
    id="58178ebe94bc2a426dfb0d388e3e49a548b9ad4f",
    name="eddy_quad",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class EddyQuadOutputs(typing.NamedTuple):
    """
    Output object returned when calling `eddy_quad(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dir_qc: OutputPathType | None
    """Quality control data outputs"""


def eddy_quad(
    eddy_base: str,
    eddy_index: InputPathType,
    eddy_params: InputPathType,
    mask: InputPathType,
    bvals: InputPathType,
    bvecs: InputPathType | None = None,
    output_dir: str | None = None,
    field: InputPathType | None = None,
    slspec: InputPathType | None = None,
    verbose: bool = False,
    runner: Runner | None = None,
) -> EddyQuadOutputs:
    """
    eddy_quad by FMRIB Software Library.
    
    QUality Assessment for DMRI.
    
    Args:
        eddy_base: Basename (including path) specified when running EDDY.
        eddy_index: File containing indices for all volumes into acquisition\
            parameters.
        eddy_params: File containing acquisition parameters.
        mask: Binary mask file.
        bvals: b-values file.
        bvecs: b-vectors file - only used when <eddyBase>.eddy_residuals file\
            is present.
        output_dir: Output directory - default = '<eddyBase>.qc'.
        field: TOPUP estimated field (in Hz).
        slspec: Text file specifying slice/group acquisition.
        verbose: Display debug messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `EddyQuadOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(EDDY_QUAD_METADATA)
    cargs = []
    cargs.append("eddy_quad")
    cargs.append(eddy_base)
    cargs.append("--eddyIdx")
    cargs.extend(["--eddyIdx", execution.input_file(eddy_index)])
    cargs.append("--eddyParams")
    cargs.extend(["--eddyParams", execution.input_file(eddy_params)])
    cargs.append("--mask")
    cargs.extend(["--mask", execution.input_file(mask)])
    cargs.append("--bvals")
    cargs.extend(["--bvals", execution.input_file(bvals)])
    cargs.append("[OPTIONS]")
    ret = EddyQuadOutputs(
        root=execution.output_file("."),
        output_dir_qc=execution.output_file(f"{output_dir}", optional=True) if output_dir is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "EDDY_QUAD_METADATA",
    "EddyQuadOutputs",
    "eddy_quad",
]
