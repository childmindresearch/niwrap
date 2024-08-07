# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

MRSI_SEGMENT_METADATA = Metadata(
    id="e3dd5e555c5831e8b1a5d8947e393fd8ddfdd05a",
    name="mrsi_segment",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="fsl/fsl:latest",
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
    mrsi_segment by FSL Team.
    
    FSL Magnetic Resonance Spectroscopy - register fast segmentation to MRSI.
    
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
    cargs.append("[--t1")
    cargs.append("T1]")
    cargs.append("[--anat")
    cargs.append("ANAT]")
    cargs.append("[--output")
    cargs.append("OUTPUT]")
    cargs.append("[--filename")
    cargs.append("FILENAME]")
    ret = MrsiSegmentOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"{output_dir}/{filename}", optional=True) if output_dir is not None and filename is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRSI_SEGMENT_METADATA",
    "MrsiSegmentOutputs",
    "mrsi_segment",
]
