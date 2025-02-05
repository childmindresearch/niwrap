# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_VOLCLUSTER_METADATA = Metadata(
    id="86e5f012e8262b1a51728b36e2469f6a4678ccf5.boutiques",
    name="mri_volcluster",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriVolclusterParameters = typing.TypedDict('MriVolclusterParameters', {
    "__STYX_TYPE__": typing.Literal["mri_volcluster"],
    "input_file": InputPathType,
    "summary_file": typing.NotRequired[str | None],
    "output_volid": typing.NotRequired[str | None],
    "output_cluster_num_volid": typing.NotRequired[str | None],
    "cwsig_volid": typing.NotRequired[str | None],
    "pointset_file": typing.NotRequired[str | None],
    "min_threshold": typing.NotRequired[float | None],
    "max_threshold": typing.NotRequired[float | None],
    "sign": typing.NotRequired[str | None],
    "no_adjust_flag": bool,
    "match_value": typing.NotRequired[float | None],
    "cwpval_threshold": typing.NotRequired[float | None],
    "registration_file": typing.NotRequired[InputPathType | None],
    "mni152reg_flag": bool,
    "regheader_subject": typing.NotRequired[str | None],
    "fsaverage_flag": bool,
    "frame_number": typing.NotRequired[float | None],
    "csd_files": typing.NotRequired[list[InputPathType] | None],
    "cwsig_map": typing.NotRequired[str | None],
    "vwsig_map": typing.NotRequired[str | None],
    "max_cwpval_file": typing.NotRequired[str | None],
    "csdpdf_file": typing.NotRequired[str | None],
    "csdpdf_only_flag": bool,
    "fwhm_value": typing.NotRequired[float | None],
    "fwhm_file": typing.NotRequired[InputPathType | None],
    "min_size": typing.NotRequired[float | None],
    "min_size_vox": typing.NotRequired[float | None],
    "min_distance": typing.NotRequired[float | None],
    "allow_diag_flag": bool,
    "bonferroni_number": typing.NotRequired[float | None],
    "bonferroni_max_number": typing.NotRequired[float | None],
    "sig2p_max_flag": bool,
    "gte_flag": bool,
    "mask_volid": typing.NotRequired[InputPathType | None],
    "mask_type": typing.NotRequired[str | None],
    "mask_frame": typing.NotRequired[float | None],
    "mask_threshold": typing.NotRequired[float | None],
    "mask_sign": typing.NotRequired[str | None],
    "mask_invert_flag": bool,
    "out_mask_volid": typing.NotRequired[str | None],
    "out_mask_type": typing.NotRequired[str | None],
    "label_file": typing.NotRequired[str | None],
    "nlabel_cluster": typing.NotRequired[float | None],
    "label_base": typing.NotRequired[str | None],
    "synth_func": typing.NotRequired[str | None],
    "diagnostic_level": typing.NotRequired[float | None],
    "fill_params": typing.NotRequired[str | None],
    "help_flag": bool,
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
        "mri_volcluster": mri_volcluster_cargs,
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
        "mri_volcluster": mri_volcluster_outputs,
    }
    return vt.get(t)


class MriVolclusterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_volcluster(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume: OutputPathType | None
    """Output volume after clustering."""
    output_cluster_number_volume: OutputPathType | None
    """Output cluster number volume."""
    output_binary_mask: OutputPathType | None
    """Final binary mask output."""
    output_label_file: OutputPathType | None
    """Saved cluster as label file."""


def mri_volcluster_params(
    input_file: InputPathType,
    summary_file: str | None = None,
    output_volid: str | None = None,
    output_cluster_num_volid: str | None = None,
    cwsig_volid: str | None = None,
    pointset_file: str | None = None,
    min_threshold: float | None = None,
    max_threshold: float | None = None,
    sign: str | None = None,
    no_adjust_flag: bool = False,
    match_value: float | None = None,
    cwpval_threshold: float | None = None,
    registration_file: InputPathType | None = None,
    mni152reg_flag: bool = False,
    regheader_subject: str | None = None,
    fsaverage_flag: bool = False,
    frame_number: float | None = None,
    csd_files: list[InputPathType] | None = None,
    cwsig_map: str | None = None,
    vwsig_map: str | None = None,
    max_cwpval_file: str | None = None,
    csdpdf_file: str | None = None,
    csdpdf_only_flag: bool = False,
    fwhm_value: float | None = None,
    fwhm_file: InputPathType | None = None,
    min_size: float | None = None,
    min_size_vox: float | None = None,
    min_distance: float | None = None,
    allow_diag_flag: bool = False,
    bonferroni_number: float | None = None,
    bonferroni_max_number: float | None = None,
    sig2p_max_flag: bool = False,
    gte_flag: bool = False,
    mask_volid: InputPathType | None = None,
    mask_type: str | None = None,
    mask_frame: float | None = None,
    mask_threshold: float | None = None,
    mask_sign: str | None = None,
    mask_invert_flag: bool = False,
    out_mask_volid: str | None = None,
    out_mask_type: str | None = None,
    label_file: str | None = None,
    nlabel_cluster: float | None = None,
    label_base: str | None = None,
    synth_func: str | None = None,
    diagnostic_level: float | None = None,
    fill_params: str | None = None,
    help_flag: bool = False,
) -> MriVolclusterParameters:
    """
    Build parameters.
    
    Args:
        input_file: Source of volume values.
        summary_file: Text summary file.
        output_volid: Output volume ID after clustering.
        output_cluster_num_volid: Output volume ID with cluster number values.
        cwsig_volid: Volume ID for clusterwise significance.
        pointset_file: Create a freeview pointset of the clusters.
        min_threshold: Minimum intensity threshold.
        max_threshold: Maximum intensity threshold.
        sign: Sign for one-sided tests (<abs>, pos, neg).
        no_adjust_flag: Do not adjust threshold for one-tailed tests.
        match_value: Set thmin=matchval-0.5 and thmax=matchval+0.5.
        cwpval_threshold: Require clusters to have cwp < threshold.
        registration_file: For reporting Talairach coordinates.
        mni152reg_flag: Input is in MNI152 space.
        regheader_subject: Use header registration with subject.
        fsaverage_flag: Assume input is in fsaverage space.
        frame_number: Perform cluster analysis on the nth frame (0-based).
        csd_files: Cluster simulation data files.
        cwsig_map: Map of corrected cluster-wise significances.
        vwsig_map: Map of corrected voxel-wise significances.
        max_cwpval_file: Save p-value of the largest cluster.
        csdpdf_file: PDF/CDF of cluster and max significance.
        csdpdf_only_flag: Write CSD PDF file and exit.
        fwhm_value: FWHM in mm^3, forces GRF analysis.
        fwhm_file: Text file with FWHM in mm^3 for GRF.
        min_size: Minimum volume (mm^3) for a cluster.
        min_size_vox: Minimum number of contiguous voxels for a cluster.
        min_distance: Minimum distance between peak clusters.
        allow_diag_flag: Allow diagonal adjacency for contiguity.
        bonferroni_number: Bonferroni correction across spaces.
        bonferroni_max_number: Bonferroni correction applied to maximum.
        sig2p_max_flag: Convert maximum significance to p-value.
        gte_flag: Use >= when computing p-value from CSD.
        mask_volid: Mask volume ID.
        mask_type: File type of mask volume.
        mask_frame: Nth frame of mask to use.
        mask_threshold: Upper threshold for the mask.
        mask_sign: Sign in mask thresholding (<abs>, neg, pos).
        mask_invert_flag: Invert mask after thresholding.
        out_mask_volid: Path for final binary mask.
        out_mask_type: File type for output mask.
        label_file: File to save nth cluster as a label.
        nlabel_cluster: Save the nth cluster as a label.
        label_base: Base name for saving clusters as labels.
        synth_func: Function for synthetic data (uniform, loguniform,\
            gaussian).
        diagnostic_level: Set diagnostic level.
        fill_params: Parameters for fill operation (invol outvol matchval).
        help_flag: Display help message and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_volcluster",
        "input_file": input_file,
        "no_adjust_flag": no_adjust_flag,
        "mni152reg_flag": mni152reg_flag,
        "fsaverage_flag": fsaverage_flag,
        "csdpdf_only_flag": csdpdf_only_flag,
        "allow_diag_flag": allow_diag_flag,
        "sig2p_max_flag": sig2p_max_flag,
        "gte_flag": gte_flag,
        "mask_invert_flag": mask_invert_flag,
        "help_flag": help_flag,
    }
    if summary_file is not None:
        params["summary_file"] = summary_file
    if output_volid is not None:
        params["output_volid"] = output_volid
    if output_cluster_num_volid is not None:
        params["output_cluster_num_volid"] = output_cluster_num_volid
    if cwsig_volid is not None:
        params["cwsig_volid"] = cwsig_volid
    if pointset_file is not None:
        params["pointset_file"] = pointset_file
    if min_threshold is not None:
        params["min_threshold"] = min_threshold
    if max_threshold is not None:
        params["max_threshold"] = max_threshold
    if sign is not None:
        params["sign"] = sign
    if match_value is not None:
        params["match_value"] = match_value
    if cwpval_threshold is not None:
        params["cwpval_threshold"] = cwpval_threshold
    if registration_file is not None:
        params["registration_file"] = registration_file
    if regheader_subject is not None:
        params["regheader_subject"] = regheader_subject
    if frame_number is not None:
        params["frame_number"] = frame_number
    if csd_files is not None:
        params["csd_files"] = csd_files
    if cwsig_map is not None:
        params["cwsig_map"] = cwsig_map
    if vwsig_map is not None:
        params["vwsig_map"] = vwsig_map
    if max_cwpval_file is not None:
        params["max_cwpval_file"] = max_cwpval_file
    if csdpdf_file is not None:
        params["csdpdf_file"] = csdpdf_file
    if fwhm_value is not None:
        params["fwhm_value"] = fwhm_value
    if fwhm_file is not None:
        params["fwhm_file"] = fwhm_file
    if min_size is not None:
        params["min_size"] = min_size
    if min_size_vox is not None:
        params["min_size_vox"] = min_size_vox
    if min_distance is not None:
        params["min_distance"] = min_distance
    if bonferroni_number is not None:
        params["bonferroni_number"] = bonferroni_number
    if bonferroni_max_number is not None:
        params["bonferroni_max_number"] = bonferroni_max_number
    if mask_volid is not None:
        params["mask_volid"] = mask_volid
    if mask_type is not None:
        params["mask_type"] = mask_type
    if mask_frame is not None:
        params["mask_frame"] = mask_frame
    if mask_threshold is not None:
        params["mask_threshold"] = mask_threshold
    if mask_sign is not None:
        params["mask_sign"] = mask_sign
    if out_mask_volid is not None:
        params["out_mask_volid"] = out_mask_volid
    if out_mask_type is not None:
        params["out_mask_type"] = out_mask_type
    if label_file is not None:
        params["label_file"] = label_file
    if nlabel_cluster is not None:
        params["nlabel_cluster"] = nlabel_cluster
    if label_base is not None:
        params["label_base"] = label_base
    if synth_func is not None:
        params["synth_func"] = synth_func
    if diagnostic_level is not None:
        params["diagnostic_level"] = diagnostic_level
    if fill_params is not None:
        params["fill_params"] = fill_params
    return params


def mri_volcluster_cargs(
    params: MriVolclusterParameters,
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
    cargs.append("mri_volcluster")
    cargs.extend([
        "--in",
        execution.input_file(params.get("input_file"))
    ])
    if params.get("summary_file") is not None:
        cargs.extend([
            "--sum",
            params.get("summary_file")
        ])
    if params.get("output_volid") is not None:
        cargs.extend([
            "--out",
            params.get("output_volid")
        ])
    if params.get("output_cluster_num_volid") is not None:
        cargs.extend([
            "--ocn",
            params.get("output_cluster_num_volid")
        ])
    if params.get("cwsig_volid") is not None:
        cargs.extend([
            "--cwsig",
            params.get("cwsig_volid")
        ])
    if params.get("pointset_file") is not None:
        cargs.extend([
            "--pointset",
            params.get("pointset_file")
        ])
    if params.get("min_threshold") is not None:
        cargs.extend([
            "--thmin",
            str(params.get("min_threshold"))
        ])
    if params.get("max_threshold") is not None:
        cargs.extend([
            "--thmax",
            str(params.get("max_threshold"))
        ])
    if params.get("sign") is not None:
        cargs.extend([
            "--sign",
            params.get("sign")
        ])
    if params.get("no_adjust_flag"):
        cargs.append("--no-adjust")
    if params.get("match_value") is not None:
        cargs.extend([
            "--match",
            str(params.get("match_value"))
        ])
    if params.get("cwpval_threshold") is not None:
        cargs.extend([
            "--cwpvalthresh",
            str(params.get("cwpval_threshold"))
        ])
    if params.get("registration_file") is not None:
        cargs.extend([
            "--reg",
            execution.input_file(params.get("registration_file"))
        ])
    if params.get("mni152reg_flag"):
        cargs.append("--mni152reg")
    if params.get("regheader_subject") is not None:
        cargs.extend([
            "--regheader",
            params.get("regheader_subject")
        ])
    if params.get("fsaverage_flag"):
        cargs.append("--fsaverage")
    if params.get("frame_number") is not None:
        cargs.extend([
            "--frame",
            str(params.get("frame_number"))
        ])
    if params.get("csd_files") is not None:
        cargs.extend([
            "--csd",
            *[execution.input_file(f) for f in params.get("csd_files")]
        ])
    if params.get("cwsig_map") is not None:
        cargs.extend([
            "--cwsig",
            params.get("cwsig_map")
        ])
    if params.get("vwsig_map") is not None:
        cargs.extend([
            "--vwsig",
            params.get("vwsig_map")
        ])
    if params.get("max_cwpval_file") is not None:
        cargs.extend([
            "--maxcwpval",
            params.get("max_cwpval_file")
        ])
    if params.get("csdpdf_file") is not None:
        cargs.extend([
            "--csdpdf",
            params.get("csdpdf_file")
        ])
    if params.get("csdpdf_only_flag"):
        cargs.append("--csdpdf-only")
    if params.get("fwhm_value") is not None:
        cargs.extend([
            "--fwhm",
            str(params.get("fwhm_value"))
        ])
    if params.get("fwhm_file") is not None:
        cargs.extend([
            "--fwhmdat",
            execution.input_file(params.get("fwhm_file"))
        ])
    if params.get("min_size") is not None:
        cargs.extend([
            "--minsize",
            str(params.get("min_size"))
        ])
    if params.get("min_size_vox") is not None:
        cargs.extend([
            "--minsizevox",
            str(params.get("min_size_vox"))
        ])
    if params.get("min_distance") is not None:
        cargs.extend([
            "--mindist",
            str(params.get("min_distance"))
        ])
    if params.get("allow_diag_flag"):
        cargs.append("--allowdiag")
    if params.get("bonferroni_number") is not None:
        cargs.extend([
            "--bonferroni",
            str(params.get("bonferroni_number"))
        ])
    if params.get("bonferroni_max_number") is not None:
        cargs.extend([
            "--bonferroni-max",
            str(params.get("bonferroni_max_number"))
        ])
    if params.get("sig2p_max_flag"):
        cargs.append("--sig2p-max")
    if params.get("gte_flag"):
        cargs.append("--gte")
    if params.get("mask_volid") is not None:
        cargs.extend([
            "--mask",
            execution.input_file(params.get("mask_volid"))
        ])
    if params.get("mask_type") is not None:
        cargs.extend([
            "--mask_type",
            params.get("mask_type")
        ])
    if params.get("mask_frame") is not None:
        cargs.extend([
            "--maskframe",
            str(params.get("mask_frame"))
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
    if params.get("mask_invert_flag"):
        cargs.append("--maskinvert")
    if params.get("out_mask_volid") is not None:
        cargs.extend([
            "--outmask",
            params.get("out_mask_volid")
        ])
    if params.get("out_mask_type") is not None:
        cargs.extend([
            "--outmask_type",
            params.get("out_mask_type")
        ])
    if params.get("label_file") is not None:
        cargs.extend([
            "--label",
            params.get("label_file")
        ])
    if params.get("nlabel_cluster") is not None:
        cargs.extend([
            "--nlabelcluster",
            str(params.get("nlabel_cluster"))
        ])
    if params.get("label_base") is not None:
        cargs.extend([
            "--labelbase",
            params.get("label_base")
        ])
    if params.get("synth_func") is not None:
        cargs.extend([
            "--synth",
            params.get("synth_func")
        ])
    if params.get("diagnostic_level") is not None:
        cargs.extend([
            "--diag",
            str(params.get("diagnostic_level"))
        ])
    if params.get("fill_params") is not None:
        cargs.extend([
            "--fill",
            params.get("fill_params")
        ])
    if params.get("help_flag"):
        cargs.append("--help")
    return cargs


def mri_volcluster_outputs(
    params: MriVolclusterParameters,
    execution: Execution,
) -> MriVolclusterOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriVolclusterOutputs(
        root=execution.output_file("."),
        output_volume=execution.output_file(params.get("output_volid")) if (params.get("output_volid") is not None) else None,
        output_cluster_number_volume=execution.output_file(params.get("output_cluster_num_volid")) if (params.get("output_cluster_num_volid") is not None) else None,
        output_binary_mask=execution.output_file(params.get("out_mask_volid")) if (params.get("out_mask_volid") is not None) else None,
        output_label_file=execution.output_file(params.get("label_file")) if (params.get("label_file") is not None) else None,
    )
    return ret


def mri_volcluster_execute(
    params: MriVolclusterParameters,
    execution: Execution,
) -> MriVolclusterOutputs:
    """
    A tool for finding clusters in a volume, useful for analyzing MRI data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriVolclusterOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_volcluster_cargs(params, execution)
    ret = mri_volcluster_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_volcluster(
    input_file: InputPathType,
    summary_file: str | None = None,
    output_volid: str | None = None,
    output_cluster_num_volid: str | None = None,
    cwsig_volid: str | None = None,
    pointset_file: str | None = None,
    min_threshold: float | None = None,
    max_threshold: float | None = None,
    sign: str | None = None,
    no_adjust_flag: bool = False,
    match_value: float | None = None,
    cwpval_threshold: float | None = None,
    registration_file: InputPathType | None = None,
    mni152reg_flag: bool = False,
    regheader_subject: str | None = None,
    fsaverage_flag: bool = False,
    frame_number: float | None = None,
    csd_files: list[InputPathType] | None = None,
    cwsig_map: str | None = None,
    vwsig_map: str | None = None,
    max_cwpval_file: str | None = None,
    csdpdf_file: str | None = None,
    csdpdf_only_flag: bool = False,
    fwhm_value: float | None = None,
    fwhm_file: InputPathType | None = None,
    min_size: float | None = None,
    min_size_vox: float | None = None,
    min_distance: float | None = None,
    allow_diag_flag: bool = False,
    bonferroni_number: float | None = None,
    bonferroni_max_number: float | None = None,
    sig2p_max_flag: bool = False,
    gte_flag: bool = False,
    mask_volid: InputPathType | None = None,
    mask_type: str | None = None,
    mask_frame: float | None = None,
    mask_threshold: float | None = None,
    mask_sign: str | None = None,
    mask_invert_flag: bool = False,
    out_mask_volid: str | None = None,
    out_mask_type: str | None = None,
    label_file: str | None = None,
    nlabel_cluster: float | None = None,
    label_base: str | None = None,
    synth_func: str | None = None,
    diagnostic_level: float | None = None,
    fill_params: str | None = None,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> MriVolclusterOutputs:
    """
    A tool for finding clusters in a volume, useful for analyzing MRI data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Source of volume values.
        summary_file: Text summary file.
        output_volid: Output volume ID after clustering.
        output_cluster_num_volid: Output volume ID with cluster number values.
        cwsig_volid: Volume ID for clusterwise significance.
        pointset_file: Create a freeview pointset of the clusters.
        min_threshold: Minimum intensity threshold.
        max_threshold: Maximum intensity threshold.
        sign: Sign for one-sided tests (<abs>, pos, neg).
        no_adjust_flag: Do not adjust threshold for one-tailed tests.
        match_value: Set thmin=matchval-0.5 and thmax=matchval+0.5.
        cwpval_threshold: Require clusters to have cwp < threshold.
        registration_file: For reporting Talairach coordinates.
        mni152reg_flag: Input is in MNI152 space.
        regheader_subject: Use header registration with subject.
        fsaverage_flag: Assume input is in fsaverage space.
        frame_number: Perform cluster analysis on the nth frame (0-based).
        csd_files: Cluster simulation data files.
        cwsig_map: Map of corrected cluster-wise significances.
        vwsig_map: Map of corrected voxel-wise significances.
        max_cwpval_file: Save p-value of the largest cluster.
        csdpdf_file: PDF/CDF of cluster and max significance.
        csdpdf_only_flag: Write CSD PDF file and exit.
        fwhm_value: FWHM in mm^3, forces GRF analysis.
        fwhm_file: Text file with FWHM in mm^3 for GRF.
        min_size: Minimum volume (mm^3) for a cluster.
        min_size_vox: Minimum number of contiguous voxels for a cluster.
        min_distance: Minimum distance between peak clusters.
        allow_diag_flag: Allow diagonal adjacency for contiguity.
        bonferroni_number: Bonferroni correction across spaces.
        bonferroni_max_number: Bonferroni correction applied to maximum.
        sig2p_max_flag: Convert maximum significance to p-value.
        gte_flag: Use >= when computing p-value from CSD.
        mask_volid: Mask volume ID.
        mask_type: File type of mask volume.
        mask_frame: Nth frame of mask to use.
        mask_threshold: Upper threshold for the mask.
        mask_sign: Sign in mask thresholding (<abs>, neg, pos).
        mask_invert_flag: Invert mask after thresholding.
        out_mask_volid: Path for final binary mask.
        out_mask_type: File type for output mask.
        label_file: File to save nth cluster as a label.
        nlabel_cluster: Save the nth cluster as a label.
        label_base: Base name for saving clusters as labels.
        synth_func: Function for synthetic data (uniform, loguniform,\
            gaussian).
        diagnostic_level: Set diagnostic level.
        fill_params: Parameters for fill operation (invol outvol matchval).
        help_flag: Display help message and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriVolclusterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_VOLCLUSTER_METADATA)
    params = mri_volcluster_params(input_file=input_file, summary_file=summary_file, output_volid=output_volid, output_cluster_num_volid=output_cluster_num_volid, cwsig_volid=cwsig_volid, pointset_file=pointset_file, min_threshold=min_threshold, max_threshold=max_threshold, sign=sign, no_adjust_flag=no_adjust_flag, match_value=match_value, cwpval_threshold=cwpval_threshold, registration_file=registration_file, mni152reg_flag=mni152reg_flag, regheader_subject=regheader_subject, fsaverage_flag=fsaverage_flag, frame_number=frame_number, csd_files=csd_files, cwsig_map=cwsig_map, vwsig_map=vwsig_map, max_cwpval_file=max_cwpval_file, csdpdf_file=csdpdf_file, csdpdf_only_flag=csdpdf_only_flag, fwhm_value=fwhm_value, fwhm_file=fwhm_file, min_size=min_size, min_size_vox=min_size_vox, min_distance=min_distance, allow_diag_flag=allow_diag_flag, bonferroni_number=bonferroni_number, bonferroni_max_number=bonferroni_max_number, sig2p_max_flag=sig2p_max_flag, gte_flag=gte_flag, mask_volid=mask_volid, mask_type=mask_type, mask_frame=mask_frame, mask_threshold=mask_threshold, mask_sign=mask_sign, mask_invert_flag=mask_invert_flag, out_mask_volid=out_mask_volid, out_mask_type=out_mask_type, label_file=label_file, nlabel_cluster=nlabel_cluster, label_base=label_base, synth_func=synth_func, diagnostic_level=diagnostic_level, fill_params=fill_params, help_flag=help_flag)
    return mri_volcluster_execute(params, execution)


__all__ = [
    "MRI_VOLCLUSTER_METADATA",
    "MriVolclusterOutputs",
    "MriVolclusterParameters",
    "mri_volcluster",
    "mri_volcluster_params",
]
