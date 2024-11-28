# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_RELABEL_NONWM_HYPOS_METADATA = Metadata(
    id="93faec099d80076ace8a12bddc7f7a4affe02681.boutiques",
    name="mri_relabel_nonwm_hypos",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriRelabelNonwmHyposOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_relabel_nonwm_hypos(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_segmentation: OutputPathType
    """Output segmentation with non-WM hypointensities relabeled."""


def mri_relabel_nonwm_hypos(
    inputseg: InputPathType,
    outputseg: str,
    segments: list[str] | None = None,
    seg_default: bool = False,
    debug: bool = False,
    checkopts: bool = False,
    runner: Runner | None = None,
) -> MriRelabelNonwmHyposOutputs:
    """
    Relabels non-WM hypointensities based on proximity to a nearby label.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        inputseg: Input segmentation file with non-wm-hypos labeled as 80, 81,\
            or 82.
        outputseg: Output segmentation file with non-wm-hypos relabeled.
        segments: Label hypos adjacent to specified segment as a new segment\
            (can be used multiple times).
        seg_default: Use the default relabeling scheme.
        debug: Turn on debugging.
        checkopts: Don't run anything, just check options and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriRelabelNonwmHyposOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_RELABEL_NONWM_HYPOS_METADATA)
    cargs = []
    cargs.append("mri_relabel_nonwm_hypos")
    cargs.extend([
        "-i",
        "-" + execution.input_file(inputseg)
    ])
    cargs.extend([
        "-o",
        "-" + outputseg
    ])
    if segments is not None:
        cargs.extend([
            "--seg",
            *segments
        ])
    if seg_default:
        cargs.append("--seg-default")
    if debug:
        cargs.append("--debug")
    if checkopts:
        cargs.append("--checkopts")
    ret = MriRelabelNonwmHyposOutputs(
        root=execution.output_file("."),
        out_segmentation=execution.output_file(outputseg),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_RELABEL_NONWM_HYPOS_METADATA",
    "MriRelabelNonwmHyposOutputs",
    "mri_relabel_nonwm_hypos",
]
