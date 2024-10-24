# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

RUN_SAMSEG_METADATA = Metadata(
    id="44643a5ac5bf2fd988d84ca267e8388b307ea24d.boutiques",
    name="run_samseg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class RunSamsegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `run_samseg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def run_samseg(
    output_dir: str,
    input_files: list[InputPathType],
    input_mode: list[str] | None = None,
    threads: float | None = None,
    reg_only: bool = False,
    reg_file: InputPathType | None = None,
    init_reg_file: InputPathType | None = None,
    atlas_dir: str | None = None,
    gmm_file: InputPathType | None = None,
    ignore_unknown: bool = False,
    options_file: InputPathType | None = None,
    pallidum_separate: bool = False,
    mesh_stiffness: float | None = None,
    smooth_wm_cortex_priors: float | None = None,
    bias_field_smoothing_kernel: float | None = None,
    lesion: bool = False,
    threshold: float | None = None,
    samples: float | None = None,
    burnin: float | None = None,
    lesion_pseudo_samples: list[float] | None = None,
    lesion_rho: float | None = None,
    lesion_mask_structure: str | None = None,
    lesion_mask_pattern: list[float] | None = None,
    random_seed: float | None = None,
    dissection_photo: str | None = None,
    history: bool = False,
    save_posteriors: list[str] | None = None,
    save_probabilities: bool = False,
    showfigs: bool = False,
    save_mesh: bool = False,
    save_warp: bool = False,
    movie: bool = False,
    runner: Runner | None = None,
) -> RunSamsegOutputs:
    """
    SAMSEG (Sequence Adaptive Multimodal SEGmentation) is a tool for automated
    segmentation of brain MRI data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        output_dir: Target directory for output.
        input_files: Input image(s) for segmentation.
        input_mode: Output basenames for the input image mode.
        threads: Number of threads to use.
        reg_only: Only perform initial affine registration.
        reg_file: Skip initial affine registration and read transform from\
            file.
        init_reg_file: Initial affine registration.
        atlas_dir: Point to an alternative atlas directory.
        gmm_file: Point to an alternative GMM file.
        ignore_unknown: Ignore final priors corresponding to unknown class.
        options_file: Override advanced options via a JSON file.
        pallidum_separate: Move pallidum outside of global white matter class.
        mesh_stiffness: Override mesh stiffness.
        smooth_wm_cortex_priors: Sigma value to smooth the WM and cortex atlas\
            priors.
        bias_field_smoothing_kernel: Distance in mm of sinc function center to\
            first zero crossing.
        lesion: Enable lesion segmentation (requires tensorflow).
        threshold: Lesion threshold for final segmentation.
        samples: Number of samples for lesion segmentation.
        burnin: Number of burn-in samples for lesion segmentation.
        lesion_pseudo_samples: Lesion pseudo samples mean and variance.
        lesion_rho: Lesion ratio.
        lesion_mask_structure: Intensity mask brain structure.
        lesion_mask_pattern: Lesion mask pattern for each input volume.
        random_seed: Random seed.
        dissection_photo: Specify hemispheres: left, right, or both.
        history: Save history of segmentation.
        save_posteriors: Save posterior volumes.
        save_probabilities: Save modal class probabilities.
        showfigs: Show figures during run.
        save_mesh: Save final mesh in template space.
        save_warp: Save image->template warp field.
        movie: Show history as controlled time sequence.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RunSamsegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RUN_SAMSEG_METADATA)
    cargs = []
    cargs.append("run_samseg")
    cargs.extend([
        "-o",
        output_dir
    ])
    cargs.extend([
        "-i",
        *[execution.input_file(f) for f in input_files]
    ])
    if input_mode is not None:
        cargs.extend([
            "-m",
            *input_mode
        ])
    if threads is not None:
        cargs.extend([
            "--threads",
            str(threads)
        ])
    if reg_only:
        cargs.append("--reg-only")
    if reg_file is not None:
        cargs.extend([
            "-r",
            execution.input_file(reg_file)
        ])
    if init_reg_file is not None:
        cargs.extend([
            "--init-reg",
            execution.input_file(init_reg_file)
        ])
    if atlas_dir is not None:
        cargs.extend([
            "-a",
            atlas_dir
        ])
    if gmm_file is not None:
        cargs.extend([
            "--gmm",
            execution.input_file(gmm_file)
        ])
    if ignore_unknown:
        cargs.append("--ignore-unknown")
    if options_file is not None:
        cargs.extend([
            "--options",
            execution.input_file(options_file)
        ])
    if pallidum_separate:
        cargs.append("--pallidum-separate")
    if mesh_stiffness is not None:
        cargs.extend([
            "--mesh-stiffness",
            str(mesh_stiffness)
        ])
    if smooth_wm_cortex_priors is not None:
        cargs.extend([
            "--smooth-wm-cortex-priors",
            str(smooth_wm_cortex_priors)
        ])
    if bias_field_smoothing_kernel is not None:
        cargs.extend([
            "--bias-field-smoothing-kernel",
            str(bias_field_smoothing_kernel)
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
    if lesion_pseudo_samples is not None:
        cargs.extend([
            "--lesion-pseudo-samples",
            *map(str, lesion_pseudo_samples)
        ])
    if lesion_rho is not None:
        cargs.extend([
            "--lesion-rho",
            str(lesion_rho)
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
    if random_seed is not None:
        cargs.extend([
            "--random-seed",
            str(random_seed)
        ])
    if dissection_photo is not None:
        cargs.extend([
            "--dissection-photo",
            dissection_photo
        ])
    if history:
        cargs.append("--history")
    if save_posteriors is not None:
        cargs.extend([
            "--save-posteriors",
            *save_posteriors
        ])
    if save_probabilities:
        cargs.append("--save-probabilities")
    if showfigs:
        cargs.append("--showfigs")
    if save_mesh:
        cargs.append("--save-mesh")
    if save_warp:
        cargs.append("--save-warp")
    if movie:
        cargs.append("--movie")
    ret = RunSamsegOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "RUN_SAMSEG_METADATA",
    "RunSamsegOutputs",
    "run_samseg",
]
