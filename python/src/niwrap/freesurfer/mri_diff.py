# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_DIFF_METADATA = Metadata(
    id="e29e7f056291727390ed03afe0470b3873fe4e24.boutiques",
    name="mri_diff",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriDiffParameters = typing.TypedDict('MriDiffParameters', {
    "__STYX_TYPE__": typing.Literal["mri_diff"],
    "vol1file": InputPathType,
    "vol2file": InputPathType,
    "resolution_check": bool,
    "acquisition_param_check": bool,
    "geometry_check": bool,
    "precision_check": bool,
    "pixel_check": bool,
    "orientation_check": bool,
    "file_type_diff_check": bool,
    "no_exit_on_diff": bool,
    "quality_assurance": bool,
    "pixel_only": bool,
    "abs_difference": bool,
    "no_abs_difference": bool,
    "difference_abs": bool,
    "percentage_difference": bool,
    "rss_save": bool,
    "ssd_print": bool,
    "rms_print": bool,
    "count_diff_voxels": bool,
    "pixel_threshold": typing.NotRequired[float | None],
    "count_thresh_voxels": typing.NotRequired[float | None],
    "log_file": typing.NotRequired[str | None],
    "difference_image": typing.NotRequired[InputPathType | None],
    "suspicious_diff_volume": typing.NotRequired[InputPathType | None],
    "segmentation_diff": typing.NotRequired[str | None],
    "merge_edits": typing.NotRequired[str | None],
    "average_difference": typing.NotRequired[str | None],
    "debug_mode": bool,
    "verbose_mode": bool,
    "check_options": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "mri_diff": mri_diff_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "mri_diff": mri_diff_outputs,
    }.get(t)


class MriDiffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_diff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    log_output: OutputPathType | None
    """Log file containing difference information."""
    difference_image_output: OutputPathType | None
    """Difference image output file."""
    suspicious_difference_output: OutputPathType | None
    """Volume with suspicious differences labeled."""


def mri_diff_params(
    vol1file: InputPathType,
    vol2file: InputPathType,
    resolution_check: bool = False,
    acquisition_param_check: bool = False,
    geometry_check: bool = False,
    precision_check: bool = False,
    pixel_check: bool = False,
    orientation_check: bool = False,
    file_type_diff_check: bool = False,
    no_exit_on_diff: bool = False,
    quality_assurance: bool = False,
    pixel_only: bool = False,
    abs_difference: bool = False,
    no_abs_difference: bool = False,
    difference_abs: bool = False,
    percentage_difference: bool = False,
    rss_save: bool = False,
    ssd_print: bool = False,
    rms_print: bool = False,
    count_diff_voxels: bool = False,
    pixel_threshold: float | None = None,
    count_thresh_voxels: float | None = None,
    log_file: str | None = None,
    difference_image: InputPathType | None = None,
    suspicious_diff_volume: InputPathType | None = None,
    segmentation_diff: str | None = None,
    merge_edits: str | None = None,
    average_difference: str | None = None,
    debug_mode: bool = False,
    verbose_mode: bool = False,
    check_options: bool = False,
) -> MriDiffParameters:
    """
    Build parameters.
    
    Args:
        vol1file: First volume to compare (e.g., vol1.mgz).
        vol2file: Second volume to compare (e.g., vol2.mgz).
        resolution_check: Do not check for resolution differences.
        acquisition_param_check: Do not check for acquisition parameter\
            differences.
        geometry_check: Do not check for geometry differences.
        precision_check: Do not check for precision differences.
        pixel_check: Do not check for pixel differences.
        orientation_check: Do not check for orientation differences.
        file_type_diff_check: Do not check for file type differences.
        no_exit_on_diff: Do not exit on difference; run through everything.
        quality_assurance: Check resolution, acquisition, precision, and\
            orientation only.
        pixel_only: Only check pixel data.
        abs_difference: Take absolute value of difference (default).
        no_abs_difference: Do not take absolute value of difference.
        difference_abs: Take absolute value before computing difference.
        percentage_difference: Compute percentage difference:\
            100*(v1-v2)/((v1+v2)/2).
        rss_save: Save square root sum squares with --diff.
        ssd_print: Print sum squared differences over all voxels.
        rms_print: Print root mean squared difference over all non-zero voxels.
        count_diff_voxels: Print number of differing voxels.
        pixel_threshold: Pixel differences must be greater than this value to\
            be considered different.
        count_thresh_voxels: There must be at least this many voxels that are\
            different.
        log_file: Store difference information in this log file.
        difference_image: Save difference image to specified volume.
        suspicious_diff_volume: Differing voxels replaced with label SUSPICIOUS\
            in the specified volume.
        segmentation_diff: Perform diff on voxels with specific label index.
        merge_edits: Merge edits from newauto, oldauto, and manedit volumes\
            into merged volume.
        average_difference: Save average difference to specified file.
        debug_mode: Enable debugging mode.
        verbose_mode: Print information on all differences found.
        check_options: Check options and exit without running anything.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_diff",
        "vol1file": vol1file,
        "vol2file": vol2file,
        "resolution_check": resolution_check,
        "acquisition_param_check": acquisition_param_check,
        "geometry_check": geometry_check,
        "precision_check": precision_check,
        "pixel_check": pixel_check,
        "orientation_check": orientation_check,
        "file_type_diff_check": file_type_diff_check,
        "no_exit_on_diff": no_exit_on_diff,
        "quality_assurance": quality_assurance,
        "pixel_only": pixel_only,
        "abs_difference": abs_difference,
        "no_abs_difference": no_abs_difference,
        "difference_abs": difference_abs,
        "percentage_difference": percentage_difference,
        "rss_save": rss_save,
        "ssd_print": ssd_print,
        "rms_print": rms_print,
        "count_diff_voxels": count_diff_voxels,
        "debug_mode": debug_mode,
        "verbose_mode": verbose_mode,
        "check_options": check_options,
    }
    if pixel_threshold is not None:
        params["pixel_threshold"] = pixel_threshold
    if count_thresh_voxels is not None:
        params["count_thresh_voxels"] = count_thresh_voxels
    if log_file is not None:
        params["log_file"] = log_file
    if difference_image is not None:
        params["difference_image"] = difference_image
    if suspicious_diff_volume is not None:
        params["suspicious_diff_volume"] = suspicious_diff_volume
    if segmentation_diff is not None:
        params["segmentation_diff"] = segmentation_diff
    if merge_edits is not None:
        params["merge_edits"] = merge_edits
    if average_difference is not None:
        params["average_difference"] = average_difference
    return params


def mri_diff_cargs(
    params: MriDiffParameters,
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
    cargs.append("mri_diff")
    cargs.append(execution.input_file(params.get("vol1file")))
    cargs.append(execution.input_file(params.get("vol2file")))
    if params.get("resolution_check"):
        cargs.append("--notallow-res")
    if params.get("acquisition_param_check"):
        cargs.append("--notallow-acq")
    if params.get("geometry_check"):
        cargs.append("--notallow-geo")
    if params.get("precision_check"):
        cargs.append("--notallow-prec")
    if params.get("pixel_check"):
        cargs.append("--notallow-pix")
    if params.get("orientation_check"):
        cargs.append("--notallow-ori")
    if params.get("file_type_diff_check"):
        cargs.append("--notallow-type")
    if params.get("no_exit_on_diff"):
        cargs.append("--no-exit-on-diff")
    if params.get("quality_assurance"):
        cargs.append("--qa")
    if params.get("pixel_only"):
        cargs.append("--pix-only")
    if params.get("abs_difference"):
        cargs.append("--absdiff")
    if params.get("no_abs_difference"):
        cargs.append("--no-absdiff")
    if params.get("difference_abs"):
        cargs.append("--diffabs")
    if params.get("percentage_difference"):
        cargs.append("--diffpct")
    if params.get("rss_save"):
        cargs.append("--rss")
    if params.get("ssd_print"):
        cargs.append("--ssd")
    if params.get("rms_print"):
        cargs.append("--rms")
    if params.get("count_diff_voxels"):
        cargs.append("--count")
    if params.get("pixel_threshold") is not None:
        cargs.extend([
            "--thresh",
            str(params.get("pixel_threshold"))
        ])
    if params.get("count_thresh_voxels") is not None:
        cargs.extend([
            "--count-thresh",
            str(params.get("count_thresh_voxels"))
        ])
    if params.get("log_file") is not None:
        cargs.extend([
            "--log",
            params.get("log_file")
        ])
    if params.get("difference_image") is not None:
        cargs.extend([
            "--diff",
            execution.input_file(params.get("difference_image"))
        ])
    if params.get("suspicious_diff_volume") is not None:
        cargs.extend([
            "--diff_label_suspicious",
            execution.input_file(params.get("suspicious_diff_volume"))
        ])
    if params.get("segmentation_diff") is not None:
        cargs.extend([
            "--segdiff",
            params.get("segmentation_diff")
        ])
    if params.get("merge_edits") is not None:
        cargs.extend([
            "--merge-edits",
            params.get("merge_edits")
        ])
    if params.get("average_difference") is not None:
        cargs.extend([
            "--avg-diff",
            params.get("average_difference")
        ])
    if params.get("debug_mode"):
        cargs.append("--debug")
    if params.get("verbose_mode"):
        cargs.append("--verbose")
    if params.get("check_options"):
        cargs.append("--checkopts")
    return cargs


def mri_diff_outputs(
    params: MriDiffParameters,
    execution: Execution,
) -> MriDiffOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriDiffOutputs(
        root=execution.output_file("."),
        log_output=execution.output_file(params.get("log_file")) if (params.get("log_file") is not None) else None,
        difference_image_output=execution.output_file(pathlib.Path(params.get("difference_image")).name) if (params.get("difference_image") is not None) else None,
        suspicious_difference_output=execution.output_file(pathlib.Path(params.get("suspicious_diff_volume")).name) if (params.get("suspicious_diff_volume") is not None) else None,
    )
    return ret


def mri_diff_execute(
    params: MriDiffParameters,
    execution: Execution,
) -> MriDiffOutputs:
    """
    Determines whether two volumes differ based on dimensions, resolutions,
    acquisition parameters, geometry, precision, and pixel data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriDiffOutputs`).
    """
    params = execution.params(params)
    cargs = mri_diff_cargs(params, execution)
    ret = mri_diff_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_diff(
    vol1file: InputPathType,
    vol2file: InputPathType,
    resolution_check: bool = False,
    acquisition_param_check: bool = False,
    geometry_check: bool = False,
    precision_check: bool = False,
    pixel_check: bool = False,
    orientation_check: bool = False,
    file_type_diff_check: bool = False,
    no_exit_on_diff: bool = False,
    quality_assurance: bool = False,
    pixel_only: bool = False,
    abs_difference: bool = False,
    no_abs_difference: bool = False,
    difference_abs: bool = False,
    percentage_difference: bool = False,
    rss_save: bool = False,
    ssd_print: bool = False,
    rms_print: bool = False,
    count_diff_voxels: bool = False,
    pixel_threshold: float | None = None,
    count_thresh_voxels: float | None = None,
    log_file: str | None = None,
    difference_image: InputPathType | None = None,
    suspicious_diff_volume: InputPathType | None = None,
    segmentation_diff: str | None = None,
    merge_edits: str | None = None,
    average_difference: str | None = None,
    debug_mode: bool = False,
    verbose_mode: bool = False,
    check_options: bool = False,
    runner: Runner | None = None,
) -> MriDiffOutputs:
    """
    Determines whether two volumes differ based on dimensions, resolutions,
    acquisition parameters, geometry, precision, and pixel data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        vol1file: First volume to compare (e.g., vol1.mgz).
        vol2file: Second volume to compare (e.g., vol2.mgz).
        resolution_check: Do not check for resolution differences.
        acquisition_param_check: Do not check for acquisition parameter\
            differences.
        geometry_check: Do not check for geometry differences.
        precision_check: Do not check for precision differences.
        pixel_check: Do not check for pixel differences.
        orientation_check: Do not check for orientation differences.
        file_type_diff_check: Do not check for file type differences.
        no_exit_on_diff: Do not exit on difference; run through everything.
        quality_assurance: Check resolution, acquisition, precision, and\
            orientation only.
        pixel_only: Only check pixel data.
        abs_difference: Take absolute value of difference (default).
        no_abs_difference: Do not take absolute value of difference.
        difference_abs: Take absolute value before computing difference.
        percentage_difference: Compute percentage difference:\
            100*(v1-v2)/((v1+v2)/2).
        rss_save: Save square root sum squares with --diff.
        ssd_print: Print sum squared differences over all voxels.
        rms_print: Print root mean squared difference over all non-zero voxels.
        count_diff_voxels: Print number of differing voxels.
        pixel_threshold: Pixel differences must be greater than this value to\
            be considered different.
        count_thresh_voxels: There must be at least this many voxels that are\
            different.
        log_file: Store difference information in this log file.
        difference_image: Save difference image to specified volume.
        suspicious_diff_volume: Differing voxels replaced with label SUSPICIOUS\
            in the specified volume.
        segmentation_diff: Perform diff on voxels with specific label index.
        merge_edits: Merge edits from newauto, oldauto, and manedit volumes\
            into merged volume.
        average_difference: Save average difference to specified file.
        debug_mode: Enable debugging mode.
        verbose_mode: Print information on all differences found.
        check_options: Check options and exit without running anything.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriDiffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_DIFF_METADATA)
    params = mri_diff_params(vol1file=vol1file, vol2file=vol2file, resolution_check=resolution_check, acquisition_param_check=acquisition_param_check, geometry_check=geometry_check, precision_check=precision_check, pixel_check=pixel_check, orientation_check=orientation_check, file_type_diff_check=file_type_diff_check, no_exit_on_diff=no_exit_on_diff, quality_assurance=quality_assurance, pixel_only=pixel_only, abs_difference=abs_difference, no_abs_difference=no_abs_difference, difference_abs=difference_abs, percentage_difference=percentage_difference, rss_save=rss_save, ssd_print=ssd_print, rms_print=rms_print, count_diff_voxels=count_diff_voxels, pixel_threshold=pixel_threshold, count_thresh_voxels=count_thresh_voxels, log_file=log_file, difference_image=difference_image, suspicious_diff_volume=suspicious_diff_volume, segmentation_diff=segmentation_diff, merge_edits=merge_edits, average_difference=average_difference, debug_mode=debug_mode, verbose_mode=verbose_mode, check_options=check_options)
    return mri_diff_execute(params, execution)


__all__ = [
    "MRI_DIFF_METADATA",
    "MriDiffOutputs",
    "MriDiffParameters",
    "mri_diff",
    "mri_diff_params",
]
