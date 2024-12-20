# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__MEASURE_BB_THICK_METADATA = Metadata(
    id="261dd15d9b87b8820a89a7b2a53c5bb9a97c42a1.boutiques",
    name="@measure_bb_thick",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VMeasureBbThickOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__measure_bb_thick(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    maxfill: OutputPathType | None
    """Thickness/depth dataset"""
    bb_thick: OutputPathType | None
    """Volumetric thickness dataset"""
    bb_thick_smooth: OutputPathType | None
    """Smoothed volumetric thickness dataset"""
    bb_thick_niml: OutputPathType | None
    """Unsmoothed thickness mapped to surface nodes"""
    bb_thick_smooth_niml: OutputPathType | None
    """Smoothed thickness mapped to surface nodes"""
    maskset_output: OutputPathType | None
    """Mask dataset"""
    maskset_resampled: OutputPathType | None
    """Resampled mask dataset"""
    anat_surface: OutputPathType | None
    """Surface representation of mask volume"""
    quick_spec: OutputPathType | None
    """Simple specification file for surface to use with suma commands"""


def v__measure_bb_thick(
    maskset: InputPathType,
    surfset: InputPathType,
    outdir: str | None = None,
    resample: str | None = None,
    increment: float | None = None,
    surfsmooth: float | None = None,
    smoothmm: float | None = None,
    maxthick: float | None = None,
    depth_search: float | None = None,
    keep_temp_files: bool = False,
    balls_only: bool = False,
    surfsmooth_method: str | None = None,
    runner: Runner | None = None,
) -> VMeasureBbThickOutputs:
    """
    Compute thickness of mask using ball and box method.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        maskset: Mask dataset for input.
        surfset: Surface dataset onto which to map thickness (e.g., pial/gray\
            matter surface).
        outdir: Output directory.
        resample: Resample input to mm in millimeters (e.g., half a voxel or\
            'auto'). No resampling is done by default.
        increment: Test thickness at increments of sub-voxel distance. Default\
            is 1/4 voxel minimum distance (in-plane).
        surfsmooth: Smooth surface map of thickness by mm millimeters. Default\
            is 6 mm.
        smoothmm: Smooth volume by mm FWHM in mask. Default is 2*voxelsize of\
            mask or resampled mask.
        maxthick: Search for maximum thickness value of mm millimeters. Default\
            is 6 mm.
        depth_search: Map to surface by looking for max along mm millimeter\
            normal vectors. Default is 3 mm.
        keep_temp_files: Do not delete the intermediate files (for testing).
        balls_only: Calculate only with spheres and skip boxes.
        surfsmooth_method: Heat method used for smoothing surfaces. Default is\
            HEAT_07 but HEAT_05 is also useful for models.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VMeasureBbThickOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__MEASURE_BB_THICK_METADATA)
    cargs = []
    cargs.append("@measure_bb_thick")
    cargs.extend([
        "-maskset",
        execution.input_file(maskset)
    ])
    cargs.extend([
        "-surfset",
        execution.input_file(surfset)
    ])
    if outdir is not None:
        cargs.extend([
            "-outdir",
            outdir
        ])
    if resample is not None:
        cargs.extend([
            "-resample",
            resample
        ])
    if increment is not None:
        cargs.extend([
            "-increment",
            str(increment)
        ])
    if surfsmooth is not None:
        cargs.extend([
            "-surfsmooth",
            str(surfsmooth)
        ])
    if smoothmm is not None:
        cargs.extend([
            "-smoothmm",
            str(smoothmm)
        ])
    if maxthick is not None:
        cargs.extend([
            "-maxthick",
            str(maxthick)
        ])
    if depth_search is not None:
        cargs.extend([
            "-depthsearch",
            str(depth_search)
        ])
    if keep_temp_files:
        cargs.append("-keep_temp_files")
    if balls_only:
        cargs.append("-balls_only")
    if surfsmooth_method is not None:
        cargs.extend([
            "-surfsmooth_method",
            surfsmooth_method
        ])
    ret = VMeasureBbThickOutputs(
        root=execution.output_file("."),
        maxfill=execution.output_file(outdir + "/maxfill.nii.gz") if (outdir is not None) else None,
        bb_thick=execution.output_file(outdir + "/bb_thick.nii.gz") if (outdir is not None) else None,
        bb_thick_smooth=execution.output_file(outdir + "/bb_thick_smooth.nii.gz") if (outdir is not None) else None,
        bb_thick_niml=execution.output_file(outdir + "/bb_thick.niml.dset") if (outdir is not None) else None,
        bb_thick_smooth_niml=execution.output_file(outdir + "/bb_thick_smooth.niml.dset") if (outdir is not None) else None,
        maskset_output=execution.output_file(outdir + "/maskset.nii.gz") if (outdir is not None) else None,
        maskset_resampled=execution.output_file(outdir + "/maskset_rs.nii.gz") if (outdir is not None) else None,
        anat_surface=execution.output_file(outdir + "/anat.gii") if (outdir is not None) else None,
        quick_spec=execution.output_file(outdir + "/quick.spec") if (outdir is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VMeasureBbThickOutputs",
    "V__MEASURE_BB_THICK_METADATA",
    "v__measure_bb_thick",
]
