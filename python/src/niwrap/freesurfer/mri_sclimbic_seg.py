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


class MriSclimbicSegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_sclimbic_seg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    segmentation_output: OutputPathType
    """Segmentation output file."""


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
    cargs = []
    cargs.append("mri_sclimbic_seg")
    cargs.extend([
        "-i",
        input_file
    ])
    cargs.extend([
        "-o",
        output_file
    ])
    if subjects is not None:
        cargs.extend([
            "-s",
            *subjects
        ])
    if subjects_dir is not None:
        cargs.extend([
            "--sd",
            subjects_dir
        ])
    if conform:
        cargs.append("--conform")
    if etiv:
        cargs.append("--etiv")
    if exclude_labels is not None:
        cargs.extend([
            "--exclude",
            *exclude_labels
        ])
    if keep_ac:
        cargs.append("--keep_ac")
    if vox_count_volumes:
        cargs.append("--vox-count-volumes")
    if model_file is not None:
        cargs.extend([
            "--model",
            execution.input_file(model_file)
        ])
    if ctab_file is not None:
        cargs.extend([
            "--ctab",
            execution.input_file(ctab_file)
        ])
    if population_stats is not None:
        cargs.extend([
            "--population-stats",
            execution.input_file(population_stats)
        ])
    if debug:
        cargs.append("--debug")
    if vmp:
        cargs.append("--vmp")
    if threads is not None:
        cargs.extend([
            "--threads",
            str(threads)
        ])
    if tal_xfm is not None:
        cargs.extend([
            "--tal",
            tal_xfm
        ])
    if write_posteriors:
        cargs.append("--write_posteriors")
    if write_volumes:
        cargs.append("--write_volumes")
    if write_qa_stats:
        cargs.append("--write_qa_stats")
    if preprocess_7_t:
        cargs.append("--7T")
    if percentile is not None:
        cargs.extend([
            "--percentile",
            str(percentile)
        ])
    if cuda_device is not None:
        cargs.extend([
            "--cuda-device",
            cuda_device
        ])
    if output_base is not None:
        cargs.extend([
            "--output-base",
            output_base
        ])
    if no_cite:
        cargs.append("--no-cite-sclimbic")
    if nchannels is not None:
        cargs.extend([
            "--nchannels",
            str(nchannels)
        ])
    ret = MriSclimbicSegOutputs(
        root=execution.output_file("."),
        segmentation_output=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_SCLIMBIC_SEG_METADATA",
    "MriSclimbicSegOutputs",
    "mri_sclimbic_seg",
]
