# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFACE_FDR_METADATA = Metadata(
    id="3e46b545665c1c069067fb7147d283fd43e9fa44.boutiques",
    name="surface_fdr",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class SurfaceFdrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_fdr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    pvals_vtk: OutputPathType
    """Output VTK file with corrected p-values"""
    fthresh_vtk: OutputPathType
    """Output VTK file with FDR thresholded values"""
    nifti_images: OutputPathType
    """Additional output NIFTI images"""


def surface_fdr(
    input_vtk: InputPathType,
    runner: Runner | None = None,
) -> SurfaceFdrOutputs:
    """
    Tool to calculate surface FDR correction for vertex analysis.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_vtk: Input VTK file from vertex analysis.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceFdrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_FDR_METADATA)
    cargs = []
    cargs.append("surface_fdr")
    cargs.append(execution.input_file(input_vtk))
    ret = SurfaceFdrOutputs(
        root=execution.output_file("."),
        pvals_vtk=execution.output_file(pathlib.Path(input_vtk).name + "_pvals.vtk"),
        fthresh_vtk=execution.output_file(pathlib.Path(input_vtk).name + "_Fthresh.vtk"),
        nifti_images=execution.output_file(pathlib.Path(input_vtk).name + "_*"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_FDR_METADATA",
    "SurfaceFdrOutputs",
    "surface_fdr",
]
