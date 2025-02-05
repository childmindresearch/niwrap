# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

BET2_METADATA = Metadata(
    id="5366bd6b3b182667b9a0f23f9cf369e360294f91.boutiques",
    name="bet2",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
Bet2Parameters = typing.TypedDict('Bet2Parameters', {
    "__STYX_TYPE__": typing.Literal["bet2"],
    "input_fileroot": str,
    "output_fileroot": str,
    "fractional_intensity": typing.NotRequired[float | None],
    "vertical_gradient": typing.NotRequired[float | None],
    "center_of_gravity": typing.NotRequired[list[float] | None],
    "outline_flag": bool,
    "mask_flag": bool,
    "skull_flag": bool,
    "no_output_flag": bool,
    "mesh_flag": bool,
    "head_radius": typing.NotRequired[float | None],
    "smooth_factor": typing.NotRequired[float | None],
    "threshold_flag": bool,
    "verbose_flag": bool,
    "help_flag": bool,
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
        "bet2": bet2_cargs,
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
        "bet2": bet2_outputs,
    }
    return vt.get(t)


class Bet2Outputs(typing.NamedTuple):
    """
    Output object returned when calling `bet2(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_mask: OutputPathType
    """Binary brain mask output (if mask flag is set)"""
    output_skull: OutputPathType
    """Approximate skull image output (if skull flag is set)"""
    output_mesh: OutputPathType
    """Brain surface mesh output in VTK format (if mesh flag is set)"""
    output_overlay: OutputPathType
    """Brain surface outline overlaid onto original image (if outline flag is
    set)"""


def bet2_params(
    input_fileroot: str,
    output_fileroot: str,
    fractional_intensity: float | None = None,
    vertical_gradient: float | None = None,
    center_of_gravity: list[float] | None = None,
    outline_flag: bool = False,
    mask_flag: bool = False,
    skull_flag: bool = False,
    no_output_flag: bool = False,
    mesh_flag: bool = False,
    head_radius: float | None = None,
    smooth_factor: float | None = None,
    threshold_flag: bool = False,
    verbose_flag: bool = False,
    help_flag: bool = False,
) -> Bet2Parameters:
    """
    Build parameters.
    
    Args:
        input_fileroot: Input file root (e.g. img).
        output_fileroot: Output file root (e.g. img_bet).
        fractional_intensity: Fractional intensity threshold (0->1);\
            default=0.5; smaller values give larger brain outline estimates.
        vertical_gradient: Vertical gradient in fractional intensity threshold\
            (-1->1); default=0; positive values give larger brain outline at\
            bottom, smaller at top.
        center_of_gravity: The xyz coordinates of the center of gravity\
            (voxels, not mm) of initial mesh surface. Must have exactly three\
            numerical entries in the list (3-vector).
        outline_flag: Generate brain surface outline overlaid onto original\
            image.
        mask_flag: Generate binary brain mask.
        skull_flag: Generate approximate skull image.
        no_output_flag: Don't generate segmented brain image output.
        mesh_flag: Generate brain surface as mesh in vtk format.
        head_radius: Head radius (mm not voxels); initial surface sphere is set\
            to half of this.
        smooth_factor: Smoothness factor; default=1; values smaller than 1\
            produce more detailed brain surface, values larger than one produce\
            smoother, less detailed surface.
        threshold_flag: Apply thresholding to segmented brain image and mask.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display help message and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "bet2",
        "input_fileroot": input_fileroot,
        "output_fileroot": output_fileroot,
        "outline_flag": outline_flag,
        "mask_flag": mask_flag,
        "skull_flag": skull_flag,
        "no_output_flag": no_output_flag,
        "mesh_flag": mesh_flag,
        "threshold_flag": threshold_flag,
        "verbose_flag": verbose_flag,
        "help_flag": help_flag,
    }
    if fractional_intensity is not None:
        params["fractional_intensity"] = fractional_intensity
    if vertical_gradient is not None:
        params["vertical_gradient"] = vertical_gradient
    if center_of_gravity is not None:
        params["center_of_gravity"] = center_of_gravity
    if head_radius is not None:
        params["head_radius"] = head_radius
    if smooth_factor is not None:
        params["smooth_factor"] = smooth_factor
    return params


def bet2_cargs(
    params: Bet2Parameters,
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
    cargs.append("bet2")
    cargs.append(params.get("input_fileroot"))
    cargs.append(params.get("output_fileroot"))
    if params.get("fractional_intensity") is not None:
        cargs.extend([
            "-f",
            str(params.get("fractional_intensity"))
        ])
    if params.get("vertical_gradient") is not None:
        cargs.extend([
            "-g",
            str(params.get("vertical_gradient"))
        ])
    if params.get("center_of_gravity") is not None:
        cargs.extend([
            "-c",
            *map(str, params.get("center_of_gravity"))
        ])
    if params.get("outline_flag"):
        cargs.append("-o")
    if params.get("mask_flag"):
        cargs.append("-m")
    if params.get("skull_flag"):
        cargs.append("-s")
    if params.get("no_output_flag"):
        cargs.append("-n")
    if params.get("mesh_flag"):
        cargs.append("-e")
    if params.get("head_radius") is not None:
        cargs.extend([
            "-r",
            str(params.get("head_radius"))
        ])
    if params.get("smooth_factor") is not None:
        cargs.extend([
            "-w",
            str(params.get("smooth_factor"))
        ])
    if params.get("threshold_flag"):
        cargs.append("-t")
    if params.get("verbose_flag"):
        cargs.append("-v")
    if params.get("help_flag"):
        cargs.append("-h")
    return cargs


def bet2_outputs(
    params: Bet2Parameters,
    execution: Execution,
) -> Bet2Outputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Bet2Outputs(
        root=execution.output_file("."),
        output_mask=execution.output_file(params.get("output_fileroot") + "_mask.nii.gz"),
        output_skull=execution.output_file(params.get("output_fileroot") + "_skull.nii.gz"),
        output_mesh=execution.output_file(params.get("output_fileroot") + "_mesh.vtk"),
        output_overlay=execution.output_file(params.get("output_fileroot") + "_overlay.nii.gz"),
    )
    return ret


def bet2_execute(
    params: Bet2Parameters,
    execution: Execution,
) -> Bet2Outputs:
    """
    Automated brain extraction tool for FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Bet2Outputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = bet2_cargs(params, execution)
    ret = bet2_outputs(params, execution)
    execution.run(cargs)
    return ret


def bet2(
    input_fileroot: str,
    output_fileroot: str,
    fractional_intensity: float | None = None,
    vertical_gradient: float | None = None,
    center_of_gravity: list[float] | None = None,
    outline_flag: bool = False,
    mask_flag: bool = False,
    skull_flag: bool = False,
    no_output_flag: bool = False,
    mesh_flag: bool = False,
    head_radius: float | None = None,
    smooth_factor: float | None = None,
    threshold_flag: bool = False,
    verbose_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> Bet2Outputs:
    """
    Automated brain extraction tool for FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_fileroot: Input file root (e.g. img).
        output_fileroot: Output file root (e.g. img_bet).
        fractional_intensity: Fractional intensity threshold (0->1);\
            default=0.5; smaller values give larger brain outline estimates.
        vertical_gradient: Vertical gradient in fractional intensity threshold\
            (-1->1); default=0; positive values give larger brain outline at\
            bottom, smaller at top.
        center_of_gravity: The xyz coordinates of the center of gravity\
            (voxels, not mm) of initial mesh surface. Must have exactly three\
            numerical entries in the list (3-vector).
        outline_flag: Generate brain surface outline overlaid onto original\
            image.
        mask_flag: Generate binary brain mask.
        skull_flag: Generate approximate skull image.
        no_output_flag: Don't generate segmented brain image output.
        mesh_flag: Generate brain surface as mesh in vtk format.
        head_radius: Head radius (mm not voxels); initial surface sphere is set\
            to half of this.
        smooth_factor: Smoothness factor; default=1; values smaller than 1\
            produce more detailed brain surface, values larger than one produce\
            smoother, less detailed surface.
        threshold_flag: Apply thresholding to segmented brain image and mask.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display help message and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Bet2Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BET2_METADATA)
    params = bet2_params(input_fileroot=input_fileroot, output_fileroot=output_fileroot, fractional_intensity=fractional_intensity, vertical_gradient=vertical_gradient, center_of_gravity=center_of_gravity, outline_flag=outline_flag, mask_flag=mask_flag, skull_flag=skull_flag, no_output_flag=no_output_flag, mesh_flag=mesh_flag, head_radius=head_radius, smooth_factor=smooth_factor, threshold_flag=threshold_flag, verbose_flag=verbose_flag, help_flag=help_flag)
    return bet2_execute(params, execution)


__all__ = [
    "BET2_METADATA",
    "Bet2Outputs",
    "Bet2Parameters",
    "bet2",
    "bet2_params",
]
