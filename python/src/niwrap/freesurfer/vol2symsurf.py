# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

VOL2SYMSURF_METADATA = Metadata(
    id="22e164f84127031ad07cd425f37456f6e49f209f.boutiques",
    name="vol2symsurf",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class Vol2symsurfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `vol2symsurf(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_lh: OutputPathType | None
    """Output for left hemisphere"""
    output_rh: OutputPathType | None
    """Output for right hemisphere"""
    output_lh_rh_difference: OutputPathType | None
    """Output for left-right hemisphere difference"""
    output_li_difference: OutputPathType | None
    """Output for laterality index"""


def vol2symsurf(
    registration_file: InputPathType,
    input_volume: InputPathType,
    fwhm: float,
    output_stem: str | None = "instem.fsaverage_sym.smFWHM.lh.hemi",
    regheader: str | None = None,
    projection_fraction: float | None = 0.5,
    no_diff: bool = False,
    laterality_index: bool = False,
    runner: Runner | None = None,
) -> Vol2symsurfOutputs:
    """
    A tool that samples a volume onto the surface of the left-right symmetric
    subject (fsaverage_sym).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        registration_file: Registration file.
        input_volume: Input volume in NIfTI format.
        fwhm: Full width at half maximum for surface smoothing.
        output_stem: Output stem.
        regheader: Subject for regheader.
        projection_fraction: Projection fraction.
        no_diff: Do not compute left-right hemisphere difference.
        laterality_index: Compute laterality index instead of simple difference.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Vol2symsurfOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOL2SYMSURF_METADATA)
    cargs = []
    cargs.append("vol2symsurf")
    cargs.extend([
        "--reg",
        execution.input_file(registration_file)
    ])
    cargs.extend([
        "--i",
        execution.input_file(input_volume)
    ])
    cargs.extend([
        "--fwhm",
        str(fwhm)
    ])
    if output_stem is not None:
        cargs.extend([
            "--o",
            output_stem
        ])
    if regheader is not None:
        cargs.extend([
            "--regheader",
            regheader
        ])
    if projection_fraction is not None:
        cargs.extend([
            "--projfrac",
            str(projection_fraction)
        ])
    if no_diff:
        cargs.append("--no-diff")
    if laterality_index:
        cargs.append("--li")
    ret = Vol2symsurfOutputs(
        root=execution.output_file("."),
        output_lh=execution.output_file(output_stem + ".lh.nii") if (output_stem is not None) else None,
        output_rh=execution.output_file(output_stem + ".rh.nii") if (output_stem is not None) else None,
        output_lh_rh_difference=execution.output_file(output_stem + ".lh-rh.nii") if (output_stem is not None) else None,
        output_li_difference=execution.output_file(output_stem + ".li.lh-rh.nii") if (output_stem is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOL2SYMSURF_METADATA",
    "Vol2symsurfOutputs",
    "vol2symsurf",
]
