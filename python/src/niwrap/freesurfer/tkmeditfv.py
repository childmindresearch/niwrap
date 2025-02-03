# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TKMEDITFV_METADATA = Metadata(
    id="c54cb02c761041c3c2bd1fa2a8964899175b9969.boutiques",
    name="tkmeditfv",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
TkmeditfvParameters = typing.TypedDict('TkmeditfvParameters', {
    "__STYX_TYPE__": typing.Literal["tkmeditfv"],
    "subject": typing.NotRequired[str | None],
    "mainvol": InputPathType,
    "aux_volume": typing.NotRequired[InputPathType | None],
    "seg_volume": typing.NotRequired[InputPathType | None],
    "overlay": typing.NotRequired[InputPathType | None],
    "timecourse": typing.NotRequired[InputPathType | None],
    "overlay_registration": typing.NotRequired[InputPathType | None],
    "surface": typing.NotRequired[list[str] | None],
    "extra_volumes": typing.NotRequired[list[InputPathType] | None],
    "crs_location": typing.NotRequired[list[float] | None],
    "zoom_level": typing.NotRequired[float | None],
    "additional_segments": typing.NotRequired[list[InputPathType] | None],
    "load_white": bool,
    "load_pial": bool,
    "load_orig": bool,
    "load_orig_nofix": bool,
    "load_smoothwm_nofix": bool,
    "load_white_preaparc": bool,
    "load_inflated": bool,
    "annot": typing.NotRequired[str | None],
    "load_aparc": bool,
    "surfext": typing.NotRequired[str | None],
    "seg_outline": bool,
    "intensity_minmax": typing.NotRequired[list[float] | None],
    "load_defects": bool,
    "load_defect_pointset": bool,
    "trilin_interpolation": bool,
    "neurological_orientation": bool,
    "rotate_around_cursor": bool,
    "vgl_display": bool,
    "use_tkmedit": bool,
    "load_aparc_aseg": bool,
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
        "tkmeditfv": tkmeditfv_cargs,
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


class TkmeditfvOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tkmeditfv(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def tkmeditfv_params(
    mainvol: InputPathType,
    subject: str | None = None,
    aux_volume: InputPathType | None = None,
    seg_volume: InputPathType | None = None,
    overlay: InputPathType | None = None,
    timecourse: InputPathType | None = None,
    overlay_registration: InputPathType | None = None,
    surface: list[str] | None = None,
    extra_volumes: list[InputPathType] | None = None,
    crs_location: list[float] | None = None,
    zoom_level: float | None = None,
    additional_segments: list[InputPathType] | None = None,
    load_white: bool = False,
    load_pial: bool = False,
    load_orig: bool = False,
    load_orig_nofix: bool = False,
    load_smoothwm_nofix: bool = False,
    load_white_preaparc: bool = False,
    load_inflated: bool = False,
    annot: str | None = None,
    load_aparc: bool = False,
    surfext: str | None = None,
    seg_outline: bool = False,
    intensity_minmax: list[float] | None = None,
    load_defects: bool = False,
    load_defect_pointset: bool = False,
    trilin_interpolation: bool = False,
    neurological_orientation: bool = False,
    rotate_around_cursor: bool = False,
    vgl_display: bool = False,
    use_tkmedit: bool = False,
    load_aparc_aseg: bool = False,
) -> TkmeditfvParameters:
    """
    Build parameters.
    
    Args:
        mainvol: Main volume file path.
        subject: Subject's name.
        aux_volume: Auxiliary volume file path.
        seg_volume: Segmentation volume file path.
        overlay: Overlay volume file path.
        timecourse: Timecourse for overlay.
        overlay_registration: Overlay timecourse registration file.
        surface: Load surface with optional color.
        extra_volumes: Load extra volume(s).
        crs_location: Place cursor at given (col, row, slice) location.
        zoom_level: Set zoom level.
        additional_segments: Add additional segmentations.
        load_white: Load lh and rh.white surfaces.
        load_pial: Load lh and rh.pial surfaces.
        load_orig: Load lh and rh.orig surfaces.
        load_orig_nofix: Load lh and rh.orig.nofix surfaces.
        load_smoothwm_nofix: Load lh and rh.smoothwm.nofix surfaces.
        load_white_preaparc: Load lh and rh.white.preaparc surfaces.
        load_inflated: Load lh and rh.inflated surfaces.
        annot: Load annotation file.
        load_aparc: Load aparc annotation.
        surfext: Add extension to the name of the surface.
        seg_outline: Enable segmentation outline mode.
        intensity_minmax: Set intensity min and max on first volume.
        load_defects: Load info needed to evaluate defects.
        load_defect_pointset: Load defect pointset.
        trilin_interpolation: Use trilinear interpolation for volume overlays.
        neurological_orientation: Use neurological orientation instead of\
            radiological.
        rotate_around_cursor: Rotate around cursor in 3D view.
        vgl_display: Set VGL_DISPLAY and run with vglrun.
        use_tkmedit: Use tkmedit instead of freeview.
        load_aparc_aseg: Load aparc+aseg.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "tkmeditfv",
        "mainvol": mainvol,
        "load_white": load_white,
        "load_pial": load_pial,
        "load_orig": load_orig,
        "load_orig_nofix": load_orig_nofix,
        "load_smoothwm_nofix": load_smoothwm_nofix,
        "load_white_preaparc": load_white_preaparc,
        "load_inflated": load_inflated,
        "load_aparc": load_aparc,
        "seg_outline": seg_outline,
        "load_defects": load_defects,
        "load_defect_pointset": load_defect_pointset,
        "trilin_interpolation": trilin_interpolation,
        "neurological_orientation": neurological_orientation,
        "rotate_around_cursor": rotate_around_cursor,
        "vgl_display": vgl_display,
        "use_tkmedit": use_tkmedit,
        "load_aparc_aseg": load_aparc_aseg,
    }
    if subject is not None:
        params["subject"] = subject
    if aux_volume is not None:
        params["aux_volume"] = aux_volume
    if seg_volume is not None:
        params["seg_volume"] = seg_volume
    if overlay is not None:
        params["overlay"] = overlay
    if timecourse is not None:
        params["timecourse"] = timecourse
    if overlay_registration is not None:
        params["overlay_registration"] = overlay_registration
    if surface is not None:
        params["surface"] = surface
    if extra_volumes is not None:
        params["extra_volumes"] = extra_volumes
    if crs_location is not None:
        params["crs_location"] = crs_location
    if zoom_level is not None:
        params["zoom_level"] = zoom_level
    if additional_segments is not None:
        params["additional_segments"] = additional_segments
    if annot is not None:
        params["annot"] = annot
    if surfext is not None:
        params["surfext"] = surfext
    if intensity_minmax is not None:
        params["intensity_minmax"] = intensity_minmax
    return params


def tkmeditfv_cargs(
    params: TkmeditfvParameters,
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
    cargs.append("tkmeditfv")
    if params.get("subject") is not None:
        cargs.append(params.get("subject"))
    cargs.append(execution.input_file(params.get("mainvol")))
    if params.get("aux_volume") is not None:
        cargs.extend([
            "-aux",
            execution.input_file(params.get("aux_volume"))
        ])
    if params.get("seg_volume") is not None:
        cargs.extend([
            "-seg",
            execution.input_file(params.get("seg_volume"))
        ])
    if params.get("overlay") is not None:
        cargs.extend([
            "-ov",
            execution.input_file(params.get("overlay"))
        ])
    if params.get("timecourse") is not None:
        cargs.extend([
            "-t",
            execution.input_file(params.get("timecourse"))
        ])
    if params.get("overlay_registration") is not None:
        cargs.extend([
            "-reg",
            execution.input_file(params.get("overlay_registration"))
        ])
    if params.get("surface") is not None:
        cargs.extend([
            "-surf",
            *params.get("surface")
        ])
    if params.get("extra_volumes") is not None:
        cargs.extend([
            "-vol",
            *[execution.input_file(f) for f in params.get("extra_volumes")]
        ])
    if params.get("crs_location") is not None:
        cargs.extend([
            "-crs",
            *map(str, params.get("crs_location"))
        ])
    if params.get("zoom_level") is not None:
        cargs.extend([
            "-zoom",
            str(params.get("zoom_level"))
        ])
    if params.get("additional_segments") is not None:
        cargs.extend([
            "-seg2",
            *[execution.input_file(f) for f in params.get("additional_segments")]
        ])
    if params.get("load_white"):
        cargs.append("-white")
    if params.get("load_pial"):
        cargs.append("-pial")
    if params.get("load_orig"):
        cargs.append("-orig")
    if params.get("load_orig_nofix"):
        cargs.append("-orig.nofix")
    if params.get("load_smoothwm_nofix"):
        cargs.append("-smoothwm.nofix")
    if params.get("load_white_preaparc"):
        cargs.append("-white.preaparc")
    if params.get("load_inflated"):
        cargs.append("-inflated")
    if params.get("annot") is not None:
        cargs.extend([
            "-annot",
            params.get("annot")
        ])
    if params.get("load_aparc"):
        cargs.append("-aparc")
    if params.get("surfext") is not None:
        cargs.extend([
            "-surfext",
            params.get("surfext")
        ])
    if params.get("seg_outline"):
        cargs.append("-seg-outline")
    if params.get("intensity_minmax") is not None:
        cargs.extend([
            "-main-minmax",
            *map(str, params.get("intensity_minmax"))
        ])
    if params.get("load_defects"):
        cargs.append("-defects")
    if params.get("load_defect_pointset"):
        cargs.append("-defectps")
    if params.get("trilin_interpolation"):
        cargs.append("-trilin")
    if params.get("neurological_orientation"):
        cargs.append("-neuro")
    if params.get("rotate_around_cursor"):
        cargs.append("-rotate-around-cursor")
    if params.get("vgl_display"):
        cargs.append("-vgl")
    if params.get("use_tkmedit"):
        cargs.append("-tkmedit")
    if params.get("load_aparc_aseg"):
        cargs.append("-aparc+aseg")
    return cargs


def tkmeditfv_outputs(
    params: TkmeditfvParameters,
    execution: Execution,
) -> TkmeditfvOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TkmeditfvOutputs(
        root=execution.output_file("."),
    )
    return ret


def tkmeditfv_execute(
    params: TkmeditfvParameters,
    execution: Execution,
) -> TkmeditfvOutputs:
    """
    A wrapper script to run Freeview with arguments similar to tkmedit, providing
    both functionalities.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TkmeditfvOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = tkmeditfv_cargs(params, execution)
    ret = tkmeditfv_outputs(params, execution)
    execution.run(cargs)
    return ret


def tkmeditfv(
    mainvol: InputPathType,
    subject: str | None = None,
    aux_volume: InputPathType | None = None,
    seg_volume: InputPathType | None = None,
    overlay: InputPathType | None = None,
    timecourse: InputPathType | None = None,
    overlay_registration: InputPathType | None = None,
    surface: list[str] | None = None,
    extra_volumes: list[InputPathType] | None = None,
    crs_location: list[float] | None = None,
    zoom_level: float | None = None,
    additional_segments: list[InputPathType] | None = None,
    load_white: bool = False,
    load_pial: bool = False,
    load_orig: bool = False,
    load_orig_nofix: bool = False,
    load_smoothwm_nofix: bool = False,
    load_white_preaparc: bool = False,
    load_inflated: bool = False,
    annot: str | None = None,
    load_aparc: bool = False,
    surfext: str | None = None,
    seg_outline: bool = False,
    intensity_minmax: list[float] | None = None,
    load_defects: bool = False,
    load_defect_pointset: bool = False,
    trilin_interpolation: bool = False,
    neurological_orientation: bool = False,
    rotate_around_cursor: bool = False,
    vgl_display: bool = False,
    use_tkmedit: bool = False,
    load_aparc_aseg: bool = False,
    runner: Runner | None = None,
) -> TkmeditfvOutputs:
    """
    A wrapper script to run Freeview with arguments similar to tkmedit, providing
    both functionalities.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        mainvol: Main volume file path.
        subject: Subject's name.
        aux_volume: Auxiliary volume file path.
        seg_volume: Segmentation volume file path.
        overlay: Overlay volume file path.
        timecourse: Timecourse for overlay.
        overlay_registration: Overlay timecourse registration file.
        surface: Load surface with optional color.
        extra_volumes: Load extra volume(s).
        crs_location: Place cursor at given (col, row, slice) location.
        zoom_level: Set zoom level.
        additional_segments: Add additional segmentations.
        load_white: Load lh and rh.white surfaces.
        load_pial: Load lh and rh.pial surfaces.
        load_orig: Load lh and rh.orig surfaces.
        load_orig_nofix: Load lh and rh.orig.nofix surfaces.
        load_smoothwm_nofix: Load lh and rh.smoothwm.nofix surfaces.
        load_white_preaparc: Load lh and rh.white.preaparc surfaces.
        load_inflated: Load lh and rh.inflated surfaces.
        annot: Load annotation file.
        load_aparc: Load aparc annotation.
        surfext: Add extension to the name of the surface.
        seg_outline: Enable segmentation outline mode.
        intensity_minmax: Set intensity min and max on first volume.
        load_defects: Load info needed to evaluate defects.
        load_defect_pointset: Load defect pointset.
        trilin_interpolation: Use trilinear interpolation for volume overlays.
        neurological_orientation: Use neurological orientation instead of\
            radiological.
        rotate_around_cursor: Rotate around cursor in 3D view.
        vgl_display: Set VGL_DISPLAY and run with vglrun.
        use_tkmedit: Use tkmedit instead of freeview.
        load_aparc_aseg: Load aparc+aseg.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TkmeditfvOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TKMEDITFV_METADATA)
    params = tkmeditfv_params(subject=subject, mainvol=mainvol, aux_volume=aux_volume, seg_volume=seg_volume, overlay=overlay, timecourse=timecourse, overlay_registration=overlay_registration, surface=surface, extra_volumes=extra_volumes, crs_location=crs_location, zoom_level=zoom_level, additional_segments=additional_segments, load_white=load_white, load_pial=load_pial, load_orig=load_orig, load_orig_nofix=load_orig_nofix, load_smoothwm_nofix=load_smoothwm_nofix, load_white_preaparc=load_white_preaparc, load_inflated=load_inflated, annot=annot, load_aparc=load_aparc, surfext=surfext, seg_outline=seg_outline, intensity_minmax=intensity_minmax, load_defects=load_defects, load_defect_pointset=load_defect_pointset, trilin_interpolation=trilin_interpolation, neurological_orientation=neurological_orientation, rotate_around_cursor=rotate_around_cursor, vgl_display=vgl_display, use_tkmedit=use_tkmedit, load_aparc_aseg=load_aparc_aseg)
    return tkmeditfv_execute(params, execution)


__all__ = [
    "TKMEDITFV_METADATA",
    "TkmeditfvOutputs",
    "tkmeditfv",
    "tkmeditfv_params",
]
