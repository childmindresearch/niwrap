# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRSI_SEGMENT_METADATA = Metadata(
    id="af23f6ec8afd0f96cc3b440f7a5499c254f9f104.boutiques",
    name="mrsi_segment",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class MrsiSegmentOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mrsi_segment(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """Output file name"""


def mrsi_segment(
    mrsi_file: InputPathType,
    t1_file: InputPathType | None = None,
    anat_dir: str | None = None,
    output_dir: str | None = None,
    filename: str | None = None,
    runner: Runner | None = None,
) -> MrsiSegmentOutputs:
    """
    FSL Magnetic Resonance Spectroscopy - register fast segmentation to MRSI.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        mrsi_file: MRSI nifti file.
        t1_file: T1 nifti file.
        anat_dir: fsl_anat output directory.
        output_dir: Output directory.
        filename: Output file name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrsiSegmentOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRSI_SEGMENT_METADATA)
    cargs = []
    cargs.append("mrsi_segment")
    cargs.append(execution.input_file(mrsi_file))
    if t1_file is not None:
        cargs.extend([
            "--t1",
            execution.input_file(t1_file)
        ])
    if anat_dir is not None:
        cargs.extend([
            "--anat",
            anat_dir
        ])
    if output_dir is not None:
        cargs.extend([
            "--output",
            output_dir
        ])
    if filename is not None:
        cargs.extend([
            "--filename",
            filename
        ])
    ret = MrsiSegmentOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(output_dir + "/" + filename) if (output_dir is not None and filename is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRSI_SEGMENT_METADATA",
    "MrsiSegmentOutputs",
    "mrsi_segment",
]
