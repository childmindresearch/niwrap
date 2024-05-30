# This file was auto generated by Styx.
# Do not edit this file directly.

import pathlib
import typing

from styxdefs import *


BET_METADATA = Metadata(
    id="a82c114929d9dd7ec1c55558ac12d78b41062a71",
    name="bet",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class BetOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bet(...)`.
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
    """The in-skull mask file from betsurf (from -A or -A2)"""
    out_inskull_mesh: OutputPathType
    """The in-skull mesh file from betsurf (from -A or -A2)"""
    out_inskull_off: OutputPathType
    """The in-skull mesh .off file from betsurf (from -A or -A2)"""
    out_outskin_mask: OutputPathType
    """The out-skin mask file from betsurf (from -A or -A2)"""
    out_outskin_mesh: OutputPathType
    """The out-skin mesh file from betsurf (from -A or -A2)"""
    out_outskin_off: OutputPathType
    """The out-skin mesh .off file from betsurf (from -A or -A2)"""
    out_outskull_mask: OutputPathType
    """The out-skull mask file from betsurf (from -A or -A2)"""
    out_outskull_mesh: OutputPathType
    """The out-skull mesh file from betsurf (from -A or -A2)"""
    out_outskull_off: OutputPathType
    """The out-skull mesh .off file from betsurf (from -A or -A2)"""


def bet(
    infile: InputPathType,
    maskfile: str = "img_bet",
    fractional_intensity: float | int | None = None,
    vg_fractional_intensity: float | int | None = None,
    center_of_gravity: list[float | int] = None,
    overlay_flag: bool = False,
    binary_mask_flag: bool = False,
    approx_skull_flag: bool = False,
    no_seg_output_flag: bool = False,
    vtk_mesh: bool = False,
    head_radius: float | int | None = None,
    thresholding_flag: bool = False,
    robust_iters_flag: bool = False,
    residual_optic_cleanup_flag: bool = False,
    reduce_bias_flag: bool = False,
    slice_padding_flag: bool = False,
    whole_set_mask_flag: bool = False,
    additional_surfaces_flag: bool = False,
    additional_surfaces_t2: InputPathType | None = None,
    verbose_flag: bool = False,
    debug_flag: bool = False,
    runner: Runner = None,
) -> BetOutputs:
    """
    bet by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Automated brain extraction tool for FSL.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/BET
    
    Args:
        infile: Input image (e.g. img.nii.gz)
        maskfile: Output brain mask (e.g. img_bet.nii.gz)
        fractional_intensity: Fractional intensity threshold (0->1);
            default=0.5; smaller values give larger brain outline estimates
        vg_fractional_intensity: Vertical gradient in fractional intensity
            threshold (-1->1); default=0; positive values give larger brain outline
            at bottom, smaller at top
        center_of_gravity: The xyz coordinates of the center of gravity (voxels,
            not mm) of initial mesh surface. Must have exactly three numerical
            entries in the list (3-vector).
        overlay_flag: Generate brain surface outline overlaid onto original
            image
        binary_mask_flag: Generate binary brain mask
        approx_skull_flag: Generate rough skull image (not as clean as betsurf)
        no_seg_output_flag: Don't generate segmented brain image output
        vtk_mesh: Generate brain surface as mesh in .vtk format
        head_radius: head radius (mm not voxels); initial surface sphere is set
            to half of this
        thresholding_flag: Apply thresholding to segmented brain image and mask
        robust_iters_flag: More robust brain center estimation, by iterating BET
            with a changing center-of-gravity.
        residual_optic_cleanup_flag: This attempts to cleanup residual eye and
            optic nerve voxels which bet2 can sometimes leave behind. This can be
            useful when running SIENA or SIENAX, for example. Various stages
            involving standard-space masking, morphpological operations and
            thresholdings are combined to produce a result which can often give
            better results than just running bet2.
        reduce_bias_flag: This attempts to reduce image bias, and residual neck
            voxels. This can be useful when running SIENA or SIENAX, for example.
            Various stages involving FAST segmentation-based bias field removal and
            standard-space masking are combined to produce a result which can often
            give better results than just running bet2.
        slice_padding_flag: This can improve the brain extraction if only a few
            slices are present in the data (i.e., a small field of view in the Z
            direction). This is achieved by padding the end slices in both
            directions, copying the end slices several times, running bet2 and then
            removing the added slices.
        whole_set_mask_flag: This option uses bet2 to determine a brain mask on
            the basis of the first volume in a 4D data set, and applies this to the
            whole data set. This is principally intended for use on FMRI data, for
            example to remove eyeballs. Because it is normally important (in this
            application) that masking be liberal (ie that there be little risk of
            cutting out valid brain voxels) the -f threshold is reduced to 0.3, and
            also the brain mask is "dilated" slightly before being used.
        additional_surfaces_flag: This runs both bet2 and betsurf programs in
            order to get the additional skull and scalp surfaces created by betsurf.
            This involves registering to standard space in order to allow betsurf to
            find the standard space masks it needs.
        additional_surfaces_t2: This is the same as -A except that a T2 image is
            also input, to further improve the estimated skull and scalp surfaces.
            As well as carrying out the standard space registration this also
            registers the T2 to the T1 input image.
        verbose_flag: Switch on diagnostic messages
        debug_flag: Don't delete temporary intermediate images
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `BetOutputs`).
    """
    runner = runner or get_global_runner()
    if fractional_intensity is not None and not (0 <= fractional_intensity <= 1): 
        raise ValueError(f"'fractional_intensity' must be between 0 <= x <= 1 but was {fractional_intensity}")
    if vg_fractional_intensity is not None and not (-1 <= vg_fractional_intensity <= 1): 
        raise ValueError(f"'vg_fractional_intensity' must be between -1 <= x <= 1 but was {vg_fractional_intensity}")
    if center_of_gravity is not None and (len(center_of_gravity) != 3): 
        raise ValueError(f"Length of 'center_of_gravity' must be 3 but was {len(center_of_gravity)}")
    if (
        robust_iters_flag +
        residual_optic_cleanup_flag +
        reduce_bias_flag +
        slice_padding_flag +
        whole_set_mask_flag +
        additional_surfaces_flag +
        (additional_surfaces_t2 is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "robust_iters_flag,\n"
            "residual_optic_cleanup_flag,\n"
            "reduce_bias_flag,\n"
            "slice_padding_flag,\n"
            "whole_set_mask_flag,\n"
            "additional_surfaces_flag,\n"
            "additional_surfaces_t2"
        )
    execution = runner.start_execution(BET_METADATA)
    cargs = []
    cargs.append("bet")
    cargs.append(execution.input_file(infile))
    cargs.append(maskfile)
    if fractional_intensity is not None:
        cargs.extend(["-f", str(fractional_intensity)])
    if vg_fractional_intensity is not None:
        cargs.extend(["-g", str(vg_fractional_intensity)])
    if center_of_gravity is not None:
        cargs.extend(["-c", *map(str, center_of_gravity)])
    if overlay_flag:
        cargs.append("-o")
    if binary_mask_flag:
        cargs.append("-m")
    if approx_skull_flag:
        cargs.append("-s")
    if no_seg_output_flag:
        cargs.append("-n")
    if vtk_mesh:
        cargs.append("-e")
    if head_radius is not None:
        cargs.extend(["-r", str(head_radius)])
    if thresholding_flag:
        cargs.append("-t")
    if robust_iters_flag:
        cargs.append("-R")
    if residual_optic_cleanup_flag:
        cargs.append("-S")
    if reduce_bias_flag:
        cargs.append("-B")
    if slice_padding_flag:
        cargs.append("-Z")
    if whole_set_mask_flag:
        cargs.append("-F")
    if additional_surfaces_flag:
        cargs.append("-A")
    if additional_surfaces_t2 is not None:
        cargs.extend(["-A2", execution.input_file(additional_surfaces_t2)])
    if verbose_flag:
        cargs.append("-v")
    if debug_flag:
        cargs.append("-d")
    ret = BetOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(f"{maskfile}.nii.gz", optional=True),
        binary_mask=execution.output_file(f"{maskfile}_mask.nii.gz", optional=True),
        overlay_file=execution.output_file(f"{maskfile}_overlay.nii.gz", optional=True),
        approx_skull_img=execution.output_file(f"{maskfile}_skull.nii.gz", optional=True),
        output_vtk_mesh=execution.output_file(f"{maskfile}_mesh.vtk", optional=True),
        skull_mask=execution.output_file(f"{maskfile}_skull_mask.nii.gz", optional=True),
        out_inskull_mask=execution.output_file(f"{maskfile}_inskull_mask.nii.gz", optional=True),
        out_inskull_mesh=execution.output_file(f"{maskfile}_inskull_mesh.nii.gz", optional=True),
        out_inskull_off=execution.output_file(f"{maskfile}_inskull_mesh.off", optional=True),
        out_outskin_mask=execution.output_file(f"{maskfile}_outskin_mask.nii.gz", optional=True),
        out_outskin_mesh=execution.output_file(f"{maskfile}_outskin_mesh.nii.gz", optional=True),
        out_outskin_off=execution.output_file(f"{maskfile}_outskin_mesh.off", optional=True),
        out_outskull_mask=execution.output_file(f"{maskfile}_outskull_mask.nii.gz", optional=True),
        out_outskull_mesh=execution.output_file(f"{maskfile}_outskull_mesh.nii.gz", optional=True),
        out_outskull_off=execution.output_file(f"{maskfile}_outskull_mesh.off", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BET_METADATA",
    "BetOutputs",
    "bet",
]
