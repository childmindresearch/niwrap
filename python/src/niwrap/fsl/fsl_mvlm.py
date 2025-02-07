# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSL_MVLM_METADATA = Metadata(
    id="90a5c14953576771eb514a02ee62df8dd4d9aa71.boutiques",
    name="fsl_mvlm",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FslMvlmParameters = typing.TypedDict('FslMvlmParameters', {
    "__STYX_TYPE__": typing.Literal["fsl_mvlm"],
    "input_file": InputPathType,
    "basename_output_files": str,
    "algorithm": typing.NotRequired[str | None],
    "design_matrix": typing.NotRequired[InputPathType | None],
    "mask_image": typing.NotRequired[InputPathType | None],
    "design_normalization": bool,
    "variance_normalisation": bool,
    "demean": bool,
    "nmf_dim": typing.NotRequired[float | None],
    "nmf_iterations": typing.NotRequired[float | None],
    "verbose": bool,
    "out_data": typing.NotRequired[str | None],
    "out_vnscales": typing.NotRequired[str | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "fsl_mvlm": fsl_mvlm_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "fsl_mvlm": fsl_mvlm_outputs,
    }.get(t)


class FslMvlmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_mvlm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Processed output file"""
    outdata: OutputPathType | None
    """Pre-processed data output file"""
    vnscales: OutputPathType | None
    """Variance normalisation scales file"""


def fsl_mvlm_params(
    input_file: InputPathType,
    basename_output_files: str,
    algorithm: str | None = None,
    design_matrix: InputPathType | None = None,
    mask_image: InputPathType | None = None,
    design_normalization: bool = False,
    variance_normalisation: bool = False,
    demean: bool = False,
    nmf_dim: float | None = None,
    nmf_iterations: float | None = None,
    verbose: bool = False,
    out_data: str | None = None,
    out_vnscales: str | None = None,
) -> FslMvlmParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input file (text matrix or 3D/4D image file).
        basename_output_files: Basename for output files.
        algorithm: Algorithm for decomposition: PCA (or SVD; default), PLS,\
            orthoPLS, CVA, SVD-CVA, MLM, NMF.
        design_matrix: File name of the GLM design matrix (time courses or\
            spatial maps).
        mask_image: Mask image file name if input is an image.
        design_normalization: Switch on normalisation of the design matrix\
            columns to unit standard deviation.
        variance_normalisation: Perform MELODIC variance-normalisation on data.
        demean: Switch on de-meaning of design and data.
        nmf_dim: Number of underlying factors for NMF.
        nmf_iterations: Number of NMF iterations (default 100).
        verbose: Switch on verbose output.
        out_data: Output file name for pre-processed data.
        out_vnscales: Output file name for scaling factors for variance\
            normalisation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fsl_mvlm",
        "input_file": input_file,
        "basename_output_files": basename_output_files,
        "design_normalization": design_normalization,
        "variance_normalisation": variance_normalisation,
        "demean": demean,
        "verbose": verbose,
    }
    if algorithm is not None:
        params["algorithm"] = algorithm
    if design_matrix is not None:
        params["design_matrix"] = design_matrix
    if mask_image is not None:
        params["mask_image"] = mask_image
    if nmf_dim is not None:
        params["nmf_dim"] = nmf_dim
    if nmf_iterations is not None:
        params["nmf_iterations"] = nmf_iterations
    if out_data is not None:
        params["out_data"] = out_data
    if out_vnscales is not None:
        params["out_vnscales"] = out_vnscales
    return params


def fsl_mvlm_cargs(
    params: FslMvlmParameters,
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
    cargs.append("fsl_mvlm")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_file"))
    ])
    cargs.extend([
        "-o",
        params.get("basename_output_files")
    ])
    if params.get("algorithm") is not None:
        cargs.extend([
            "-a",
            params.get("algorithm")
        ])
    if params.get("design_matrix") is not None:
        cargs.extend([
            "-d",
            execution.input_file(params.get("design_matrix"))
        ])
    if params.get("mask_image") is not None:
        cargs.extend([
            "-m",
            execution.input_file(params.get("mask_image"))
        ])
    if params.get("design_normalization"):
        cargs.append("--des_norm")
    if params.get("variance_normalisation"):
        cargs.append("--vn")
    if params.get("demean"):
        cargs.append("--demean")
    if params.get("nmf_dim") is not None:
        cargs.extend([
            "--nmf_dim",
            str(params.get("nmf_dim"))
        ])
    if params.get("nmf_iterations") is not None:
        cargs.extend([
            "--nmfitt",
            str(params.get("nmf_iterations"))
        ])
    if params.get("verbose"):
        cargs.append("-v")
    if params.get("out_data") is not None:
        cargs.extend([
            "--out_data",
            params.get("out_data")
        ])
    if params.get("out_vnscales") is not None:
        cargs.extend([
            "--out_vnscales",
            params.get("out_vnscales")
        ])
    return cargs


def fsl_mvlm_outputs(
    params: FslMvlmParameters,
    execution: Execution,
) -> FslMvlmOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslMvlmOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(params.get("basename_output_files") + "_out.nii.gz"),
        outdata=execution.output_file(params.get("out_data") + ".nii.gz") if (params.get("out_data") is not None) else None,
        vnscales=execution.output_file(params.get("out_vnscales") + ".txt") if (params.get("out_vnscales") is not None) else None,
    )
    return ret


def fsl_mvlm_execute(
    params: FslMvlmParameters,
    execution: Execution,
) -> FslMvlmOutputs:
    """
    Multivariate Linear Model regression on time courses and/or 3D/4D images using
    SVD (PCA), PLS, normalised PLS, CVA, SVD-CVA or MLM.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslMvlmOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fsl_mvlm_cargs(params, execution)
    ret = fsl_mvlm_outputs(params, execution)
    execution.run(cargs)
    return ret


def fsl_mvlm(
    input_file: InputPathType,
    basename_output_files: str,
    algorithm: str | None = None,
    design_matrix: InputPathType | None = None,
    mask_image: InputPathType | None = None,
    design_normalization: bool = False,
    variance_normalisation: bool = False,
    demean: bool = False,
    nmf_dim: float | None = None,
    nmf_iterations: float | None = None,
    verbose: bool = False,
    out_data: str | None = None,
    out_vnscales: str | None = None,
    runner: Runner | None = None,
) -> FslMvlmOutputs:
    """
    Multivariate Linear Model regression on time courses and/or 3D/4D images using
    SVD (PCA), PLS, normalised PLS, CVA, SVD-CVA or MLM.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Input file (text matrix or 3D/4D image file).
        basename_output_files: Basename for output files.
        algorithm: Algorithm for decomposition: PCA (or SVD; default), PLS,\
            orthoPLS, CVA, SVD-CVA, MLM, NMF.
        design_matrix: File name of the GLM design matrix (time courses or\
            spatial maps).
        mask_image: Mask image file name if input is an image.
        design_normalization: Switch on normalisation of the design matrix\
            columns to unit standard deviation.
        variance_normalisation: Perform MELODIC variance-normalisation on data.
        demean: Switch on de-meaning of design and data.
        nmf_dim: Number of underlying factors for NMF.
        nmf_iterations: Number of NMF iterations (default 100).
        verbose: Switch on verbose output.
        out_data: Output file name for pre-processed data.
        out_vnscales: Output file name for scaling factors for variance\
            normalisation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslMvlmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_MVLM_METADATA)
    params = fsl_mvlm_params(input_file=input_file, basename_output_files=basename_output_files, algorithm=algorithm, design_matrix=design_matrix, mask_image=mask_image, design_normalization=design_normalization, variance_normalisation=variance_normalisation, demean=demean, nmf_dim=nmf_dim, nmf_iterations=nmf_iterations, verbose=verbose, out_data=out_data, out_vnscales=out_vnscales)
    return fsl_mvlm_execute(params, execution)


__all__ = [
    "FSL_MVLM_METADATA",
    "FslMvlmOutputs",
    "FslMvlmParameters",
    "fsl_mvlm",
    "fsl_mvlm_params",
]
