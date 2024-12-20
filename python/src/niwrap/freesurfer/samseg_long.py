# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SAMSEG_LONG_METADATA = Metadata(
    id="686e2f45cf8bcf8f37552255f101cc1d16f93f40.boutiques",
    name="samseg-long",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class SamsegLongOutputs(typing.NamedTuple):
    """
    Output object returned when calling `samseg_long(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    tp001_output: OutputPathType
    """Samseg output folder for the first time point."""
    tp002_output: OutputPathType
    """Samseg output folder for the second time point."""
    base_output: OutputPathType
    """Base folder created by the samseg-long process."""


def samseg_long(
    output_dir: str,
    input_files: list[InputPathType],
    align_no_mc: bool = False,
    threads: float | None = None,
    save_posteriors: bool = False,
    force_update: bool = False,
    runner: Runner | None = None,
) -> SamsegLongOutputs:
    """
    Longitudinal analysis tool using SAMSEG in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        output_dir: Output directory.
        input_files: Input image files. All inputs must be a single modality.
        align_no_mc: Do not align inputs using robust register.
        threads: Number of threads to use.
        save_posteriors: Save posterior probabilities.
        force_update: Force update of outputs.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SamsegLongOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SAMSEG_LONG_METADATA)
    cargs = []
    cargs.append("samseg-long")
    cargs.extend([
        "--o",
        output_dir
    ])
    if align_no_mc:
        cargs.append("--no-mc")
    if threads is not None:
        cargs.extend([
            "--threads",
            str(threads)
        ])
    cargs.extend([
        "--i",
        *[execution.input_file(f) for f in input_files]
    ])
    if save_posteriors:
        cargs.append("--save-posteriors")
    if force_update:
        cargs.append("--force-update")
    ret = SamsegLongOutputs(
        root=execution.output_file("."),
        tp001_output=execution.output_file(output_dir + "/tp001"),
        tp002_output=execution.output_file(output_dir + "/tp002"),
        base_output=execution.output_file(output_dir + "/base"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SAMSEG_LONG_METADATA",
    "SamsegLongOutputs",
    "samseg_long",
]
