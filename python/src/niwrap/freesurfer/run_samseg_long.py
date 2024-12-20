# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

RUN_SAMSEG_LONG_METADATA = Metadata(
    id="053d1261eca217932b41a5fecb7c25f4e497aefd.boutiques",
    name="run_samseg_long",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class RunSamsegLongOutputs(typing.NamedTuple):
    """
    Output object returned when calling `run_samseg_long(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def run_samseg_long(
    timepoint: list[InputPathType],
    output: str,
    lesion: bool = False,
    threshold: float | None = None,
    samples: float | None = None,
    burnin: float | None = None,
    lesion_mask_structure: str | None = None,
    lesion_mask_pattern: list[float] | None = None,
    mode: list[str] | None = None,
    atlas: str | None = None,
    deformation_hyperprior: float | None = None,
    gmm_hyperprior: float | None = None,
    save_warp: bool = False,
    save_mesh: bool = False,
    save_posteriors: list[str] | None = None,
    pallidum_separate: bool = False,
    threads: float | None = None,
    tp_to_base_transform: list[InputPathType] | None = None,
    force_different_resolutions: bool = False,
    history: bool = False,
    showfigs: bool = False,
    movie: bool = False,
    runner: Runner | None = None,
) -> RunSamsegLongOutputs:
    """
    Longitudinal image segmentation using SAMSEG.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        timepoint: Configure a timepoint with multiple inputs.
        output: Output directory.
        lesion: Enable lesion segmentation (requires tensorflow).
        threshold: Lesion threshold for final segmentation. Requires lesion\
            segmentation.
        samples: Number of samples for lesion segmentation. Requires lesion\
            segmentation.
        burnin: Number of burn-in samples for lesion segmentation. Requires\
            lesion segmentation.
        lesion_mask_structure: Intensity mask brain structure. Requires lesion\
            segmentation.
        lesion_mask_pattern: Lesion mask list: -1 below lesion mask structure\
            mean, +1 above, 0 no mask. Requires lesion segmentation.
        mode: Output basenames for the input image mode.
        atlas: Point to an alternative atlas directory.
        deformation_hyperprior: Strength of the latent deformation hyperprior.
        gmm_hyperprior: Strength of the latent GMM hyperprior.
        save_warp: Save the image->template warp fields.
        save_mesh: Save the final mesh of each timepoint in template space.
        save_posteriors: Save posterior volumes to the 'posteriors'\
            subdirectory.
        pallidum_separate: Move pallidum outside of global white matter class.\
            Use with T2/flair.
        threads: Number of threads to use. Defaults to OMP_NUM_THREADS or 1.
        tp_to_base_transform: Transformation file for each time point to base.
        force_different_resolutions: Force run even if time points have\
            different resolutions.
        history: Save history.
        showfigs: Show figures during run.
        movie: Show history as arrow key controlled time sequence.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RunSamsegLongOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RUN_SAMSEG_LONG_METADATA)
    cargs = []
    cargs.append("run_samseg_long")
    cargs.extend([
        "-t",
        *[execution.input_file(f) for f in timepoint]
    ])
    cargs.extend([
        "-o",
        output
    ])
    if lesion:
        cargs.append("--lesion")
    if threshold is not None:
        cargs.extend([
            "--threshold",
            str(threshold)
        ])
    if samples is not None:
        cargs.extend([
            "--samples",
            str(samples)
        ])
    if burnin is not None:
        cargs.extend([
            "--burnin",
            str(burnin)
        ])
    if lesion_mask_structure is not None:
        cargs.extend([
            "--lesion-mask-structure",
            lesion_mask_structure
        ])
    if lesion_mask_pattern is not None:
        cargs.extend([
            "--lesion-mask-pattern",
            *map(str, lesion_mask_pattern)
        ])
    if mode is not None:
        cargs.extend([
            "-m",
            *mode
        ])
    if atlas is not None:
        cargs.extend([
            "-a",
            atlas
        ])
    if deformation_hyperprior is not None:
        cargs.extend([
            "--deformation-hyperprior",
            str(deformation_hyperprior)
        ])
    if gmm_hyperprior is not None:
        cargs.extend([
            "--gmm-hyperprior",
            str(gmm_hyperprior)
        ])
    if save_warp:
        cargs.append("--save-warp")
    if save_mesh:
        cargs.append("--save-mesh")
    if save_posteriors is not None:
        cargs.extend([
            "--save-posteriors",
            *save_posteriors
        ])
    if pallidum_separate:
        cargs.append("--pallidum-separate")
    if threads is not None:
        cargs.extend([
            "--threads",
            str(threads)
        ])
    if tp_to_base_transform is not None:
        cargs.extend([
            "--tp-to-base-transform",
            *[execution.input_file(f) for f in tp_to_base_transform]
        ])
    if force_different_resolutions:
        cargs.append("--force-different-resolutions")
    if history:
        cargs.append("--history")
    if showfigs:
        cargs.append("--showfigs")
    if movie:
        cargs.append("--movie")
    ret = RunSamsegLongOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "RUN_SAMSEG_LONG_METADATA",
    "RunSamsegLongOutputs",
    "run_samseg_long",
]
