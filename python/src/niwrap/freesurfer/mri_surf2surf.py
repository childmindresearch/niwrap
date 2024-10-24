# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_SURF2SURF_METADATA = Metadata(
    id="d67a0abaca8f23d784a32410fdaa560c5667746c.boutiques",
    name="mri_surf2surf",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriSurf2surfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_surf2surf(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_values: OutputPathType | None
    """File in which to store output values."""
    trg_distances: OutputPathType | None
    """File containing distances from source to target vertices."""


def mri_surf2surf(
    src_subject: str,
    trg_subject: str,
    sval_path: InputPathType | None = None,
    sval_xyz: str | None = None,
    projfrac: list[str] | None = None,
    projabs: list[str] | None = None,
    sval_tal_xyz: str | None = None,
    sval_area: str | None = None,
    sval_annot: InputPathType | None = None,
    sval_nxyz: str | None = None,
    patch: list[str] | None = None,
    sfmt: str | None = None,
    reg: list[str] | None = None,
    reg_inv: list[str] | None = None,
    srcicoorder: int | None = None,
    trgicoorder: int | None = None,
    tval_path: str | None = None,
    tval_xyz: str | None = None,
    tfmt: str | None = None,
    trg_dist: str | None = None,
    s: str | None = None,
    hemi: str | None = None,
    src_hemi: str | None = None,
    trg_hemi: str | None = None,
    dual_hemi: bool = False,
    jac: bool = False,
    surfreg: str | None = None,
    src_surfreg: str | None = None,
    trg_surfreg: str | None = None,
    mapmethod: str | None = None,
    frame: int | None = None,
    fwhm_src: float | None = None,
    fwhm_trg: float | None = None,
    nsmooth_in: int | None = None,
    nsmooth_out: int | None = None,
    cortex: bool = False,
    no_cortex: bool = False,
    label_src: InputPathType | None = None,
    label_trg: InputPathType | None = None,
    mul: float | None = None,
    div: float | None = None,
    reshape: bool = False,
    reshape_factor: int | None = None,
    reshape3d: bool = False,
    split: bool = False,
    synth: bool = False,
    ones: bool = False,
    normvar: bool = False,
    seed: int | None = None,
    prune: bool = False,
    no_prune: bool = False,
    proj_surf: list[str] | None = None,
    proj_norm: list[str] | None = None,
    reg_diff: str | None = None,
    rms: InputPathType | None = None,
    rms_mask: InputPathType | None = None,
    runner: Runner | None = None,
) -> MriSurf2surfOutputs:
    """
    Resample one surface onto another using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        src_subject: Name of source subject as found in $SUBJECTS_DIR or ico\
            for icosahedron.
        trg_subject: Name of target subject as found in $SUBJECTS_DIR or ico\
            for icosahedron.
        sval_path: Path of the file with input values.
        sval_xyz: Use xyz of a surface as input.
        projfrac: Use projected xyz of a surface as input.
        projabs: Use projected xyz absolute of a surface as input.
        sval_tal_xyz: Use tal xyz of a surface as input.
        sval_area: Use vertex area of a surface as input.
        sval_annot: Map annotation file.
        sval_nxyz: Use surface normals of a surface as input.
        patch: Specify source patch file, target surface and number of\
            dilations.
        sfmt: Source format type string.
        reg: Apply registration file to sval-xyz.
        reg_inv: Apply inverse registration file to sval-xyz.
        srcicoorder: Icosahedron order for the source.
        trgicoorder: Icosahedron order for the target.
        tval_path: Path of the file in which to store output values.
        tval_xyz: Save target value as a surface file with source xyz.
        tfmt: Target format type string.
        trg_dist: Save distance from source to target vertices.
        s: Use the same subject for both source and target.
        hemi: Hemisphere for both source and target (lh or rh).
        src_hemi: Hemisphere for source (lh or rh).
        trg_hemi: Hemisphere for target (lh or rh).
        dual_hemi: Assume source ?h.?h.surfreg file name.
        jac: Turn on jacobian correction, needed when applying to area or\
            volume.
        surfreg: Surface registration for source and target (sphere.reg).
        src_surfreg: Source surface registration (sphere.reg).
        trg_surfreg: Target surface registration (sphere.reg).
        mapmethod: Method used to map from the vertices in one subject to\
            another (nnfr or nnf).
        frame: Save only nth frame (when using paint output format).
        fwhm_src: Smooth the source to given FWHM.
        fwhm_trg: Smooth the target to given FWHM.
        nsmooth_in: Number of smoothing iterations for input.
        nsmooth_out: Number of smoothing iterations for output.
        cortex: Use ?h.cortex.label as a smoothing mask.
        no_cortex: Do NOT use ?h.cortex.label as a smoothing mask (default).
        label_src: Source smoothing mask.
        label_trg: Target smoothing mask.
        mul: Multiply the input by the given value.
        div: Divide the input by the given value.
        reshape: Reshape output to multiple 'slices'.
        reshape_factor: Reshape to Nfactor 'slices'.
        reshape3d: Reshape fsaverage (ico7) into 42 x 47 x 83.
        split: Output each frame separately.
        synth: Replace input with white Gaussian noise.
        ones: Replace input with 1s.
        normvar: Rescale so that stddev=1 (good with --synth).
        seed: Seed for synth (default is auto).
        prune: Remove any voxel that is zero in any time point (for smoothing).
        no_prune: Do not prune (default).
        proj_surf: Project vertices by mag*scale at each vertex.
        proj_norm: Project vertices by distmm at each vertex.
        reg_diff: Subtract reg2 from --reg (primarily for testing).
        rms: Save RMS of reg1-reg2 (primarily for testing).
        rms_mask: Compute RMS in mask (primarily for testing).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriSurf2surfOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_SURF2SURF_METADATA)
    cargs = []
    cargs.append("mri_surf2surf")
    cargs.extend([
        "--srcsubject",
        src_subject
    ])
    if sval_path is not None:
        cargs.extend([
            "--sval",
            execution.input_file(sval_path)
        ])
    if sval_xyz is not None:
        cargs.extend([
            "--sval-xyz",
            sval_xyz
        ])
    if projfrac is not None:
        cargs.extend([
            "--projfrac",
            *projfrac
        ])
    if projabs is not None:
        cargs.extend([
            "--projabs",
            *projabs
        ])
    if sval_tal_xyz is not None:
        cargs.extend([
            "--sval-tal-xyz",
            sval_tal_xyz
        ])
    if sval_area is not None:
        cargs.extend([
            "--sval-area",
            sval_area
        ])
    if sval_annot is not None:
        cargs.extend([
            "--sval-annot",
            execution.input_file(sval_annot)
        ])
    if sval_nxyz is not None:
        cargs.extend([
            "--sval-nxyz",
            sval_nxyz
        ])
    if patch is not None:
        cargs.extend([
            "--patch",
            *patch
        ])
    if sfmt is not None:
        cargs.extend([
            "--sfmt",
            sfmt
        ])
    if reg is not None:
        cargs.extend([
            "--reg",
            *reg
        ])
    if reg_inv is not None:
        cargs.extend([
            "--reg-inv",
            *reg_inv
        ])
    if srcicoorder is not None:
        cargs.extend([
            "--srcicoorder",
            str(srcicoorder)
        ])
    cargs.extend([
        "--trgsubject",
        trg_subject
    ])
    if trgicoorder is not None:
        cargs.extend([
            "--trgicoorder",
            str(trgicoorder)
        ])
    if tval_path is not None:
        cargs.extend([
            "--tval",
            tval_path
        ])
    if tval_xyz is not None:
        cargs.extend([
            "--tval-xyz",
            tval_xyz
        ])
    if tfmt is not None:
        cargs.extend([
            "--tfmt",
            tfmt
        ])
    if trg_dist is not None:
        cargs.extend([
            "--trgdist",
            trg_dist
        ])
    if s is not None:
        cargs.extend([
            "--s",
            s
        ])
    if hemi is not None:
        cargs.extend([
            "--hemi",
            hemi
        ])
    if src_hemi is not None:
        cargs.extend([
            "--srchemi",
            src_hemi
        ])
    if trg_hemi is not None:
        cargs.extend([
            "--trghemi",
            trg_hemi
        ])
    if dual_hemi:
        cargs.append("--dual-hemi")
    if jac:
        cargs.append("--jac")
    if surfreg is not None:
        cargs.extend([
            "--surfreg",
            surfreg
        ])
    if src_surfreg is not None:
        cargs.extend([
            "--srcsurfreg",
            src_surfreg
        ])
    if trg_surfreg is not None:
        cargs.extend([
            "--trgsurfreg",
            trg_surfreg
        ])
    if mapmethod is not None:
        cargs.extend([
            "--mapmethod",
            mapmethod
        ])
    if frame is not None:
        cargs.extend([
            "--frame",
            str(frame)
        ])
    if fwhm_src is not None:
        cargs.extend([
            "--fwhm-src",
            str(fwhm_src)
        ])
    if fwhm_trg is not None:
        cargs.extend([
            "--fwhm-trg",
            str(fwhm_trg)
        ])
    if nsmooth_in is not None:
        cargs.extend([
            "--nsmooth-in",
            str(nsmooth_in)
        ])
    if nsmooth_out is not None:
        cargs.extend([
            "--nsmooth-out",
            str(nsmooth_out)
        ])
    if cortex:
        cargs.append("--cortex")
    if no_cortex:
        cargs.append("--no-cortex")
    if label_src is not None:
        cargs.extend([
            "--label-src",
            execution.input_file(label_src)
        ])
    if label_trg is not None:
        cargs.extend([
            "--label-trg",
            execution.input_file(label_trg)
        ])
    if mul is not None:
        cargs.extend([
            "--mul",
            str(mul)
        ])
    if div is not None:
        cargs.extend([
            "--div",
            str(div)
        ])
    if reshape:
        cargs.append("--reshape")
    if reshape_factor is not None:
        cargs.extend([
            "--reshape-factor",
            str(reshape_factor)
        ])
    if reshape3d:
        cargs.append("--reshape3d")
    if split:
        cargs.append("--split")
    if synth:
        cargs.append("--synth")
    if ones:
        cargs.append("--ones")
    if normvar:
        cargs.append("--normvar")
    if seed is not None:
        cargs.extend([
            "--seed",
            str(seed)
        ])
    if prune:
        cargs.append("--prune")
    if no_prune:
        cargs.append("--no-prune")
    if proj_surf is not None:
        cargs.extend([
            "--proj-surf",
            *proj_surf
        ])
    if proj_norm is not None:
        cargs.extend([
            "--proj-norm",
            *proj_norm
        ])
    if reg_diff is not None:
        cargs.extend([
            "--reg-diff",
            reg_diff
        ])
    if rms is not None:
        cargs.extend([
            "--rms",
            execution.input_file(rms)
        ])
    if rms_mask is not None:
        cargs.extend([
            "--rms-mask",
            execution.input_file(rms_mask)
        ])
    ret = MriSurf2surfOutputs(
        root=execution.output_file("."),
        output_values=execution.output_file(tval_path) if (tval_path is not None) else None,
        trg_distances=execution.output_file(trg_dist) if (trg_dist is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_SURF2SURF_METADATA",
    "MriSurf2surfOutputs",
    "mri_surf2surf",
]
