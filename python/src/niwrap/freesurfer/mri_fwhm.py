# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_FWHM_METADATA = Metadata(
    id="d03adb51c2f77acaf364735a5ea7ff81b4be91ea.boutiques",
    name="mri_fwhm",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriFwhmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_fwhm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume_file: OutputPathType
    """Output volume after smoothing."""
    final_mask_output_file: OutputPathType | None
    """Final mask volume."""
    summary_log_file: OutputPathType | None
    """Summary log file."""
    final_fwhm_estimate_file: OutputPathType | None
    """Final FWHM estimate file."""
    fwhm_of_each_dimension_file: OutputPathType | None
    """File containing the FWHM of each dimension."""
    mean_fwhm_volume_file: OutputPathType | None
    """Mean FWHM from volume file."""
    fwhm_volume_file: OutputPathType | None
    """FWHM volume file."""


def mri_fwhm(
    inputvol: InputPathType,
    outputvol: str,
    save_detrended: bool = False,
    save_unmasked: bool = False,
    smooth_only: bool = False,
    mask: InputPathType | None = None,
    mask_thresh: float | None = None,
    auto_mask: float | None = None,
    nerode: float | None = None,
    mask_inv: bool = False,
    out_mask: str | None = None,
    detrend_matrix: InputPathType | None = None,
    detrend_order: float | None = None,
    square_input: bool = False,
    smooth_by_fwhm: float | None = None,
    smooth_by_gstd: float | None = None,
    median_filter: float | None = None,
    smooth_to_fwhm: float | None = None,
    to_fwhm_tol: float | None = None,
    to_fwhm_nmax: float | None = None,
    to_fwhm_file: str | None = None,
    summary_file: str | None = None,
    dat_file: str | None = None,
    fwhm_dat_file: str | None = None,
    fwhm_vol_mean_file: str | None = None,
    fwhm_vol: str | None = None,
    synth: bool = False,
    synth_frames: float | None = None,
    nframes_min: float | None = None,
    ispm: bool = False,
    nspm_zero_padding: float | None = None,
    threads: float | None = None,
    debug: bool = False,
    checkopts: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MriFwhmOutputs:
    """
    FreeSurfer program to estimate the global Gaussian smoothness of a multi-frame,
    volume-based data set.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        inputvol: Input volume file. Format must be something readable by\
            mri_convert (e.g., mgh, mgz, img, nii, nii.gz).
        outputvol: Output volume file: save input after smoothing.
        save_detrended: Save input after smoothing and detrending.
        save_unmasked: Do not mask output volume.
        smooth_only: Smooth and save, do not compute fwhm.
        mask: Binary mask file.
        mask_thresh: Threshold for mask (default is 0.5).
        auto_mask: Auto compute mask based on global mean threshold.
        nerode: Erode mask n times prior to FWHM computation.
        mask_inv: Invert mask.
        out_mask: Save final mask to outmaskvol.
        detrend_matrix: Detrending matrix file in MATLAB4 format.
        detrend_order: Polynomial detrending order (default 0).
        square_input: Compute square of input before smoothing.
        smooth_by_fwhm: Smooth BY fwhm before measuring.
        smooth_by_gstd: Smooth using gstd (equivalent to --fwhm).
        median_filter: Perform median filtering instead of Gaussian.
        smooth_to_fwhm: Smooth TO this FWHM.
        to_fwhm_tol: Tolerance for smoothing to FWHM (default 0.5mm).
        to_fwhm_nmax: Maximum iterations for smoothing to FWHM (default 20).
        to_fwhm_file: Save smoothing to FWHM parameters to file.
        summary_file: Summary/log file.
        dat_file: Prints only the final FWHM estimate into this file.
        fwhm_dat_file: Compute and save the FWHM of each dimension.
        fwhm_vol_mean_file: Compute and save the FWHM of each dimension based\
            on fwhmvol.
        fwhm_vol: Save FWHM volume.
        synth: Synthesize input with white Gaussian noise.
        synth_frames: Number of frames for synthesized input (default is 10).
        nframes_min: Require at least this many frames.
        ispm: Input is SPM-analyze.
        nspm_zero_padding: Zero-padding for SPM-analyze.
        threads: Set OPEN MP threads.
        debug: Turn on debugging.
        checkopts: Check options and exit without running.
        version: Print version and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriFwhmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_FWHM_METADATA)
    cargs = []
    cargs.append("mri_fwhm")
    cargs.extend([
        "--i",
        execution.input_file(inputvol)
    ])
    cargs.extend([
        "--o",
        outputvol
    ])
    if save_detrended:
        cargs.append("--save-detrended")
    if save_unmasked:
        cargs.append("--save-unmasked")
    if smooth_only:
        cargs.append("--smooth-only")
    if mask is not None:
        cargs.extend([
            "--mask",
            execution.input_file(mask)
        ])
    if mask_thresh is not None:
        cargs.extend([
            "--mask-thresh",
            str(mask_thresh)
        ])
    if auto_mask is not None:
        cargs.extend([
            "--auto-mask",
            str(auto_mask)
        ])
    if nerode is not None:
        cargs.extend([
            "--nerode",
            str(nerode)
        ])
    if mask_inv:
        cargs.append("--mask-inv")
    if out_mask is not None:
        cargs.extend([
            "--out-mask",
            out_mask
        ])
    if detrend_matrix is not None:
        cargs.extend([
            "--X",
            execution.input_file(detrend_matrix)
        ])
    if detrend_order is not None:
        cargs.extend([
            "--detrend",
            str(detrend_order)
        ])
    if square_input:
        cargs.append("--sqr")
    if smooth_by_fwhm is not None:
        cargs.extend([
            "--fwhm",
            str(smooth_by_fwhm)
        ])
    if smooth_by_gstd is not None:
        cargs.extend([
            "--gstd",
            str(smooth_by_gstd)
        ])
    if median_filter is not None:
        cargs.extend([
            "--median",
            str(median_filter)
        ])
    if smooth_to_fwhm is not None:
        cargs.extend([
            "--to-fwhm",
            str(smooth_to_fwhm)
        ])
    if to_fwhm_tol is not None:
        cargs.extend([
            "--to-fwhm-tol",
            str(to_fwhm_tol)
        ])
    if to_fwhm_nmax is not None:
        cargs.extend([
            "--to-fwhm-nmax",
            str(to_fwhm_nmax)
        ])
    if to_fwhm_file is not None:
        cargs.extend([
            "--to-fwhm-file",
            to_fwhm_file
        ])
    if summary_file is not None:
        cargs.extend([
            "--sum",
            summary_file
        ])
    if dat_file is not None:
        cargs.extend([
            "--dat",
            dat_file
        ])
    if fwhm_dat_file is not None:
        cargs.extend([
            "--fwhmdat",
            fwhm_dat_file
        ])
    if fwhm_vol_mean_file is not None:
        cargs.extend([
            "--fwhmvolmn",
            fwhm_vol_mean_file
        ])
    if fwhm_vol is not None:
        cargs.extend([
            "--fwhmvol",
            fwhm_vol
        ])
    if synth:
        cargs.append("--synth")
    if synth_frames is not None:
        cargs.extend([
            "--synth-frames",
            str(synth_frames)
        ])
    if nframes_min is not None:
        cargs.extend([
            "--nframesmin",
            str(nframes_min)
        ])
    if ispm:
        cargs.append("--ispm")
    if nspm_zero_padding is not None:
        cargs.extend([
            "--in_nspmzeropad",
            str(nspm_zero_padding)
        ])
    if threads is not None:
        cargs.extend([
            "--nthreads",
            str(threads)
        ])
    if debug:
        cargs.append("--debug")
    if checkopts:
        cargs.append("--checkopts")
    if version:
        cargs.append("--version")
    ret = MriFwhmOutputs(
        root=execution.output_file("."),
        output_volume_file=execution.output_file(outputvol),
        final_mask_output_file=execution.output_file(out_mask) if (out_mask is not None) else None,
        summary_log_file=execution.output_file(summary_file) if (summary_file is not None) else None,
        final_fwhm_estimate_file=execution.output_file(dat_file) if (dat_file is not None) else None,
        fwhm_of_each_dimension_file=execution.output_file(fwhm_dat_file) if (fwhm_dat_file is not None) else None,
        mean_fwhm_volume_file=execution.output_file(fwhm_vol_mean_file) if (fwhm_vol_mean_file is not None) else None,
        fwhm_volume_file=execution.output_file(fwhm_vol) if (fwhm_vol is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_FWHM_METADATA",
    "MriFwhmOutputs",
    "mri_fwhm",
]
