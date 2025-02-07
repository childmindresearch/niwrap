# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_SEGMENT_HYPOTHALAMIC_SUBUNITS_METADATA = Metadata(
    id="f03ac3b7165171b1e5dc19884858113ebce6c791.boutiques",
    name="mri_segment_hypothalamic_subunits",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriSegmentHypothalamicSubunitsParameters = typing.TypedDict('MriSegmentHypothalamicSubunitsParameters', {
    "__STYX_TYPE__": typing.Literal["mri_segment_hypothalamic_subunits"],
    "subjects": typing.NotRequired[list[str] | None],
    "subjects_dir": typing.NotRequired[str | None],
    "write_posteriors": bool,
    "image_input": typing.NotRequired[str | None],
    "output": typing.NotRequired[str | None],
    "posteriors": typing.NotRequired[str | None],
    "resample": typing.NotRequired[str | None],
    "volume_output": typing.NotRequired[str | None],
    "crop_size": typing.NotRequired[list[float] | None],
    "threads": typing.NotRequired[float | None],
    "cpu": bool,
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
        "mri_segment_hypothalamic_subunits": mri_segment_hypothalamic_subunits_cargs,
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
        "mri_segment_hypothalamic_subunits": mri_segment_hypothalamic_subunits_outputs,
    }.get(t)


class MriSegmentHypothalamicSubunitsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_segment_hypothalamic_subunits(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    segmentation_output_files: OutputPathType | None
    """Segmentation output(s) in T1 mode."""
    posteriors_output: OutputPathType | None
    """Posteriors output(s)."""
    resampled_output: OutputPathType | None
    """Resampled image(s) output."""
    volume_output_csv: OutputPathType | None
    """CSV file with volumes for all structures and subjects."""


def mri_segment_hypothalamic_subunits_params(
    subjects: list[str] | None = None,
    subjects_dir: str | None = None,
    write_posteriors: bool = False,
    image_input: str | None = None,
    output: str | None = None,
    posteriors: str | None = None,
    resample: str | None = None,
    volume_output: str | None = None,
    crop_size: list[float] | None = None,
    threads: float | None = None,
    cpu: bool = False,
) -> MriSegmentHypothalamicSubunitsParameters:
    """
    Build parameters.
    
    Args:
        subjects: (required in FS mode) Name of one or several subjects in\
            $SUBJECTS_DIR on which to run the module, assuming recon-all has been\
            run on the specified subjects.
        subjects_dir: (FS mode, optional) Override current $SUBJECTS_DIR.
        write_posteriors: (FS mode, optional) Save posteriors; default is\
            False.
        image_input: (required in T1 mode) Image(s) to segment. Can be a path\
            to a single image or to a folder.
        output: (required in T1 mode) Segmentation output(s). Must be a folder\
            if --i designates a folder.
        posteriors: (T1 mode, optional) Posteriors output(s). Must be a folder\
            if --i designates a folder.
        resample: (T1 mode, optional) Resampled image(s). Must be a folder if\
            --i designates a folder.
        volume_output: (T1 mode, optional) Output CSV file with volumes for all\
            structures and subjects.
        crop_size: (both modes, optional) Size of the central patch to analyse\
            (must be divisible by 8). The whole image is analysed by default.
        threads: (both modes, optional) Number of cores to be used. Default\
            uses 1 core.
        cpu: (both modes, optional) Enforce running with CPU rather than GPU.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_segment_hypothalamic_subunits",
        "write_posteriors": write_posteriors,
        "cpu": cpu,
    }
    if subjects is not None:
        params["subjects"] = subjects
    if subjects_dir is not None:
        params["subjects_dir"] = subjects_dir
    if image_input is not None:
        params["image_input"] = image_input
    if output is not None:
        params["output"] = output
    if posteriors is not None:
        params["posteriors"] = posteriors
    if resample is not None:
        params["resample"] = resample
    if volume_output is not None:
        params["volume_output"] = volume_output
    if crop_size is not None:
        params["crop_size"] = crop_size
    if threads is not None:
        params["threads"] = threads
    return params


def mri_segment_hypothalamic_subunits_cargs(
    params: MriSegmentHypothalamicSubunitsParameters,
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
    cargs.append("mri_segment_hypothalamic_subunits")
    if params.get("subjects") is not None:
        cargs.extend([
            "--s",
            *params.get("subjects")
        ])
    if params.get("subjects_dir") is not None:
        cargs.extend([
            "--sd",
            params.get("subjects_dir")
        ])
    if params.get("write_posteriors"):
        cargs.append("--write_posteriors")
    if params.get("image_input") is not None:
        cargs.extend([
            "--i",
            params.get("image_input")
        ])
    if params.get("output") is not None:
        cargs.extend([
            "--o",
            params.get("output")
        ])
    if params.get("posteriors") is not None:
        cargs.extend([
            "--post",
            params.get("posteriors")
        ])
    if params.get("resample") is not None:
        cargs.extend([
            "--resample",
            params.get("resample")
        ])
    if params.get("volume_output") is not None:
        cargs.extend([
            "--vol",
            params.get("volume_output")
        ])
    if params.get("crop_size") is not None:
        cargs.extend([
            "--crop",
            *map(str, params.get("crop_size"))
        ])
    if params.get("threads") is not None:
        cargs.extend([
            "--threads",
            str(params.get("threads"))
        ])
    if params.get("cpu"):
        cargs.append("--cpu")
    return cargs


def mri_segment_hypothalamic_subunits_outputs(
    params: MriSegmentHypothalamicSubunitsParameters,
    execution: Execution,
) -> MriSegmentHypothalamicSubunitsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriSegmentHypothalamicSubunitsOutputs(
        root=execution.output_file("."),
        segmentation_output_files=execution.output_file(params.get("output")) if (params.get("output") is not None) else None,
        posteriors_output=execution.output_file(params.get("posteriors")) if (params.get("posteriors") is not None) else None,
        resampled_output=execution.output_file(params.get("resample")) if (params.get("resample") is not None) else None,
        volume_output_csv=execution.output_file(params.get("volume_output")) if (params.get("volume_output") is not None) else None,
    )
    return ret


def mri_segment_hypothalamic_subunits_execute(
    params: MriSegmentHypothalamicSubunitsParameters,
    execution: Execution,
) -> MriSegmentHypothalamicSubunitsOutputs:
    """
    This module segments hypothalamic subunits and can be run in two modes: on
    FreeSurfer subjects or on any T1-weighted scan(s) of approximately 1mm
    resolution.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriSegmentHypothalamicSubunitsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_segment_hypothalamic_subunits_cargs(params, execution)
    ret = mri_segment_hypothalamic_subunits_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_segment_hypothalamic_subunits(
    subjects: list[str] | None = None,
    subjects_dir: str | None = None,
    write_posteriors: bool = False,
    image_input: str | None = None,
    output: str | None = None,
    posteriors: str | None = None,
    resample: str | None = None,
    volume_output: str | None = None,
    crop_size: list[float] | None = None,
    threads: float | None = None,
    cpu: bool = False,
    runner: Runner | None = None,
) -> MriSegmentHypothalamicSubunitsOutputs:
    """
    This module segments hypothalamic subunits and can be run in two modes: on
    FreeSurfer subjects or on any T1-weighted scan(s) of approximately 1mm
    resolution.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjects: (required in FS mode) Name of one or several subjects in\
            $SUBJECTS_DIR on which to run the module, assuming recon-all has been\
            run on the specified subjects.
        subjects_dir: (FS mode, optional) Override current $SUBJECTS_DIR.
        write_posteriors: (FS mode, optional) Save posteriors; default is\
            False.
        image_input: (required in T1 mode) Image(s) to segment. Can be a path\
            to a single image or to a folder.
        output: (required in T1 mode) Segmentation output(s). Must be a folder\
            if --i designates a folder.
        posteriors: (T1 mode, optional) Posteriors output(s). Must be a folder\
            if --i designates a folder.
        resample: (T1 mode, optional) Resampled image(s). Must be a folder if\
            --i designates a folder.
        volume_output: (T1 mode, optional) Output CSV file with volumes for all\
            structures and subjects.
        crop_size: (both modes, optional) Size of the central patch to analyse\
            (must be divisible by 8). The whole image is analysed by default.
        threads: (both modes, optional) Number of cores to be used. Default\
            uses 1 core.
        cpu: (both modes, optional) Enforce running with CPU rather than GPU.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriSegmentHypothalamicSubunitsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_SEGMENT_HYPOTHALAMIC_SUBUNITS_METADATA)
    params = mri_segment_hypothalamic_subunits_params(subjects=subjects, subjects_dir=subjects_dir, write_posteriors=write_posteriors, image_input=image_input, output=output, posteriors=posteriors, resample=resample, volume_output=volume_output, crop_size=crop_size, threads=threads, cpu=cpu)
    return mri_segment_hypothalamic_subunits_execute(params, execution)


__all__ = [
    "MRI_SEGMENT_HYPOTHALAMIC_SUBUNITS_METADATA",
    "MriSegmentHypothalamicSubunitsOutputs",
    "MriSegmentHypothalamicSubunitsParameters",
    "mri_segment_hypothalamic_subunits",
    "mri_segment_hypothalamic_subunits_params",
]
