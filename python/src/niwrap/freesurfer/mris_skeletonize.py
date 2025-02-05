# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_SKELETONIZE_METADATA = Metadata(
    id="0b067079e3dfa4d5ff1e1cf5bf10adf3ec69d818.boutiques",
    name="mris_skeletonize",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisSkeletonizeParameters = typing.TypedDict('MrisSkeletonizeParameters', {
    "__STYX_TYPE__": typing.Literal["mris_skeletonize"],
    "surface": str,
    "surfvals": str,
    "mask": str,
    "k1": bool,
    "curv_nonmaxsup": bool,
    "gyrus": bool,
    "sulcus": bool,
    "outdir": typing.NotRequired[str | None],
    "sphere": typing.NotRequired[str | None],
    "pointset": typing.NotRequired[str | None],
    "label": typing.NotRequired[str | None],
    "nbrsize": typing.NotRequired[float | None],
    "threshold": typing.NotRequired[float | None],
    "cluster": typing.NotRequired[float | None],
    "fwhm": typing.NotRequired[float | None],
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
        "mris_skeletonize": mris_skeletonize_cargs,
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
        "mris_skeletonize": mris_skeletonize_outputs,
    }
    return vt.get(t)


class MrisSkeletonizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_skeletonize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    skeleton_output: OutputPathType | None
    """Output skeletonized mask."""
    pointset_output: OutputPathType | None
    """Output point set of the skeleton."""
    skeleton_label: OutputPathType | None
    """Label file for the skeletonized output."""


def mris_skeletonize_params(
    surface: str,
    surfvals: str,
    mask: str,
    k1: bool = False,
    curv_nonmaxsup: bool = False,
    gyrus: bool = False,
    sulcus: bool = False,
    outdir: str | None = None,
    sphere: str | None = None,
    pointset: str | None = None,
    label: str | None = None,
    nbrsize: float | None = 2,
    threshold: float | None = None,
    cluster: float | None = None,
    fwhm: float | None = None,
) -> MrisSkeletonizeParameters:
    """
    Build parameters.
    
    Args:
        surface: Path to the surface file.
        surfvals: Pass input explicitly rather than computing it.
        mask: Final skeletonized mask file.
        k1: Use k1 from surface (not with --curv-nonmaxsup).
        curv_nonmaxsup: Use curvature H computed from surface with non-max\
            suppression (not with --k1).
        gyrus: Skeletonize the crowns of the gyri.
        sulcus: Skeletonize the fundi of the sulci.
        outdir: Directory where all outputs will be saved.
        sphere: Sphere path, only needed for nonmax suppression.
        pointset: Point set of the skeleton (PointSet.json).
        label: Surface label of the skeleton (label file path).
        nbrsize: Neighborhood size for 2nd FF (default is 2).
        threshold: Used to create initial mask that will be skeletonized\
            (typically about 0.3).
        cluster: Cluster the thresholded input and keep the largest nkeep\
            clusters.
        fwhm: Smooth surface values by this FWHM.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_skeletonize",
        "surface": surface,
        "surfvals": surfvals,
        "mask": mask,
        "k1": k1,
        "curv_nonmaxsup": curv_nonmaxsup,
        "gyrus": gyrus,
        "sulcus": sulcus,
    }
    if outdir is not None:
        params["outdir"] = outdir
    if sphere is not None:
        params["sphere"] = sphere
    if pointset is not None:
        params["pointset"] = pointset
    if label is not None:
        params["label"] = label
    if nbrsize is not None:
        params["nbrsize"] = nbrsize
    if threshold is not None:
        params["threshold"] = threshold
    if cluster is not None:
        params["cluster"] = cluster
    if fwhm is not None:
        params["fwhm"] = fwhm
    return params


def mris_skeletonize_cargs(
    params: MrisSkeletonizeParameters,
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
    cargs.append("mris_skeletonize")
    cargs.extend([
        "--surf",
        params.get("surface")
    ])
    cargs.extend([
        "--surfvals",
        params.get("surfvals")
    ])
    cargs.extend([
        "--mask",
        params.get("mask")
    ])
    if params.get("k1"):
        cargs.append("--k1")
    if params.get("curv_nonmaxsup"):
        cargs.append("--curv-nonmaxsup")
    if params.get("gyrus"):
        cargs.append("--gyrus")
    if params.get("sulcus"):
        cargs.append("--sulcus")
    if params.get("outdir") is not None:
        cargs.extend([
            "--outdir",
            params.get("outdir")
        ])
    if params.get("sphere") is not None:
        cargs.extend([
            "--sphere",
            params.get("sphere")
        ])
    if params.get("pointset") is not None:
        cargs.extend([
            "--ps",
            params.get("pointset")
        ])
    if params.get("label") is not None:
        cargs.extend([
            "--label",
            params.get("label")
        ])
    if params.get("nbrsize") is not None:
        cargs.extend([
            "--nbrsize",
            str(params.get("nbrsize"))
        ])
    if params.get("threshold") is not None:
        cargs.extend([
            "--threshold",
            str(params.get("threshold"))
        ])
    if params.get("cluster") is not None:
        cargs.extend([
            "--cluster",
            str(params.get("cluster"))
        ])
    if params.get("fwhm") is not None:
        cargs.extend([
            "--fwhm",
            str(params.get("fwhm"))
        ])
    return cargs


def mris_skeletonize_outputs(
    params: MrisSkeletonizeParameters,
    execution: Execution,
) -> MrisSkeletonizeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisSkeletonizeOutputs(
        root=execution.output_file("."),
        skeleton_output=execution.output_file(params.get("outdir") + "/skeleton.mgz") if (params.get("outdir") is not None) else None,
        pointset_output=execution.output_file(params.get("outdir") + "/PointSet.json") if (params.get("outdir") is not None) else None,
        skeleton_label=execution.output_file(params.get("outdir") + "/skeleton_label.mgz") if (params.get("outdir") is not None) else None,
    )
    return ret


def mris_skeletonize_execute(
    params: MrisSkeletonizeParameters,
    execution: Execution,
) -> MrisSkeletonizeOutputs:
    """
    Computes the skeleton of gyri (ie, the crowns) or sulci (ie, the fundi).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisSkeletonizeOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_skeletonize_cargs(params, execution)
    ret = mris_skeletonize_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_skeletonize(
    surface: str,
    surfvals: str,
    mask: str,
    k1: bool = False,
    curv_nonmaxsup: bool = False,
    gyrus: bool = False,
    sulcus: bool = False,
    outdir: str | None = None,
    sphere: str | None = None,
    pointset: str | None = None,
    label: str | None = None,
    nbrsize: float | None = 2,
    threshold: float | None = None,
    cluster: float | None = None,
    fwhm: float | None = None,
    runner: Runner | None = None,
) -> MrisSkeletonizeOutputs:
    """
    Computes the skeleton of gyri (ie, the crowns) or sulci (ie, the fundi).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surface: Path to the surface file.
        surfvals: Pass input explicitly rather than computing it.
        mask: Final skeletonized mask file.
        k1: Use k1 from surface (not with --curv-nonmaxsup).
        curv_nonmaxsup: Use curvature H computed from surface with non-max\
            suppression (not with --k1).
        gyrus: Skeletonize the crowns of the gyri.
        sulcus: Skeletonize the fundi of the sulci.
        outdir: Directory where all outputs will be saved.
        sphere: Sphere path, only needed for nonmax suppression.
        pointset: Point set of the skeleton (PointSet.json).
        label: Surface label of the skeleton (label file path).
        nbrsize: Neighborhood size for 2nd FF (default is 2).
        threshold: Used to create initial mask that will be skeletonized\
            (typically about 0.3).
        cluster: Cluster the thresholded input and keep the largest nkeep\
            clusters.
        fwhm: Smooth surface values by this FWHM.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisSkeletonizeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_SKELETONIZE_METADATA)
    params = mris_skeletonize_params(surface=surface, surfvals=surfvals, mask=mask, k1=k1, curv_nonmaxsup=curv_nonmaxsup, gyrus=gyrus, sulcus=sulcus, outdir=outdir, sphere=sphere, pointset=pointset, label=label, nbrsize=nbrsize, threshold=threshold, cluster=cluster, fwhm=fwhm)
    return mris_skeletonize_execute(params, execution)


__all__ = [
    "MRIS_SKELETONIZE_METADATA",
    "MrisSkeletonizeOutputs",
    "MrisSkeletonizeParameters",
    "mris_skeletonize",
    "mris_skeletonize_params",
]
