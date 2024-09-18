# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FABBER_DSC_METADATA = Metadata(
    id="f0e99d5d1d58cbb5fed7da548eb3a03fb5be1e2e.boutiques",
    name="fabber_dsc",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class FabberDscOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fabber_dsc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    paramnames_file: OutputPathType
    """Parameter names output file"""
    model_fit_file: OutputPathType
    """Model fit output file"""
    residuals_file: OutputPathType
    """Residuals output file"""
    model_extras_file: OutputPathType
    """Model extras output file"""
    mvn_file: OutputPathType
    """MVN distributions output file"""
    mean_file: OutputPathType
    """Parameter means output file"""
    std_file: OutputPathType
    """Parameter standard deviations output file"""
    var_file: OutputPathType
    """Parameter variances output file"""
    zstat_file: OutputPathType
    """Parameter Zstats output file"""
    noise_mean_file: OutputPathType
    """Noise means output file"""
    noise_std_file: OutputPathType
    """Noise standard deviations output file"""
    free_energy_file: OutputPathType
    """Free energy output file"""


def fabber_dsc(
    runner: Runner | None = None,
) -> FabberDscOutputs:
    """
    A flexible model fitting and Bayesian inference tool for fMRI data.
    
    Author: FMRIB, University of Oxford
    
    URL: https://fabber.readthedocs.io/
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FabberDscOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FABBER_DSC_METADATA)
    cargs = []
    cargs.append("fabber")
    cargs.append("[OPTIONS]")
    ret = FabberDscOutputs(
        root=execution.output_file("."),
        paramnames_file=execution.output_file("[OUTPUT]/paramnames.txt"),
        model_fit_file=execution.output_file("[OUTPUT]/model_fit.nii.gz"),
        residuals_file=execution.output_file("[OUTPUT]/residuals.nii.gz"),
        model_extras_file=execution.output_file("[OUTPUT]/model_extras.nii.gz"),
        mvn_file=execution.output_file("[OUTPUT]/mvn.nii.gz"),
        mean_file=execution.output_file("[OUTPUT]/mean.nii.gz"),
        std_file=execution.output_file("[OUTPUT]/std.nii.gz"),
        var_file=execution.output_file("[OUTPUT]/var.nii.gz"),
        zstat_file=execution.output_file("[OUTPUT]/zstat.nii.gz"),
        noise_mean_file=execution.output_file("[OUTPUT]/noise_mean.nii.gz"),
        noise_std_file=execution.output_file("[OUTPUT]/noise_std.nii.gz"),
        free_energy_file=execution.output_file("[OUTPUT]/free_energy.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FABBER_DSC_METADATA",
    "FabberDscOutputs",
    "fabber_dsc",
]