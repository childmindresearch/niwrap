# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_VOLMASK_NOVTK_METADATA = Metadata(
    id="cbd19c74730136999fd3325b2d680e2b4bbb3842.boutiques",
    name="mris_volmask_novtk",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisVolmaskNovtkParameters = typing.TypedDict('MrisVolmaskNovtkParameters', {
    "__STYX_TYPE__": typing.Literal["mris_volmask_novtk"],
    "io": str,
    "cap_distance": typing.NotRequired[float | None],
    "label_background": typing.NotRequired[float | None],
    "label_left_white": typing.NotRequired[float | None],
    "label_left_ribbon": typing.NotRequired[float | None],
    "label_right_white": typing.NotRequired[float | None],
    "label_right_ribbon": typing.NotRequired[float | None],
    "surf_white": typing.NotRequired[str | None],
    "surf_pial": typing.NotRequired[str | None],
    "aseg_name": typing.NotRequired[str | None],
    "out_root": typing.NotRequired[str | None],
    "subjects_dir": typing.NotRequired[str | None],
    "save_distance": bool,
    "lh_only": bool,
    "rh_only": bool,
    "parallel": bool,
    "edit_aseg": bool,
    "save_ribbon": bool,
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
        "mris_volmask_novtk": mris_volmask_novtk_cargs,
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
    vt = {}
    return vt.get(t)


class MrisVolmaskNovtkOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_volmask_novtk(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_volmask_novtk_params(
    io_: str,
    cap_distance: float | None = None,
    label_background: float | None = None,
    label_left_white: float | None = None,
    label_left_ribbon: float | None = None,
    label_right_white: float | None = None,
    label_right_ribbon: float | None = None,
    surf_white: str | None = None,
    surf_pial: str | None = None,
    aseg_name: str | None = None,
    out_root: str | None = None,
    subjects_dir: str | None = None,
    save_distance: bool = False,
    lh_only: bool = False,
    rh_only: bool = False,
    parallel: bool = False,
    edit_aseg: bool = False,
    save_ribbon: bool = False,
) -> MrisVolmaskNovtkParameters:
    """
    Build parameters.
    
    Args:
        io_: Positional argument for input/output.
        cap_distance: Maximum distance up to which the signed distance function\
            computation is accurate.
        label_background: Override default value for background label value (0).
        label_left_white: Override default value for left white matter label\
            (20).
        label_left_ribbon: Override default value for left ribbon label (10).
        label_right_white: Override default value for right white matter label\
            (120).
        label_right_ribbon: Override default value for right ribbon label (110).
        surf_white: Surface root name, default value is white.
        surf_pial: Surface root name, default value is pial.
        aseg_name: Allows specifying a different name for the aseg input file.\
            Default value is aseg.
        out_root: Output root name, default value is ribbon.
        subjects_dir: Option to specify SUBJECTS_DIR.
        save_distance: Option to save the signed distance function.
        lh_only: Only process left hemisphere.
        rh_only: Only process right hemisphere.
        parallel: Run hemispheres in parallel and combine the result.
        edit_aseg: Edit the aseg using the ribbons and save to aseg.ribbon.mgz.
        save_ribbon: Save just the ribbon for the hemispheres.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_volmask_novtk",
        "io": io_,
        "save_distance": save_distance,
        "lh_only": lh_only,
        "rh_only": rh_only,
        "parallel": parallel,
        "edit_aseg": edit_aseg,
        "save_ribbon": save_ribbon,
    }
    if cap_distance is not None:
        params["cap_distance"] = cap_distance
    if label_background is not None:
        params["label_background"] = label_background
    if label_left_white is not None:
        params["label_left_white"] = label_left_white
    if label_left_ribbon is not None:
        params["label_left_ribbon"] = label_left_ribbon
    if label_right_white is not None:
        params["label_right_white"] = label_right_white
    if label_right_ribbon is not None:
        params["label_right_ribbon"] = label_right_ribbon
    if surf_white is not None:
        params["surf_white"] = surf_white
    if surf_pial is not None:
        params["surf_pial"] = surf_pial
    if aseg_name is not None:
        params["aseg_name"] = aseg_name
    if out_root is not None:
        params["out_root"] = out_root
    if subjects_dir is not None:
        params["subjects_dir"] = subjects_dir
    return params


def mris_volmask_novtk_cargs(
    params: MrisVolmaskNovtkParameters,
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
    cargs.append("mris_volmask_novtk")
    cargs.append(params.get("io"))
    if params.get("cap_distance") is not None:
        cargs.extend([
            "--cap_distance",
            str(params.get("cap_distance"))
        ])
    if params.get("label_background") is not None:
        cargs.extend([
            "--label_background",
            str(params.get("label_background"))
        ])
    if params.get("label_left_white") is not None:
        cargs.extend([
            "--label_left_white",
            str(params.get("label_left_white"))
        ])
    if params.get("label_left_ribbon") is not None:
        cargs.extend([
            "--label_left_ribbon",
            str(params.get("label_left_ribbon"))
        ])
    if params.get("label_right_white") is not None:
        cargs.extend([
            "--label_right_white",
            str(params.get("label_right_white"))
        ])
    if params.get("label_right_ribbon") is not None:
        cargs.extend([
            "--label_right_ribbon",
            str(params.get("label_right_ribbon"))
        ])
    if params.get("surf_white") is not None:
        cargs.extend([
            "--surf_white",
            params.get("surf_white")
        ])
    if params.get("surf_pial") is not None:
        cargs.extend([
            "--surf_pial",
            params.get("surf_pial")
        ])
    if params.get("aseg_name") is not None:
        cargs.extend([
            "--aseg_name",
            params.get("aseg_name")
        ])
    if params.get("out_root") is not None:
        cargs.extend([
            "--out_root",
            params.get("out_root")
        ])
    if params.get("subjects_dir") is not None:
        cargs.extend([
            "--sd",
            params.get("subjects_dir")
        ])
    if params.get("save_distance"):
        cargs.append("--save_distance")
    if params.get("lh_only"):
        cargs.append("--lh-only")
    if params.get("rh_only"):
        cargs.append("--rh-only")
    if params.get("parallel"):
        cargs.append("--parallel")
    if params.get("edit_aseg"):
        cargs.append("--edit_aseg")
    if params.get("save_ribbon"):
        cargs.append("--save_ribbon")
    return cargs


def mris_volmask_novtk_outputs(
    params: MrisVolmaskNovtkParameters,
    execution: Execution,
) -> MrisVolmaskNovtkOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisVolmaskNovtkOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_volmask_novtk_execute(
    params: MrisVolmaskNovtkParameters,
    execution: Execution,
) -> MrisVolmaskNovtkOutputs:
    """
    Computes a volume mask at the same resolution as <subject>/mri/brain.mgz and
    labels voxels based on the signed-distance function from the surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisVolmaskNovtkOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_volmask_novtk_cargs(params, execution)
    ret = mris_volmask_novtk_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_volmask_novtk(
    io_: str,
    cap_distance: float | None = None,
    label_background: float | None = None,
    label_left_white: float | None = None,
    label_left_ribbon: float | None = None,
    label_right_white: float | None = None,
    label_right_ribbon: float | None = None,
    surf_white: str | None = None,
    surf_pial: str | None = None,
    aseg_name: str | None = None,
    out_root: str | None = None,
    subjects_dir: str | None = None,
    save_distance: bool = False,
    lh_only: bool = False,
    rh_only: bool = False,
    parallel: bool = False,
    edit_aseg: bool = False,
    save_ribbon: bool = False,
    runner: Runner | None = None,
) -> MrisVolmaskNovtkOutputs:
    """
    Computes a volume mask at the same resolution as <subject>/mri/brain.mgz and
    labels voxels based on the signed-distance function from the surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        io_: Positional argument for input/output.
        cap_distance: Maximum distance up to which the signed distance function\
            computation is accurate.
        label_background: Override default value for background label value (0).
        label_left_white: Override default value for left white matter label\
            (20).
        label_left_ribbon: Override default value for left ribbon label (10).
        label_right_white: Override default value for right white matter label\
            (120).
        label_right_ribbon: Override default value for right ribbon label (110).
        surf_white: Surface root name, default value is white.
        surf_pial: Surface root name, default value is pial.
        aseg_name: Allows specifying a different name for the aseg input file.\
            Default value is aseg.
        out_root: Output root name, default value is ribbon.
        subjects_dir: Option to specify SUBJECTS_DIR.
        save_distance: Option to save the signed distance function.
        lh_only: Only process left hemisphere.
        rh_only: Only process right hemisphere.
        parallel: Run hemispheres in parallel and combine the result.
        edit_aseg: Edit the aseg using the ribbons and save to aseg.ribbon.mgz.
        save_ribbon: Save just the ribbon for the hemispheres.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisVolmaskNovtkOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_VOLMASK_NOVTK_METADATA)
    params = mris_volmask_novtk_params(io_=io_, cap_distance=cap_distance, label_background=label_background, label_left_white=label_left_white, label_left_ribbon=label_left_ribbon, label_right_white=label_right_white, label_right_ribbon=label_right_ribbon, surf_white=surf_white, surf_pial=surf_pial, aseg_name=aseg_name, out_root=out_root, subjects_dir=subjects_dir, save_distance=save_distance, lh_only=lh_only, rh_only=rh_only, parallel=parallel, edit_aseg=edit_aseg, save_ribbon=save_ribbon)
    return mris_volmask_novtk_execute(params, execution)


__all__ = [
    "MRIS_VOLMASK_NOVTK_METADATA",
    "MrisVolmaskNovtkOutputs",
    "mris_volmask_novtk",
    "mris_volmask_novtk_params",
]
