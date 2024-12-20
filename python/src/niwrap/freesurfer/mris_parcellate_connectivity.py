# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_PARCELLATE_CONNECTIVITY_METADATA = Metadata(
    id="0c3b840a03cfbf5cf09f4768e47a63ba51235eb2.boutiques",
    name="mris_parcellate_connectivity",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisParcellateConnectivityOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_parcellate_connectivity(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    parcellation_output: OutputPathType
    """The resulting output parcellation."""


def mris_parcellate_connectivity(
    input_surface: InputPathType,
    input_correlations: InputPathType,
    output_parcellation: str,
    smooth_iterations: float | None = None,
    runner: Runner | None = None,
) -> MrisParcellateConnectivityOutputs:
    """
    A tool to parcellate brain connectivity using surface and correlation data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: Input surface file.
        input_correlations: Input correlations file.
        output_parcellation: Output parcellation file.
        smooth_iterations: Number of averaging iterations for smoothing\
            correlation matrix.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisParcellateConnectivityOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_PARCELLATE_CONNECTIVITY_METADATA)
    cargs = []
    cargs.append("mris_parcellate_connectivity")
    if smooth_iterations is not None:
        cargs.extend([
            "-n",
            str(smooth_iterations)
        ])
    cargs.append(execution.input_file(input_surface))
    cargs.append(execution.input_file(input_correlations))
    cargs.append(output_parcellation)
    ret = MrisParcellateConnectivityOutputs(
        root=execution.output_file("."),
        parcellation_output=execution.output_file(output_parcellation),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_PARCELLATE_CONNECTIVITY_METADATA",
    "MrisParcellateConnectivityOutputs",
    "mris_parcellate_connectivity",
]
