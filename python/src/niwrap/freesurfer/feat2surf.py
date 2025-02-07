# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FEAT2SURF_METADATA = Metadata(
    id="40f6609e9dff7742a78a92c30e97a51a671a1ed7.boutiques",
    name="feat2surf",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
Feat2surfParameters = typing.TypedDict('Feat2surfParameters', {
    "__STYX_TYPE__": typing.Literal["feat2surf"],
    "feat_dirs": list[str],
    "feat_dirfile": typing.NotRequired[InputPathType | None],
    "proj_frac": typing.NotRequired[float | None],
    "hemi": typing.NotRequired[str | None],
    "target": typing.NotRequired[str | None],
    "surf": typing.NotRequired[str | None],
    "cope_only": bool,
    "debug_flag": bool,
    "nolog_flag": bool,
    "out_dir": typing.NotRequired[str | None],
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
        "feat2surf": feat2surf_cargs,
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
        "feat2surf": feat2surf_outputs,
    }.get(t)


class Feat2surfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `feat2surf(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    lh_output: OutputPathType | None
    """Output statistics on the left hemisphere for the subject"""
    rh_output: OutputPathType | None
    """Output statistics on the right hemisphere for the subject"""
    lh_target_output: OutputPathType | None
    """Output statistics on the left hemisphere for the target subject"""
    rh_target_output: OutputPathType | None
    """Output statistics on the right hemisphere for the target subject"""


def feat2surf_params(
    feat_dirs: list[str],
    feat_dirfile: InputPathType | None = None,
    proj_frac: float | None = None,
    hemi: str | None = None,
    target: str | None = None,
    surf: str | None = None,
    cope_only: bool = False,
    debug_flag: bool = False,
    nolog_flag: bool = False,
    out_dir: str | None = None,
) -> Feat2surfParameters:
    """
    Build parameters.
    
    Args:
        feat_dirs: Directory where Feat results are stored. Can specify\
            multiple directories.
        feat_dirfile: File with a list of Feat directories.
        proj_frac: Sample functional a fraction of the cortical thickness\
            normal to the surface. Default is 0.
        hemi: Run on specified hemisphere (lh or rh) only. Default is both\
            hemispheres.
        target: Subject used to define common surface space. Default is\
            fsaverage.
        surf: Surface to resample to. Default is white.
        cope_only: Only map the copes and varcopes to the common surface space.
        debug_flag: Turn on debugging.
        nolog_flag: Do not create a log file.
        out_dir: Output directory to use instead of default\
            feat/reg_surf-?h/stats.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "feat2surf",
        "feat_dirs": feat_dirs,
        "cope_only": cope_only,
        "debug_flag": debug_flag,
        "nolog_flag": nolog_flag,
    }
    if feat_dirfile is not None:
        params["feat_dirfile"] = feat_dirfile
    if proj_frac is not None:
        params["proj_frac"] = proj_frac
    if hemi is not None:
        params["hemi"] = hemi
    if target is not None:
        params["target"] = target
    if surf is not None:
        params["surf"] = surf
    if out_dir is not None:
        params["out_dir"] = out_dir
    return params


def feat2surf_cargs(
    params: Feat2surfParameters,
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
    cargs.append("feat2surf")
    cargs.extend([
        "--feat",
        *params.get("feat_dirs")
    ])
    if params.get("feat_dirfile") is not None:
        cargs.extend([
            "--featdirfile",
            execution.input_file(params.get("feat_dirfile"))
        ])
    if params.get("proj_frac") is not None:
        cargs.extend([
            "--projfrac",
            str(params.get("proj_frac"))
        ])
    if params.get("hemi") is not None:
        cargs.extend([
            "--hemi",
            params.get("hemi")
        ])
    if params.get("target") is not None:
        cargs.extend([
            "--target",
            params.get("target")
        ])
    if params.get("surf") is not None:
        cargs.extend([
            "--surf",
            params.get("surf")
        ])
    if params.get("cope_only"):
        cargs.append("--cope-only")
    if params.get("debug_flag"):
        cargs.append("--debug")
    if params.get("nolog_flag"):
        cargs.append("--nolog")
    if params.get("out_dir") is not None:
        cargs.extend([
            "--out",
            params.get("out_dir")
        ])
    return cargs


def feat2surf_outputs(
    params: Feat2surfParameters,
    execution: Execution,
) -> Feat2surfOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Feat2surfOutputs(
        root=execution.output_file("."),
        lh_output=execution.output_file(params.get("out_dir") + "/reg_surf-lh-Subject/stats") if (params.get("out_dir") is not None) else None,
        rh_output=execution.output_file(params.get("out_dir") + "/reg_surf-rh-Subject/stats") if (params.get("out_dir") is not None) else None,
        lh_target_output=execution.output_file(params.get("out_dir") + "/reg_surf-lh-targid/stats") if (params.get("out_dir") is not None) else None,
        rh_target_output=execution.output_file(params.get("out_dir") + "/reg_surf-rh-targid/stats") if (params.get("out_dir") is not None) else None,
    )
    return ret


def feat2surf_execute(
    params: Feat2surfParameters,
    execution: Execution,
) -> Feat2surfOutputs:
    """
    Resamples Feat statistics onto the surface of the subject and onto a
    stereo-taxic surface atlas.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Feat2surfOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = feat2surf_cargs(params, execution)
    ret = feat2surf_outputs(params, execution)
    execution.run(cargs)
    return ret


def feat2surf(
    feat_dirs: list[str],
    feat_dirfile: InputPathType | None = None,
    proj_frac: float | None = None,
    hemi: str | None = None,
    target: str | None = None,
    surf: str | None = None,
    cope_only: bool = False,
    debug_flag: bool = False,
    nolog_flag: bool = False,
    out_dir: str | None = None,
    runner: Runner | None = None,
) -> Feat2surfOutputs:
    """
    Resamples Feat statistics onto the surface of the subject and onto a
    stereo-taxic surface atlas.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        feat_dirs: Directory where Feat results are stored. Can specify\
            multiple directories.
        feat_dirfile: File with a list of Feat directories.
        proj_frac: Sample functional a fraction of the cortical thickness\
            normal to the surface. Default is 0.
        hemi: Run on specified hemisphere (lh or rh) only. Default is both\
            hemispheres.
        target: Subject used to define common surface space. Default is\
            fsaverage.
        surf: Surface to resample to. Default is white.
        cope_only: Only map the copes and varcopes to the common surface space.
        debug_flag: Turn on debugging.
        nolog_flag: Do not create a log file.
        out_dir: Output directory to use instead of default\
            feat/reg_surf-?h/stats.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Feat2surfOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FEAT2SURF_METADATA)
    params = feat2surf_params(feat_dirs=feat_dirs, feat_dirfile=feat_dirfile, proj_frac=proj_frac, hemi=hemi, target=target, surf=surf, cope_only=cope_only, debug_flag=debug_flag, nolog_flag=nolog_flag, out_dir=out_dir)
    return feat2surf_execute(params, execution)


__all__ = [
    "FEAT2SURF_METADATA",
    "Feat2surfOutputs",
    "Feat2surfParameters",
    "feat2surf",
    "feat2surf_params",
]
