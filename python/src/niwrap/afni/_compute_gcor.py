# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

_COMPUTE_GCOR_METADATA = Metadata(
    id="9edffe7e6664387e6668dcb72018a59747de55e5",
    name="@compute_gcor",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class ComputeGcorOutputs(typing.NamedTuple):
    """
    Output object returned when calling `_compute_gcor(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    corr_vol_brik: OutputPathType | None
    """Output correlation volume BRIK file"""
    corr_vol_head: OutputPathType | None
    """Output correlation volume HEAD file"""


def _compute_gcor(
    input_: InputPathType,
    mask: InputPathType | None = None,
    corr_vol_prefix: str | None = None,
    initial_trs: float | int | None = None,
    no_demean: bool = False,
    save_tmp: bool = False,
    verbose: float | int | None = None,
    runner: Runner | None = None,
) -> ComputeGcorOutputs:
    """
    @compute_gcor by AFNI Team.
    
    Compute GCOR, the global correlation.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@compute_gcor.html
    
    Args:
        input_: Specify input dataset to compute the GCOR over.
        mask: Specify mask dataset, for restricting the computation.
        corr_vol_prefix: Specify prefix for correlation volume output.
        initial_trs: Specify number of initial TRs to ignore.
        no_demean: Do not demean as the first step.
        save_tmp: Save temporary files (do not remove at end).
        verbose: Set verbose level (0=quiet, 3=max).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ComputeGcorOutputs`).
    """
    runner = runner or get_global_runner()
    if verbose is not None and not (0 <= verbose <= 3): 
        raise ValueError(f"'verbose' must be between 0 <= x <= 3 but was {verbose}")
    execution = runner.start_execution(_COMPUTE_GCOR_METADATA)
    cargs = []
    cargs.append("@compute_gcor")
    cargs.append(execution.input_file(input_))
    if mask is not None:
        cargs.append(execution.input_file(mask))
    if corr_vol_prefix is not None:
        cargs.extend(["-corr_vol", corr_vol_prefix])
    if initial_trs is not None:
        cargs.extend(["-nfirst", str(initial_trs)])
    if no_demean:
        cargs.append("-no_demean")
    if save_tmp:
        cargs.append("-savetmp")
    if verbose is not None:
        cargs.extend(["-verb", str(verbose)])
    ret = ComputeGcorOutputs(
        root=execution.output_file("."),
        corr_vol_brik=execution.output_file(f"{corr_vol_prefix}+tlrc.BRIK", optional=True) if corr_vol_prefix is not None else None,
        corr_vol_head=execution.output_file(f"{corr_vol_prefix}+tlrc.HEAD", optional=True) if corr_vol_prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ComputeGcorOutputs",
    "_COMPUTE_GCOR_METADATA",
    "_compute_gcor",
]
