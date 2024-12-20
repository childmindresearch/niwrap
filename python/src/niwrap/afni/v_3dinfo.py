# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3DINFO_METADATA = Metadata(
    id="c0b7ae1e6ddb0557936952320119fb7853d0bfcd.boutiques",
    name="3dinfo",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dinfoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dinfo(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    info: list[str]
    """Sort-of-useful information from a 3D dataset's header"""


def v_3dinfo(
    dataset: list[InputPathType],
    orient: bool = False,
    lextent: bool = False,
    rextent: bool = False,
    aextent: bool = False,
    pextent: bool = False,
    iextent: bool = False,
    sextent: bool = False,
    all_names: bool = False,
    verb: bool = False,
    very_verbose: bool = False,
    short: bool = False,
    no_hist: bool = False,
    h: bool = False,
    help_: bool = False,
    extreme_help: bool = False,
    h_view: bool = False,
    h_web: bool = False,
    h_find: str | None = None,
    h_raw: bool = False,
    h_spx: bool = False,
    h_aspx: bool = False,
    all_opts: bool = False,
    label2index: str | None = None,
    niml_hdr: bool = False,
    subbrick_info: bool = False,
    exists: bool = False,
    id_: bool = False,
    is_atlas: bool = False,
    is_atlas_or_labeltable: bool = False,
    is_nifti: bool = False,
    dset_extension: bool = False,
    storage_mode: bool = False,
    space: bool = False,
    gen_space: bool = False,
    av_space: bool = False,
    nifti_code: bool = False,
    is_oblique: bool = False,
    handedness: bool = False,
    obliquity: bool = False,
    prefix: bool = False,
    prefix_noext: bool = False,
    ni: bool = False,
    nj: bool = False,
    nk: bool = False,
    nijk: bool = False,
    nv: bool = False,
    nt_: bool = False,
    n4: bool = False,
    nvi: bool = False,
    nti: bool = False,
    ntimes: bool = False,
    max_node: bool = False,
    di: bool = False,
    dj: bool = False,
    dk: bool = False,
    d3: bool = False,
    adi: bool = False,
    adj: bool = False,
    adk: bool = False,
    ad3: bool = False,
    voxvol: bool = False,
    oi: bool = False,
    oj: bool = False,
    ok: bool = False,
    o3: bool = False,
    dcx: bool = False,
    dcy: bool = False,
    dcz: bool = False,
    dc3: bool = False,
    tr: bool = False,
    dmin: bool = False,
    dmax: bool = False,
    dminus: bool = False,
    dmaxus: bool = False,
    smode: bool = False,
    header_name: bool = False,
    brick_name: bool = False,
    iname: bool = False,
    extent: bool = False,
    fac: bool = False,
    label: bool = False,
    datum: bool = False,
    min_: bool = False,
    max_: bool = False,
    minus: bool = False,
    maxus: bool = False,
    labeltable: bool = False,
    labeltable_as_atlas_points: bool = False,
    atlas_points: bool = False,
    history: bool = False,
    slice_timing: bool = False,
    header_line: bool = False,
    hdr: bool = False,
    sb_delim: str | None = None,
    na_flag: str | None = None,
    atr_delim: str | None = None,
    aform_real: bool = False,
    aform_real_oneline: bool = False,
    aform_real_refit_ori: bool = False,
    is_aform_real_orth: bool = False,
    aform_orth: bool = False,
    perm_to_orient: str | None = None,
    same_grid: bool = False,
    same_dim: bool = False,
    same_delta: bool = False,
    same_orient: bool = False,
    same_center: bool = False,
    same_obl: bool = False,
    same_all_grid: bool = False,
    val_diff: bool = False,
    sval_diff: bool = False,
    monog_pairs: bool = False,
    runner: Runner | None = None,
) -> V3dinfoOutputs:
    """
    Prints out sort-of-useful information from a 3D dataset's header.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset: Datasets to retrieve information from.
        orient: Value of orientation string. For example, LPI means: i\
            direction grows from Left(negative) to Right(positive). j direction\
            grows from Posterior (neg.) to Anterior (pos.) k direction grows from\
            Inferior (neg.) to Superior (pos.).
        lextent: Extent along L.
        rextent: Extent along R.
        aextent: Extent along A.
        pextent: Extent along P.
        iextent: Extent along I.
        sextent: Extent along S.
        all_names: Value of various dset structures handling filenames.
        verb: Print out lots of information.
        very_verbose: Print out even more information including slice time\
            offsets.
        short: Print out less information (default).
        no_hist: Omit the HISTORY text.
        h: Mini help.
        help_: Display entire help output.
        extreme_help: Extreme help.
        h_view: Open help in text editor.
        h_web: Open help in web browser.
        h_find: Look for lines in help output that match WORD.
        h_raw: Display unedited help string.
        h_spx: Help string in sphinx format without autoformatting options.
        h_aspx: Help string in sphinx format with autoformatting options.
        all_opts: Try to identify all options for the program from the help\
            output.
        label2index: Output index corresponding to label.
        niml_hdr: Output entire NIML-formatted header.
        subbrick_info: Output only sub-brick part of information.
        exists: 1 if dset is loadable, 0 otherwise. This works on prefix also.
        id_: Idcodestring of dset.
        is_atlas: 1 if dset is an atlas.
        is_atlas_or_labeltable: 1 if dset has an atlas or labeltable.
        is_nifti: 1 if dset is NIFTI format, 0 otherwise.
        dset_extension: Show filename extension for valid dataset (e.g.\
            .nii.gz).
        storage_mode: Show internal storage mode of dataset (e.g. NIFTI).
        space: Dataset's space.
        gen_space: Dataset's generic space.
        av_space: AFNI format's view extension for the space.
        nifti_code: What AFNI would use for an output NIFTI (q)sform_code.
        is_oblique: 1 if dset is oblique.
        handedness: L if orientation is Left handed, R if it is right handed.
        obliquity: Angle from plumb direction. Angles of 0 (or close) are for\
            cardinal orientations.
        prefix: Return the prefix.
        prefix_noext: Return the prefix without extensions.
        ni: Return the number of voxels in i dimension.
        nj: Return the number of voxels in j dimension.
        nk: Return the number of voxels in k dimension.
        nijk: Return ni*nj*nk.
        nv: Return number of points in time or the number of sub-bricks.
        nt_: Same as -nv.
        n4: Same as -ni -nj -nk -nv.
        nvi: The maximum sub-brick index (= nv -1 ).
        nti: Same as -nvi.
        ntimes: Return number of sub-bricks points in time. This is an option\
            for debugging use, stay away from it.
        max_node: For a surface-based dset, return the maximum node index.
        di: Signed displacement per voxel along i direction, aka dx.
        dj: Signed displacement per voxel along j direction, aka dy.
        dk: Signed displacement per voxel along k direction, aka dz.
        d3: Same as -di -dj -dk.
        adi: Voxel size along i direction (abs(di)).
        adj: Voxel size along j direction (abs(dj)).
        adk: Voxel size along k direction (abs(dk)).
        ad3: Same as -adi -adj -adk.
        voxvol: Voxel volume in cubic millimeters.
        oi: Volume origin along the i direction.
        oj: Volume origin along the j direction.
        ok: Volume origin along the k direction.
        o3: Same as -oi -oj -ok.
        dcx: Volumetric center in x direction (DICOM coordinates).
        dcy: Volumetric center in y direction (DICOM coordinates).
        dcz: Volumetric center in z direction (DICOM coordinates).
        dc3: Same as -dcx -dcy -dcz.
        tr: The TR value in seconds.
        dmin: The dataset's minimum value, scaled by fac.
        dmax: The dataset's maximum value, scaled by fac.
        dminus: The dataset's minimum value, unscaled.
        dmaxus: The dataset's maximum value, unscaled.
        smode: Dset storage mode string.
        header_name: Value of dset structure (sub)field 'header_name'.
        brick_name: Value of dset structure (sub)field 'brick_name'.
        iname: Name of dset as input on the command line.
        extent: The spatial extent of the dataset along R, L, A, P, I and S.
        fac: Return the float scaling factor.
        label: The label of each sub-brick.
        datum: The data storage type.
        min_: The minimum value, scaled by fac.
        max_: The maximum value, scaled by fac.
        minus: The minimum value, unscaled.
        maxus: The maximum value, unscaled.
        labeltable: Show label table, if any.
        labeltable_as_atlas_points: Show label table in atlas point format.
        atlas_points: Show atlas points list, if any.
        history: History note.
        slice_timing: Show slice timing.
        header_line: Output as the first line the names of attributes in each\
            field (column).
        hdr: Same as -header_line.
        sb_delim: Delimiter string between sub-brick values. Default SB_DELIM\
            is '|'.
        na_flag: String to use when a field is not found or not applicable.\
            Default is 'NA'.
        atr_delim: Delimiter string between attributes. Default ATR_DELIM is\
            the tab character.
        aform_real: Display full 3x4 'aform_real' matrix (AFNI's RAI equivalent\
            of the sform matrix in NIFTI, may contain obliquity info), with comment\
            line first.
        aform_real_oneline: Display full 'aform_real' matrix (see\
            '-aform_real') as 1 row of 12 numbers. No additional comment.
        aform_real_refit_ori: Display full 3x4 'aform_real' matrix (see\
            '-aform_real') *if* the dset were reoriented (via 3drefit) to new\
            orient XXX. Includes comment line first.
        is_aform_real_orth: If true, aform_real == aform_orth, which should be\
            a very common occurrence.
        aform_orth: Display full 3x4 'aform_orth' matrix (AFNI's RAI matrix\
            equivalent of the NIFTI quaternion, which may contain obliquity info),\
            with comment line first. This matrix is the orthogonalized form of\
            aform_real, and very often AFNI-produced dsets, we will have:\
            aform_orth == aform_real.
        perm_to_orient: Display 3x3 permutation matrix to go from the dset's\
            current orientation to the YYY orient.
        same_grid: Output 1 if the grid is identical between two dsets, 0\
            otherwise. For -same_grid to be 1, all of -same_dim, -same_delta,\
            -same_orient, -same_center, and -same_obl must return 1.
        same_dim: 1 if dimensions (nx, ny, nz) are the same between dset pairs.
        same_delta: 1 if voxel sizes are the same between dset pairs.
        same_orient: 1 if orientation is the same between dset pairs.
        same_center: 1 if geometric center is the same between dset pairs.
        same_obl: 1 if obliquity is the same between dset pairs.
        same_all_grid: Equivalent to listing all of -same_dim, -same_delta,\
            -same_orient, -same_center, and -same_obl on the command line.
        val_diff: Output the sum of absolute differences of all voxels in the\
            dataset pair. A -1.0 value indicates a grid mismatch between volume\
            pairs.
        sval_diff: Same as -val_diff, but the sum is divided (scaled) by the\
            total number of voxels that are not zero in at least one of the two\
            datasets.
        monog_pairs: Instead of pairing each dset with the first, pair each\
            couple separately. This requires you to have an even number of dsets on\
            the command line.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dinfoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DINFO_METADATA)
    cargs = []
    cargs.append("3dinfo")
    if orient:
        cargs.append("-orient")
    if lextent:
        cargs.append("-Lextent")
    if rextent:
        cargs.append("-Rextent")
    if aextent:
        cargs.append("-Aextent")
    if pextent:
        cargs.append("-Pextent")
    if iextent:
        cargs.append("-Iextent")
    if sextent:
        cargs.append("-Sextent")
    if all_names:
        cargs.append("-all_names")
    if verb:
        cargs.append("-verb")
    if very_verbose:
        cargs.append("-VERB")
    if short:
        cargs.append("-short")
    if no_hist:
        cargs.append("-no_hist")
    if h:
        cargs.append("-h")
    if help_:
        cargs.append("-help")
    if extreme_help:
        cargs.append("-HELP")
    if h_view:
        cargs.append("-h_view")
    if h_web:
        cargs.append("-h_web")
    if h_find is not None:
        cargs.extend([
            "-h_find",
            h_find
        ])
    if h_raw:
        cargs.append("-h_raw")
    if h_spx:
        cargs.append("-h_spx")
    if h_aspx:
        cargs.append("-h_aspx")
    if all_opts:
        cargs.append("-all_opts")
    if label2index is not None:
        cargs.extend([
            "-label2index",
            label2index
        ])
    if niml_hdr:
        cargs.append("-niml_hdr")
    if subbrick_info:
        cargs.append("-subbrick_info")
    if exists:
        cargs.append("-exists")
    if id_:
        cargs.append("-id")
    if is_atlas:
        cargs.append("-is_atlas")
    if is_atlas_or_labeltable:
        cargs.append("-is_atlas_or_labeltable")
    if is_nifti:
        cargs.append("-is_nifti")
    if dset_extension:
        cargs.append("-dset_extension")
    if storage_mode:
        cargs.append("-storage_mode")
    if space:
        cargs.append("-space")
    if gen_space:
        cargs.append("-gen_space")
    if av_space:
        cargs.append("-av_space")
    if nifti_code:
        cargs.append("-nifti_code")
    if is_oblique:
        cargs.append("-is_oblique")
    if handedness:
        cargs.append("-handedness")
    if obliquity:
        cargs.append("-obliquity")
    if prefix:
        cargs.append("-prefix")
    if prefix_noext:
        cargs.append("-prefix_noext")
    if ni:
        cargs.append("-ni")
    if nj:
        cargs.append("-nj")
    if nk:
        cargs.append("-nk")
    if nijk:
        cargs.append("-nijk")
    if nv:
        cargs.append("-nv")
    if nt_:
        cargs.append("-nt")
    if n4:
        cargs.append("-n4")
    if nvi:
        cargs.append("-nvi")
    if nti:
        cargs.append("-nti")
    if ntimes:
        cargs.append("-ntimes")
    if max_node:
        cargs.append("-max_node")
    if di:
        cargs.append("-di")
    if dj:
        cargs.append("-dj")
    if dk:
        cargs.append("-dk")
    if d3:
        cargs.append("-d3")
    if adi:
        cargs.append("-adi")
    if adj:
        cargs.append("-adj")
    if adk:
        cargs.append("-adk")
    if ad3:
        cargs.append("-ad3")
    if voxvol:
        cargs.append("-voxvol")
    if oi:
        cargs.append("-oi")
    if oj:
        cargs.append("-oj")
    if ok:
        cargs.append("-ok")
    if o3:
        cargs.append("-o3")
    if dcx:
        cargs.append("-dcx")
    if dcy:
        cargs.append("-dcy")
    if dcz:
        cargs.append("-dcz")
    if dc3:
        cargs.append("-dc3")
    if tr:
        cargs.append("-tr")
    if dmin:
        cargs.append("-dmin")
    if dmax:
        cargs.append("-dmax")
    if dminus:
        cargs.append("-dminus")
    if dmaxus:
        cargs.append("-dmaxus")
    if smode:
        cargs.append("-smode")
    if header_name:
        cargs.append("-header_name")
    if brick_name:
        cargs.append("-brick_name")
    if iname:
        cargs.append("-iname")
    if extent:
        cargs.append("-extent")
    if fac:
        cargs.append("-fac")
    if label:
        cargs.append("-label")
    if datum:
        cargs.append("-datum")
    if min_:
        cargs.append("-min")
    if max_:
        cargs.append("-max")
    if minus:
        cargs.append("-minus")
    if maxus:
        cargs.append("-maxus")
    if labeltable:
        cargs.append("-labeltable")
    if labeltable_as_atlas_points:
        cargs.append("-labeltable_as_atlas_points")
    if atlas_points:
        cargs.append("-atlas_points")
    if history:
        cargs.append("-history")
    if slice_timing:
        cargs.append("-slice_timing")
    if header_line:
        cargs.append("-header_line")
    if hdr:
        cargs.append("-hdr")
    if sb_delim is not None:
        cargs.extend([
            "-sb_delim",
            sb_delim
        ])
    if na_flag is not None:
        cargs.extend([
            "-NA_flag",
            na_flag
        ])
    if atr_delim is not None:
        cargs.extend([
            "-atr_delim",
            atr_delim
        ])
    if aform_real:
        cargs.append("-aform_real")
    if aform_real_oneline:
        cargs.append("-aform_real_oneline")
    if aform_real_refit_ori:
        cargs.append("-aform_real_refit_ori")
    if is_aform_real_orth:
        cargs.append("-is_aform_real_orth")
    if aform_orth:
        cargs.append("-aform_orth")
    if perm_to_orient is not None:
        cargs.extend([
            "-perm_to_orient",
            perm_to_orient
        ])
    if same_grid:
        cargs.append("-same_grid")
    if same_dim:
        cargs.append("-same_dim")
    if same_delta:
        cargs.append("-same_delta")
    if same_orient:
        cargs.append("-same_orient")
    if same_center:
        cargs.append("-same_center")
    if same_obl:
        cargs.append("-same_obl")
    if same_all_grid:
        cargs.append("-same_all_grid")
    if val_diff:
        cargs.append("-val_diff")
    if sval_diff:
        cargs.append("-sval_diff")
    if monog_pairs:
        cargs.append("-monog_pairs")
    cargs.extend([execution.input_file(f) for f in dataset])
    ret = V3dinfoOutputs(
        root=execution.output_file("."),
        info=[],
    )
    execution.run(cargs, handle_stdout=lambda s: ret.info.append(s))
    return ret


__all__ = [
    "V3dinfoOutputs",
    "V_3DINFO_METADATA",
    "v_3dinfo",
]
