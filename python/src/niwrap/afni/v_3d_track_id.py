# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_TRACK_ID_METADATA = Metadata(
    id="5cf38d09f658de902f96f871914d246c66fcdb31",
    name="3dTrackID",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dTrackIdOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_track_id(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    indimap: OutputPathType
    """Output of INDIMAP"""
    pairmap: OutputPathType
    """Output of PAIRMAP"""
    grid: OutputPathType
    """Text file output of statistics of WM-ROIs"""
    niml_tract: OutputPathType
    """Track-like output for viewing in SUMA"""
    niml_dset: OutputPathType
    """Dataset output for use with *.niml.tract"""
    trk: OutputPathType
    """TrackVis-like output for viewing in TrackVis"""
    pairmap_labeltable: OutputPathType
    """Output of PAIRMAP labeltable"""
    roi_labels: OutputPathType
    """Output file of all ROI labels"""
    option_values: OutputPathType
    """Output of all option values"""


def v_3d_track_id(
    mode: typing.Literal["DET", "MINIP", "PROB"],
    netrois: InputPathType,
    prefix: str,
    logic: typing.Literal["OR", "AND"],
    dti_in: str | None = None,
    dti_list: InputPathType | None = None,
    dti_extra: str | None = None,
    dti_search_no: bool = False,
    hardi_gfa: InputPathType | None = None,
    hardi_dirs: InputPathType | None = None,
    hardi_pars: str | None = None,
    mask: InputPathType | None = None,
    thru_mask: InputPathType | None = None,
    targ_surf_stop: bool = False,
    targ_surf_twixt: bool = False,
    mini_num: float | int | None = None,
    uncert: InputPathType | None = None,
    unc_min_fa: float | int | None = None,
    unc_min_v: float | int | None = None,
    algopt: InputPathType | None = None,
    alg_thresh_fa: float | int | None = None,
    alg_thresh_ang: float | int | None = None,
    alg_thresh_len: float | int | None = None,
    alg_nseed_x: float | int | None = None,
    alg_nseed_y: float | int | None = None,
    alg_nseed_z: float | int | None = None,
    alg_thresh_frac: float | int | None = None,
    alg_nseed_vox: float | int | None = None,
    alg_nmonte: float | int | None = None,
    extra_tr_par: bool = False,
    uncut_at_rois: bool = False,
    dump_rois: typing.Literal["DUMP", "AFNI", "BOTH", "AFNI_MAP"] | None = None,
    dump_no_labtab: bool = False,
    dump_lab_consec: bool = False,
    posteriori: bool = False,
    rec_orig: bool = False,
    do_trk_out: bool = False,
    trk_opp_orient: bool = False,
    nifti: bool = False,
    no_indipair_out: bool = False,
    write_rois: bool = False,
    write_opts: bool = False,
    pair_out_power: bool = False,
    verb: float | int | None = None,
    runner: Runner | None = None,
) -> V3dTrackIdOutputs:
    """
    3dTrackID by AFNI Team.
    
    FACTID-based tractography code for AFNI, part of FATCAT.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dTrackID.html
    
    Args:
        mode: The mode of tracking: DET, MINIP, or PROB.
        netrois: Network ROI mask(s).
        prefix: Prefix for output files.
        logic: Control logic connections among target ROIs per network.
        dti_in: Input DTI volumes basename.
        dti_list: Alternative way to specify DTI input files, a NIML-formatted\
            text file.
        dti_extra: Option for extra scalar for WM skeleton thresholding.
        dti_search_no: Turn off automatic search for additional scalar files to\
            include in output.
        hardi_gfa: Single brik dataset with generalized FA (GFA) info.
        hardi_dirs: Directions file for HARDI data containing directions\
            components.
        hardi_pars: Prefix to search for scalar files naming format.
        mask: Mask within which tracking is done. Optional but highly\
            recommended.
        thru_mask: Extra restrictor mask through which paths are strictly\
            required to pass.
        targ_surf_stop: Make tracts stop at outer surfaces of the target ROIs.
        targ_surf_twixt: Make tracts stop just before entering target surfaces.
        mini_num: Number of whole brain Monte Carlo iterations for\
            mini-probabilistic tracking.
        uncert: Uncertainty values file.
        unc_min_fa: Minimum stdev for perturbing FA.
        unc_min_v: Minimum stdev for perturbing direction-vectors.
        algopt: Specify tracking parameter quantities file in ASCII.
        alg_thresh_fa: Set threshold for FA map or other WM proxy.
        alg_thresh_ang: Set maximum angle for turning during propagation.
        alg_thresh_len: Set minimum physical length of tracts to keep.
        alg_nseed_x: Number of seeds per voxel in x-direction.
        alg_nseed_y: Number of seeds per voxel in y-direction.
        alg_nseed_z: Number of seeds per voxel in z-direction.
        alg_thresh_frac: Value for thresholding the fraction of tracks through\
            a voxel for a given connection.
        alg_nseed_vox: Number of seeds per voxel per Monte Carlo iteration.
        alg_nmonte: Number of Monte Carlo iterations.
        extra_tr_par: Run three extra track parameter scalings for each\
            connection.
        uncut_at_rois: Keep entire track even if overshoots a target.
        dump_rois: Output individual masks of ROI connections.
        dump_no_labtab: Turn off label table use in ROI dump output.
        dump_lab_consec: DON'T apply numerical labels of original ROIs in dump\
            output.
        posteriori: Output individual files with number of tracks per voxel per\
            pair.
        rec_orig: Record dataset origin in header of *.trk file.
        do_trk_out: Output *.trk files for viewing in TrackVis.
        trk_opp_orient: Oppositize voxel_order for TRK files.
        nifti: Output files in *.nii.gz format.
        no_indipair_out: Do not output INDIMAP and PAIRMAP volumes.
        write_rois: Write out ROI labels.
        write_opts: Write out all option values.
        pair_out_power: Switch to use powers of two labelling for PAIRMAP.
        verb: Set verbosity level.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTrackIdOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TRACK_ID_METADATA)
    cargs = []
    cargs.append("3dTrackID")
    cargs.append("-mode")
    cargs.append("{DET")
    cargs.append("|")
    cargs.append("MINIP")
    cargs.append("|")
    cargs.append("PROB}")
    cargs.append("[ALL_REQUIRED_OPTIONS]")
    cargs.append("[MODEL_SPECIFIC_OPTIONS]")
    cargs.append("[MODE_SPECIFIC_OPTIONS]")
    cargs.append("[OTHER_OPTIONS]")
    ret = V3dTrackIdOutputs(
        root=execution.output_file("."),
        indimap=execution.output_file(f"{prefix}_INDIMAP.nii.gz", optional=True),
        pairmap=execution.output_file(f"{prefix}_PAIRMAP.nii.gz", optional=True),
        grid=execution.output_file(f"{prefix}.grid", optional=True),
        niml_tract=execution.output_file(f"{prefix}.niml.tract", optional=True),
        niml_dset=execution.output_file(f"{prefix}.niml.dset", optional=True),
        trk=execution.output_file(f"{prefix}.trk", optional=True),
        pairmap_labeltable=execution.output_file(f"{prefix}_PAIRS.niml.lt", optional=True),
        roi_labels=execution.output_file(f"{prefix}_roi.labs", optional=True),
        option_values=execution.output_file(f"{prefix}.niml.opts", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dTrackIdOutputs",
    "V_3D_TRACK_ID_METADATA",
    "v_3d_track_id",
]
