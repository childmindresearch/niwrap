# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

COMPUTE_LABEL_VOLUMES_CSH_METADATA = Metadata(
    id="82638ae4faa0eb9506df9c2f3a56c833cb5de288.boutiques",
    name="compute_label_volumes.csh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class ComputeLabelVolumesCshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `compute_label_volumes_csh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    result_file: OutputPathType
    """Text file with the computed number of voxels and volumes"""


def compute_label_volumes_csh(
    label_vol: InputPathType,
    output_file: str,
    label_l: str | None = None,
    version: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> ComputeLabelVolumesCshOutputs:
    """
    Computes the number of voxels and the volumes of either all or a particular
    label in the input label volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        label_vol: Label volume to be analyzed.
        output_file: Text file where the results are written.
        label_l: The particular label to be analyzed (case-insensitive option).
        version: Print version and exit.
        help_: Print help and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ComputeLabelVolumesCshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(COMPUTE_LABEL_VOLUMES_CSH_METADATA)
    cargs = []
    cargs.append("compute_label_volumes")
    cargs.extend([
        "--vol",
        execution.input_file(label_vol)
    ])
    cargs.extend([
        "--out",
        output_file
    ])
    if label_l is not None:
        cargs.extend([
            "--l",
            label_l
        ])
    if version:
        cargs.append("--version")
    if help_:
        cargs.append("--help")
    ret = ComputeLabelVolumesCshOutputs(
        root=execution.output_file("."),
        result_file=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "COMPUTE_LABEL_VOLUMES_CSH_METADATA",
    "ComputeLabelVolumesCshOutputs",
    "compute_label_volumes_csh",
]
