# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

BET_FSL_METADATA = Metadata(
    id="05134dd9049bee70d91cad11059af4110900a569.boutiques",
    name="bet.fsl",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class BetFslOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bet_fsl(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Main default mask output of BET"""
    binary_mask: OutputPathType
    """Binary mask file (from -m option)"""
    overlay_file: OutputPathType
    """Overlaid brain surface onto original image"""
    approx_skull_img: OutputPathType
    """Approximate skull image file"""
    output_vtk_mesh: OutputPathType
    """Mesh in VTK format"""
    skull_mask: OutputPathType
    """Output mask for skull image"""
    out_inskull_mask: OutputPathType
    """The in-skull mask file from betsurf"""
    out_inskull_mesh: OutputPathType
    """The in-skull mesh file from betsurf"""
    out_inskull_off: OutputPathType
    """The in-skull mesh .off file from betsurf"""
    out_outskin_mask: OutputPathType
    """The out-skin mask file from betsurf"""
    out_outskin_mesh: OutputPathType
    """The out-skin mesh file from betsurf"""
    out_outskin_off: OutputPathType
    """The out-skin mesh .off file from betsurf"""
    out_outskull_mask: OutputPathType
    """The out-skull mask file from betsurf"""
    out_outskull_mesh: OutputPathType
    """The out-skull mesh file from betsurf"""
    out_outskull_off: OutputPathType
    """The out-skull mesh .off file from betsurf"""


def bet_fsl(
    infile: InputPathType,
    maskfile: str = "img_bet",
    fractional_intensity: float | None = None,
    vg_fractional_intensity: float | None = None,
    center_of_gravity: list[float] | None = None,
    overlay: bool = False,
    binary_mask: bool = False,
    approx_skull: bool = False,
    no_seg_output: bool = False,
    vtk_mesh: bool = False,
    head_radius: float | None = None,
    thresholding: bool = False,
    robust_iters: bool = False,
    residual_optic_cleanup: bool = False,
    reduce_bias: bool = False,
    slice_padding: bool = False,
    whole_set_mask: bool = False,
    additional_surfaces: bool = False,
    additional_surfaces_t2: InputPathType | None = None,
    verbose: bool = False,
    debug: bool = False,
    runner: Runner | None = None,
) -> BetFslOutputs:
    """
    Automated brain extraction tool for FSL.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        infile: Input image (e.g. img.nii.gz).
        maskfile: Output brain mask (e.g. img_bet.nii.gz).
        fractional_intensity: Fractional intensity threshold (0->1);\
            default=0.5; smaller values give larger brain outline estimates.
        vg_fractional_intensity: Vertical gradient in fractional intensity\
            threshold (-1->1); default=0; positive values give larger brain outline\
            at bottom, smaller at top.
        center_of_gravity: The xyz coordinates of the center of gravity\
            (voxels, not mm) of initial mesh surface. Must have exactly three\
            numerical entries in the list (3-vector).
        overlay: Generate brain surface outline overlaid onto original image.
        binary_mask: Generate binary brain mask.
        approx_skull: Generate approximate skull image.
        no_seg_output: Don't generate segmented brain image output.
        vtk_mesh: Generate brain surface as mesh in .vtk format.
        head_radius: Head radius (mm not voxels); initial surface sphere is set\
            to half of this.
        thresholding: Apply thresholding to segmented brain image and mask.
        robust_iters: Robust brain centre estimation (iterates BET several\
            times).
        residual_optic_cleanup: Eye & optic nerve cleanup (can be useful in\
            SIENA).
        reduce_bias: Bias field & neck cleanup (can be useful in SIENA).
        slice_padding: Improve BET if FOV is very small in Z (by temporarily\
            padding end slices).
        whole_set_mask: Apply to 4D FMRI data (uses -f 0.3 and dilates brain\
            mask slightly).
        additional_surfaces: Run bet2 and then betsurf to get additional skull\
            and scalp surfaces (includes registrations).
        additional_surfaces_t2: As with -A, when also feeding in\
            non-brain-extracted T2 (includes registrations).
        verbose: Verbose (switch on diagnostic messages).
        debug: Debug (don't delete temporary intermediate images).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BetFslOutputs`).
    """
    if fractional_intensity is not None and not (0 <= fractional_intensity <= 1): 
        raise ValueError(f"'fractional_intensity' must be between 0 <= x <= 1 but was {fractional_intensity}")
    if vg_fractional_intensity is not None and not (-1 <= vg_fractional_intensity <= 1): 
        raise ValueError(f"'vg_fractional_intensity' must be between -1 <= x <= 1 but was {vg_fractional_intensity}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(BET_FSL_METADATA)
    cargs = []
    cargs.append("bet.fsl")
    cargs.append(execution.input_file(infile))
    cargs.append(maskfile)
    if fractional_intensity is not None:
        cargs.extend([
            "-f",
            str(fractional_intensity)
        ])
    if vg_fractional_intensity is not None:
        cargs.extend([
            "-g",
            str(vg_fractional_intensity)
        ])
    if center_of_gravity is not None:
        cargs.extend([
            "-c",
            *map(str, center_of_gravity)
        ])
    if overlay:
        cargs.append("-o")
    if binary_mask:
        cargs.append("-m")
    if approx_skull:
        cargs.append("-s")
    if no_seg_output:
        cargs.append("-n")
    if vtk_mesh:
        cargs.append("-e")
    if head_radius is not None:
        cargs.extend([
            "-r",
            str(head_radius)
        ])
    if thresholding:
        cargs.append("-t")
    if robust_iters:
        cargs.append("-R")
    if residual_optic_cleanup:
        cargs.append("-S")
    if reduce_bias:
        cargs.append("-B")
    if slice_padding:
        cargs.append("-Z")
    if whole_set_mask:
        cargs.append("-F")
    if additional_surfaces:
        cargs.append("-A")
    if additional_surfaces_t2 is not None:
        cargs.extend([
            "-A2",
            execution.input_file(additional_surfaces_t2)
        ])
    if verbose:
        cargs.append("-v")
    if debug:
        cargs.append("-d")
    ret = BetFslOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(maskfile + ".nii.gz"),
        binary_mask=execution.output_file(maskfile + "_mask.nii.gz"),
        overlay_file=execution.output_file(maskfile + "_overlay.nii.gz"),
        approx_skull_img=execution.output_file(maskfile + "_skull.nii.gz"),
        output_vtk_mesh=execution.output_file(maskfile + "_mesh.vtk"),
        skull_mask=execution.output_file(maskfile + "_skull_mask.nii.gz"),
        out_inskull_mask=execution.output_file(maskfile + "_inskull_mask.nii.gz"),
        out_inskull_mesh=execution.output_file(maskfile + "_inskull_mesh.nii.gz"),
        out_inskull_off=execution.output_file(maskfile + "_inskull_mesh.off"),
        out_outskin_mask=execution.output_file(maskfile + "_outskin_mask.nii.gz"),
        out_outskin_mesh=execution.output_file(maskfile + "_outskin_mesh.nii.gz"),
        out_outskin_off=execution.output_file(maskfile + "_outskin_mesh.off"),
        out_outskull_mask=execution.output_file(maskfile + "_outskull_mask.nii.gz"),
        out_outskull_mesh=execution.output_file(maskfile + "_outskull_mesh.nii.gz"),
        out_outskull_off=execution.output_file(maskfile + "_outskull_mesh.off"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BET_FSL_METADATA",
    "BetFslOutputs",
    "bet_fsl",
]
