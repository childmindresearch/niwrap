# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DT_RECON_METADATA = Metadata(
    id="2b8457b9d61edcd3ebcd8e361c6c29d3e697032b.boutiques",
    name="dt_recon",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
DtReconParameters = typing.TypedDict('DtReconParameters', {
    "__STYX_TYPE__": typing.Literal["dt_recon"],
    "input_volume": InputPathType,
    "bvals_bvecs": typing.NotRequired[str | None],
    "subject_id": str,
    "output_dir": str,
    "info_dump": typing.NotRequired[InputPathType | None],
    "ec_reference": typing.NotRequired[float | None],
    "no_ec_flag": bool,
    "no_reg_flag": bool,
    "register_file": typing.NotRequired[InputPathType | None],
    "no_tal_flag": bool,
    "subjects_dir": typing.NotRequired[str | None],
    "save_ec_residuals_flag": bool,
    "pca_analysis_flag": bool,
    "mask_prune_threshold": typing.NotRequired[float | None],
    "init_spm_flag": bool,
    "init_fsl_flag": bool,
    "debug_flag": bool,
    "version_flag": bool,
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
        "dt_recon": dt_recon_cargs,
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
        "dt_recon": dt_recon_outputs,
    }.get(t)


class DtReconOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dt_recon(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    dwi_nifti: OutputPathType
    """Converted input to NIFTI format."""
    dwi_eddy_corrected: OutputPathType
    """DWI after eddy-current correction."""
    tensor_map: OutputPathType
    """Tensor map."""
    fa_map: OutputPathType
    """Fractional anisotropy (FA) map."""
    fa_tal_map: OutputPathType
    """FA map in Talairach space."""
    register_file_output: OutputPathType
    """Registration file."""
    mask_file: OutputPathType
    """Mask file."""


def dt_recon_params(
    input_volume: InputPathType,
    subject_id: str,
    output_dir: str,
    bvals_bvecs: str | None = None,
    info_dump: InputPathType | None = None,
    ec_reference: float | None = None,
    no_ec_flag: bool = False,
    no_reg_flag: bool = False,
    register_file: InputPathType | None = None,
    no_tal_flag: bool = False,
    subjects_dir: str | None = None,
    save_ec_residuals_flag: bool = False,
    pca_analysis_flag: bool = False,
    mask_prune_threshold: float | None = None,
    init_spm_flag: bool = False,
    init_fsl_flag: bool = False,
    debug_flag: bool = False,
    version_flag: bool = False,
) -> DtReconParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Input volume (DWI data).
        subject_id: Subject ID.
        output_dir: Output directory.
        bvals_bvecs: B-values and B-vectors files.
        info_dump: Use info dump created by unpacksdcmdir or dcmunpack.
        ec_reference: Use specified time points as 0-based reference for eddy\
            current correction.
        no_ec_flag: Turn off eddy/motion correction.
        no_reg_flag: Do not register to subject or resample to talairach.
        register_file: Supply a register.lta file instead of registering.
        no_tal_flag: Do not resample FA to talairach space.
        subjects_dir: Specify subjects directory (default env SUBJECTS_DIR).
        save_ec_residuals_flag: Save residual error (dwires and eres).
        pca_analysis_flag: Run PCA/SVD analysis on eres (saves in pca-eres\
            dir).
        mask_prune_threshold: Set threshold for masking (default is FLT_MIN).
        init_spm_flag: Initialize BBR with SPM instead of coreg (requires\
            MATLAB).
        init_fsl_flag: Initialize BBR with FSL instead of coreg.
        debug_flag: Print out lots of info.
        version_flag: Print version of this script and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dt_recon",
        "input_volume": input_volume,
        "subject_id": subject_id,
        "output_dir": output_dir,
        "no_ec_flag": no_ec_flag,
        "no_reg_flag": no_reg_flag,
        "no_tal_flag": no_tal_flag,
        "save_ec_residuals_flag": save_ec_residuals_flag,
        "pca_analysis_flag": pca_analysis_flag,
        "init_spm_flag": init_spm_flag,
        "init_fsl_flag": init_fsl_flag,
        "debug_flag": debug_flag,
        "version_flag": version_flag,
    }
    if bvals_bvecs is not None:
        params["bvals_bvecs"] = bvals_bvecs
    if info_dump is not None:
        params["info_dump"] = info_dump
    if ec_reference is not None:
        params["ec_reference"] = ec_reference
    if register_file is not None:
        params["register_file"] = register_file
    if subjects_dir is not None:
        params["subjects_dir"] = subjects_dir
    if mask_prune_threshold is not None:
        params["mask_prune_threshold"] = mask_prune_threshold
    return params


def dt_recon_cargs(
    params: DtReconParameters,
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
    cargs.append("dt_recon")
    cargs.extend([
        "--i",
        execution.input_file(params.get("input_volume"))
    ])
    if params.get("bvals_bvecs") is not None:
        cargs.extend([
            "--b",
            params.get("bvals_bvecs")
        ])
    cargs.extend([
        "--s",
        params.get("subject_id")
    ])
    cargs.extend([
        "--o",
        params.get("output_dir")
    ])
    if params.get("info_dump") is not None:
        cargs.extend([
            "--info-dump",
            execution.input_file(params.get("info_dump"))
        ])
    if params.get("ec_reference") is not None:
        cargs.extend([
            "--ecref",
            str(params.get("ec_reference"))
        ])
    if params.get("no_ec_flag"):
        cargs.append("--no-ec")
    if params.get("no_reg_flag"):
        cargs.append("--no-reg")
    if params.get("register_file") is not None:
        cargs.extend([
            "--reg",
            execution.input_file(params.get("register_file"))
        ])
    if params.get("no_tal_flag"):
        cargs.append("--no-tal")
    if params.get("subjects_dir") is not None:
        cargs.extend([
            "--sd",
            params.get("subjects_dir")
        ])
    if params.get("save_ec_residuals_flag"):
        cargs.append("--eres-save")
    if params.get("pca_analysis_flag"):
        cargs.append("--pca")
    if params.get("mask_prune_threshold") is not None:
        cargs.extend([
            "--prune_thr",
            str(params.get("mask_prune_threshold"))
        ])
    if params.get("init_spm_flag"):
        cargs.append("--init-spm")
    if params.get("init_fsl_flag"):
        cargs.append("--init-fsl")
    if params.get("debug_flag"):
        cargs.append("--debug")
    if params.get("version_flag"):
        cargs.append("--version")
    return cargs


def dt_recon_outputs(
    params: DtReconParameters,
    execution: Execution,
) -> DtReconOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DtReconOutputs(
        root=execution.output_file("."),
        dwi_nifti=execution.output_file(params.get("output_dir") + "/dwi.nii.gz"),
        dwi_eddy_corrected=execution.output_file(params.get("output_dir") + "/dwi-ec.nii.gz"),
        tensor_map=execution.output_file(params.get("output_dir") + "/tensor.nii.gz"),
        fa_map=execution.output_file(params.get("output_dir") + "/fa.nii.gz"),
        fa_tal_map=execution.output_file(params.get("output_dir") + "/fa-tal.nii.gz"),
        register_file_output=execution.output_file(params.get("output_dir") + "/register.lta"),
        mask_file=execution.output_file(params.get("output_dir") + "/mask.nii.gz"),
    )
    return ret


def dt_recon_execute(
    params: DtReconParameters,
    execution: Execution,
) -> DtReconOutputs:
    """
    Performs DTI reconstruction from the raw DWI input files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DtReconOutputs`).
    """
    cargs = dt_recon_cargs(params, execution)
    ret = dt_recon_outputs(params, execution)
    execution.run(cargs)
    return ret


def dt_recon(
    input_volume: InputPathType,
    subject_id: str,
    output_dir: str,
    bvals_bvecs: str | None = None,
    info_dump: InputPathType | None = None,
    ec_reference: float | None = None,
    no_ec_flag: bool = False,
    no_reg_flag: bool = False,
    register_file: InputPathType | None = None,
    no_tal_flag: bool = False,
    subjects_dir: str | None = None,
    save_ec_residuals_flag: bool = False,
    pca_analysis_flag: bool = False,
    mask_prune_threshold: float | None = None,
    init_spm_flag: bool = False,
    init_fsl_flag: bool = False,
    debug_flag: bool = False,
    version_flag: bool = False,
    runner: Runner | None = None,
) -> DtReconOutputs:
    """
    Performs DTI reconstruction from the raw DWI input files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume (DWI data).
        subject_id: Subject ID.
        output_dir: Output directory.
        bvals_bvecs: B-values and B-vectors files.
        info_dump: Use info dump created by unpacksdcmdir or dcmunpack.
        ec_reference: Use specified time points as 0-based reference for eddy\
            current correction.
        no_ec_flag: Turn off eddy/motion correction.
        no_reg_flag: Do not register to subject or resample to talairach.
        register_file: Supply a register.lta file instead of registering.
        no_tal_flag: Do not resample FA to talairach space.
        subjects_dir: Specify subjects directory (default env SUBJECTS_DIR).
        save_ec_residuals_flag: Save residual error (dwires and eres).
        pca_analysis_flag: Run PCA/SVD analysis on eres (saves in pca-eres\
            dir).
        mask_prune_threshold: Set threshold for masking (default is FLT_MIN).
        init_spm_flag: Initialize BBR with SPM instead of coreg (requires\
            MATLAB).
        init_fsl_flag: Initialize BBR with FSL instead of coreg.
        debug_flag: Print out lots of info.
        version_flag: Print version of this script and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DtReconOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DT_RECON_METADATA)
    params = dt_recon_params(input_volume=input_volume, bvals_bvecs=bvals_bvecs, subject_id=subject_id, output_dir=output_dir, info_dump=info_dump, ec_reference=ec_reference, no_ec_flag=no_ec_flag, no_reg_flag=no_reg_flag, register_file=register_file, no_tal_flag=no_tal_flag, subjects_dir=subjects_dir, save_ec_residuals_flag=save_ec_residuals_flag, pca_analysis_flag=pca_analysis_flag, mask_prune_threshold=mask_prune_threshold, init_spm_flag=init_spm_flag, init_fsl_flag=init_fsl_flag, debug_flag=debug_flag, version_flag=version_flag)
    return dt_recon_execute(params, execution)


__all__ = [
    "DT_RECON_METADATA",
    "DtReconOutputs",
    "DtReconParameters",
    "dt_recon",
    "dt_recon_params",
]
