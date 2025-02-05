# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__SUMA_ALIGN_TO_EXPERIMENT_METADATA = Metadata(
    id="8f81484159017f8749f8211125315dcfa8d64e88.boutiques",
    name="@SUMA_AlignToExperiment",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VSumaAlignToExperimentParameters = typing.TypedDict('VSumaAlignToExperimentParameters', {
    "__STYX_TYPE__": typing.Literal["@SUMA_AlignToExperiment"],
    "exp_anat": InputPathType,
    "surf_anat": InputPathType,
    "dxyz": typing.NotRequired[float | None],
    "out_dxyz": typing.NotRequired[float | None],
    "wd": bool,
    "al": bool,
    "al_opt": typing.NotRequired[str | None],
    "ok_change_view": bool,
    "strip_skull": typing.NotRequired[str | None],
    "skull_strip_opt": typing.NotRequired[str | None],
    "align_centers": bool,
    "init_xform": typing.NotRequired[InputPathType | None],
    "EA_clip_below": typing.NotRequired[float | None],
    "prefix": typing.NotRequired[str | None],
    "surf_anat_followers": typing.NotRequired[str | None],
    "followers_interp": typing.NotRequired[str | None],
    "atlas_followers": bool,
    "echo": bool,
    "keep_tmp": bool,
    "overwrite_resp": typing.NotRequired[str | None],
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
        "@SUMA_AlignToExperiment": v__suma_align_to_experiment_cargs,
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
        "@SUMA_AlignToExperiment": v__suma_align_to_experiment_outputs,
    }
    return vt.get(t)


class VSumaAlignToExperimentOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__suma_align_to_experiment(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    aligned_volume: OutputPathType | None
    """Output volume after alignment."""
    additional_followers: OutputPathType | None
    """Output followers dataset after transforming."""


def v__suma_align_to_experiment_params(
    exp_anat: InputPathType,
    surf_anat: InputPathType,
    dxyz: float | None = None,
    out_dxyz: float | None = None,
    wd: bool = False,
    al: bool = False,
    al_opt: str | None = None,
    ok_change_view: bool = False,
    strip_skull: str | None = None,
    skull_strip_opt: str | None = None,
    align_centers: bool = False,
    init_xform: InputPathType | None = None,
    ea_clip_below: float | None = None,
    prefix: str | None = None,
    surf_anat_followers: str | None = None,
    followers_interp: str | None = None,
    atlas_followers: bool = False,
    echo: bool = False,
    keep_tmp: bool = False,
    overwrite_resp: str | None = None,
) -> VSumaAlignToExperimentParameters:
    """
    Build parameters.
    
    Args:
        exp_anat: Name of high resolution anatomical data set in register with\
            experimental data.
        surf_anat: Path and name of high resolution antomical data set used to\
            create the surface.
        dxyz: Optional parameter to downsample anatomical volumes to dxyz mm\
            voxel resolution before registration.
        out_dxyz: Output the final aligned volume at a cubic voxelsize of\
            DXYZmm.
        wd: Use 3dWarpDrive's general affine transform (12 param) instead of\
            3dvolreg's 6 parameters.
        al: Use 3dAllineate to do the 12 parameter alignment. Cost function is\
            'lpa'.
        al_opt: Specify set of options to pass to 3dAllineate.
        ok_change_view: Be quiet when view of registered volume is changed to\
            match that of the Experiment_Anatomy.
        strip_skull: Use 3dSkullStrip to remove non-brain tissue.
        skull_strip_opt: Pass the options to 3dSkullStrip.
        align_centers: Add an additional transformation to align the volume\
            centers.
        init_xform: Apply affine transform file to Surface_Anatomy before\
            beginning registration.
        ea_clip_below: Set slices below CLPmm in 'Experiment Anatomy' to zero.
        prefix: Prefix for the output volume.
        surf_anat_followers: Apply the same alignment transform to additional\
            datasets.
        followers_interp: Set the interpolation mode for the follower datasets.
        atlas_followers: Automatically set the followers to be atlases in the\
            directory of -surf_anat.
        echo: Echo all commands to terminal for debugging.
        keep_tmp: Keep temporary files for debugging.
        overwrite_resp: Answer 'overwrite' questions automatically.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@SUMA_AlignToExperiment",
        "exp_anat": exp_anat,
        "surf_anat": surf_anat,
        "wd": wd,
        "al": al,
        "ok_change_view": ok_change_view,
        "align_centers": align_centers,
        "atlas_followers": atlas_followers,
        "echo": echo,
        "keep_tmp": keep_tmp,
    }
    if dxyz is not None:
        params["dxyz"] = dxyz
    if out_dxyz is not None:
        params["out_dxyz"] = out_dxyz
    if al_opt is not None:
        params["al_opt"] = al_opt
    if strip_skull is not None:
        params["strip_skull"] = strip_skull
    if skull_strip_opt is not None:
        params["skull_strip_opt"] = skull_strip_opt
    if init_xform is not None:
        params["init_xform"] = init_xform
    if ea_clip_below is not None:
        params["EA_clip_below"] = ea_clip_below
    if prefix is not None:
        params["prefix"] = prefix
    if surf_anat_followers is not None:
        params["surf_anat_followers"] = surf_anat_followers
    if followers_interp is not None:
        params["followers_interp"] = followers_interp
    if overwrite_resp is not None:
        params["overwrite_resp"] = overwrite_resp
    return params


def v__suma_align_to_experiment_cargs(
    params: VSumaAlignToExperimentParameters,
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
    cargs.append("@SUMA_AlignToExperiment")
    cargs.extend([
        "-exp_anat",
        execution.input_file(params.get("exp_anat"))
    ])
    cargs.extend([
        "-surf_anat",
        execution.input_file(params.get("surf_anat"))
    ])
    if params.get("dxyz") is not None:
        cargs.extend([
            "-dxyz",
            str(params.get("dxyz"))
        ])
    if params.get("out_dxyz") is not None:
        cargs.extend([
            "-out_dxyz",
            str(params.get("out_dxyz"))
        ])
    if params.get("wd"):
        cargs.append("-wd")
    if params.get("al"):
        cargs.append("-al")
    if params.get("al_opt") is not None:
        cargs.extend([
            "-al_opt",
            params.get("al_opt")
        ])
    if params.get("ok_change_view"):
        cargs.append("-ok_change_view")
    if params.get("strip_skull") is not None:
        cargs.extend([
            "-strip_skull",
            params.get("strip_skull")
        ])
    if params.get("skull_strip_opt") is not None:
        cargs.extend([
            "-skull_strip_opt",
            params.get("skull_strip_opt")
        ])
    if params.get("align_centers"):
        cargs.append("-align_centers")
    if params.get("init_xform") is not None:
        cargs.extend([
            "-init_xform",
            execution.input_file(params.get("init_xform"))
        ])
    if params.get("EA_clip_below") is not None:
        cargs.extend([
            "-EA_clip_below",
            str(params.get("EA_clip_below"))
        ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("surf_anat_followers") is not None:
        cargs.extend([
            "-surf_anat_followers",
            params.get("surf_anat_followers")
        ])
    if params.get("followers_interp") is not None:
        cargs.extend([
            "-followers_interp",
            params.get("followers_interp")
        ])
    if params.get("atlas_followers"):
        cargs.append("-atlas_followers")
    if params.get("echo"):
        cargs.append("-echo")
    if params.get("keep_tmp"):
        cargs.append("-keep_tmp")
    if params.get("overwrite_resp") is not None:
        cargs.extend([
            "-overwrite_resp",
            params.get("overwrite_resp")
        ])
    return cargs


def v__suma_align_to_experiment_outputs(
    params: VSumaAlignToExperimentParameters,
    execution: Execution,
) -> VSumaAlignToExperimentOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VSumaAlignToExperimentOutputs(
        root=execution.output_file("."),
        aligned_volume=execution.output_file(params.get("prefix") + "_Alnd_Exp.nii.gz") if (params.get("prefix") is not None) else None,
        additional_followers=execution.output_file(params.get("prefix") + "_Alnd_Exp_Fdset.nii.gz") if (params.get("prefix") is not None) else None,
    )
    return ret


def v__suma_align_to_experiment_execute(
    params: VSumaAlignToExperimentParameters,
    execution: Execution,
) -> VSumaAlignToExperimentOutputs:
    """
    Creates a version of Surface Anatomy that is registered to Experiment Anatomy.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VSumaAlignToExperimentOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v__suma_align_to_experiment_cargs(params, execution)
    ret = v__suma_align_to_experiment_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__suma_align_to_experiment(
    exp_anat: InputPathType,
    surf_anat: InputPathType,
    dxyz: float | None = None,
    out_dxyz: float | None = None,
    wd: bool = False,
    al: bool = False,
    al_opt: str | None = None,
    ok_change_view: bool = False,
    strip_skull: str | None = None,
    skull_strip_opt: str | None = None,
    align_centers: bool = False,
    init_xform: InputPathType | None = None,
    ea_clip_below: float | None = None,
    prefix: str | None = None,
    surf_anat_followers: str | None = None,
    followers_interp: str | None = None,
    atlas_followers: bool = False,
    echo: bool = False,
    keep_tmp: bool = False,
    overwrite_resp: str | None = None,
    runner: Runner | None = None,
) -> VSumaAlignToExperimentOutputs:
    """
    Creates a version of Surface Anatomy that is registered to Experiment Anatomy.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        exp_anat: Name of high resolution anatomical data set in register with\
            experimental data.
        surf_anat: Path and name of high resolution antomical data set used to\
            create the surface.
        dxyz: Optional parameter to downsample anatomical volumes to dxyz mm\
            voxel resolution before registration.
        out_dxyz: Output the final aligned volume at a cubic voxelsize of\
            DXYZmm.
        wd: Use 3dWarpDrive's general affine transform (12 param) instead of\
            3dvolreg's 6 parameters.
        al: Use 3dAllineate to do the 12 parameter alignment. Cost function is\
            'lpa'.
        al_opt: Specify set of options to pass to 3dAllineate.
        ok_change_view: Be quiet when view of registered volume is changed to\
            match that of the Experiment_Anatomy.
        strip_skull: Use 3dSkullStrip to remove non-brain tissue.
        skull_strip_opt: Pass the options to 3dSkullStrip.
        align_centers: Add an additional transformation to align the volume\
            centers.
        init_xform: Apply affine transform file to Surface_Anatomy before\
            beginning registration.
        ea_clip_below: Set slices below CLPmm in 'Experiment Anatomy' to zero.
        prefix: Prefix for the output volume.
        surf_anat_followers: Apply the same alignment transform to additional\
            datasets.
        followers_interp: Set the interpolation mode for the follower datasets.
        atlas_followers: Automatically set the followers to be atlases in the\
            directory of -surf_anat.
        echo: Echo all commands to terminal for debugging.
        keep_tmp: Keep temporary files for debugging.
        overwrite_resp: Answer 'overwrite' questions automatically.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VSumaAlignToExperimentOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SUMA_ALIGN_TO_EXPERIMENT_METADATA)
    params = v__suma_align_to_experiment_params(exp_anat=exp_anat, surf_anat=surf_anat, dxyz=dxyz, out_dxyz=out_dxyz, wd=wd, al=al, al_opt=al_opt, ok_change_view=ok_change_view, strip_skull=strip_skull, skull_strip_opt=skull_strip_opt, align_centers=align_centers, init_xform=init_xform, ea_clip_below=ea_clip_below, prefix=prefix, surf_anat_followers=surf_anat_followers, followers_interp=followers_interp, atlas_followers=atlas_followers, echo=echo, keep_tmp=keep_tmp, overwrite_resp=overwrite_resp)
    return v__suma_align_to_experiment_execute(params, execution)


__all__ = [
    "VSumaAlignToExperimentOutputs",
    "VSumaAlignToExperimentParameters",
    "V__SUMA_ALIGN_TO_EXPERIMENT_METADATA",
    "v__suma_align_to_experiment",
    "v__suma_align_to_experiment_params",
]
