# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFACE_FDR_METADATA = Metadata(
    id="94b53ea7d88621220b891d96dc62c9924e143dac.boutiques",
    name="surface_fdr",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
SurfaceFdrParameters = typing.TypedDict('SurfaceFdrParameters', {
    "__STYX_TYPE__": typing.Literal["surface_fdr"],
    "input_vtk": InputPathType,
})


def dyn_cargs(
    t: str,
) -> None:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    vt = {
        "surface_fdr": surface_fdr_cargs,
    }
    return vt.get(t)


def dyn_outputs(
    t: str,
) -> None:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    vt = {
        "surface_fdr": surface_fdr_outputs,
    }
    return vt.get(t)


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


def surface_fdr_params(
    input_vtk: InputPathType,
) -> SurfaceFdrParameters:
    """
    Build parameters.
    
    Args:
        input_vtk: Input VTK file from vertex analysis.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surface_fdr",
        "input_vtk": input_vtk,
    }
    return params


def surface_fdr_cargs(
    params: SurfaceFdrParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("surface_fdr")
    cargs.append(execution.input_file(params.get("input_vtk")))
    return cargs


def surface_fdr_outputs(
    params: SurfaceFdrParameters,
    execution: Execution,
) -> SurfaceFdrOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfaceFdrOutputs(
        root=execution.output_file("."),
        pvals_vtk=execution.output_file(pathlib.Path(params.get("input_vtk")).name + "_pvals.vtk"),
        fthresh_vtk=execution.output_file(pathlib.Path(params.get("input_vtk")).name + "_Fthresh.vtk"),
        nifti_images=execution.output_file(pathlib.Path(params.get("input_vtk")).name + "_*"),
    )
    return ret


def surface_fdr_execute(
    params: SurfaceFdrParameters,
    execution: Execution,
) -> SurfaceFdrOutputs:
    """
    Tool to calculate surface FDR correction for vertex analysis.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfaceFdrOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = surface_fdr_cargs(params, execution)
    ret = surface_fdr_outputs(params, execution)
    execution.run(cargs)
    return ret


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
    params = surface_fdr_params(input_vtk=input_vtk)
    return surface_fdr_execute(params, execution)


__all__ = [
    "SURFACE_FDR_METADATA",
    "SurfaceFdrOutputs",
    "SurfaceFdrParameters",
    "surface_fdr",
    "surface_fdr_params",
]
