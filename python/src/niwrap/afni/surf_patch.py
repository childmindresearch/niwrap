# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURF_PATCH_METADATA = Metadata(
    id="1b9f54ccf622083c532013b3e22205e01ab00c46.boutiques",
    name="SurfPatch",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
SurfPatchParameters = typing.TypedDict('SurfPatchParameters', {
    "__STYX_TYPE__": typing.Literal["SurfPatch"],
    "spec_file": InputPathType,
    "surf_A": InputPathType,
    "surf_B": InputPathType,
    "nodefile": InputPathType,
    "inode": float,
    "ilabel": float,
    "prefix": str,
    "hits": typing.NotRequired[float | None],
    "masklabel": typing.NotRequired[str | None],
    "vol": bool,
    "vol_only": bool,
    "patch2surf": bool,
    "coord_gain": typing.NotRequired[float | None],
    "check_bowtie": bool,
    "fix_bowtie": bool,
    "ok_bowtie": bool,
    "adjust_contour": bool,
    "do_not_adjust_contour": bool,
    "stitched_surface": typing.NotRequired[InputPathType | None],
    "flip_orientation": bool,
    "verbosity": typing.NotRequired[float | None],
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
        "SurfPatch": surf_patch_cargs,
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
        "SurfPatch": surf_patch_outputs,
    }
    return vt.get(t)


class SurfPatchOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf_patch(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outpatch_a: OutputPathType
    """Output patch for surface A"""
    outpatch_b: OutputPathType
    """Output patch for surface B"""
    out_stitched_surface: OutputPathType
    """Stitched surface file"""


def surf_patch_params(
    spec_file: InputPathType,
    surf_a: InputPathType,
    surf_b: InputPathType,
    nodefile: InputPathType,
    inode: float,
    ilabel: float,
    prefix: str,
    hits: float | None = None,
    masklabel: str | None = None,
    vol: bool = False,
    vol_only: bool = False,
    patch2surf: bool = False,
    coord_gain: float | None = None,
    check_bowtie: bool = False,
    fix_bowtie: bool = False,
    ok_bowtie: bool = False,
    adjust_contour: bool = False,
    do_not_adjust_contour: bool = False,
    stitched_surface: InputPathType | None = None,
    flip_orientation: bool = False,
    verbosity: float | None = None,
) -> SurfPatchParameters:
    """
    Build parameters.
    
    Args:
        spec_file: Spec file containing input surfaces.
        surf_a: Input surface A.
        surf_b: Input surface B.
        nodefile: File containing nodes defining the patch.
        inode: Index of the column containing the nodes.
        ilabel: Index of the column containing labels of the nodes in column\
            inode.
        prefix: Prefix of output patch.
        hits: Minimum number of nodes specified for a triangle to be made a\
            part of the patch (1 <= min_hits <= 3); default is 2.
        masklabel: Only nodes that are labeled with this label are considered\
            for the patch.
        vol: Calculate the volume formed by the patch on surf_A and surf_B.\
            Requires only two surfaces specified with surf_A and surf_B.
        vol_only: Only calculate the volume, don't write out patches.
        patch2surf: Turn surface patch into a surface where only nodes used in\
            forming the mesh are preserved.
        coord_gain: Multiply node coordinates by a gain. Useful for enlarging\
            tiny patches for easier viewing in SUMA.
        check_bowtie: Check if the patch has a section hanging by one node to\
            the rest of the mesh. Default when -vol or -vol_only are used.
        fix_bowtie: Modify patch to eliminate bowties.
        ok_bowtie: Do not check for, or fix bowties. Default when -vol* are not\
            used.
        adjust_contour: Shrink patch contours at nodes that were not in\
            nodefile.
        do_not_adjust_contour: Do not adjust contours. This is the default.
        stitched_surface: Write out the stitched surface used to calculate the\
            volume.
        flip_orientation: Change orientation of triangles before writing\
            surfaces.
        verbosity: Set verbosity level, 1 is the default.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SurfPatch",
        "spec_file": spec_file,
        "surf_A": surf_a,
        "surf_B": surf_b,
        "nodefile": nodefile,
        "inode": inode,
        "ilabel": ilabel,
        "prefix": prefix,
        "vol": vol,
        "vol_only": vol_only,
        "patch2surf": patch2surf,
        "check_bowtie": check_bowtie,
        "fix_bowtie": fix_bowtie,
        "ok_bowtie": ok_bowtie,
        "adjust_contour": adjust_contour,
        "do_not_adjust_contour": do_not_adjust_contour,
        "flip_orientation": flip_orientation,
    }
    if hits is not None:
        params["hits"] = hits
    if masklabel is not None:
        params["masklabel"] = masklabel
    if coord_gain is not None:
        params["coord_gain"] = coord_gain
    if stitched_surface is not None:
        params["stitched_surface"] = stitched_surface
    if verbosity is not None:
        params["verbosity"] = verbosity
    return params


def surf_patch_cargs(
    params: SurfPatchParameters,
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
    cargs.append("SurfPatch")
    cargs.append(execution.input_file(params.get("spec_file")))
    cargs.extend([
        "-surf_A",
        execution.input_file(params.get("surf_A"))
    ])
    cargs.extend([
        "-surf_B",
        execution.input_file(params.get("surf_B"))
    ])
    cargs.extend([
        "-input",
        execution.input_file(params.get("nodefile"))
    ])
    cargs.append(str(params.get("inode")))
    cargs.append(str(params.get("ilabel")))
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("hits") is not None:
        cargs.extend([
            "-hits",
            str(params.get("hits"))
        ])
    if params.get("masklabel") is not None:
        cargs.extend([
            "-masklabel",
            params.get("masklabel")
        ])
    if params.get("vol"):
        cargs.append("-vol")
    if params.get("vol_only"):
        cargs.append("-vol_only")
    if params.get("patch2surf"):
        cargs.append("-patch2surf")
    if params.get("coord_gain") is not None:
        cargs.extend([
            "-coord_gain",
            str(params.get("coord_gain"))
        ])
    if params.get("check_bowtie"):
        cargs.append("-check_bowtie")
    if params.get("fix_bowtie"):
        cargs.append("-fix_bowtie")
    if params.get("ok_bowtie"):
        cargs.append("-ok_bowtie")
    if params.get("adjust_contour"):
        cargs.append("-adjust_contour")
    if params.get("do_not_adjust_contour"):
        cargs.append("-do-not-adjust_contour")
    if params.get("stitched_surface") is not None:
        cargs.extend([
            "-stitched_surface",
            execution.input_file(params.get("stitched_surface"))
        ])
    if params.get("flip_orientation"):
        cargs.append("-flip_orientation")
    if params.get("verbosity") is not None:
        cargs.extend([
            "-verb",
            str(params.get("verbosity"))
        ])
    return cargs


def surf_patch_outputs(
    params: SurfPatchParameters,
    execution: Execution,
) -> SurfPatchOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfPatchOutputs(
        root=execution.output_file("."),
        outpatch_a=execution.output_file(params.get("prefix") + "_A"),
        outpatch_b=execution.output_file(params.get("prefix") + "_B"),
        out_stitched_surface=execution.output_file(params.get("prefix") + "_stitched"),
    )
    return ret


def surf_patch_execute(
    params: SurfPatchParameters,
    execution: Execution,
) -> SurfPatchOutputs:
    """
    Creates a patch of surface formed by nodes in a nodefile and optionally
    calculates the volume between the same patch on two isotopic surfaces.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfPatchOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = surf_patch_cargs(params, execution)
    ret = surf_patch_outputs(params, execution)
    execution.run(cargs)
    return ret


def surf_patch(
    spec_file: InputPathType,
    surf_a: InputPathType,
    surf_b: InputPathType,
    nodefile: InputPathType,
    inode: float,
    ilabel: float,
    prefix: str,
    hits: float | None = None,
    masklabel: str | None = None,
    vol: bool = False,
    vol_only: bool = False,
    patch2surf: bool = False,
    coord_gain: float | None = None,
    check_bowtie: bool = False,
    fix_bowtie: bool = False,
    ok_bowtie: bool = False,
    adjust_contour: bool = False,
    do_not_adjust_contour: bool = False,
    stitched_surface: InputPathType | None = None,
    flip_orientation: bool = False,
    verbosity: float | None = None,
    runner: Runner | None = None,
) -> SurfPatchOutputs:
    """
    Creates a patch of surface formed by nodes in a nodefile and optionally
    calculates the volume between the same patch on two isotopic surfaces.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        spec_file: Spec file containing input surfaces.
        surf_a: Input surface A.
        surf_b: Input surface B.
        nodefile: File containing nodes defining the patch.
        inode: Index of the column containing the nodes.
        ilabel: Index of the column containing labels of the nodes in column\
            inode.
        prefix: Prefix of output patch.
        hits: Minimum number of nodes specified for a triangle to be made a\
            part of the patch (1 <= min_hits <= 3); default is 2.
        masklabel: Only nodes that are labeled with this label are considered\
            for the patch.
        vol: Calculate the volume formed by the patch on surf_A and surf_B.\
            Requires only two surfaces specified with surf_A and surf_B.
        vol_only: Only calculate the volume, don't write out patches.
        patch2surf: Turn surface patch into a surface where only nodes used in\
            forming the mesh are preserved.
        coord_gain: Multiply node coordinates by a gain. Useful for enlarging\
            tiny patches for easier viewing in SUMA.
        check_bowtie: Check if the patch has a section hanging by one node to\
            the rest of the mesh. Default when -vol or -vol_only are used.
        fix_bowtie: Modify patch to eliminate bowties.
        ok_bowtie: Do not check for, or fix bowties. Default when -vol* are not\
            used.
        adjust_contour: Shrink patch contours at nodes that were not in\
            nodefile.
        do_not_adjust_contour: Do not adjust contours. This is the default.
        stitched_surface: Write out the stitched surface used to calculate the\
            volume.
        flip_orientation: Change orientation of triangles before writing\
            surfaces.
        verbosity: Set verbosity level, 1 is the default.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfPatchOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF_PATCH_METADATA)
    params = surf_patch_params(spec_file=spec_file, surf_a=surf_a, surf_b=surf_b, nodefile=nodefile, inode=inode, ilabel=ilabel, prefix=prefix, hits=hits, masklabel=masklabel, vol=vol, vol_only=vol_only, patch2surf=patch2surf, coord_gain=coord_gain, check_bowtie=check_bowtie, fix_bowtie=fix_bowtie, ok_bowtie=ok_bowtie, adjust_contour=adjust_contour, do_not_adjust_contour=do_not_adjust_contour, stitched_surface=stitched_surface, flip_orientation=flip_orientation, verbosity=verbosity)
    return surf_patch_execute(params, execution)


__all__ = [
    "SURF_PATCH_METADATA",
    "SurfPatchOutputs",
    "SurfPatchParameters",
    "surf_patch",
    "surf_patch_params",
]
