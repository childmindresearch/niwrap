# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_SCLIMBIC_SEG_METADATA = Metadata(
    id="1ec74b6aef5bd2cf5b900639f4d636aba2915275.boutiques",
    name="mri_sclimbic_seg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriSclimbicSegParameters = typing.TypedDict('MriSclimbicSegParameters', {
    "__STYX_TYPE__": typing.Literal["mri_sclimbic_seg"],
    "input_file": str,
    "output_file": str,
    "subjects": typing.NotRequired[list[str] | None],
    "subjects_dir": typing.NotRequired[str | None],
    "conform": bool,
    "etiv": bool,
    "exclude_labels": typing.NotRequired[list[str] | None],
    "keep_ac": bool,
    "vox_count_volumes": bool,
    "model_file": typing.NotRequired[InputPathType | None],
    "ctab_file": typing.NotRequired[InputPathType | None],
    "population_stats": typing.NotRequired[InputPathType | None],
    "debug": bool,
    "vmp": bool,
    "threads": typing.NotRequired[int | None],
    "tal_xfm": typing.NotRequired[str | None],
    "write_posteriors": bool,
    "write_volumes": bool,
    "write_qa_stats": bool,
    "preprocess_7T": bool,
    "percentile": typing.NotRequired[float | None],
    "cuda_device": typing.NotRequired[str | None],
    "output_base": typing.NotRequired[str | None],
    "no_cite": bool,
    "nchannels": typing.NotRequired[int | None],
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
        "mri_sclimbic_seg": mri_sclimbic_seg_cargs,
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
        "mri_sclimbic_seg": mri_sclimbic_seg_outputs,
    }
    return vt.get(t)


class MriSclimbicSegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_sclimbic_seg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    segmentation_output: OutputPathType
    """Segmentation output file."""


