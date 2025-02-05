# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_BINARIZE_METADATA = Metadata(
    id="bc9047e09f0005244a935fc141f4ec627626d141.boutiques",
    name="mri_binarize",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriBinarizeParameters = typing.TypedDict('MriBinarizeParameters', {
    "__STYX_TYPE__": typing.Literal["mri_binarize"],
    "input_volume": InputPathType,
    "output_volume": str,
    "min_threshold": typing.NotRequired[float | None],
    "max_threshold": typing.NotRequired[float | None],
    "pct_threshold": typing.NotRequired[float | None],
    "rmin": typing.NotRequired[float | None],
    "rmax": typing.NotRequired[float | None],
    "fdr_threshold": typing.NotRequired[float | None],
    "match_values": typing.NotRequired[list[float] | None],
    "replace_values": typing.NotRequired[list[float] | None],
    "binval": typing.NotRequired[float | None],
    "binval_not": typing.NotRequired[float | None],
    "frame": typing.NotRequired[float | None],
    "merge_volume": typing.NotRequired[InputPathType | None],
    "mask_volume": typing.NotRequired[InputPathType | None],
    "mask_threshold": typing.NotRequired[float | None],
    "surf_name": typing.NotRequired[str | None],
    "surf_smooth": typing.NotRequired[float | None],
    "threads": typing.NotRequired[float | None],
    "ctx_wm_flag": bool,
    "all_wm_flag": bool,
    "ventricles_flag": bool,
    "wm_vcsf_flag": bool,
    "gm_flag": bool,
    "subcort_gm_flag": bool,
    "scm_lh_flag": bool,
    "scm_rh_flag": bool,
    "zero_edges_flag": bool,
    "zero_slice_edges_flag": bool,
    "dilate_vertex": typing.NotRequired[str | None],
    "remove_islands_flag": bool,
    "fill_holes_flag": bool,
    "noverbose_flag": bool,
    "debug_flag": bool,
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
        "mri_binarize": mri_binarize_cargs,
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
        "mri_binarize": mri_binarize_outputs,
    }
    return vt.get(t)


class MriBinarizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_binarize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_volume: OutputPathType
    """The resulting binarized volume."""


def mri_binarize_params(
    input_volume: InputPathType,
    output_volume: str,
    min_threshold: float | None = None,
    max_threshold: float | None = None,
    pct_threshold: float | None = None,
    rmin: float | None = None,
    rmax: float | None = None,
    fdr_threshold: float | None = None,
    match_values: list[float] | None = None,
    replace_values: list[float] | None = None,
    binval: float | None = None,
    binval_not: float | None = None,
    frame: float | None = None,
    merge_volume: InputPathType | None = None,
    mask_volume: InputPathType | None = None,
    mask_threshold: float | None = None,
    surf_name: str | None = None,
    surf_smooth: float | None = None,
    threads: float | None = None,
    ctx_wm_flag: bool = False,
    all_wm_flag: bool = False,
    ventricles_flag: bool = False,
    wm_vcsf_flag: bool = False,
    gm_flag: bool = False,
    subcort_gm_flag: bool = False,
    scm_lh_flag: bool = False,
    scm_rh_flag: bool = False,
    zero_edges_flag: bool = False,
    zero_slice_edges_flag: bool = False,
    dilate_vertex: str | None = None,
    remove_islands_flag: bool = False,
    fill_holes_flag: bool = False,
    noverbose_flag: bool = False,
    debug_flag: bool = False,
) -> MriBinarizeParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Input volume to be binarized.
        output_volume: Path to output volume.
        min_threshold: Minimum threshold (default is -inf).
        max_threshold: Maximum threshold (default is +inf).
        pct_threshold: Set threshold to capture top P% of voxels.
        rmin: Compute min threshold based on rmin times global mean.
        rmax: Compute max threshold based on rmax times global mean.
        fdr_threshold: Compute min threshold based on FDR.
        match_values: Binarize based on matching values.
        replace_values: Replace voxels with specified values. Format: V1 V2.
        binval: Set voxel value within threshold to specified value (default is\
            1).
        binval_not: Set voxel value outside threshold range to specified value\
            (default is 0).
        frame: Use specific frame of the input. 0-based index.
        merge_volume: Merge with another volume. Must be the same dimensions as\
            input volume.
        mask_volume: Mask input with a specified mask volume.
        mask_threshold: Set threshold for mask volume (default is 0.5).
        surf_name: Create a surface mesh from the binarization.
        surf_smooth: Smooth the surface mesh iteratively, specifying the number\
            of iterations.
        threads: Specify number of threads to use.
        ctx_wm_flag: Set match values for cerebral white matter.
        all_wm_flag: Set match values for all white matter.
        ventricles_flag: Set match values for ventricles and choroid.
        wm_vcsf_flag: Match for WM and ventricular CSF.
        gm_flag: Match for all WM, VCSF and background, then invert.
        subcort_gm_flag: Match for subcortical gray matter.
        scm_lh_flag: Subcortical mass for left hemisphere.
        scm_rh_flag: Subcortical mass for right hemisphere.
        zero_edges_flag: Set edge voxels to zero.
        zero_slice_edges_flag: Set edge slice voxels to zero.
        dilate_vertex: Dilate vertex to a specific target area.
        remove_islands_flag: Remove islands in the mask.
        fill_holes_flag: Remove holes in the mask.
        noverbose_flag: Suppress verbose output.
        debug_flag: Enable debugging output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_binarize",
        "input_volume": input_volume,
        "output_volume": output_volume,
        "ctx_wm_flag": ctx_wm_flag,
        "all_wm_flag": all_wm_flag,
        "ventricles_flag": ventricles_flag,
        "wm_vcsf_flag": wm_vcsf_flag,
        "gm_flag": gm_flag,
        "subcort_gm_flag": subcort_gm_flag,
        "scm_lh_flag": scm_lh_flag,
        "scm_rh_flag": scm_rh_flag,
        "zero_edges_flag": zero_edges_flag,
        "zero_slice_edges_flag": zero_slice_edges_flag,
        "remove_islands_flag": remove_islands_flag,
        "fill_holes_flag": fill_holes_flag,
        "noverbose_flag": noverbose_flag,
        "debug_flag": debug_flag,
    }
    if min_threshold is not None:
        params["min_threshold"] = min_threshold
    if max_threshold is not None:
        params["max_threshold"] = max_threshold
    if pct_threshold is not None:
        params["pct_threshold"] = pct_threshold
    if rmin is not None:
        params["rmin"] = rmin
    if rmax is not None:
        params["rmax"] = rmax
    if fdr_threshold is not None:
        params["fdr_threshold"] = fdr_threshold
    if match_values is not None:
        params["match_values"] = match_values
    if replace_values is not None:
        params["replace_values"] = replace_values
    if binval is not None:
        params["binval"] = binval
    if binval_not is not None:
        params["binval_not"] = binval_not
    if frame is not None:
        params["frame"] = frame
    if merge_volume is not None:
        params["merge_volume"] = merge_volume
    if mask_volume is not None:
        params["mask_volume"] = mask_volume
    if mask_threshold is not None:
        params["mask_threshold"] = mask_threshold
    if surf_name is not None:
        params["surf_name"] = surf_name
    if surf_smooth is not None:
        params["surf_smooth"] = surf_smooth
    if threads is not None:
        params["threads"] = threads
    if dilate_vertex is not None:
        params["dilate_vertex"] = dilate_vertex
    return params


