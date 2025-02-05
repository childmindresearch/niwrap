# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_SEGSTATS_METADATA = Metadata(
    id="de1b9dfa3f1dac83d5a96b745b8f327109cb07d4.boutiques",
    name="mri_segstats",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriSegstatsParameters = typing.TypedDict('MriSegstatsParameters', {
    "__STYX_TYPE__": typing.Literal["mri_segstats"],
    "segvol": InputPathType,
    "annot_subject": typing.NotRequired[str | None],
    "annot_hemisphere": typing.NotRequired[str | None],
    "annot_parcellation": typing.NotRequired[str | None],
    "slabel_subject": typing.NotRequired[str | None],
    "slabel_hemisphere": typing.NotRequired[str | None],
    "slabel_label": typing.NotRequired[InputPathType | None],
    "output_file": str,
    "partial_vol_comp": typing.NotRequired[InputPathType | None],
    "input_volume": typing.NotRequired[InputPathType | None],
    "seg_erode": typing.NotRequired[float | None],
    "frame": typing.NotRequired[float | None],
    "robust": typing.NotRequired[float | None],
    "square_input": bool,
    "sqrt_input": bool,
    "multiply_input": typing.NotRequired[float | None],
    "divide_input": typing.NotRequired[float | None],
    "snr_column": bool,
    "absolute_value": bool,
    "accumulate_mean": bool,
    "color_table": typing.NotRequired[InputPathType | None],
    "default_color_table": bool,
    "gca_color_table": typing.NotRequired[InputPathType | None],
    "ids": typing.NotRequired[str | None],
    "exclude_ids": typing.NotRequired[str | None],
    "exclude_gm_wm": bool,
    "surf_wm_vol": bool,
    "surf_ctx_vol": bool,
    "no_global_stats": bool,
    "empty_segments": bool,
    "ctab_output": typing.NotRequired[str | None],
    "mask_volume": typing.NotRequired[InputPathType | None],
    "mask_threshold": typing.NotRequired[float | None],
    "mask_sign": typing.NotRequired[str | None],
    "mask_frame": typing.NotRequired[float | None],
    "invert_mask": bool,
    "mask_erode": typing.NotRequired[float | None],
    "brain_vol_seg": bool,
    "brain_mask_vol": typing.NotRequired[InputPathType | None],
    "subcortical_gray": bool,
    "total_gray": bool,
    "intracranial_volume": bool,
    "intracranial_volume_only": bool,
    "old_intracranial_volume_only": bool,
    "talairach_transform": typing.NotRequired[InputPathType | None],
    "xfm_to_etiv": typing.NotRequired[str | None],
    "euler_hole_count": bool,
    "avg_waveform": typing.NotRequired[str | None],
    "sum_waveform": typing.NotRequired[str | None],
    "avg_waveform_vol": typing.NotRequired[str | None],
    "remove_avgwf_mean": bool,
    "spatial_frame_avg": typing.NotRequired[str | None],
    "voxel_crs": typing.NotRequired[str | None],
    "replace_ids": typing.NotRequired[str | None],
    "replace_ids_file": typing.NotRequired[InputPathType | None],
    "gtm_default_seg_merge": bool,
    "gtm_default_seg_merge_choroid": bool,
    "qa_stats_file": typing.NotRequired[str | None],
    "subjects_dir": typing.NotRequired[str | None],
    "random_seed": typing.NotRequired[float | None],
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
        "mri_segstats": mri_segstats_cargs,
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
        "mri_segstats": mri_segstats_outputs,
    }
    return vt.get(t)


class MriSegstatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_segstats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    summary_output_file: OutputPathType
    """Output file for summary statistics."""
    avg_waveform_output: OutputPathType | None
    """Average waveform output text file."""
    sum_waveform_output: OutputPathType | None
    """Sum waveform output text file."""
    avg_waveform_vol_output: OutputPathType | None
    """Average waveform volume output file."""
    spatial_frame_avg_output: OutputPathType | None
    """Spatial frame average output file."""
    ctab_output_file: OutputPathType | None
    """Output color table with the reported segmentations."""


def mri_segstats_params(
    segvol: InputPathType,
    output_file: str,
    annot_subject: str | None = None,
    annot_hemisphere: str | None = None,
    annot_parcellation: str | None = None,
    slabel_subject: str | None = None,
    slabel_hemisphere: str | None = None,
    slabel_label: InputPathType | None = None,
    partial_vol_comp: InputPathType | None = None,
    input_volume: InputPathType | None = None,
    seg_erode: float | None = None,
    frame: float | None = None,
    robust: float | None = None,
    square_input: bool = False,
    sqrt_input: bool = False,
    multiply_input: float | None = None,
    divide_input: float | None = None,
    snr_column: bool = False,
    absolute_value: bool = False,
    accumulate_mean: bool = False,
    color_table: InputPathType | None = None,
    default_color_table: bool = False,
    gca_color_table: InputPathType | None = None,
    ids: str | None = None,
    exclude_ids: str | None = None,
    exclude_gm_wm: bool = False,
    surf_wm_vol: bool = False,
    surf_ctx_vol: bool = False,
    no_global_stats: bool = False,
    empty_segments: bool = False,
    ctab_output: str | None = None,
    mask_volume: InputPathType | None = None,
    mask_threshold: float | None = None,
    mask_sign: str | None = None,
    mask_frame: float | None = None,
    invert_mask: bool = False,
    mask_erode: float | None = None,
    brain_vol_seg: bool = False,
    brain_mask_vol: InputPathType | None = None,
    subcortical_gray: bool = False,
    total_gray: bool = False,
    intracranial_volume: bool = False,
    intracranial_volume_only: bool = False,
    old_intracranial_volume_only: bool = False,
    talairach_transform: InputPathType | None = None,
    xfm_to_etiv: str | None = None,
    euler_hole_count: bool = False,
    avg_waveform: str | None = None,
    sum_waveform: str | None = None,
    avg_waveform_vol: str | None = None,
    remove_avgwf_mean: bool = False,
    spatial_frame_avg: str | None = None,
    voxel_crs: str | None = None,
    replace_ids: str | None = None,
    replace_ids_file: InputPathType | None = None,
    gtm_default_seg_merge: bool = False,
    gtm_default_seg_merge_choroid: bool = False,
    qa_stats_file: str | None = None,
    subjects_dir: str | None = None,
    random_seed: float | None = None,
) -> MriSegstatsParameters:
    """
    Build parameters.
    
    Args:
        segvol: Input segmentation volume. This volume's voxel values indicate\
            a segmentation or class.
        output_file: ASCII file in which summary statistics are saved.
        annot_subject: Create a segmentation from hemi.parc.annot. Subject is\
            the name of the subject.
        annot_hemisphere:.
        annot_parcellation:.
        slabel_subject: Create a segmentation from the given surface label. The\
            points in the label are given a value of 1; 0 for outside.
        slabel_hemisphere:.
        slabel_label:.
        partial_vol_comp: Use pvvol to compensate for partial voluming,\
            resulting in more accurate volumes.
        input_volume: Input volume from which to compute more statistics.
        seg_erode: Erode segmentation boundaries by Nerodes.
        frame: Report statistics of the input volume at the specified 0-based\
            frame number.
        robust: Compute stats after excluding a percentage of high and low\
            values.
        square_input: Compute the square of the input before computing stats.
        sqrt_input: Compute the square root of the input before computing\
            stats.
        multiply_input: Multiply input by value.
        divide_input: Divide input by value.
        snr_column: Save mean/std as extra column in output table.
        absolute_value: Compute absolute value of input before spatial average.
        accumulate_mean: Save mean*nvoxels instead of mean.
        color_table: FreeSurfer color table file to specify how each\
            segmentation index is mapped to a segmentation name and color.
        default_color_table: Use default color table from\
            FreeSurferColorLUT.txt.
        gca_color_table: Get color table from the given GCA file.
        ids: Specify numeric segmentation ids.
        exclude_ids: Exclude the given segmentation id(s) from report.
        exclude_gm_wm: Exclude cortical gray and white matter based on\
            predefined IDs.
        surf_wm_vol: Compute cortical matter volume based on the white surface\
            volume.
        surf_ctx_vol: Compute cortical volumes from surface.
        no_global_stats: Turns off computation of global stats.
        empty_segments: Report on segmentations listed in the color table even\
            if they are not found in the segmentation volume.
        ctab_output: Create an output color table with just the segmentations\
            reported.
        mask_volume: Exclude voxels that are not in the mask. Voxels to be\
            excluded are assigned a segid of 0.
        mask_threshold: Exclude voxels that are below thresh, above -thresh, or\
            between -thresh and +thresh.
        mask_sign: Specify sign for masking threshold. Choices are abs, pos,\
            and neg.
        mask_frame: Derive the mask volume from the specified 0-based frame.
        invert_mask: After applying all the masking criteria, invert the mask.
        mask_erode: Erode mask by specified number of iterations.
        brain_vol_seg: Get volume of brain as the sum of the volumes of the\
            segmentations that are in the brain.
        brain_mask_vol: Load brain mask and compute brain volume from non-zero\
            voxels.
        subcortical_gray: Compute volume of subcortical gray matter.
        total_gray: Compute volume of total gray matter.
        intracranial_volume: Compute intracranial volume from talairach.xfm.
        intracranial_volume_only: Compute intracranial volume from\
            talairach.xfm and exit.
        old_intracranial_volume_only: Compute intracranial volume from\
            talairach_with_skull.lta and exit.
        talairach_transform: Specify path to talairach.xfm file for eTIV.
        xfm_to_etiv: Convert xfm to eTIV and write to output file.
        euler_hole_count: Write out number of defect holes based on the Euler\
            number.
        avg_waveform: Compute the average waveform and save to text file.
        sum_waveform: Compute the sum waveform and save to text file.
        avg_waveform_vol: Compute average waveform and save to MRI volume.
        remove_avgwf_mean: Remove temporal mean from avgwf and avgwfvol.
        spatial_frame_avg: Save mean across space and frame.
        voxel_crs: Replace segmentation with all 0s except at specified voxel.
        replace_ids: Replace segmentation ID1 with ID2.
        replace_ids_file: Replace segmentations based on pairs in file.
        gtm_default_seg_merge: Replace segmentations based on GTM default.
        gtm_default_seg_merge_choroid: Replace segmentations based on GTM\
            default excluding choroid.
        qa_stats_file: Compute stats useful for quality control.
        subjects_dir: Set SUBJECTS_DIR environment variable.
        random_seed: Set random number generator seed value.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_segstats",
        "segvol": segvol,
        "output_file": output_file,
        "square_input": square_input,
        "sqrt_input": sqrt_input,
        "snr_column": snr_column,
        "absolute_value": absolute_value,
        "accumulate_mean": accumulate_mean,
        "default_color_table": default_color_table,
        "exclude_gm_wm": exclude_gm_wm,
        "surf_wm_vol": surf_wm_vol,
        "surf_ctx_vol": surf_ctx_vol,
        "no_global_stats": no_global_stats,
        "empty_segments": empty_segments,
        "invert_mask": invert_mask,
        "brain_vol_seg": brain_vol_seg,
        "subcortical_gray": subcortical_gray,
        "total_gray": total_gray,
        "intracranial_volume": intracranial_volume,
        "intracranial_volume_only": intracranial_volume_only,
        "old_intracranial_volume_only": old_intracranial_volume_only,
        "euler_hole_count": euler_hole_count,
        "remove_avgwf_mean": remove_avgwf_mean,
        "gtm_default_seg_merge": gtm_default_seg_merge,
        "gtm_default_seg_merge_choroid": gtm_default_seg_merge_choroid,
    }
    if annot_subject is not None:
        params["annot_subject"] = annot_subject
    if annot_hemisphere is not None:
        params["annot_hemisphere"] = annot_hemisphere
    if annot_parcellation is not None:
        params["annot_parcellation"] = annot_parcellation
    if slabel_subject is not None:
        params["slabel_subject"] = slabel_subject
    if slabel_hemisphere is not None:
        params["slabel_hemisphere"] = slabel_hemisphere
    if slabel_label is not None:
        params["slabel_label"] = slabel_label
    if partial_vol_comp is not None:
        params["partial_vol_comp"] = partial_vol_comp
    if input_volume is not None:
        params["input_volume"] = input_volume
    if seg_erode is not None:
        params["seg_erode"] = seg_erode
    if frame is not None:
        params["frame"] = frame
    if robust is not None:
        params["robust"] = robust
    if multiply_input is not None:
        params["multiply_input"] = multiply_input
    if divide_input is not None:
        params["divide_input"] = divide_input
    if color_table is not None:
        params["color_table"] = color_table
    if gca_color_table is not None:
        params["gca_color_table"] = gca_color_table
    if ids is not None:
        params["ids"] = ids
    if exclude_ids is not None:
        params["exclude_ids"] = exclude_ids
    if ctab_output is not None:
        params["ctab_output"] = ctab_output
    if mask_volume is not None:
        params["mask_volume"] = mask_volume
    if mask_threshold is not None:
        params["mask_threshold"] = mask_threshold
    if mask_sign is not None:
        params["mask_sign"] = mask_sign
    if mask_frame is not None:
        params["mask_frame"] = mask_frame
    if mask_erode is not None:
        params["mask_erode"] = mask_erode
    if brain_mask_vol is not None:
        params["brain_mask_vol"] = brain_mask_vol
    if talairach_transform is not None:
        params["talairach_transform"] = talairach_transform
    if xfm_to_etiv is not None:
        params["xfm_to_etiv"] = xfm_to_etiv
    if avg_waveform is not None:
        params["avg_waveform"] = avg_waveform
    if sum_waveform is not None:
        params["sum_waveform"] = sum_waveform
    if avg_waveform_vol is not None:
        params["avg_waveform_vol"] = avg_waveform_vol
    if spatial_frame_avg is not None:
        params["spatial_frame_avg"] = spatial_frame_avg
    if voxel_crs is not None:
        params["voxel_crs"] = voxel_crs
    if replace_ids is not None:
        params["replace_ids"] = replace_ids
    if replace_ids_file is not None:
        params["replace_ids_file"] = replace_ids_file
    if qa_stats_file is not None:
        params["qa_stats_file"] = qa_stats_file
    if subjects_dir is not None:
        params["subjects_dir"] = subjects_dir
    if random_seed is not None:
        params["random_seed"] = random_seed
    return params


def mri_segstats_cargs(
    params: MriSegstatsParameters,
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
    cargs.append("mri_segstats")
    cargs.extend([
        "--seg",
        execution.input_file(params.get("segvol"))
    ])
    if params.get("annot_subject") is not None:
        cargs.extend([
            "--annot",
            params.get("annot_subject")
        ])
    if params.get("annot_hemisphere") is not None:
        cargs.append(params.get("annot_hemisphere"))
    if params.get("annot_parcellation") is not None:
        cargs.append(params.get("annot_parcellation"))
    if params.get("slabel_subject") is not None:
        cargs.extend([
            "--slabel",
            params.get("slabel_subject")
        ])
    if params.get("slabel_hemisphere") is not None:
        cargs.append(params.get("slabel_hemisphere"))
    if params.get("slabel_label") is not None:
        cargs.append(execution.input_file(params.get("slabel_label")))
    cargs.extend([
        "--o",
        params.get("output_file")
    ])
    if params.get("partial_vol_comp") is not None:
        cargs.extend([
            "--pv",
            execution.input_file(params.get("partial_vol_comp"))
        ])
    if params.get("input_volume") is not None:
        cargs.extend([
            "--i",
            execution.input_file(params.get("input_volume"))
        ])
    if params.get("seg_erode") is not None:
        cargs.extend([
            "--seg-erode",
            str(params.get("seg_erode"))
        ])
    if params.get("frame") is not None:
        cargs.extend([
            "--frame",
            str(params.get("frame"))
        ])
    if params.get("robust") is not None:
        cargs.extend([
            "--robust",
            str(params.get("robust"))
        ])
    if params.get("square_input"):
        cargs.append("--sqr")
    if params.get("sqrt_input"):
        cargs.append("--sqrt")
    if params.get("multiply_input") is not None:
        cargs.extend([
            "--mul",
            str(params.get("multiply_input"))
        ])
    if params.get("divide_input") is not None:
        cargs.extend([
            "--div",
            str(params.get("divide_input"))
        ])
    if params.get("snr_column"):
        cargs.append("--snr")
    if params.get("absolute_value"):
        cargs.append("--abs")
    if params.get("accumulate_mean"):
        cargs.append("--accumulate")
    if params.get("color_table") is not None:
        cargs.extend([
            "--ctab",
            execution.input_file(params.get("color_table"))
        ])
    if params.get("default_color_table"):
        cargs.append("--ctab-default")
    if params.get("gca_color_table") is not None:
        cargs.extend([
            "--ctab-gca",
            execution.input_file(params.get("gca_color_table"))
        ])
    if params.get("ids") is not None:
        cargs.extend([
            "--id",
            params.get("ids")
        ])
    if params.get("exclude_ids") is not None:
        cargs.extend([
            "--excludeid",
            params.get("exclude_ids")
        ])
    if params.get("exclude_gm_wm"):
        cargs.append("--excl-ctxgmwm")
    if params.get("surf_wm_vol"):
        cargs.append("--surf-wm-vol")
    if params.get("surf_ctx_vol"):
        cargs.append("--surf-ctx-vol")
    if params.get("no_global_stats"):
        cargs.append("--no-global-stats")
    if params.get("empty_segments"):
        cargs.append("--empty")
    if params.get("ctab_output") is not None:
        cargs.extend([
            "--ctab-out",
            params.get("ctab_output")
        ])
    if params.get("mask_volume") is not None:
        cargs.extend([
            "--mask",
            execution.input_file(params.get("mask_volume"))
        ])
    if params.get("mask_threshold") is not None:
        cargs.extend([
            "--maskthresh",
            str(params.get("mask_threshold"))
        ])
    if params.get("mask_sign") is not None:
        cargs.extend([
            "--masksign",
            params.get("mask_sign")
        ])
    if params.get("mask_frame") is not None:
        cargs.extend([
            "--maskframe",
            str(params.get("mask_frame"))
        ])
    if params.get("invert_mask"):
        cargs.append("--maskinvert")
    if params.get("mask_erode") is not None:
        cargs.extend([
            "--maskerode",
            str(params.get("mask_erode"))
        ])
    if params.get("brain_vol_seg"):
        cargs.append("--brain-vol-from-seg")
    if params.get("brain_mask_vol") is not None:
        cargs.extend([
            "--brainmask",
            execution.input_file(params.get("brain_mask_vol"))
        ])
    if params.get("subcortical_gray"):
        cargs.append("--subcortgray")
    if params.get("total_gray"):
        cargs.append("--totalgray")
    if params.get("intracranial_volume"):
        cargs.append("--etiv")
    if params.get("intracranial_volume_only"):
        cargs.append("--etiv-only")
    if params.get("old_intracranial_volume_only"):
        cargs.append("--old-etiv-only")
    if params.get("talairach_transform") is not None:
        cargs.extend([
            "--talxfm",
            execution.input_file(params.get("talairach_transform"))
        ])
    if params.get("xfm_to_etiv") is not None:
        cargs.extend([
            "--xfm2etiv",
            params.get("xfm_to_etiv")
        ])
    if params.get("euler_hole_count"):
        cargs.append("--euler")
    if params.get("avg_waveform") is not None:
        cargs.extend([
            "--avgwf",
            params.get("avg_waveform")
        ])
    if params.get("sum_waveform") is not None:
        cargs.extend([
            "--sumwf",
            params.get("sum_waveform")
        ])
    if params.get("avg_waveform_vol") is not None:
        cargs.extend([
            "--avgwfvol",
            params.get("avg_waveform_vol")
        ])
    if params.get("remove_avgwf_mean"):
        cargs.append("--avgwf-remove-mean")
    if params.get("spatial_frame_avg") is not None:
        cargs.extend([
            "--sfavg",
            params.get("spatial_frame_avg")
        ])
    if params.get("voxel_crs") is not None:
        cargs.extend([
            "--vox",
            params.get("voxel_crs")
        ])
    if params.get("replace_ids") is not None:
        cargs.extend([
            "--replace",
            params.get("replace_ids")
        ])
    if params.get("replace_ids_file") is not None:
        cargs.extend([
            "--replace-file",
            execution.input_file(params.get("replace_ids_file"))
        ])
    if params.get("gtm_default_seg_merge"):
        cargs.append("--gtm-default-seg-merge")
    if params.get("gtm_default_seg_merge_choroid"):
        cargs.append("--gtm-default-seg-merge-choroid")
    if params.get("qa_stats_file") is not None:
        cargs.extend([
            "--qa-stats",
            params.get("qa_stats_file")
        ])
    if params.get("subjects_dir") is not None:
        cargs.extend([
            "--sd",
            params.get("subjects_dir")
        ])
    if params.get("random_seed") is not None:
        cargs.extend([
            "--seed",
            str(params.get("random_seed"))
        ])
    return cargs


def mri_segstats_outputs(
    params: MriSegstatsParameters,
    execution: Execution,
) -> MriSegstatsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriSegstatsOutputs(
        root=execution.output_file("."),
        summary_output_file=execution.output_file(params.get("output_file")),
        avg_waveform_output=execution.output_file(params.get("avg_waveform")) if (params.get("avg_waveform") is not None) else None,
        sum_waveform_output=execution.output_file(params.get("sum_waveform")) if (params.get("sum_waveform") is not None) else None,
        avg_waveform_vol_output=execution.output_file(params.get("avg_waveform_vol")) if (params.get("avg_waveform_vol") is not None) else None,
        spatial_frame_avg_output=execution.output_file(params.get("spatial_frame_avg")) if (params.get("spatial_frame_avg") is not None) else None,
        ctab_output_file=execution.output_file(params.get("ctab_output")) if (params.get("ctab_output") is not None) else None,
    )
    return ret


def mri_segstats_execute(
    params: MriSegstatsParameters,
    execution: Execution,
) -> MriSegstatsOutputs:
    """
    Calculates measures and stats derived from brain segmentation data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriSegstatsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_segstats_cargs(params, execution)
    ret = mri_segstats_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_segstats(
    segvol: InputPathType,
    output_file: str,
    annot_subject: str | None = None,
    annot_hemisphere: str | None = None,
    annot_parcellation: str | None = None,
    slabel_subject: str | None = None,
    slabel_hemisphere: str | None = None,
    slabel_label: InputPathType | None = None,
    partial_vol_comp: InputPathType | None = None,
    input_volume: InputPathType | None = None,
    seg_erode: float | None = None,
    frame: float | None = None,
    robust: float | None = None,
    square_input: bool = False,
    sqrt_input: bool = False,
    multiply_input: float | None = None,
    divide_input: float | None = None,
    snr_column: bool = False,
    absolute_value: bool = False,
    accumulate_mean: bool = False,
    color_table: InputPathType | None = None,
    default_color_table: bool = False,
    gca_color_table: InputPathType | None = None,
    ids: str | None = None,
    exclude_ids: str | None = None,
    exclude_gm_wm: bool = False,
    surf_wm_vol: bool = False,
    surf_ctx_vol: bool = False,
    no_global_stats: bool = False,
    empty_segments: bool = False,
    ctab_output: str | None = None,
    mask_volume: InputPathType | None = None,
    mask_threshold: float | None = None,
    mask_sign: str | None = None,
    mask_frame: float | None = None,
    invert_mask: bool = False,
    mask_erode: float | None = None,
    brain_vol_seg: bool = False,
    brain_mask_vol: InputPathType | None = None,
    subcortical_gray: bool = False,
    total_gray: bool = False,
    intracranial_volume: bool = False,
    intracranial_volume_only: bool = False,
    old_intracranial_volume_only: bool = False,
    talairach_transform: InputPathType | None = None,
    xfm_to_etiv: str | None = None,
    euler_hole_count: bool = False,
    avg_waveform: str | None = None,
    sum_waveform: str | None = None,
    avg_waveform_vol: str | None = None,
    remove_avgwf_mean: bool = False,
    spatial_frame_avg: str | None = None,
    voxel_crs: str | None = None,
    replace_ids: str | None = None,
    replace_ids_file: InputPathType | None = None,
    gtm_default_seg_merge: bool = False,
    gtm_default_seg_merge_choroid: bool = False,
    qa_stats_file: str | None = None,
    subjects_dir: str | None = None,
    random_seed: float | None = None,
    runner: Runner | None = None,
) -> MriSegstatsOutputs:
    """
    Calculates measures and stats derived from brain segmentation data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        segvol: Input segmentation volume. This volume's voxel values indicate\
            a segmentation or class.
        output_file: ASCII file in which summary statistics are saved.
        annot_subject: Create a segmentation from hemi.parc.annot. Subject is\
            the name of the subject.
        annot_hemisphere:.
        annot_parcellation:.
        slabel_subject: Create a segmentation from the given surface label. The\
            points in the label are given a value of 1; 0 for outside.
        slabel_hemisphere:.
        slabel_label:.
        partial_vol_comp: Use pvvol to compensate for partial voluming,\
            resulting in more accurate volumes.
        input_volume: Input volume from which to compute more statistics.
        seg_erode: Erode segmentation boundaries by Nerodes.
        frame: Report statistics of the input volume at the specified 0-based\
            frame number.
        robust: Compute stats after excluding a percentage of high and low\
            values.
        square_input: Compute the square of the input before computing stats.
        sqrt_input: Compute the square root of the input before computing\
            stats.
        multiply_input: Multiply input by value.
        divide_input: Divide input by value.
        snr_column: Save mean/std as extra column in output table.
        absolute_value: Compute absolute value of input before spatial average.
        accumulate_mean: Save mean*nvoxels instead of mean.
        color_table: FreeSurfer color table file to specify how each\
            segmentation index is mapped to a segmentation name and color.
        default_color_table: Use default color table from\
            FreeSurferColorLUT.txt.
        gca_color_table: Get color table from the given GCA file.
        ids: Specify numeric segmentation ids.
        exclude_ids: Exclude the given segmentation id(s) from report.
        exclude_gm_wm: Exclude cortical gray and white matter based on\
            predefined IDs.
        surf_wm_vol: Compute cortical matter volume based on the white surface\
            volume.
        surf_ctx_vol: Compute cortical volumes from surface.
        no_global_stats: Turns off computation of global stats.
        empty_segments: Report on segmentations listed in the color table even\
            if they are not found in the segmentation volume.
        ctab_output: Create an output color table with just the segmentations\
            reported.
        mask_volume: Exclude voxels that are not in the mask. Voxels to be\
            excluded are assigned a segid of 0.
        mask_threshold: Exclude voxels that are below thresh, above -thresh, or\
            between -thresh and +thresh.
        mask_sign: Specify sign for masking threshold. Choices are abs, pos,\
            and neg.
        mask_frame: Derive the mask volume from the specified 0-based frame.
        invert_mask: After applying all the masking criteria, invert the mask.
        mask_erode: Erode mask by specified number of iterations.
        brain_vol_seg: Get volume of brain as the sum of the volumes of the\
            segmentations that are in the brain.
        brain_mask_vol: Load brain mask and compute brain volume from non-zero\
            voxels.
        subcortical_gray: Compute volume of subcortical gray matter.
        total_gray: Compute volume of total gray matter.
        intracranial_volume: Compute intracranial volume from talairach.xfm.
        intracranial_volume_only: Compute intracranial volume from\
            talairach.xfm and exit.
        old_intracranial_volume_only: Compute intracranial volume from\
            talairach_with_skull.lta and exit.
        talairach_transform: Specify path to talairach.xfm file for eTIV.
        xfm_to_etiv: Convert xfm to eTIV and write to output file.
        euler_hole_count: Write out number of defect holes based on the Euler\
            number.
        avg_waveform: Compute the average waveform and save to text file.
        sum_waveform: Compute the sum waveform and save to text file.
        avg_waveform_vol: Compute average waveform and save to MRI volume.
        remove_avgwf_mean: Remove temporal mean from avgwf and avgwfvol.
        spatial_frame_avg: Save mean across space and frame.
        voxel_crs: Replace segmentation with all 0s except at specified voxel.
        replace_ids: Replace segmentation ID1 with ID2.
        replace_ids_file: Replace segmentations based on pairs in file.
        gtm_default_seg_merge: Replace segmentations based on GTM default.
        gtm_default_seg_merge_choroid: Replace segmentations based on GTM\
            default excluding choroid.
        qa_stats_file: Compute stats useful for quality control.
        subjects_dir: Set SUBJECTS_DIR environment variable.
        random_seed: Set random number generator seed value.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriSegstatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_SEGSTATS_METADATA)
    params = mri_segstats_params(segvol=segvol, annot_subject=annot_subject, annot_hemisphere=annot_hemisphere, annot_parcellation=annot_parcellation, slabel_subject=slabel_subject, slabel_hemisphere=slabel_hemisphere, slabel_label=slabel_label, output_file=output_file, partial_vol_comp=partial_vol_comp, input_volume=input_volume, seg_erode=seg_erode, frame=frame, robust=robust, square_input=square_input, sqrt_input=sqrt_input, multiply_input=multiply_input, divide_input=divide_input, snr_column=snr_column, absolute_value=absolute_value, accumulate_mean=accumulate_mean, color_table=color_table, default_color_table=default_color_table, gca_color_table=gca_color_table, ids=ids, exclude_ids=exclude_ids, exclude_gm_wm=exclude_gm_wm, surf_wm_vol=surf_wm_vol, surf_ctx_vol=surf_ctx_vol, no_global_stats=no_global_stats, empty_segments=empty_segments, ctab_output=ctab_output, mask_volume=mask_volume, mask_threshold=mask_threshold, mask_sign=mask_sign, mask_frame=mask_frame, invert_mask=invert_mask, mask_erode=mask_erode, brain_vol_seg=brain_vol_seg, brain_mask_vol=brain_mask_vol, subcortical_gray=subcortical_gray, total_gray=total_gray, intracranial_volume=intracranial_volume, intracranial_volume_only=intracranial_volume_only, old_intracranial_volume_only=old_intracranial_volume_only, talairach_transform=talairach_transform, xfm_to_etiv=xfm_to_etiv, euler_hole_count=euler_hole_count, avg_waveform=avg_waveform, sum_waveform=sum_waveform, avg_waveform_vol=avg_waveform_vol, remove_avgwf_mean=remove_avgwf_mean, spatial_frame_avg=spatial_frame_avg, voxel_crs=voxel_crs, replace_ids=replace_ids, replace_ids_file=replace_ids_file, gtm_default_seg_merge=gtm_default_seg_merge, gtm_default_seg_merge_choroid=gtm_default_seg_merge_choroid, qa_stats_file=qa_stats_file, subjects_dir=subjects_dir, random_seed=random_seed)
    return mri_segstats_execute(params, execution)


__all__ = [
    "MRI_SEGSTATS_METADATA",
    "MriSegstatsOutputs",
    "MriSegstatsParameters",
    "mri_segstats",
    "mri_segstats_params",
]