def mri_sclimbic_seg_params(
    input_file: str,
    output_file: str,
    subjects: list[str] | None = None,
    subjects_dir: str | None = None,
    conform: bool = False,
    etiv: bool = False,
    exclude_labels: list[str] | None = None,
    keep_ac: bool = False,
    vox_count_volumes: bool = False,
    model_file: InputPathType | None = None,
    ctab_file: InputPathType | None = None,
    population_stats: InputPathType | None = None,
    debug: bool = False,
    vmp: bool = False,
    threads: int | None = None,
    tal_xfm: str | None = None,
    write_posteriors: bool = False,
    write_volumes: bool = False,
    write_qa_stats: bool = False,
    preprocess_7_t: bool = False,
    percentile: float | None = None,
    cuda_device: str | None = None,
    output_base: str | None = None,
    no_cite: bool = False,
    nchannels: int | None = None,
) -> MriSclimbicSegParameters:
    """
    Build parameters.
    
    Args:
        input_file: T1-w image(s) to segment. Can be a path to a single image\
            or a directory of images.
        output_file: Segmentation output (required if --i is provided). Must be\
            the same type as the input path (a single file or directory).
        subjects: Process a series of freesurfer recon-all subjects (enables\
            subject-mode).
        subjects_dir: Set the subjects directory (overrides the SUBJECTS_DIR\
            env variable).
        conform: Resample input to 1mm-iso; results will be put back in native\
            resolution.
        etiv: Include eTIV in volume stats (enabled by default in subject-mode\
            and --tal).
        exclude_labels: List of label IDs to exclude in any output stats files.
        keep_ac: Explicitly keep anterior commissure in the volume/qa files.
        vox_count_volumes: Use discrete voxel count for label volumes.
        model_file: Alternative model weights to load.
        ctab_file: Alternative color lookup table to embed in segmentation.\
            Must be minimal, including 0, and sorted.
        population_stats: Alternative population volume stats for QA output.
        debug: Enable debug logging.
        vmp: Enable printing of vmpeak at the end.
        threads: Number of threads to use. Default is 1.
        tal_xfm: Alternative talairach xfm transform for estimating TIV. Can be\
            file or suffix (for multiple inputs).
        write_posteriors: Save the label posteriors.
        write_volumes: Save label volume stats (enabled by default in\
            subject-mode).
        write_qa_stats: Save QA stats (z and confidence).
        preprocess_7_t: Preprocess 7T images (just sets percentile to 99.9).
        percentile: Use intensity percentile threshold for normalization.
        cuda_device: Cuda device for GPU support.
        output_base: String to use in output file name; default is sclimbic.
        no_cite: Do not cite sclimbic paper at the end.
        nchannels: Number of channels.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_sclimbic_seg",
        "input_file": input_file,
        "output_file": output_file,
        "conform": conform,
        "etiv": etiv,
        "keep_ac": keep_ac,
        "vox_count_volumes": vox_count_volumes,
        "debug": debug,
        "vmp": vmp,
        "write_posteriors": write_posteriors,
        "write_volumes": write_volumes,
        "write_qa_stats": write_qa_stats,
        "preprocess_7T": preprocess_7_t,
        "no_cite": no_cite,
    }
    if subjects is not None:
        params["subjects"] = subjects
    if subjects_dir is not None:
        params["subjects_dir"] = subjects_dir
    if exclude_labels is not None:
        params["exclude_labels"] = exclude_labels
    if model_file is not None:
        params["model_file"] = model_file
    if ctab_file is not None:
        params["ctab_file"] = ctab_file
    if population_stats is not None:
        params["population_stats"] = population_stats
    if threads is not None:
        params["threads"] = threads
    if tal_xfm is not None:
        params["tal_xfm"] = tal_xfm
    if percentile is not None:
        params["percentile"] = percentile
    if cuda_device is not None:
        params["cuda_device"] = cuda_device
    if output_base is not None:
        params["output_base"] = output_base
    if nchannels is not None:
        params["nchannels"] = nchannels
    return params


def mri_sclimbic_seg_cargs(
    params: MriSclimbicSegParameters,
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
    cargs.append("mri_sclimbic_seg")
    cargs.extend([
        "-i",
        params.get("input_file")
    ])
    cargs.extend([
        "-o",
        params.get("output_file")
    ])
    if params.get("subjects") is not None:
        cargs.extend([
            "-s",
            *params.get("subjects")
        ])
    if params.get("subjects_dir") is not None:
        cargs.extend([
            "--sd",
            params.get("subjects_dir")
        ])
    if params.get("conform"):
        cargs.append("--conform")
    if params.get("etiv"):
        cargs.append("--etiv")
    if params.get("exclude_labels") is not None:
        cargs.extend([
            "--exclude",
            *params.get("exclude_labels")
        ])
    if params.get("keep_ac"):
        cargs.append("--keep_ac")
    if params.get("vox_count_volumes"):
        cargs.append("--vox-count-volumes")
    if params.get("model_file") is not None:
        cargs.extend([
            "--model",
            execution.input_file(params.get("model_file"))
        ])
    if params.get("ctab_file") is not None:
        cargs.extend([
            "--ctab",
            execution.input_file(params.get("ctab_file"))
        ])
    if params.get("population_stats") is not None:
        cargs.extend([
            "--population-stats",
            execution.input_file(params.get("population_stats"))
        ])
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("vmp"):
        cargs.append("--vmp")
    if params.get("threads") is not None:
        cargs.extend([
            "--threads",
            str(params.get("threads"))
        ])
    if params.get("tal_xfm") is not None:
        cargs.extend([
            "--tal",
            params.get("tal_xfm")
        ])
    if params.get("write_posteriors"):
        cargs.append("--write_posteriors")
    if params.get("write_volumes"):
        cargs.append("--write_volumes")
    if params.get("write_qa_stats"):
        cargs.append("--write_qa_stats")
    if params.get("preprocess_7T"):
        cargs.append("--7T")
    if params.get("percentile") is not None:
        cargs.extend([
            "--percentile",
            str(params.get("percentile"))
        ])
    if params.get("cuda_device") is not None:
        cargs.extend([
            "--cuda-device",
            params.get("cuda_device")
        ])
    if params.get("output_base") is not None:
        cargs.extend([
            "--output-base",
            params.get("output_base")
        ])
    if params.get("no_cite"):
        cargs.append("--no-cite-sclimbic")
    if params.get("nchannels") is not None:
        cargs.extend([
            "--nchannels",
            str(params.get("nchannels"))
        ])
    return cargs


def mri_sclimbic_seg_outputs(
    params: MriSclimbicSegParameters,
    execution: Execution,
) -> MriSclimbicSegOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriSclimbicSegOutputs(
        root=execution.output_file("."),
        segmentation_output=execution.output_file(params.get("output_file")),
    )
    return ret


def mri_sclimbic_seg_execute(
    params: MriSclimbicSegParameters,
    execution: Execution,
) -> MriSclimbicSegOutputs:
    """
    Segment subcortical limbic structures using Freesurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriSclimbicSegOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_sclimbic_seg_cargs(params, execution)
    ret = mri_sclimbic_seg_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_sclimbic_seg(
    input_file: str,
    output_file: str,
    subjects: list[str] | None = None,
    subjects_dir: str | None = None,
    conform: bool = False,
    etiv: bool = False,
    exclude_labels: list[str] | None = None,
    keep_ac: bool = False,
    vox_count_volumes: bool = False,
    model_file: InputPathType | None = None,
    ctab_file: InputPathType | None = None,
    population_stats: InputPathType | None = None,
    debug: bool = False,
    vmp: bool = False,
    threads: int | None = None,
    tal_xfm: str | None = None,
    write_posteriors: bool = False,
    write_volumes: bool = False,
    write_qa_stats: bool = False,
    preprocess_7_t: bool = False,
    percentile: float | None = None,
    cuda_device: str | None = None,
    output_base: str | None = None,
    no_cite: bool = False,
    nchannels: int | None = None,
    runner: Runner | None = None,
) -> MriSclimbicSegOutputs:
    """
    Segment subcortical limbic structures using Freesurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: T1-w image(s) to segment. Can be a path to a single image\
            or a directory of images.
        output_file: Segmentation output (required if --i is provided). Must be\
            the same type as the input path (a single file or directory).
        subjects: Process a series of freesurfer recon-all subjects (enables\
            subject-mode).
        subjects_dir: Set the subjects directory (overrides the SUBJECTS_DIR\
            env variable).
        conform: Resample input to 1mm-iso; results will be put back in native\
            resolution.
        etiv: Include eTIV in volume stats (enabled by default in subject-mode\
            and --tal).
        exclude_labels: List of label IDs to exclude in any output stats files.
        keep_ac: Explicitly keep anterior commissure in the volume/qa files.
        vox_count_volumes: Use discrete voxel count for label volumes.
        model_file: Alternative model weights to load.
        ctab_file: Alternative color lookup table to embed in segmentation.\
            Must be minimal, including 0, and sorted.
        population_stats: Alternative population volume stats for QA output.
        debug: Enable debug logging.
        vmp: Enable printing of vmpeak at the end.
        threads: Number of threads to use. Default is 1.
        tal_xfm: Alternative talairach xfm transform for estimating TIV. Can be\
            file or suffix (for multiple inputs).
        write_posteriors: Save the label posteriors.
        write_volumes: Save label volume stats (enabled by default in\
            subject-mode).
        write_qa_stats: Save QA stats (z and confidence).
        preprocess_7_t: Preprocess 7T images (just sets percentile to 99.9).
        percentile: Use intensity percentile threshold for normalization.
        cuda_device: Cuda device for GPU support.
        output_base: String to use in output file name; default is sclimbic.
        no_cite: Do not cite sclimbic paper at the end.
        nchannels: Number of channels.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriSclimbicSegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_SCLIMBIC_SEG_METADATA)
    params = mri_sclimbic_seg_params(input_file=input_file, output_file=output_file, subjects=subjects, subjects_dir=subjects_dir, conform=conform, etiv=etiv, exclude_labels=exclude_labels, keep_ac=keep_ac, vox_count_volumes=vox_count_volumes, model_file=model_file, ctab_file=ctab_file, population_stats=population_stats, debug=debug, vmp=vmp, threads=threads, tal_xfm=tal_xfm, write_posteriors=write_posteriors, write_volumes=write_volumes, write_qa_stats=write_qa_stats, preprocess_7_t=preprocess_7_t, percentile=percentile, cuda_device=cuda_device, output_base=output_base, no_cite=no_cite, nchannels=nchannels)
    return mri_sclimbic_seg_execute(params, execution)


__all__ = [
    "MRI_SCLIMBIC_SEG_METADATA",
    "MriSclimbicSegOutputs",
    "MriSclimbicSegParameters",
    "mri_sclimbic_seg",
    "mri_sclimbic_seg_params",
]
