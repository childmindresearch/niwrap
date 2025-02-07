# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

GCA_APPLY_METADATA = Metadata(
    id="004863971f906d9a0b7892c9101381a0f012a5c2.boutiques",
    name="gca-apply",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
GcaApplyParameters = typing.TypedDict('GcaApplyParameters', {
    "__STYX_TYPE__": typing.Literal["gca-apply"],
    "gcafile": InputPathType,
    "subject": str,
    "nthreads": typing.NotRequired[float | None],
    "base": typing.NotRequired[str | None],
    "no_segstats": bool,
    "subjects_dir": typing.NotRequired[str | None],
    "dice_seg": typing.NotRequired[str | None],
    "dice_file": typing.NotRequired[str | None],
    "lta": typing.NotRequired[InputPathType | None],
    "norm": typing.NotRequired[InputPathType | None],
    "input_mgz": typing.NotRequired[InputPathType | None],
    "brainmask": typing.NotRequired[InputPathType | None],
    "output_dir": typing.NotRequired[str | None],
    "no_v6labopts": bool,
    "m3z_file": typing.NotRequired[InputPathType | None],
    "gca_rb_2016": bool,
    "force_update": bool,
    "gcareg_iters": typing.NotRequired[float | None],
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
        "gca-apply": gca_apply_cargs,
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
        "gca-apply": gca_apply_outputs,
    }.get(t)


class GcaApplyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `gca_apply(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_lta: OutputPathType | None
    """Output LTA file"""
    output_m3z: OutputPathType | None
    """Output M3Z file"""
    normalized_gca: OutputPathType | None
    """Normalized GCA base MGZ file"""
    segmented_gca: OutputPathType | None
    """Segmented GCA base MGZ file"""
    stats_output: OutputPathType | None
    """Statistical output file"""


def gca_apply_params(
    gcafile: InputPathType,
    subject: str,
    nthreads: float | None = None,
    base: str | None = None,
    no_segstats: bool = False,
    subjects_dir: str | None = None,
    dice_seg: str | None = None,
    dice_file: str | None = None,
    lta: InputPathType | None = None,
    norm: InputPathType | None = None,
    input_mgz: InputPathType | None = None,
    brainmask: InputPathType | None = None,
    output_dir: str | None = None,
    no_v6labopts: bool = False,
    m3z_file: InputPathType | None = None,
    gca_rb_2016: bool = False,
    force_update: bool = False,
    gcareg_iters: float | None = None,
) -> GcaApplyParameters:
    """
    Build parameters.
    
    Args:
        gcafile: GCA file.
        subject: Subject.
        nthreads: Number of OMP threads.
        base: Use gcabase for naming output files (default is basename gcafile).
        no_segstats: Do not compute segstats.
        subjects_dir: Subjects directory.
        dice_seg: Specify dice coefficient computation parameters.
        dice_file: Specify dice coefficient computation file.
        lta: Use SrcLTA instead of running mri_em_register.
        norm: Use SrcNorm instead of running mri_ca_normalize.
        input_mgz: Input file, default is nu.mgz.
        brainmask: Brainmask file, default is brainmask.mgz.
        output_dir: Output directory (default: SUBJECTS_DIR/subject).
        no_v6labopts: Do not include v6 command line options.
        m3z_file: M3Z file.
        gca_rb_2016: Use RB_all_2016-05-10.vc700.gca.
        force_update: Force recreation of a file even if it is younger than its\
            parents.
        gcareg_iters: Set to 1, only for testing.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "gca-apply",
        "gcafile": gcafile,
        "subject": subject,
        "no_segstats": no_segstats,
        "no_v6labopts": no_v6labopts,
        "gca_rb_2016": gca_rb_2016,
        "force_update": force_update,
    }
    if nthreads is not None:
        params["nthreads"] = nthreads
    if base is not None:
        params["base"] = base
    if subjects_dir is not None:
        params["subjects_dir"] = subjects_dir
    if dice_seg is not None:
        params["dice_seg"] = dice_seg
    if dice_file is not None:
        params["dice_file"] = dice_file
    if lta is not None:
        params["lta"] = lta
    if norm is not None:
        params["norm"] = norm
    if input_mgz is not None:
        params["input_mgz"] = input_mgz
    if brainmask is not None:
        params["brainmask"] = brainmask
    if output_dir is not None:
        params["output_dir"] = output_dir
    if m3z_file is not None:
        params["m3z_file"] = m3z_file
    if gcareg_iters is not None:
        params["gcareg_iters"] = gcareg_iters
    return params


def gca_apply_cargs(
    params: GcaApplyParameters,
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
    cargs.extend([
        "-apply",
        "gca" + execution.input_file(params.get("gcafile"))
    ])
    cargs.append(params.get("subject"))
    if params.get("nthreads") is not None:
        cargs.extend([
            "--nthreads",
            str(params.get("nthreads"))
        ])
    if params.get("base") is not None:
        cargs.extend([
            "--base",
            params.get("base")
        ])
    if params.get("no_segstats"):
        cargs.append("--no-segstats")
    if params.get("subjects_dir") is not None:
        cargs.extend([
            "--sd",
            params.get("subjects_dir")
        ])
    if params.get("dice_seg") is not None:
        cargs.extend([
            "--dice",
            params.get("dice_seg")
        ])
    if params.get("dice_file") is not None:
        cargs.append(params.get("dice_file"))
    if params.get("lta") is not None:
        cargs.extend([
            "--lta",
            execution.input_file(params.get("lta"))
        ])
    if params.get("norm") is not None:
        cargs.extend([
            "--norm",
            execution.input_file(params.get("norm"))
        ])
    if params.get("input_mgz") is not None:
        cargs.extend([
            "--input",
            execution.input_file(params.get("input_mgz"))
        ])
    if params.get("brainmask") is not None:
        cargs.extend([
            "--brainmask",
            execution.input_file(params.get("brainmask"))
        ])
    if params.get("output_dir") is not None:
        cargs.extend([
            "--o",
            params.get("output_dir")
        ])
    if params.get("no_v6labopts"):
        cargs.append("--no-v6labopts")
    if params.get("m3z_file") is not None:
        cargs.extend([
            "--m3z",
            execution.input_file(params.get("m3z_file"))
        ])
    if params.get("gca_rb_2016"):
        cargs.append("--gca-rb-2016")
    if params.get("force_update"):
        cargs.append("--force-update")
    if params.get("gcareg_iters") is not None:
        cargs.extend([
            "--gcareg-iters",
            str(params.get("gcareg_iters"))
        ])
    return cargs


def gca_apply_outputs(
    params: GcaApplyParameters,
    execution: Execution,
) -> GcaApplyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = GcaApplyOutputs(
        root=execution.output_file("."),
        output_lta=execution.output_file(params.get("base") + ".lta") if (params.get("base") is not None) else None,
        output_m3z=execution.output_file(params.get("base") + ".m3z") if (params.get("base") is not None) else None,
        normalized_gca=execution.output_file("norm." + params.get("base") + ".mgz") if (params.get("base") is not None) else None,
        segmented_gca=execution.output_file(params.get("base") + ".aseg.mgz") if (params.get("base") is not None) else None,
        stats_output=execution.output_file(params.get("base") + ".stats") if (params.get("base") is not None) else None,
    )
    return ret


def gca_apply_execute(
    params: GcaApplyParameters,
    execution: Execution,
) -> GcaApplyOutputs:
    """
    Applies a GCA, performing the steps of mri_em_register, mri_ca_normalize,
    mri_ca_register, and mri_ca_label. This script replicates the stages in
    recon-all without overwriting files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `GcaApplyOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = gca_apply_cargs(params, execution)
    ret = gca_apply_outputs(params, execution)
    execution.run(cargs)
    return ret


def gca_apply(
    gcafile: InputPathType,
    subject: str,
    nthreads: float | None = None,
    base: str | None = None,
    no_segstats: bool = False,
    subjects_dir: str | None = None,
    dice_seg: str | None = None,
    dice_file: str | None = None,
    lta: InputPathType | None = None,
    norm: InputPathType | None = None,
    input_mgz: InputPathType | None = None,
    brainmask: InputPathType | None = None,
    output_dir: str | None = None,
    no_v6labopts: bool = False,
    m3z_file: InputPathType | None = None,
    gca_rb_2016: bool = False,
    force_update: bool = False,
    gcareg_iters: float | None = None,
    runner: Runner | None = None,
) -> GcaApplyOutputs:
    """
    Applies a GCA, performing the steps of mri_em_register, mri_ca_normalize,
    mri_ca_register, and mri_ca_label. This script replicates the stages in
    recon-all without overwriting files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        gcafile: GCA file.
        subject: Subject.
        nthreads: Number of OMP threads.
        base: Use gcabase for naming output files (default is basename gcafile).
        no_segstats: Do not compute segstats.
        subjects_dir: Subjects directory.
        dice_seg: Specify dice coefficient computation parameters.
        dice_file: Specify dice coefficient computation file.
        lta: Use SrcLTA instead of running mri_em_register.
        norm: Use SrcNorm instead of running mri_ca_normalize.
        input_mgz: Input file, default is nu.mgz.
        brainmask: Brainmask file, default is brainmask.mgz.
        output_dir: Output directory (default: SUBJECTS_DIR/subject).
        no_v6labopts: Do not include v6 command line options.
        m3z_file: M3Z file.
        gca_rb_2016: Use RB_all_2016-05-10.vc700.gca.
        force_update: Force recreation of a file even if it is younger than its\
            parents.
        gcareg_iters: Set to 1, only for testing.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GcaApplyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GCA_APPLY_METADATA)
    params = gca_apply_params(gcafile=gcafile, subject=subject, nthreads=nthreads, base=base, no_segstats=no_segstats, subjects_dir=subjects_dir, dice_seg=dice_seg, dice_file=dice_file, lta=lta, norm=norm, input_mgz=input_mgz, brainmask=brainmask, output_dir=output_dir, no_v6labopts=no_v6labopts, m3z_file=m3z_file, gca_rb_2016=gca_rb_2016, force_update=force_update, gcareg_iters=gcareg_iters)
    return gca_apply_execute(params, execution)


__all__ = [
    "GCA_APPLY_METADATA",
    "GcaApplyOutputs",
    "GcaApplyParameters",
    "gca_apply",
    "gca_apply_params",
]