def mri_binarize_cargs(
    params: MriBinarizeParameters,
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
    cargs.append("mri_binarize")
    cargs.extend([
        "--i",
        execution.input_file(params.get("input_volume"))
    ])
    cargs.extend([
        "--o",
        params.get("output_volume")
    ])
    if params.get("min_threshold") is not None:
        cargs.extend([
            "--min",
            str(params.get("min_threshold"))
        ])
    if params.get("max_threshold") is not None:
        cargs.extend([
            "--max",
            str(params.get("max_threshold"))
        ])
    if params.get("pct_threshold") is not None:
        cargs.extend([
            "--pct",
            str(params.get("pct_threshold"))
        ])
    if params.get("rmin") is not None:
        cargs.extend([
            "--rmin",
            str(params.get("rmin"))
        ])
    if params.get("rmax") is not None:
        cargs.extend([
            "--rmax",
            str(params.get("rmax"))
        ])
    if params.get("fdr_threshold") is not None:
        cargs.extend([
            "--fdr",
            str(params.get("fdr_threshold"))
        ])
    if params.get("match_values") is not None:
        cargs.extend([
            "--match",
            *map(str, params.get("match_values"))
        ])
    if params.get("replace_values") is not None:
        cargs.extend([
            "--replace",
            *map(str, params.get("replace_values"))
        ])
    if params.get("binval") is not None:
        cargs.extend([
            "--binval",
            str(params.get("binval"))
        ])
    if params.get("binval_not") is not None:
        cargs.extend([
            "--binvalnot",
            str(params.get("binval_not"))
        ])
    if params.get("frame") is not None:
        cargs.extend([
            "--frame",
            str(params.get("frame"))
        ])
    if params.get("merge_volume") is not None:
        cargs.extend([
            "--merge",
            execution.input_file(params.get("merge_volume"))
        ])
    if params.get("mask_volume") is not None:
        cargs.extend([
            "--mask",
            execution.input_file(params.get("mask_volume"))
        ])
    if params.get("mask_threshold") is not None:
        cargs.extend([
            "--mask-thresh",
            str(params.get("mask_threshold"))
        ])
    if params.get("surf_name") is not None:
        cargs.extend([
            "--surf",
            params.get("surf_name")
        ])
    if params.get("surf_smooth") is not None:
        cargs.extend([
            "--surf-smooth",
            str(params.get("surf_smooth"))
        ])
    if params.get("threads") is not None:
        cargs.extend([
            "--threads",
            str(params.get("threads"))
        ])
    if params.get("ctx_wm_flag"):
        cargs.append("--ctx-wm")
    if params.get("all_wm_flag"):
        cargs.append("--all-wm")
    if params.get("ventricles_flag"):
        cargs.append("--ventricles")
    if params.get("wm_vcsf_flag"):
        cargs.append("--wm+vcsf")
    if params.get("gm_flag"):
        cargs.append("--gm")
    if params.get("subcort_gm_flag"):
        cargs.append("--subcort-gm")
    if params.get("scm_lh_flag"):
        cargs.append("--scm-lh")
    if params.get("scm_rh_flag"):
        cargs.append("--scm-rh")
    if params.get("zero_edges_flag"):
        cargs.append("--zero-edges")
    if params.get("zero_slice_edges_flag"):
        cargs.append("--zero-slice-edges")
    if params.get("dilate_vertex") is not None:
        cargs.extend([
            "--dilate-vertex",
            params.get("dilate_vertex")
        ])
    if params.get("remove_islands_flag"):
        cargs.append("--remove-islands")
    if params.get("fill_holes_flag"):
        cargs.append("--fill-holes")
    if params.get("noverbose_flag"):
        cargs.append("--noverbose")
    if params.get("debug_flag"):
        cargs.append("--debug")
    return cargs


def mri_binarize_outputs(
    params: MriBinarizeParameters,
    execution: Execution,
) -> MriBinarizeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriBinarizeOutputs(
        root=execution.output_file("."),
        out_volume=execution.output_file(params.get("output_volume")),
    )
    return ret


def mri_binarize_execute(
    params: MriBinarizeParameters,
    execution: Execution,
) -> MriBinarizeOutputs:
    """
    A program to binarize a volume or volume-encoded surface file, with options to
    merge and manipulate binarized output.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriBinarizeOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_binarize_cargs(params, execution)
    ret = mri_binarize_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_binarize(
    input_volume: InputPathType,
    output_volume: str,
    min_threshold: float | None = None,
    max_threshold: float | None = None,
    pct_threshold: float | None = None,
    rmin: float | None = None,
    rmax: float | None = None,
    fdr_threshold: float | None = None,
    match_values: list[float] | None = None,
    replace_values: list[float] | None = None,
    binval: float | None = None,
    binval_not: float | None = None,
    frame: float | None = None,
    merge_volume: InputPathType | None = None,
    mask_volume: InputPathType | None = None,
    mask_threshold: float | None = None,
    surf_name: str | None = None,
    surf_smooth: float | None = None,
    threads: float | None = None,
    ctx_wm_flag: bool = False,
    all_wm_flag: bool = False,
    ventricles_flag: bool = False,
    wm_vcsf_flag: bool = False,
    gm_flag: bool = False,
    subcort_gm_flag: bool = False,
    scm_lh_flag: bool = False,
    scm_rh_flag: bool = False,
    zero_edges_flag: bool = False,
    zero_slice_edges_flag: bool = False,
    dilate_vertex: str | None = None,
    remove_islands_flag: bool = False,
    fill_holes_flag: bool = False,
    noverbose_flag: bool = False,
    debug_flag: bool = False,
    runner: Runner | None = None,
) -> MriBinarizeOutputs:
    """
    A program to binarize a volume or volume-encoded surface file, with options to
    merge and manipulate binarized output.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume to be binarized.
        output_volume: Path to output volume.
        min_threshold: Minimum threshold (default is -inf).
        max_threshold: Maximum threshold (default is +inf).
        pct_threshold: Set threshold to capture top P% of voxels.
        rmin: Compute min threshold based on rmin times global mean.
        rmax: Compute max threshold based on rmax times global mean.
        fdr_threshold: Compute min threshold based on FDR.
        match_values: Binarize based on matching values.
        replace_values: Replace voxels with specified values. Format: V1 V2.
        binval: Set voxel value within threshold to specified value (default is\
            1).
        binval_not: Set voxel value outside threshold range to specified value\
            (default is 0).
        frame: Use specific frame of the input. 0-based index.
        merge_volume: Merge with another volume. Must be the same dimensions as\
            input volume.
        mask_volume: Mask input with a specified mask volume.
        mask_threshold: Set threshold for mask volume (default is 0.5).
        surf_name: Create a surface mesh from the binarization.
        surf_smooth: Smooth the surface mesh iteratively, specifying the number\
            of iterations.
        threads: Specify number of threads to use.
        ctx_wm_flag: Set match values for cerebral white matter.
        all_wm_flag: Set match values for all white matter.
        ventricles_flag: Set match values for ventricles and choroid.
        wm_vcsf_flag: Match for WM and ventricular CSF.
        gm_flag: Match for all WM, VCSF and background, then invert.
        subcort_gm_flag: Match for subcortical gray matter.
        scm_lh_flag: Subcortical mass for left hemisphere.
        scm_rh_flag: Subcortical mass for right hemisphere.
        zero_edges_flag: Set edge voxels to zero.
        zero_slice_edges_flag: Set edge slice voxels to zero.
        dilate_vertex: Dilate vertex to a specific target area.
        remove_islands_flag: Remove islands in the mask.
        fill_holes_flag: Remove holes in the mask.
        noverbose_flag: Suppress verbose output.
        debug_flag: Enable debugging output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriBinarizeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_BINARIZE_METADATA)
    params = mri_binarize_params(input_volume=input_volume, output_volume=output_volume, min_threshold=min_threshold, max_threshold=max_threshold, pct_threshold=pct_threshold, rmin=rmin, rmax=rmax, fdr_threshold=fdr_threshold, match_values=match_values, replace_values=replace_values, binval=binval, binval_not=binval_not, frame=frame, merge_volume=merge_volume, mask_volume=mask_volume, mask_threshold=mask_threshold, surf_name=surf_name, surf_smooth=surf_smooth, threads=threads, ctx_wm_flag=ctx_wm_flag, all_wm_flag=all_wm_flag, ventricles_flag=ventricles_flag, wm_vcsf_flag=wm_vcsf_flag, gm_flag=gm_flag, subcort_gm_flag=subcort_gm_flag, scm_lh_flag=scm_lh_flag, scm_rh_flag=scm_rh_flag, zero_edges_flag=zero_edges_flag, zero_slice_edges_flag=zero_slice_edges_flag, dilate_vertex=dilate_vertex, remove_islands_flag=remove_islands_flag, fill_holes_flag=fill_holes_flag, noverbose_flag=noverbose_flag, debug_flag=debug_flag)
    return mri_binarize_execute(params, execution)


__all__ = [
    "MRI_BINARIZE_METADATA",
    "MriBinarizeOutputs",
    "MriBinarizeParameters",
    "mri_binarize",
    "mri_binarize_params",
]
