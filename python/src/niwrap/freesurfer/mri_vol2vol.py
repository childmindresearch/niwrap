# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_VOL2VOL_METADATA = Metadata(
    id="77d3504583fc4d7f61c4962c2cc361faf9664a7d.boutiques",
    name="mri_vol2vol",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriVol2volOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_vol2vol(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume: OutputPathType
    """Resampled output volume."""


def mri_vol2vol(
    movvol: InputPathType,
    targvol: InputPathType,
    outvol: InputPathType,
    dispvol: InputPathType | None = None,
    downsample: list[float] | None = None,
    register_dat: InputPathType | None = None,
    lta: InputPathType | None = None,
    lta_inv: InputPathType | None = None,
    fsl: InputPathType | None = None,
    xfm: InputPathType | None = None,
    inv: bool = False,
    tal: bool = False,
    talres: float | None = None,
    talxfm: InputPathType | None = None,
    m3z: InputPathType | None = None,
    inv_morph: bool = False,
    fstarg: str | None = None,
    crop: float | None = None,
    slice_crop: list[float] | None = None,
    slice_reverse: bool = False,
    slice_bias: float | None = None,
    interp: str | None = None,
    fill_average: bool = False,
    fill_conserve: bool = False,
    fill_up: float | None = None,
    mul: float | None = None,
    precision: str | None = None,
    keep_precision: bool = False,
    kernel: bool = False,
    copy_ctab: bool = False,
    gcam: str | None = None,
    spm_warp: str | None = None,
    map_point: str | None = None,
    map_point_inv_lta: str | None = None,
    no_resample: bool = False,
    rot: list[float] | None = None,
    trans: list[float] | None = None,
    shear: list[float] | None = None,
    reg_final: InputPathType | None = None,
    synth: bool = False,
    seed: float | None = None,
    save_reg: bool = False,
    debug: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MriVol2volOutputs:
    """
    Resamples a volume into another field-of-view using various types of matrices
    (FreeSurfer, FSL, SPM, and MNI).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        movvol: Input volume (or output template with --inv).
        targvol: Output template (or input with --inv).
        outvol: Output volume.
        dispvol: Displacement volume.
        downsample: Downsample factor (e.g., 2) (do not include a targ or\
            registration).
        register_dat: tkRAS-to-tkRAS matrix (tkregister2 format).
        lta: Linear Transform Array (usually only 1 transform).
        lta_inv: LTA, invert (may not be the same as --lta --inv with --fstal).
        fsl: fslRAS-to-fslRAS matrix (FSL format).
        xfm: ScannerRAS-to-ScannerRAS matrix (MNI format).
        inv: Sample from targ to mov.
        tal: Map to a sub FOV of MNI305 (with --reg only).
        talres: Set voxel size 1mm or 2mm (default is 1).
        talxfm: Path to the talairach transformation file. Default is\
            talairach.xfm (looks in mri/transforms).
        m3z: Non-linear morph encoded in the m3z format.
        inv_morph: Compute and use the inverse of the m3z morph.
        fstarg: Optionally use the specified volume from the subject in --reg\
            as target. Default is orig.mgz.
        crop: Crop and change voxel size.
        slice_crop: Crop output slices to be within specified start and end\
            indices.
        slice_reverse: Reverse order of slices, update vox2ras.
        slice_bias: Apply half-cosine bias field.
        interp: Interpolation method: cubic, trilin, or nearest (default is\
            trilin).
        fill_average: Compute mean of all source voxels in a given target voxel.
        fill_conserve: Compute sum of all source voxels in a given target voxel.
        fill_up: Source upsampling factor for --fill-{avg,cons} (default is 2).
        mul: Multiply output by the specified value.
        precision: Output precision (default is float).
        keep_precision: Set output precision to that of the input.
        kernel: Save the trilinear interpolation kernel at each voxel instead\
            of the interpolated image.
        copy_ctab: Setenv FS_COPY_HEADER_CTAB to copy any ctab in the mov\
            header.
        gcam: GCAM warp procedure.
        spm_warp: SPM warp procedure.
        map_point: Standalone option to map a point to another space.
        map_point_inv_lta: Same as --map-point but inverts the LTA.
        no_resample: Do not resample, just change vox2ras matrix.
        rot: Rotation angles (degrees) to apply to registration matrix.
        trans: Translation (mm) to apply to registration matrix.
        shear: Shearing factors. Sxy Sxz Syz with xz as in-plane.
        reg_final: Final registration matrix after rotation and translation\
            (but not inversion).
        synth: Replace input with white Gaussian noise.
        seed: Seed for synth (default is to set from time of day).
        save_reg: Write out output volume registration matrix.
        debug: Turn on debugging output.
        version: Print out version string and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriVol2volOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_VOL2VOL_METADATA)
    cargs = []
    cargs.append("mri_vol2vol")
    cargs.append(execution.input_file(movvol))
    cargs.append(execution.input_file(targvol))
    cargs.append(execution.input_file(outvol))
    if dispvol is not None:
        cargs.extend([
            "--disp",
            execution.input_file(dispvol)
        ])
    if downsample is not None:
        cargs.extend([
            "--downsample",
            *map(str, downsample)
        ])
    if register_dat is not None:
        cargs.extend([
            "--reg",
            execution.input_file(register_dat)
        ])
    if lta is not None:
        cargs.extend([
            "--lta",
            execution.input_file(lta)
        ])
    if lta_inv is not None:
        cargs.extend([
            "--lta-inv",
            execution.input_file(lta_inv)
        ])
    if fsl is not None:
        cargs.extend([
            "--fsl",
            execution.input_file(fsl)
        ])
    if xfm is not None:
        cargs.extend([
            "--xfm",
            execution.input_file(xfm)
        ])
    if inv:
        cargs.append("--inv")
    if tal:
        cargs.append("--tal")
    if talres is not None:
        cargs.extend([
            "--talres",
            str(talres)
        ])
    if talxfm is not None:
        cargs.extend([
            "--talxfm",
            execution.input_file(talxfm)
        ])
    if m3z is not None:
        cargs.extend([
            "--m3z",
            execution.input_file(m3z)
        ])
    if inv_morph:
        cargs.append("--inv-morph")
    if fstarg is not None:
        cargs.extend([
            "--fstarg",
            fstarg
        ])
    if crop is not None:
        cargs.extend([
            "--crop",
            str(crop)
        ])
    if slice_crop is not None:
        cargs.extend([
            "--slice-crop",
            *map(str, slice_crop)
        ])
    if slice_reverse:
        cargs.append("--slice-reverse")
    if slice_bias is not None:
        cargs.extend([
            "--slice-bias",
            str(slice_bias)
        ])
    if interp is not None:
        cargs.extend([
            "--interp",
            interp
        ])
    if fill_average:
        cargs.append("--fill-average")
    if fill_conserve:
        cargs.append("--fill-conserve")
    if fill_up is not None:
        cargs.extend([
            "--fill-upsample",
            str(fill_up)
        ])
    if mul is not None:
        cargs.extend([
            "--mul",
            str(mul)
        ])
    if precision is not None:
        cargs.extend([
            "--precision",
            precision
        ])
    if keep_precision:
        cargs.append("--keep-precision")
    if kernel:
        cargs.append("--kernel")
    if copy_ctab:
        cargs.append("--copy-ctab")
    if gcam is not None:
        cargs.extend([
            "--gcam",
            gcam
        ])
    if spm_warp is not None:
        cargs.extend([
            "--spm-warp",
            spm_warp
        ])
    if map_point is not None:
        cargs.extend([
            "--map-point",
            map_point
        ])
    if map_point_inv_lta is not None:
        cargs.extend([
            "--map-point-inv-lta",
            map_point_inv_lta
        ])
    if no_resample:
        cargs.append("--no-resample")
    if rot is not None:
        cargs.extend([
            "--rot",
            *map(str, rot)
        ])
    if trans is not None:
        cargs.extend([
            "--trans",
            *map(str, trans)
        ])
    if shear is not None:
        cargs.extend([
            "--shear",
            *map(str, shear)
        ])
    if reg_final is not None:
        cargs.extend([
            "--reg-final",
            execution.input_file(reg_final)
        ])
    if synth:
        cargs.append("--synth")
    if seed is not None:
        cargs.extend([
            "--seed",
            str(seed)
        ])
    if save_reg:
        cargs.append("--save-reg")
    if debug:
        cargs.append("--debug")
    if version:
        cargs.append("--version")
    ret = MriVol2volOutputs(
        root=execution.output_file("."),
        output_volume=execution.output_file(pathlib.Path(outvol).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_VOL2VOL_METADATA",
    "MriVol2volOutputs",
    "mri_vol2vol",
]
