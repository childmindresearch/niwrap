# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MAKE_BIANCA_MASK_METADATA = Metadata(
    id="6301fdafc66328cb8c345bedf78a2080c05aa6ca.boutiques",
    name="make_bianca_mask",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
MakeBiancaMaskParameters = typing.TypedDict('MakeBiancaMaskParameters', {
    "__STYX_TYPE__": typing.Literal["make_bianca_mask"],
    "input_image": InputPathType,
    "output_image": str,
    "overlay_flag": bool,
    "binary_mask_flag": bool,
    "approx_skull_flag": bool,
    "no_seg_output_flag": bool,
    "fractional_intensity": typing.NotRequired[float | None],
    "vg_fractional_intensity": typing.NotRequired[float | None],
    "head_radius": typing.NotRequired[float | None],
    "center_of_gravity": typing.NotRequired[str | None],
    "thresholding_flag": bool,
    "vtk_mesh": bool,
    "robust_iters_flag": bool,
    "residual_optic_cleanup_flag": bool,
    "reduce_bias_flag": bool,
    "slice_padding_flag": bool,
    "whole_set_mask_flag": bool,
    "additional_surfaces_flag": bool,
    "additional_surfaces_t2": typing.NotRequired[InputPathType | None],
    "verbose_flag": bool,
    "debug_flag": bool,
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
        "make_bianca_mask": make_bianca_mask_cargs,
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
        "make_bianca_mask": make_bianca_mask_outputs,
    }.get(t)


class MakeBiancaMaskOutputs(typing.NamedTuple):
    """
    Output object returned when calling `make_bianca_mask(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image: OutputPathType
    """Output image"""


def make_bianca_mask_params(
    input_image: InputPathType,
    output_image: str,
    overlay_flag: bool = False,
    binary_mask_flag: bool = False,
    approx_skull_flag: bool = False,
    no_seg_output_flag: bool = False,
    fractional_intensity: float | None = None,
    vg_fractional_intensity: float | None = None,
    head_radius: float | None = None,
    center_of_gravity: str | None = None,
    thresholding_flag: bool = False,
    vtk_mesh: bool = False,
    robust_iters_flag: bool = False,
    residual_optic_cleanup_flag: bool = False,
    reduce_bias_flag: bool = False,
    slice_padding_flag: bool = False,
    whole_set_mask_flag: bool = False,
    additional_surfaces_flag: bool = False,
    additional_surfaces_t2: InputPathType | None = None,
    verbose_flag: bool = False,
    debug_flag: bool = False,
) -> MakeBiancaMaskParameters:
    """
    Build parameters.
    
    Args:
        input_image: Input image.
        output_image: Output image.
        overlay_flag: Generate brain surface outline overlaid onto original\
            image.
        binary_mask_flag: Generate binary brain mask.
        approx_skull_flag: Generate approximate skull image.
        no_seg_output_flag: Don't generate segmented brain image output.
        fractional_intensity: Fractional intensity threshold (0->1);\
            default=0.5; smaller values give larger brain outline estimates.
        vg_fractional_intensity: Vertical gradient in fractional intensity\
            threshold (-1->1); default=0; positive values give larger brain outline\
            at bottom, smaller at top.
        head_radius: Head radius (mm not voxels); initial surface sphere is set\
            to half of this.
        center_of_gravity: Centre-of-gravity (voxels not mm) of initial mesh\
            surface.
        thresholding_flag: Apply thresholding to segmented brain image and mask.
        vtk_mesh: Generates brain surface as mesh in .vtk format.
        robust_iters_flag: Robust brain center estimation (iterates BET several\
            times).
        residual_optic_cleanup_flag: Eye & optic nerve cleanup (can be useful\
            in SIENA - disables -o option).
        reduce_bias_flag: Bias field & neck cleanup (can be useful in SIENA).
        slice_padding_flag: Improve BET if FOV is very small in Z (by\
            temporarily padding end slices).
        whole_set_mask_flag: Apply to 4D FMRI data (uses -f 0.3 and dilates\
            brain mask slightly).
        additional_surfaces_flag: Run bet2 and then betsurf to get additional\
            skull and scalp surfaces (includes registrations).
        additional_surfaces_t2: As with -A, when also feeding in\
            non-brain-extracted T2 (includes registrations).
        verbose_flag: Verbose (switch on diagnostic messages).
        debug_flag: Debug (don't delete temporary intermediate images).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "make_bianca_mask",
        "input_image": input_image,
        "output_image": output_image,
        "overlay_flag": overlay_flag,
        "binary_mask_flag": binary_mask_flag,
        "approx_skull_flag": approx_skull_flag,
        "no_seg_output_flag": no_seg_output_flag,
        "thresholding_flag": thresholding_flag,
        "vtk_mesh": vtk_mesh,
        "robust_iters_flag": robust_iters_flag,
        "residual_optic_cleanup_flag": residual_optic_cleanup_flag,
        "reduce_bias_flag": reduce_bias_flag,
        "slice_padding_flag": slice_padding_flag,
        "whole_set_mask_flag": whole_set_mask_flag,
        "additional_surfaces_flag": additional_surfaces_flag,
        "verbose_flag": verbose_flag,
        "debug_flag": debug_flag,
    }
    if fractional_intensity is not None:
        params["fractional_intensity"] = fractional_intensity
    if vg_fractional_intensity is not None:
        params["vg_fractional_intensity"] = vg_fractional_intensity
    if head_radius is not None:
        params["head_radius"] = head_radius
    if center_of_gravity is not None:
        params["center_of_gravity"] = center_of_gravity
    if additional_surfaces_t2 is not None:
        params["additional_surfaces_t2"] = additional_surfaces_t2
    return params


def make_bianca_mask_cargs(
    params: MakeBiancaMaskParameters,
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
    cargs.append("make_bianca_mask")
    cargs.append(execution.input_file(params.get("input_image")))
    cargs.append(params.get("output_image"))
    if params.get("overlay_flag"):
        cargs.append("-o")
    if params.get("binary_mask_flag"):
        cargs.append("-m")
    if params.get("approx_skull_flag"):
        cargs.append("-s")
    if params.get("no_seg_output_flag"):
        cargs.append("-n")
    if params.get("fractional_intensity") is not None:
        cargs.extend([
            "-f",
            str(params.get("fractional_intensity"))
        ])
    if params.get("vg_fractional_intensity") is not None:
        cargs.extend([
            "-g",
            str(params.get("vg_fractional_intensity"))
        ])
    if params.get("head_radius") is not None:
        cargs.extend([
            "-r",
            str(params.get("head_radius"))
        ])
    if params.get("center_of_gravity") is not None:
        cargs.extend([
            "-c",
            params.get("center_of_gravity")
        ])
    if params.get("thresholding_flag"):
        cargs.append("-t")
    if params.get("vtk_mesh"):
        cargs.append("-e")
    if params.get("robust_iters_flag"):
        cargs.append("-R")
    if params.get("residual_optic_cleanup_flag"):
        cargs.append("-S")
    if params.get("reduce_bias_flag"):
        cargs.append("-B")
    if params.get("slice_padding_flag"):
        cargs.append("-Z")
    if params.get("whole_set_mask_flag"):
        cargs.append("-F")
    if params.get("additional_surfaces_flag"):
        cargs.append("-A")
    if params.get("additional_surfaces_t2") is not None:
        cargs.extend([
            "-A2",
            execution.input_file(params.get("additional_surfaces_t2"))
        ])
    if params.get("verbose_flag"):
        cargs.append("-v")
    if params.get("debug_flag"):
        cargs.append("-d")
    return cargs


def make_bianca_mask_outputs(
    params: MakeBiancaMaskParameters,
    execution: Execution,
) -> MakeBiancaMaskOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MakeBiancaMaskOutputs(
        root=execution.output_file("."),
        output_image=execution.output_file(params.get("output_image")),
    )
    return ret


def make_bianca_mask_execute(
    params: MakeBiancaMaskParameters,
    execution: Execution,
) -> MakeBiancaMaskOutputs:
    """
    A script for generating BIANCA masks.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MakeBiancaMaskOutputs`).
    """
    params = execution.params(params)
    cargs = make_bianca_mask_cargs(params, execution)
    ret = make_bianca_mask_outputs(params, execution)
    execution.run(cargs)
    return ret


def make_bianca_mask(
    input_image: InputPathType,
    output_image: str,
    overlay_flag: bool = False,
    binary_mask_flag: bool = False,
    approx_skull_flag: bool = False,
    no_seg_output_flag: bool = False,
    fractional_intensity: float | None = None,
    vg_fractional_intensity: float | None = None,
    head_radius: float | None = None,
    center_of_gravity: str | None = None,
    thresholding_flag: bool = False,
    vtk_mesh: bool = False,
    robust_iters_flag: bool = False,
    residual_optic_cleanup_flag: bool = False,
    reduce_bias_flag: bool = False,
    slice_padding_flag: bool = False,
    whole_set_mask_flag: bool = False,
    additional_surfaces_flag: bool = False,
    additional_surfaces_t2: InputPathType | None = None,
    verbose_flag: bool = False,
    debug_flag: bool = False,
    runner: Runner | None = None,
) -> MakeBiancaMaskOutputs:
    """
    A script for generating BIANCA masks.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_image: Input image.
        output_image: Output image.
        overlay_flag: Generate brain surface outline overlaid onto original\
            image.
        binary_mask_flag: Generate binary brain mask.
        approx_skull_flag: Generate approximate skull image.
        no_seg_output_flag: Don't generate segmented brain image output.
        fractional_intensity: Fractional intensity threshold (0->1);\
            default=0.5; smaller values give larger brain outline estimates.
        vg_fractional_intensity: Vertical gradient in fractional intensity\
            threshold (-1->1); default=0; positive values give larger brain outline\
            at bottom, smaller at top.
        head_radius: Head radius (mm not voxels); initial surface sphere is set\
            to half of this.
        center_of_gravity: Centre-of-gravity (voxels not mm) of initial mesh\
            surface.
        thresholding_flag: Apply thresholding to segmented brain image and mask.
        vtk_mesh: Generates brain surface as mesh in .vtk format.
        robust_iters_flag: Robust brain center estimation (iterates BET several\
            times).
        residual_optic_cleanup_flag: Eye & optic nerve cleanup (can be useful\
            in SIENA - disables -o option).
        reduce_bias_flag: Bias field & neck cleanup (can be useful in SIENA).
        slice_padding_flag: Improve BET if FOV is very small in Z (by\
            temporarily padding end slices).
        whole_set_mask_flag: Apply to 4D FMRI data (uses -f 0.3 and dilates\
            brain mask slightly).
        additional_surfaces_flag: Run bet2 and then betsurf to get additional\
            skull and scalp surfaces (includes registrations).
        additional_surfaces_t2: As with -A, when also feeding in\
            non-brain-extracted T2 (includes registrations).
        verbose_flag: Verbose (switch on diagnostic messages).
        debug_flag: Debug (don't delete temporary intermediate images).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MakeBiancaMaskOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAKE_BIANCA_MASK_METADATA)
    params = make_bianca_mask_params(input_image=input_image, output_image=output_image, overlay_flag=overlay_flag, binary_mask_flag=binary_mask_flag, approx_skull_flag=approx_skull_flag, no_seg_output_flag=no_seg_output_flag, fractional_intensity=fractional_intensity, vg_fractional_intensity=vg_fractional_intensity, head_radius=head_radius, center_of_gravity=center_of_gravity, thresholding_flag=thresholding_flag, vtk_mesh=vtk_mesh, robust_iters_flag=robust_iters_flag, residual_optic_cleanup_flag=residual_optic_cleanup_flag, reduce_bias_flag=reduce_bias_flag, slice_padding_flag=slice_padding_flag, whole_set_mask_flag=whole_set_mask_flag, additional_surfaces_flag=additional_surfaces_flag, additional_surfaces_t2=additional_surfaces_t2, verbose_flag=verbose_flag, debug_flag=debug_flag)
    return make_bianca_mask_execute(params, execution)


__all__ = [
    "MAKE_BIANCA_MASK_METADATA",
    "MakeBiancaMaskOutputs",
    "MakeBiancaMaskParameters",
    "make_bianca_mask",
    "make_bianca_mask_params",
]
