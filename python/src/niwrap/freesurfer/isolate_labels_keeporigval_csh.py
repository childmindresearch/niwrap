# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ISOLATE_LABELS_KEEPORIGVAL_CSH_METADATA = Metadata(
    id="6feb5e5bb20cc74c2d8708554651a3dbef953d64.boutiques",
    name="isolate_labels_keeporigval.csh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class IsolateLabelsKeeporigvalCshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `isolate_labels_keeporigval_csh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_label_files: OutputPathType
    """Output binary label file(s)"""


def isolate_labels_keeporigval_csh(
    vol: InputPathType,
    outprefix: str,
    label: str | None = None,
    version: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> IsolateLabelsKeeporigvalCshOutputs:
    """
    Separates out a particular or all labels into individual binary files keeping
    the original label values for subsequent shape analysis.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        vol: Label volume to be analyzed.
        outprefix: Prefix for output binary label file(s).
        label: The particular label to be analyzed. By default, it is ALL\
            labels in the volume.
        version: Print version and exit.
        help_: Print help and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `IsolateLabelsKeeporigvalCshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ISOLATE_LABELS_KEEPORIGVAL_CSH_METADATA)
    cargs = []
    cargs.append("isolate_labels_keeporigval.csh")
    cargs.append("--vol")
    cargs.extend([
        "--vol",
        execution.input_file(vol)
    ])
    cargs.append("--outprefix")
    cargs.extend([
        "--outprefix",
        outprefix
    ])
    if label is not None:
        cargs.extend([
            "--l",
            label
        ])
    if version:
        cargs.append("--version")
    if help_:
        cargs.append("--help")
    ret = IsolateLabelsKeeporigvalCshOutputs(
        root=execution.output_file("."),
        output_label_files=execution.output_file(outprefix + "_label*.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ISOLATE_LABELS_KEEPORIGVAL_CSH_METADATA",
    "IsolateLabelsKeeporigvalCshOutputs",
    "isolate_labels_keeporigval_csh",
]