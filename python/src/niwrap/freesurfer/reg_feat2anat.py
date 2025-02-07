# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

REG_FEAT2ANAT_METADATA = Metadata(
    id="6d99523d12853983a4cb41cacabf4975bd54d655.boutiques",
    name="reg-feat2anat",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
RegFeat2anatParameters = typing.TypedDict('RegFeat2anatParameters', {
    "__STYX_TYPE__": typing.Literal["reg-feat2anat"],
    "feat_dir": str,
    "subject_id": str,
    "overwrite_exf2std": bool,
    "manual": bool,
    "manxfm_type": typing.NotRequired[str | None],
    "dof": typing.NotRequired[int | None],
    "bins": typing.NotRequired[int | None],
    "cost": typing.NotRequired[str | None],
    "max_angle": typing.NotRequired[float | None],
    "bet": bool,
    "title": typing.NotRequired[str | None],
    "no_bbr": bool,
    "spm": bool,
    "no_inorm": bool,
    "fmov": typing.NotRequired[str | None],
    "debug": bool,
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
        "reg-feat2anat": reg_feat2anat_cargs,
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
        "reg-feat2anat": reg_feat2anat_outputs,
    }.get(t)


class RegFeat2anatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `reg_feat2anat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    anat2std_register: OutputPathType
    """Init FS reg from anat to FSL-standard"""
    std2anat_fsl_mat: OutputPathType
    """Init FSL reg from FSL-standard to anat"""
    exf2anat_init_fsl_mat: OutputPathType
    """Init FSL reg from example_func to anat"""
    exf2anat_fsl_mat: OutputPathType
    """Final FSL reg from example_func to anat"""
    anat2exf_register: OutputPathType
    """Final FS reg from example_func to anat"""
    register_dat: OutputPathType
    """Same as anat2exf.register.dat"""
    example_func2standard_mat: OutputPathType
    """Replacement for feat-generated"""
    log_file: OutputPathType
    """Log file for registration"""


def reg_feat2anat_params(
    feat_dir: str,
    subject_id: str,
    overwrite_exf2std: bool = False,
    manual: bool = False,
    manxfm_type: str | None = None,
    dof: int | None = None,
    bins: int | None = None,
    cost: str | None = None,
    max_angle: float | None = None,
    bet: bool = False,
    title: str | None = None,
    no_bbr: bool = False,
    spm: bool = False,
    no_inorm: bool = False,
    fmov: str | None = None,
    debug: bool = False,
) -> RegFeat2anatParameters:
    """
    Build parameters.
    
    Args:
        feat_dir: Directory in which to find example_func.
        subject_id: FreeSurfer subject identifier as found in SUBJECTS_DIR.
        overwrite_exf2std: Replace Feat-generated example_func2standard.
        manual: Interactively view/edit registration.
        manxfm_type: Interactively view/edit registration for xfm type. xfmtype\
            can be: func2anat, std2anat, or func2std.
        dof: FLIRT degrees of freedom (default is 6).
        bins: FLIRT number of bins (default is 256).
        cost: FLIRT cost function (default is corratio).
        max_angle: FLIRT maximum search angle (default is 90).
        bet: Run betfunc on example_func (not with FSL 4.0).
        title: Title for tkregister window.
        no_bbr: Do not use boundary-based registration.
        spm: Use SPM instead of FLIRT, 6 dof only.
        no_inorm: Do not inorm when running tkregister2.
        fmov: fmov argument for tkregister2.
        debug: Turn on debugging.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "reg-feat2anat",
        "feat_dir": feat_dir,
        "subject_id": subject_id,
        "overwrite_exf2std": overwrite_exf2std,
        "manual": manual,
        "bet": bet,
        "no_bbr": no_bbr,
        "spm": spm,
        "no_inorm": no_inorm,
        "debug": debug,
    }
    if manxfm_type is not None:
        params["manxfm_type"] = manxfm_type
    if dof is not None:
        params["dof"] = dof
    if bins is not None:
        params["bins"] = bins
    if cost is not None:
        params["cost"] = cost
    if max_angle is not None:
        params["max_angle"] = max_angle
    if title is not None:
        params["title"] = title
    if fmov is not None:
        params["fmov"] = fmov
    return params


def reg_feat2anat_cargs(
    params: RegFeat2anatParameters,
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
    cargs.append("reg-feat2anat")
    cargs.extend([
        "--feat",
        params.get("feat_dir")
    ])
    cargs.extend([
        "--subject",
        params.get("subject_id")
    ])
    if params.get("overwrite_exf2std"):
        cargs.append("--overwrite-exf2std")
    if params.get("manual"):
        cargs.append("--manual")
    if params.get("manxfm_type") is not None:
        cargs.extend([
            "--manxfm",
            params.get("manxfm_type")
        ])
    if params.get("dof") is not None:
        cargs.extend([
            "--dof",
            str(params.get("dof"))
        ])
    if params.get("bins") is not None:
        cargs.extend([
            "--bins",
            str(params.get("bins"))
        ])
    if params.get("cost") is not None:
        cargs.extend([
            "--cost",
            params.get("cost")
        ])
    if params.get("max_angle") is not None:
        cargs.extend([
            "--maxangle",
            str(params.get("max_angle"))
        ])
    if params.get("bet"):
        cargs.append("--bet")
    if params.get("title") is not None:
        cargs.extend([
            "--title",
            params.get("title")
        ])
    if params.get("no_bbr"):
        cargs.append("--no-bbr")
    if params.get("spm"):
        cargs.append("--spm")
    if params.get("no_inorm"):
        cargs.append("--no-inorm")
    if params.get("fmov") is not None:
        cargs.extend([
            "--fmov",
            params.get("fmov")
        ])
    if params.get("debug"):
        cargs.append("--debug")
    return cargs


def reg_feat2anat_outputs(
    params: RegFeat2anatParameters,
    execution: Execution,
) -> RegFeat2anatOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RegFeat2anatOutputs(
        root=execution.output_file("."),
        anat2std_register=execution.output_file("featdir/reg/freesurfer/anat2std.register.dat"),
        std2anat_fsl_mat=execution.output_file("featdir/reg/freesurfer/std2anat.fsl.mat"),
        exf2anat_init_fsl_mat=execution.output_file("featdir/reg/freesurfer/exf2anat.init.fsl.mat"),
        exf2anat_fsl_mat=execution.output_file("featdir/reg/freesurfer/exf2anat.fsl.mat"),
        anat2exf_register=execution.output_file("featdir/reg/freesurfer/anat2exf.register.dat"),
        register_dat=execution.output_file("featdir/reg/freesurfer/register.dat"),
        example_func2standard_mat=execution.output_file("featdir/reg/freesurfer/example_func2standard.mat"),
        log_file=execution.output_file("reg/freesurfer/reg-feat2anat.log"),
    )
    return ret


def reg_feat2anat_execute(
    params: RegFeat2anatParameters,
    execution: Execution,
) -> RegFeat2anatOutputs:
    """
    Registers FSL-Feat example_func to FreeSurfer anatomical data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RegFeat2anatOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = reg_feat2anat_cargs(params, execution)
    ret = reg_feat2anat_outputs(params, execution)
    execution.run(cargs)
    return ret


def reg_feat2anat(
    feat_dir: str,
    subject_id: str,
    overwrite_exf2std: bool = False,
    manual: bool = False,
    manxfm_type: str | None = None,
    dof: int | None = None,
    bins: int | None = None,
    cost: str | None = None,
    max_angle: float | None = None,
    bet: bool = False,
    title: str | None = None,
    no_bbr: bool = False,
    spm: bool = False,
    no_inorm: bool = False,
    fmov: str | None = None,
    debug: bool = False,
    runner: Runner | None = None,
) -> RegFeat2anatOutputs:
    """
    Registers FSL-Feat example_func to FreeSurfer anatomical data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        feat_dir: Directory in which to find example_func.
        subject_id: FreeSurfer subject identifier as found in SUBJECTS_DIR.
        overwrite_exf2std: Replace Feat-generated example_func2standard.
        manual: Interactively view/edit registration.
        manxfm_type: Interactively view/edit registration for xfm type. xfmtype\
            can be: func2anat, std2anat, or func2std.
        dof: FLIRT degrees of freedom (default is 6).
        bins: FLIRT number of bins (default is 256).
        cost: FLIRT cost function (default is corratio).
        max_angle: FLIRT maximum search angle (default is 90).
        bet: Run betfunc on example_func (not with FSL 4.0).
        title: Title for tkregister window.
        no_bbr: Do not use boundary-based registration.
        spm: Use SPM instead of FLIRT, 6 dof only.
        no_inorm: Do not inorm when running tkregister2.
        fmov: fmov argument for tkregister2.
        debug: Turn on debugging.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RegFeat2anatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REG_FEAT2ANAT_METADATA)
    params = reg_feat2anat_params(feat_dir=feat_dir, subject_id=subject_id, overwrite_exf2std=overwrite_exf2std, manual=manual, manxfm_type=manxfm_type, dof=dof, bins=bins, cost=cost, max_angle=max_angle, bet=bet, title=title, no_bbr=no_bbr, spm=spm, no_inorm=no_inorm, fmov=fmov, debug=debug)
    return reg_feat2anat_execute(params, execution)


__all__ = [
    "REG_FEAT2ANAT_METADATA",
    "RegFeat2anatOutputs",
    "RegFeat2anatParameters",
    "reg_feat2anat",
    "reg_feat2anat_params",
]
