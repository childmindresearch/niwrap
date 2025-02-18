# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

BRAIN_SKIN_METADATA = Metadata(
    id="4f110568466cb173a0801348ecaabe46ca587148.boutiques",
    name="BrainSkin",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
BrainSkinParameters = typing.TypedDict('BrainSkinParameters', {
    "__STYX_TYPE__": typing.Literal["BrainSkin"],
    "surface": str,
    "skingrid_volume": InputPathType,
    "prefix": str,
    "plimit": typing.NotRequired[float | None],
    "dlimit": typing.NotRequired[float | None],
    "segdo": typing.NotRequired[str | None],
    "voxelize": typing.NotRequired[str | None],
    "infill": typing.NotRequired[str | None],
    "out_file": typing.NotRequired[InputPathType | None],
    "vol_hull": typing.NotRequired[InputPathType | None],
    "no_zero_attraction": bool,
    "node_dbg": typing.NotRequired[float | None],
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
        "BrainSkin": brain_skin_cargs,
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
        "BrainSkin": brain_skin_outputs,
    }.get(t)


class BrainSkinOutputs(typing.NamedTuple):
    """
    Output object returned when calling `brain_skin(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    stitch_surface: OutputPathType
    """A bunch of triangles for closing the surface."""
    initial_skin_surface: OutputPathType
    """Initial skin surface"""
    reduced_skin_surface: OutputPathType
    """Reduced mesh version of initial skin surface."""
    inflated_skin_surface: OutputPathType
    """Original surface inflated inside skin surface."""
    patching_voxels: OutputPathType
    """Surface patching voxels."""
    surf_voxels: OutputPathType
    """Voxels inside original surface"""
    skin_voxels: OutputPathType
    """Mix of ptchvox and surfvox."""
    infilled_voxels: OutputPathType
    """Skin vox dataset filled in."""
    node_pairs_results: OutputPathType
    """Results of computations for finding node pairs that span sulci."""
    inflating_surface_results: OutputPathType
    """Results of computations for inflating initial surface inside skin
    surface."""
    segments_display: OutputPathType
    """Segments between node pairs spanning sulci."""


def brain_skin_params(
    surface: str,
    skingrid_volume: InputPathType,
    prefix: str,
    plimit: float | None = None,
    dlimit: float | None = None,
    segdo: str | None = None,
    voxelize: str | None = None,
    infill: str | None = None,
    out_file: InputPathType | None = None,
    vol_hull: InputPathType | None = None,
    no_zero_attraction: bool = False,
    node_dbg: float | None = None,
) -> BrainSkinParameters:
    """
    Build parameters.
    
    Args:
        surface: Surface to smooth or the domain over which DSET is defined.
        skingrid_volume: A high-res volume to provide a grid for voxelization\
            steps.
        prefix: Prefix to use for variety of output files.
        plimit: Maximum length of path along surface in mm for node pairing.
        dlimit: Maximum length of Euclidean distance in mm for node pairing.
        segdo: Output a displayable object file that contains segments between\
            paired nodes.
        voxelize: Voxelization method. Choose from: slow: Sure footed but slow,\
            fast: Faster and works OK, mask: Fastest and works OK too (default).
        infill: Infill method. Choose from: slow: proper infill, but not\
            needed, fast: brutish infill, all we need (default).
        out_file: Output intermediary results from skin forming step.
        vol_hull: Deform an Icosahedron to match the convex hull of a mask\
            volume.
        no_zero_attraction: With vol_skin, the surface will try to shrink\
            aggressively, even if there is no promise of non-zero values below.
        node_dbg: Output debugging information for node N for -vol_skin and\
            -vol_hull options.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "BrainSkin",
        "surface": surface,
        "skingrid_volume": skingrid_volume,
        "prefix": prefix,
        "no_zero_attraction": no_zero_attraction,
    }
    if plimit is not None:
        params["plimit"] = plimit
    if dlimit is not None:
        params["dlimit"] = dlimit
    if segdo is not None:
        params["segdo"] = segdo
    if voxelize is not None:
        params["voxelize"] = voxelize
    if infill is not None:
        params["infill"] = infill
    if out_file is not None:
        params["out_file"] = out_file
    if vol_hull is not None:
        params["vol_hull"] = vol_hull
    if node_dbg is not None:
        params["node_dbg"] = node_dbg
    return params


def brain_skin_cargs(
    params: BrainSkinParameters,
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
    cargs.append("BrainSkin")
    cargs.append(params.get("surface"))
    cargs.extend([
        "-skingrid",
        execution.input_file(params.get("skingrid_volume"))
    ])
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("plimit") is not None:
        cargs.extend([
            "-plimit",
            str(params.get("plimit"))
        ])
    if params.get("dlimit") is not None:
        cargs.extend([
            "-dlimit",
            str(params.get("dlimit"))
        ])
    if params.get("segdo") is not None:
        cargs.extend([
            "-segdo",
            params.get("segdo")
        ])
    if params.get("voxelize") is not None:
        cargs.extend([
            "-voxelize",
            params.get("voxelize")
        ])
    if params.get("infill") is not None:
        cargs.extend([
            "-infill",
            params.get("infill")
        ])
    if params.get("out_file") is not None:
        cargs.extend([
            "-out",
            execution.input_file(params.get("out_file"))
        ])
    if params.get("vol_hull") is not None:
        cargs.extend([
            "-vol_hull",
            execution.input_file(params.get("vol_hull"))
        ])
    if params.get("no_zero_attraction"):
        cargs.append("-no_zero_attraction")
    if params.get("node_dbg") is not None:
        cargs.extend([
            "-node_dbg",
            str(params.get("node_dbg"))
        ])
    return cargs


def brain_skin_outputs(
    params: BrainSkinParameters,
    execution: Execution,
) -> BrainSkinOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BrainSkinOutputs(
        root=execution.output_file("."),
        stitch_surface=execution.output_file(params.get("prefix") + ".stitch.gii"),
        initial_skin_surface=execution.output_file(params.get("prefix") + ".skin.gii"),
        reduced_skin_surface=execution.output_file(params.get("prefix") + ".skin_simp.gii"),
        inflated_skin_surface=execution.output_file(params.get("prefix") + ".skin.isotopic.gii"),
        patching_voxels=execution.output_file(params.get("prefix") + ".ptchvox+orig"),
        surf_voxels=execution.output_file(params.get("prefix") + ".surfvox+orig"),
        skin_voxels=execution.output_file(params.get("prefix") + ".skinvox+orig"),
        infilled_voxels=execution.output_file(params.get("prefix") + ".infilled+orig"),
        node_pairs_results=execution.output_file(params.get("prefix") + ".niml.dset"),
        inflating_surface_results=execution.output_file(params.get("prefix") + ".areas.niml.dset"),
        segments_display=execution.output_file(params.get("prefix") + ".1D.do"),
    )
    return ret


def brain_skin_execute(
    params: BrainSkinParameters,
    execution: Execution,
) -> BrainSkinOutputs:
    """
    A program to create an unfolded surface that wraps the brain (skin) and
    Gyrification Indices.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BrainSkinOutputs`).
    """
    params = execution.params(params)
    cargs = brain_skin_cargs(params, execution)
    ret = brain_skin_outputs(params, execution)
    execution.run(cargs)
    return ret


def brain_skin(
    surface: str,
    skingrid_volume: InputPathType,
    prefix: str,
    plimit: float | None = None,
    dlimit: float | None = None,
    segdo: str | None = None,
    voxelize: str | None = None,
    infill: str | None = None,
    out_file: InputPathType | None = None,
    vol_hull: InputPathType | None = None,
    no_zero_attraction: bool = False,
    node_dbg: float | None = None,
    runner: Runner | None = None,
) -> BrainSkinOutputs:
    """
    A program to create an unfolded surface that wraps the brain (skin) and
    Gyrification Indices.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        surface: Surface to smooth or the domain over which DSET is defined.
        skingrid_volume: A high-res volume to provide a grid for voxelization\
            steps.
        prefix: Prefix to use for variety of output files.
        plimit: Maximum length of path along surface in mm for node pairing.
        dlimit: Maximum length of Euclidean distance in mm for node pairing.
        segdo: Output a displayable object file that contains segments between\
            paired nodes.
        voxelize: Voxelization method. Choose from: slow: Sure footed but slow,\
            fast: Faster and works OK, mask: Fastest and works OK too (default).
        infill: Infill method. Choose from: slow: proper infill, but not\
            needed, fast: brutish infill, all we need (default).
        out_file: Output intermediary results from skin forming step.
        vol_hull: Deform an Icosahedron to match the convex hull of a mask\
            volume.
        no_zero_attraction: With vol_skin, the surface will try to shrink\
            aggressively, even if there is no promise of non-zero values below.
        node_dbg: Output debugging information for node N for -vol_skin and\
            -vol_hull options.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BrainSkinOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BRAIN_SKIN_METADATA)
    params = brain_skin_params(surface=surface, skingrid_volume=skingrid_volume, prefix=prefix, plimit=plimit, dlimit=dlimit, segdo=segdo, voxelize=voxelize, infill=infill, out_file=out_file, vol_hull=vol_hull, no_zero_attraction=no_zero_attraction, node_dbg=node_dbg)
    return brain_skin_execute(params, execution)


__all__ = [
    "BRAIN_SKIN_METADATA",
    "BrainSkinOutputs",
    "BrainSkinParameters",
    "brain_skin",
    "brain_skin_params",
]
