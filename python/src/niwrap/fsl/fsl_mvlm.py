# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSL_MVLM_METADATA = Metadata(
    id="1a8f691f76268ff455d3f6b68dcdfb98ad1cb04c.boutiques",
    name="fsl_mvlm",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


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
    out_data: InputPathType | None = None,
    out_vnscales: InputPathType | None = None,
    runner: Runner | None = None,
) -> FslMvlmOutputs:
    """
    Multivariate Linear Model regression on time courses and/or 3D/4D images using
    SVD (PCA), PLS, normalised PLS, CVA, SVD-CVA or MLM.
    
    Author: Christian F. Beckmann
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/
    
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
    cargs = []
    cargs.append("fsl_mvlm")
    cargs.append("-i")
    cargs.append(execution.input_file(input_file))
    cargs.append("-o")
    cargs.append(basename_output_files)
    if algorithm is not None:
        cargs.extend([
            "-a",
            algorithm
        ])
    if design_matrix is not None:
        cargs.extend([
            "-d",
            execution.input_file(design_matrix)
        ])
    if mask_image is not None:
        cargs.extend([
            "-m",
            execution.input_file(mask_image)
        ])
    if design_normalization:
        cargs.append("--des_norm")
    if variance_normalisation:
        cargs.append("--vn")
    if demean:
        cargs.append("--demean")
    if nmf_dim is not None:
        cargs.extend([
            "--nmf_dim",
            str(nmf_dim)
        ])
    if nmf_iterations is not None:
        cargs.extend([
            "--nmfitt",
            str(nmf_iterations)
        ])
    if verbose:
        cargs.append("-v")
    if out_data is not None:
        cargs.extend([
            "--out_data",
            execution.input_file(out_data)
        ])
    if out_vnscales is not None:
        cargs.extend([
            "--out_vnscales",
            execution.input_file(out_vnscales)
        ])
    ret = FslMvlmOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(basename_output_files + "_out.nii.gz"),
        outdata=execution.output_file(pathlib.Path(out_data).name + ".nii.gz") if (out_data is not None) else None,
        vnscales=execution.output_file(pathlib.Path(out_vnscales).name + ".txt") if (out_vnscales is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSL_MVLM_METADATA",
    "FslMvlmOutputs",
    "fsl_mvlm",
]