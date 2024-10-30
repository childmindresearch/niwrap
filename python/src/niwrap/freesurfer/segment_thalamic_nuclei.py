# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SEGMENT_THALAMIC_NUCLEI_METADATA = Metadata(
    id="6d4f3bd43ea02912a67101dc7d2bc3abdee4ebd2.boutiques",
    name="SegmentThalamicNuclei",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class SegmentThalamicNucleiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `segment_thalamic_nuclei(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    seg_output: OutputPathType
    """The output segmentation file of thalamic nuclei."""


def segment_thalamic_nuclei(
    t1_image: InputPathType,
    output_dir: str,
    runner: Runner | None = None,
) -> SegmentThalamicNucleiOutputs:
    """
    A tool for segmenting thalamic nuclei using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        t1_image: The T1-weighted image to process.
        output_dir: Directory to store segmentation results.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SegmentThalamicNucleiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SEGMENT_THALAMIC_NUCLEI_METADATA)
    cargs = []
    cargs.append("SegmentThalamicNuclei")
    cargs.append(execution.input_file(t1_image))
    cargs.append(output_dir)
    ret = SegmentThalamicNucleiOutputs(
        root=execution.output_file("."),
        seg_output=execution.output_file(output_dir + "/thalamic_nuclei_seg.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SEGMENT_THALAMIC_NUCLEI_METADATA",
    "SegmentThalamicNucleiOutputs",
    "segment_thalamic_nuclei",
]