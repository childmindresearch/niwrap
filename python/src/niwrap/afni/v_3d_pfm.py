# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_PFM_METADATA = Metadata(
    id="c5e5e30b454a1a81f02535de2e794be7d716492a.boutiques",
    name="3dPFM",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dPfmParameters = typing.TypedDict('V3dPfmParameters', {
    "__STYX_TYPE__": typing.Literal["3dPFM"],
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
        "3dPFM": v_3d_pfm_cargs,
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
        "3dPFM": v_3d_pfm_outputs,
    }.get(t)


class V3dPfmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_pfm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    beta: OutputPathType
    """Prefix for the neuronal-related (i.e. deconvolved) time series."""
    betafitts: OutputPathType
    """Prefix of the convolved neuronal-related time series."""
    fitts: OutputPathType
    """Prefix for the fitted time series."""
    resid: OutputPathType
    """Prefix for the residuals of the fit to the data."""
    mean: OutputPathType
    """Prefix for the intercept of the model."""
    lhsest: OutputPathType
    """Prefix for the estimates of the LHS parameters."""
    lhsfitts: OutputPathType
    """Prefix for the fitted time series of the LHS parameters."""
    lambda_: OutputPathType
    """Prefix for output volume with the regularization parameter of the
    deconvolution of each voxel."""
    costs: OutputPathType
    """Prefix for output volume of the cost function used to select the
    regularization parameter according to the selected criteria."""
    tstats_beta: OutputPathType
    """Prefix for the T-statistics of beta at each time point."""
    tdf_beta: OutputPathType
    """Prefix for degrees of freedom of the T-statistics of beta."""
    z_tstats_beta: OutputPathType
    """Prefix for (normalized) z-scores of the T-statistics of beta."""
    fstats_beta: OutputPathType
    """Prefix for the F-statistics of the deconvolved component."""
    fdf_beta: OutputPathType
    """Prefix for degrees of freedom of Fstats_beta."""
    z_fstats_beta: OutputPathType
    """Prefix for (normalized) z-scores of the Fstats_beta."""
    tstats_lhs: OutputPathType
    """Prefix for T-statistics of LHS regressors at each time point."""
    tdf_lhs: OutputPathType
    """Prefix for degrees of freedom of the Tstats_LHS."""
    z_tstats_lhs: OutputPathType
    """Prefix for (normalized) z-scores of the Tstats_LHS."""
    fstats_lhs: OutputPathType
    """Prefix for the F-statistics of the LHS regressors."""
    fdf_lhs: OutputPathType
    """Prefix for degrees of freedom of Fstats_LHS."""
    z_fstats_lhs: OutputPathType
    """Prefix for (normalized) z-scores of Fstats_LHS."""
    fstats_full: OutputPathType
    """Prefix for the F-statistics of the full model."""
    fdf_full: OutputPathType
    """Prefix for degrees of freedom of Fstats_full."""
    z_fstats_full: OutputPathType
    """Prefix for (normalized) z-scores of Fstats_full."""
    r2_full: OutputPathType
    """Prefix for R² (coefficient of determination) of the full model."""
    r2adj_full: OutputPathType
    """Prefix for Adjusted R² coefficient for the full model."""


def v_3d_pfm_params(
) -> V3dPfmParameters:
    """
    Build parameters.
    
    Args:
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dPFM",
    }
    return params


def v_3d_pfm_cargs(
    params: V3dPfmParameters,
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
    cargs.append("3dPFM")
    cargs.append("[PARAMETERS]")
    return cargs


def v_3d_pfm_outputs(
    params: V3dPfmParameters,
    execution: Execution,
) -> V3dPfmOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dPfmOutputs(
        root=execution.output_file("."),
        beta=execution.output_file("[BETA]"),
        betafitts=execution.output_file("[BETAFITTS]"),
        fitts=execution.output_file("[FITTS]"),
        resid=execution.output_file("[RESID]"),
        mean=execution.output_file("[MEAN]"),
        lhsest=execution.output_file("[LHSEST]"),
        lhsfitts=execution.output_file("[LHSFITTS]"),
        lambda_=execution.output_file("[LAMBDA]"),
        costs=execution.output_file("[COSTS]"),
        tstats_beta=execution.output_file("[TSTATS_BETA]"),
        tdf_beta=execution.output_file("[TDF_BETA]"),
        z_tstats_beta=execution.output_file("[Z_TSTATS_BETA]"),
        fstats_beta=execution.output_file("[FSTATS_BETA]"),
        fdf_beta=execution.output_file("[FDF_BETA]"),
        z_fstats_beta=execution.output_file("[Z_FSTATS_BETA]"),
        tstats_lhs=execution.output_file("[TSTATS_LHS]"),
        tdf_lhs=execution.output_file("[TDF_LHS]"),
        z_tstats_lhs=execution.output_file("[Z_TSTATS_LHS]"),
        fstats_lhs=execution.output_file("[FSTATS_LHS]"),
        fdf_lhs=execution.output_file("[FDF_LHS]"),
        z_fstats_lhs=execution.output_file("[Z_FSTATS_LHS]"),
        fstats_full=execution.output_file("[FSTATS_FULL]"),
        fdf_full=execution.output_file("[FDF_FULL]"),
        z_fstats_full=execution.output_file("[Z_FSTATS_FULL]"),
        r2_full=execution.output_file("[R2_FULL]"),
        r2adj_full=execution.output_file("[R2ADJ_FULL]"),
    )
    return ret


def v_3d_pfm_execute(
    params: V3dPfmParameters,
    execution: Execution,
) -> V3dPfmOutputs:
    """
    Program for identifying brief BOLD events in fMRI time series using Paradigm
    Free Mapping.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dPfmOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_pfm_cargs(params, execution)
    ret = v_3d_pfm_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_pfm(
    runner: Runner | None = None,
) -> V3dPfmOutputs:
    """
    Program for identifying brief BOLD events in fMRI time series using Paradigm
    Free Mapping.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dPfmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_PFM_METADATA)
    params = v_3d_pfm_params()
    return v_3d_pfm_execute(params, execution)


__all__ = [
    "V3dPfmOutputs",
    "V3dPfmParameters",
    "V_3D_PFM_METADATA",
    "v_3d_pfm",
    "v_3d_pfm_params",
]
